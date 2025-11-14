"""
批量任务：从 pre-process/mid.txt 读取每位老师的 k 篇最近论文与 k 篇最高引用论文（已排序），
下载 PDF 与元数据，并按 data/<teacher> 目录结构落盘：
- main/  保存主选论文（recent + most_cited）
- ref1/  保存这些主选论文的参考文献（references）
- cited/  保存这些主选论文的被引文献（citations）

输入 mid.txt 支持两种格式：
1) JSON：
{
  "张三": {"recent": ["10.x/..", ...], "cited": ["10.y/..", ...]},
  "李四": {"recent": [...], "cited": [...]}
}
2) 纯文本块：
teacher: 张三
recent: 10.x/.., 10.y/..
cited:  10.a/.., 10.b/..

teacher: 李四
recent: ...
cited:  ...

用法示例：
  python batch_from_mid.py --mid-file pre-process/mid.txt --k 5 --data-root ./data
  python batch_from_mid.py --mid-file pre-process/mid.txt --teacher 张三 --k 3 -o ./data

说明：
- 年轻作者相关字段由 doi_downloader 里的逻辑计算并写入每条条目（items 元数据），本脚本直接复用。
- 若需仅索引相关文献而不下载，可加 --no-related-downloads。
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import configparser
import random
import concurrent.futures as futures

# 简易进度打印（避免外部依赖问题）
def progress_iter(items: List[str], desc: str, unit: str = "item"):
    total = len(items)
    if total == 0:
        return
    print(f"{desc}: 0/{total} {unit}s")
    for idx, it in enumerate(items, 1):
        yield it
        print(f"{desc}: {idx}/{total} {unit}s")

# 路径设置：确保可以导入 inspirehep_source/main 包
import sys
CUR_DIR = Path(__file__).resolve().parent
# 仓库根目录（Check-Mentor）
PROJ_ROOT = CUR_DIR.parents[2]
# 源码根目录（inspirehep_source）
SRC_ROOT = PROJ_ROOT / 'inspirehep_source'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

"""
动态加载 InspireHEPClient：
优先从 inspirehep_source/main/client.py 加载；若不存在，则回退到
inspirehep_source/inspirehep_downloader/inspirehep_downloader/client.py。
"""
import importlib.util as iu

# 首选：仓库旧结构（main/client.py）
client_cls = None
MAIN_CLIENT_PATH = SRC_ROOT / 'main' / 'client.py'
if MAIN_CLIENT_PATH.exists():
    _spec_client = iu.spec_from_file_location('ih_main_client_mod', str(MAIN_CLIENT_PATH))
    if _spec_client and _spec_client.loader:
        _mod_client = iu.module_from_spec(_spec_client)
        _spec_client.loader.exec_module(_mod_client)  # type: ignore
        client_cls = getattr(_mod_client, 'InspireHEPClient', None)

# 回退：新结构（inspirehep_downloader/inspirehep_downloader/client.py）
if client_cls is None:
    ALT_CLIENT_PATH = SRC_ROOT / 'inspirehep_downloader' / 'inspirehep_downloader' / 'client.py'
    _spec_client2 = iu.spec_from_file_location('ih_pkg_client_mod', str(ALT_CLIENT_PATH))
    if _spec_client2 and _spec_client2.loader:
        _mod_client2 = iu.module_from_spec(_spec_client2)
        _spec_client2.loader.exec_module(_mod_client2)  # type: ignore
        client_cls = getattr(_mod_client2, 'InspireHEPClient', None)

if client_cls is None:
    raise RuntimeError('无法加载 InspireHEPClient：请确认存在 main/client.py 或 inspirehep_downloader/inspirehep_downloader/client.py')

InspireHEPClient = client_cls  # type: ignore

# 直接导入同目录的 doi_downloader 辅助函数
from doi_downloader import (
    process_one_by_doi,
    process_one_by_record_id_using_url,
    get_young_author_years,
    fetch_related_ids,
    dir_name_from_metadata,
    parse_year_month,
)


def parse_mid_file(mid_path: Path) -> Dict[str, Dict[str, List[str]]]:
    """解析 mid.txt 为 {teacher: {recent: [doi...], cited: [doi...]}}"""
    text = mid_path.read_text(encoding='utf-8').strip()
    # 优先尝试 JSON
    if text.startswith('{'):
        try:
            obj = json.loads(text)
            result: Dict[str, Dict[str, List[str]]] = {}
            for teacher, payload in obj.items():
                recent = list(payload.get('recent', []) or [])
                cited = list(payload.get('cited', []) or payload.get('most_cited', []) or [])
                result[str(teacher)] = {
                    'recent': [str(d).strip() for d in recent if str(d).strip()],
                    'cited': [str(d).strip() for d in cited if str(d).strip()],
                }
            return result
        except Exception:
            pass
    # 退化为纯文本块解析
    result: Dict[str, Dict[str, List[str]]] = {}
    teacher: Optional[str] = None
    recent: List[str] = []
    cited: List[str] = []
    def _commit():
        nonlocal teacher, recent, cited
        if teacher:
            result[teacher] = {
                'recent': [d for d in recent if d],
                'cited': [d for d in cited if d],
            }
        teacher, recent, cited = None, [], []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            _commit()
            continue
        if line.lower().startswith('teacher:') or line.startswith('教师:'):
            _commit()
            teacher = line.split(':', 1)[1].strip()
        elif line.lower().startswith('recent:'):
            part = line.split(':', 1)[1]
            recent = [p.strip() for p in part.split(',') if p.strip()]
        elif line.lower().startswith('cited:') or line.lower().startswith('most_cited:'):
            part = line.split(':', 1)[1]
            cited = [p.strip() for p in part.split(',') if p.strip()]
        else:
            # 兼容：若行是 DOI 列表（无键名），追加到 recent
            if any(ch in line for ch in ['10.', '/']):
                recent.extend([p.strip() for p in line.split(',') if p.strip()])
    return result


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def get_default_k(config_path: Optional[Path] = None) -> Optional[int]:
    """从 config.ini 读取 [batch] k_per_list，未配置则返回 None。"""
    if config_path is None:
        config_path = PROJ_ROOT / 'config.ini'
    try:
        if config_path.exists():
            cp = configparser.ConfigParser()
            cp.read(config_path, encoding='utf-8')
            if cp.has_section('batch') and cp.has_option('batch', 'k_per_list'):
                raw = cp.get('batch', 'k_per_list').strip()
                if raw.isdigit():
                    return int(raw)
    except Exception:
        # 配置读取失败则回退为 None
        pass
    return None


def get_sampling_cfg(config_path: Optional[Path] = None) -> Tuple[Optional[int], Optional[int]]:
    """读取采样配置（当 refs/cited 数量超过 n 时，随机抽样 m 篇）。

    来自 config.ini 的 [download] 段：
      - sample_threshold: 超过该数量才启用抽样（n）
      - sample_size: 抽样数量（m）

    若缺失或无效，返回 (None, None) 表示不启用抽样。
    """
    if config_path is None:
        config_path = PROJ_ROOT / 'config.ini'
    try:
        if config_path.exists():
            cp = configparser.ConfigParser()
            cp.read(config_path, encoding='utf-8')
            if cp.has_section('download'):
                n_raw = cp.get('download', 'sample_threshold', fallback='').strip()
                m_raw = cp.get('download', 'sample_size', fallback='').strip()
                n_val: Optional[int] = int(n_raw) if n_raw.isdigit() else None
                m_val: Optional[int] = int(m_raw) if m_raw.isdigit() else None
                # 合法性检查
                if (n_val is not None and n_val <= 0) or (m_val is not None and m_val <= 0):
                    return None, None
                return n_val, m_val
    except Exception:
        pass
    return None, None


def get_worker_cfg(config_path: Optional[Path] = None) -> Tuple[int, int]:
    """读取并发配置，返回 (workers_main, workers_related)。

    来自 config.ini 的 [download] 段：
      - workers_main: 处理主文献 DOI 的并发度（默认 4）
      - workers_related: 处理 refs/cited 的并发度（默认 6）
    """
    if config_path is None:
        config_path = PROJ_ROOT / 'config.ini'
    wm, wr = 4, 6
    try:
        if config_path.exists():
            cp = configparser.ConfigParser()
            cp.read(config_path, encoding='utf-8')
            if cp.has_section('download'):
                wmr = cp.get('download', 'workers_main', fallback='').strip()
                wrr = cp.get('download', 'workers_related', fallback='').strip()
                if wmr.isdigit():
                    wm = max(1, int(wmr))
                if wrr.isdigit():
                    wr = max(1, int(wrr))
    except Exception:
        pass
    return wm, wr


def _sanitize_file_title(title: str) -> str:
    s = (
        title.replace('\\', '_')
        .replace('/', '_')
        .replace(':', '_')
        .replace('*', '_')
        .replace('?', '_')
        .replace('"', "'")
        .replace('<', '_')
        .replace('>', '_')
        .replace('|', '_')
        .strip()
    )
    return (s[:150] + '..') if len(s) > 150 else s


def _sanitize_folder_name(name: str) -> str:
    s = name.strip().replace('..', '.').strip()
    for ch in '\\/:*?"<>|#&':
        s = s.replace(ch, '_')
    return s or 'unknown'


def _update_history_json(root: Path, teacher: str, subdir: str, entry: Dict) -> None:
    t = _sanitize_folder_name(teacher)
    folder = root / t / subdir
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / 'history.json'
    data = {"items": []}
    try:
        if path.exists():
            data = json.loads(path.read_text(encoding='utf-8')) or {"items": []}
    except Exception:
        data = {"items": []}
    items = data.get('items') if isinstance(data, dict) else None
    if items is None:
        data = {"items": []}
        items = data['items']
    doi = entry.get('doi')
    updated = False
    for i, it in enumerate(items):
        if isinstance(it, dict) and it.get('doi') == doi:
            items[i] = entry
            updated = True
            break
    if not updated:
        items.append(entry)
    tmp = str(path) + '.tmp'
    try:
        Path(tmp).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        Path(tmp).replace(path)
    except Exception:
        pass


def _copy_pdf_to_layout(downloads_root: Path, teacher: str, subdir: str, title: str, pdf_src: Path) -> Path | None:
    try:
        if not pdf_src.exists():
            return None
        t = _sanitize_folder_name(teacher)
        dst_dir = downloads_root / t / subdir
        dst_dir.mkdir(parents=True, exist_ok=True)
        fname = f"{_sanitize_file_title(title)}.pdf"
        dst = dst_dir / fname
        # 避免同名覆盖：若已存在不同文件，追加序号
        if dst.exists() and pdf_src.resolve() != dst.resolve():
            base = dst.stem
            suf = dst.suffix
            idx = 1
            while True:
                cand = dst_dir / f"{base} ({idx}){suf}"
                if not cand.exists():
                    dst = cand
                    break
                idx += 1
        import shutil
        shutil.copy2(str(pdf_src), str(dst))
        return dst
    except Exception:
        return None


def download_for_teacher(client: InspireHEPClient, teacher: str, recent_dois: List[str], cited_dois: List[str], k: Optional[int], data_root: Path, no_related_downloads: bool, verbose: bool = False, *, pdf_root: Optional[Path] = None) -> None:
    # 直接写入 Downloads_pdf：使用 .staging 作为临时目录承载 *_metadata.json 与源 PDF，再镜像到最终目录与 history.json
    downloads_root = pdf_root or (PROJ_ROOT / 'Downloads_pdf')
    staging_root = downloads_root / '.staging' / _sanitize_folder_name(teacher)
    main_dir = staging_root / 'main'
    ref1_dir = staging_root / 'ref1'
    cited_dir = staging_root / 'cited'
    ensure_dir(main_dir)
    ensure_dir(ref1_dir)
    ensure_dir(cited_dir)

    years_window = get_young_author_years()
    def printv(*a, **kw):
        if verbose:
            print(*a, **kw)

    def has_any_metadata_json(dir_path: Path) -> bool:
        try:
            if not dir_path.exists() or not dir_path.is_dir():
                return False
            # 任意 *_metadata.json 即视为已完成
            return any(dir_path.glob("*_metadata.json"))
        except Exception:
            return False

    # 读取一次采样配置
    sample_threshold, sample_size = get_sampling_cfg()
    workers_main, workers_related = get_worker_cfg()

    def maybe_sample(ids: List[str], label: str) -> List[str]:
        """当 ids 数量超过阈值时，对其进行随机抽样。

        - label: 用于日志（refs/cited）
        """
        if sample_threshold is None or sample_size is None:
            return ids
        if len(ids) > sample_threshold:
            k = min(len(ids), sample_size)
            # 不改变原列表顺序的前提下进行随机抽取：先复制索引抽样，再保持原顺序
            indices = list(range(len(ids)))
            random.shuffle(indices)
            chosen = set(indices[:k])
            picked = [x for i, x in enumerate(ids) if i in chosen]
            printv(f"[{{teacher}}]   {label}: {len(ids)} 超过阈值 {sample_threshold}，随机抽样 {len(picked)} 篇进行处理")
            return picked
        return ids

    # downloads_root 已在函数开头定义

    def handle_one_doi(doi: str):
        printv(f"[{teacher}] ▶ main DOI: {doi}")
        # 先根据 DOI 直接定位输出目录，若已存在则跳过网络查询
        out_dir = main_dir / (doi.replace('/', '_'))
        rid = None
        if has_any_metadata_json(out_dir):
            printv(f"[{teacher}] ↷ 跳过 main（已存在）: {out_dir}")
        else:
            hit = client.find_record_by_doi(doi)
            if not hit:
                print(f"未找到 DOI={doi} 对应记录，跳过")
                return
            rid = str(hit.get('id'))
            item = process_one_by_doi(client, doi, str(out_dir), download=True, years_window=years_window, compute_young=True)
            printv(f"[{teacher}] ✓ main saved at {out_dir}")
        # 将 main PDF 复制到 Downloads_pdf/<老师>/main，并写入 history.json
        try:
            meta_path = next(out_dir.glob("*_metadata.json"), None)
            if meta_path is not None:
                meta_norm = json.loads(meta_path.read_text(encoding='utf-8'))
                title = meta_norm.get('title') or doi
                doi_norm = meta_norm.get('doi') or doi
                authors = meta_norm.get('authors') or []
                pub = {}
                # 尝试解析年份
                ym = parse_year_month(meta_norm.get('publication_date'))
                if ym:
                    pub = ym
                pdf_file = None
                # 定位 PDF：与 *_metadata.json 同名前缀
                stem = meta_path.name[:-len("_metadata.json")] if meta_path.name.endswith("_metadata.json") else meta_path.stem
                cand_pdf = out_dir / f"{stem}.pdf"
                if cand_pdf.exists():
                    pdf_file = cand_pdf
                if pdf_file is not None:
                    dst = _copy_pdf_to_layout(downloads_root, teacher, 'main', title, pdf_file)
                    entry = {
                        "title": title,
                        "doi": doi_norm,
                        "authors": authors,
                        "published": pub or {},
                        "young_authors": item.get('young_authors', []),
                    }
                    _update_history_json(downloads_root, teacher, 'main', entry)
        except Exception as e:
            if verbose:
                print(f"[warn] 复制 main 到 Downloads_pdf 失败: {e}")
        # 参考文献 → ref1（目录名优先 DOI/arXiv）
        # 若尚未解析 rid，则此处查一次
        if rid is None:
            try:
                hit2 = client.find_record_by_doi(doi)
                if hit2:
                    rid = str(hit2.get('id'))
            except Exception:
                rid = None
        if not rid:
            return
        ref_ids = fetch_related_ids(client, rid, kind="references", limit=1000)
        ref_ids = maybe_sample(ref_ids, label="refs")
        printv(f"[{teacher}]   refs total = {len(ref_ids)} (并发 {workers_related})")
        # 去重（同一老师内）
        seen_ref: set[str] = set()
        ref_ids = [x for x in ref_ids if (x not in seen_ref and not seen_ref.add(x))]

        def _handle_ref(rr: str, idx: int):
            try:
                md_norm = client.get_metadata(rr)
                name = dir_name_from_metadata(md_norm)
                target = ref1_dir / name
                if has_any_metadata_json(target):
                    printv(f"[{teacher}]   refs {idx}/{len(ref_ids)} -> 跳过（已存在） dir={name}")
                    # 即便已存在，也尝试复制 PDF 与写入 history.json（幂等）
                else:
                    printv(f"[{teacher}]   refs {idx}/{len(ref_ids)} -> id={rr} dir={name}")
                    process_one_by_record_id_using_url(client, rr, str(target), download=not no_related_downloads, years_window=years_window, compute_young=False)
                # 复制到 Downloads_pdf/ref1 并写入 history
                try:
                    meta_path = next(target.glob("*_metadata.json"), None)
                    if meta_path is not None:
                        meta_norm2 = json.loads(meta_path.read_text(encoding='utf-8'))
                        title2 = meta_norm2.get('title') or name
                        doi2 = meta_norm2.get('doi') or ''
                        authors2 = meta_norm2.get('authors') or []
                        pub2 = parse_year_month(meta_norm2.get('publication_date')) or {}
                        stem2 = meta_path.name[:-len("_metadata.json")] if meta_path.name.endswith("_metadata.json") else meta_path.stem
                        pdf_src2 = target / f"{stem2}.pdf"
                        if pdf_src2.exists():
                            _copy_pdf_to_layout(downloads_root, teacher, 'ref1', title2, pdf_src2)
                        entry2 = {
                            "title": title2,
                            "doi": doi2,
                            "authors": authors2,
                            "published": pub2,
                            "young_authors": [],
                        }
                        _update_history_json(downloads_root, teacher, 'ref1', entry2)
                except Exception as ie:
                    if verbose:
                        print(f"[warn] 写入 ref1 history 失败: {ie}")
            except Exception as e:
                print(f"参考文献 {rr} 处理失败: {e}")

        if ref_ids:
            with futures.ThreadPoolExecutor(max_workers=workers_related) as pool:
                list(pool.map(lambda t: _handle_ref(t[1], t[0]), enumerate(ref_ids, 1)))
        # 被引文献 → cited（目录名优先 DOI/arXiv）
        cit_ids = fetch_related_ids(client, rid, kind="citations", limit=1000)
        cit_ids = maybe_sample(cit_ids, label="cited")
        printv(f"[{teacher}]   cited total = {len(cit_ids)} (并发 {workers_related})")
        # 去重（同一老师内）
        seen_cit: set[str] = set()
        cit_ids = [x for x in cit_ids if (x not in seen_cit and not seen_cit.add(x))]

        def _handle_cit(cc: str, idx: int):
            try:
                md_norm = client.get_metadata(cc)
                name = dir_name_from_metadata(md_norm)
                target = cited_dir / name
                if has_any_metadata_json(target):
                    printv(f"[{teacher}]   cited {idx}/{len(cit_ids)} -> 跳过（已存在） dir={name}")
                    # 同样进行复制与 history 写入
                else:
                    printv(f"[{teacher}]   cited {idx}/{len(cit_ids)} -> id={cc} dir={name}")
                    process_one_by_record_id_using_url(client, cc, str(target), download=not no_related_downloads, years_window=years_window, compute_young=False)
                try:
                    meta_path = next(target.glob("*_metadata.json"), None)
                    if meta_path is not None:
                        meta_norm2 = json.loads(meta_path.read_text(encoding='utf-8'))
                        title2 = meta_norm2.get('title') or name
                        doi2 = meta_norm2.get('doi') or ''
                        authors2 = meta_norm2.get('authors') or []
                        pub2 = parse_year_month(meta_norm2.get('publication_date')) or {}
                        stem2 = meta_path.name[:-len("_metadata.json")] if meta_path.name.endswith("_metadata.json") else meta_path.stem
                        pdf_src2 = target / f"{stem2}.pdf"
                        if pdf_src2.exists():
                            _copy_pdf_to_layout(downloads_root, teacher, 'cited', title2, pdf_src2)
                        entry2 = {
                            "title": title2,
                            "doi": doi2,
                            "authors": authors2,
                            "published": pub2,
                            "young_authors": [],
                        }
                        _update_history_json(downloads_root, teacher, 'cited', entry2)
                except Exception as ie:
                    if verbose:
                        print(f"[warn] 写入 cited history 失败: {ie}")
            except Exception as e:
                print(f"被引文献 {cc} 处理失败: {e}")

        if cit_ids:
            with futures.ThreadPoolExecutor(max_workers=workers_related) as pool:
                list(pool.map(lambda t: _handle_cit(t[1], t[0]), enumerate(cit_ids, 1)))

    # helper: 根据 k 选择子集
    def take_k(items: List[str]) -> List[str]:
        if k is None:
            return items
        return items[: max(0, min(len(items), k))]

    # recent & cited with concurrency
    recent_slice = take_k(recent_dois)
    cited_slice = take_k(cited_dois)

    def _run_batch(items: List[str], label: str):
        if not items:
            return
        printv(f"[{teacher}] 开始处理 {label}: {len(items)} 篇（并发 {workers_main}）")
        with futures.ThreadPoolExecutor(max_workers=workers_main) as pool:
            list(pool.map(handle_one_doi, items))

    _run_batch(recent_slice, 'recent')
    _run_batch(cited_slice, 'cited')


def main():
    ap = argparse.ArgumentParser(description='根据 mid.txt 批量下载老师的最近/高被引论文，并同步其引用与被引到 ref1/cited')
    ap.add_argument('--mid-file', required=True, help='pre-process/mid.txt 路径，支持 JSON 或文本块格式')
    ap.add_argument('--teacher', default=None, help='仅处理该老师（可选）')
    ap.add_argument('--k', type=int, default=None, help='每个列表最多处理前 K 篇（可选，默认读取 config.ini [batch] k_per_list）')
    ap.add_argument('-o', '--data-root', default=str(PROJ_ROOT / 'data'), help='data 根目录（兼容参数，直接写入 Downloads_pdf 时仅用作占位）')
    ap.add_argument('--pdf-root', default=str(PROJ_ROOT / 'Downloads_pdf'), help='PDF 根目录（最终输出与 history.json 的位置），默认项目根下 Downloads_pdf')
    ap.add_argument('--no-related-downloads', action='store_true', help='仅索引相关文献，不下载其 PDF/元数据')
    ap.add_argument('--verbose', action='store_true', help='详细显示处理进度（主文献/refs/cited 的逐条信息）')
    args = ap.parse_args()

    mid_path = Path(args.mid_file)
    if not mid_path.exists():
        raise FileNotFoundError(f"mid 文件不存在: {mid_path}")

    plan = parse_mid_file(mid_path)
    if not plan:
        print('mid 文件未解析出任何老师/DOI，已退出')
        return 0

    data_root = Path(args.data_root)
    ensure_dir(Path(args.pdf_root))

    client = InspireHEPClient()
    # 若未提供 --k，读取 config.ini 的默认值
    if args.k is None:
        args.k = get_default_k()
    for teacher, items in plan.items():
        if args.teacher and teacher != args.teacher:
            continue
        recents = items.get('recent', [])
        citeds = items.get('cited', [])
        print(f"\n=== 处理老师: {teacher} | recent={len(recents)} | cited={len(citeds)} ===")
        download_for_teacher(client, teacher, recents, citeds, args.k, data_root, args.no_related_downloads, verbose=args.verbose, pdf_root=Path(args.pdf_root))

    print('\n✓ 处理完成')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
