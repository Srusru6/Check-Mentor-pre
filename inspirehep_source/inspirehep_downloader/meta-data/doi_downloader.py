"""
基于 INSPIRE-HEP 下载器的 DOI 工具。

功能：
- 输入 DOI，解析对应 INSPIRE 记录，下载 PDF 与元数据
- 索引该文献的被引（citations）与参考文献（references）
- 可选下载相关文献（被引/参考）的 PDF 与元数据
- 生成与主程序兼容的元数据（items 格式：{title, doi, authors, published:{year, month}}）

用法（示例）：
  python doi_downloader.py --doi 10.1103/PhysRevLett.116.061102 -o ./downloads --related-limit 5 --no-related-downloads
"""

import argparse
import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
import configparser
from pathlib import Path
import concurrent.futures as futures

# 处理包导入路径：将 inspirehep_source 加入 sys.path 以便导入下载器包
import sys
CUR_DIR = Path(__file__).resolve().parent
PROJ_ROOT = CUR_DIR.parents[2]
SRC_ROOT = PROJ_ROOT / 'inspirehep_source'
PKG_ROOT = SRC_ROOT / 'inspirehep_downloader'
for p in (SRC_ROOT, PKG_ROOT):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

# 引入 DOI_source 的下载方法（publisher/Unpaywall/Sci-Hub）
DOI_SRC_DIR = PROJ_ROOT / 'DOI_source'
if str(DOI_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(DOI_SRC_DIR))
import importlib.util as iu2
_dl_path = DOI_SRC_DIR / 'download.py'
_spec_dl = iu2.spec_from_file_location('doi_source_download_mod', str(_dl_path))
doi_src_mod = None
if _spec_dl and _spec_dl.loader:
    doi_src_mod = iu2.module_from_spec(_spec_dl)
    _spec_dl.loader.exec_module(doi_src_mod)  # type: ignore

# 从新版包结构导入：通过路径加载 client.py（其内部不含相对导入问题）
import importlib.util as iu
_client_path = PKG_ROOT / 'inspirehep_downloader' / 'client.py'
_spec_cli = iu.spec_from_file_location('ih_cli_mod', str(_client_path))
_mod_cli = iu.module_from_spec(_spec_cli)
assert _spec_cli and _spec_cli.loader
_spec_cli.loader.exec_module(_mod_cli)  # type: ignore
InspireHEPClient = getattr(_mod_cli, 'InspireHEPClient')  # type: ignore

# 直接内联实现下载函数，避免导入 downloader.py 的相对导入问题
def download_pdf(record_id: str, output_dir: str = ".", filename: Optional[str] = None) -> str:
    client = InspireHEPClient()
    pdf_url = client.get_pdf_url(record_id)
    if not pdf_url:
        raise ValueError(f"记录 {record_id} 没有可用的 PDF")
    os.makedirs(output_dir, exist_ok=True)
    if filename is None:
        filename = f"{record_id}.pdf"
    output_path = os.path.join(output_dir, filename)
    client.download_file(pdf_url, output_path)
    return output_path


def download_metadata(record_id: str, output_dir: str = ".", filename: Optional[str] = None, format: str = "json") -> str:
    if format not in ["json", "txt"]:
        raise ValueError(f"不支持的格式: {format}。请使用 'json' 或 'txt'")
    client = InspireHEPClient()
    metadata = client.get_metadata(record_id)
    os.makedirs(output_dir, exist_ok=True)
    if filename is None:
        filename = f"{record_id}_metadata.{format}"
    output_path = os.path.join(output_dir, filename)
    if format == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
    else:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"INSPIRE-HEP 记录: {metadata.get('record_id')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"标题: {metadata.get('title','')}\n\n")
            f.write(f"作者: {', '.join(metadata.get('authors', []))}\n\n")
            f.write(f"出版日期: {metadata.get('publication_date','')}\n")
            f.write(f"arXiv ID: {metadata.get('arxiv_id','')}\n")
            f.write(f"DOI: {metadata.get('doi','')}\n")
            f.write(f"引文: {metadata.get('citations',0)}\n")
            f.write(f"INSPIRE URL: {metadata.get('inspire_url','')}\n\n")
            kws = metadata.get('keywords') or []
            if kws:
                f.write(f"关键字: {', '.join(kws)}\n\n")
            f.write(f"摘要:\n{metadata.get('abstract','')}\n")
    return output_path


def download_record(record_id: str, output_dir: str = ".", download_pdf_flag: bool = True, download_metadata_flag: bool = True) -> Dict[str, Optional[str]]:
    results: Dict[str, Optional[str]] = {}
    if download_metadata_flag:
        try:
            results["metadata"] = download_metadata(record_id, output_dir)
        except Exception as e:
            print(f"警告: 无法下载元数据: {e}")
            results["metadata"] = None
    if download_pdf_flag:
        try:
            results["pdf"] = download_pdf(record_id, output_dir)
        except Exception as e:
            print(f"警告: 无法下载 PDF: {e}")
            results["pdf"] = None
    return results


# ---------------------------
# 配置：年轻作者年限（n 年内算年轻作者）
# 优先级：环境变量 YOUNG_AUTHOR_YEARS > config.ini [metadata] young_author_years > 默认 5
# ---------------------------
def get_young_author_years(config_path: Optional[Path] = None) -> int:
    val_env = os.getenv("YOUNG_AUTHOR_YEARS")
    if val_env and val_env.isdigit():
        return int(val_env)
    if config_path is None:
        # 仓库根目录下的 config.ini
        config_path = PROJ_ROOT / "config.ini"
    try:
        if config_path.exists():
            cp = configparser.ConfigParser()
            cp.read(config_path, encoding="utf-8")
            if cp.has_section("metadata") and cp.has_option("metadata", "young_author_years"):
                years = cp.get("metadata", "young_author_years").strip()
                if years.isdigit():
                    return int(years)
    except Exception:
        pass
    return 5


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def parse_year_month(pub_date: Any) -> Dict[str, int]:
    """将多种形式的出版日期解析为 {year, month?}。
    支持：YYYY、YYYY-MM、YYYY-MM-DD、int 年份。
    """
    year_month: Dict[str, int] = {}
    if pub_date is None:
        return year_month
    try:
        # 直接是年份数字
        if isinstance(pub_date, int):
            if 1000 <= pub_date <= 9999:
                year_month["year"] = pub_date
                return year_month
        # 字符串解析
        if isinstance(pub_date, str) and pub_date.strip():
            txt = pub_date.strip()
            # 尝试标准 ISO 格式
            for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
                try:
                    dt = datetime.strptime(txt, fmt)
                    year_month["year"] = dt.year
                    # 只有在包含月份信息时写入
                    if fmt in ("%Y-%m-%d", "%Y-%m"):
                        year_month["month"] = dt.month
                    return year_month
                except ValueError:
                    continue
    except Exception:
        pass
    return year_month


# ---------------------------
# 当缺少 PDF URL 时，使用 DOI_source 的方法回退获取
# ---------------------------

def _load_download_cfg(config_path: Optional[Path] = None) -> tuple[Optional[str], Optional[list[str]]]:
    """从 config.ini 或环境变量读取 Unpaywall 邮箱与 Sci-Hub 域名列表。
    环境变量优先：UNPAYWALL_EMAIL, SCIHUB_DOMAINS(逗号分隔)。
    配置文件段 [download] 中可选键：unpaywall_email, scihub_domains
    """
    email = os.getenv('UNPAYWALL_EMAIL') or None
    domains_env = os.getenv('SCIHUB_DOMAINS') or None
    domains = [s.strip() for s in domains_env.split(',')] if domains_env else None
    if config_path is None:
        config_path = PROJ_ROOT / 'config.ini'
    try:
        if config_path.exists():
            cp = configparser.ConfigParser()
            cp.read(config_path, encoding='utf-8')
            if not email:
                email = cp.get('download', 'unpaywall_email', fallback='').strip() or None
            if domains is None:
                raw = cp.get('download', 'scihub_domains', fallback='').strip()
                if raw:
                    parts = [p.strip() for p in raw.split(',') if p.strip()]
                    domains = parts or None
    except Exception:
        pass
    return email, domains


def _download_binary(url: str, output_path: str, timeout: int = 60) -> None:
    """以流方式下载二进制文件到指定路径。"""
    import requests
    headers = getattr(doi_src_mod, 'DEFAULT_HEADERS', {
        'User-Agent': 'Mozilla/5.0'
    })
    sess = getattr(doi_src_mod, 'session', requests.Session())
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with sess.get(url, headers=headers, timeout=timeout, stream=True) as r:
        r.raise_for_status()
        # 简单类型校验
        ctype = (r.headers.get('Content-Type') or '').lower()
        first = True
        with open(output_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 256):
                if not chunk:
                    continue
                if first:
                    if (('pdf' not in ctype) and not chunk.startswith(b'%PDF')):
                        raise ValueError(f'URL 不是 PDF 内容: {ctype}')
                    first = False
                f.write(chunk)


def resolve_pdf_via_doi_source(doi: str) -> Optional[str]:
    """使用 DOI_source 的三段式策略解析 PDF 直链。"""
    if doi_src_mod is None:
        return None
    email, domains = _load_download_cfg()
    # 1) Publisher
    try:
        get_pub = getattr(doi_src_mod, 'get_pdf_from_publisher', None)
        if callable(get_pub):
            url = get_pub(doi)
            if url:
                return url
    except Exception:
        pass
    # 2) Unpaywall
    try:
        get_oa = getattr(doi_src_mod, 'get_pdf_from_unpaywall', None)
        if callable(get_oa):
            url = get_oa(doi, email)
            if url:
                return url
    except Exception:
        pass
    # 3) Sci-Hub
    try:
        get_sh = getattr(doi_src_mod, 'GetDownloadUrl', None)
        if callable(get_sh):
            url = get_sh(doi, scihub_domains=domains)
            if url:
                return url
    except Exception:
        pass
    return None


def to_items_metadata(record_meta: Dict[str, Any], role: Optional[str] = None) -> Dict[str, Any]:
    """将 client.get_metadata 返回的结构转为主程序兼容的 items 元素。"""
    item: Dict[str, Any] = {
        "title": record_meta.get("title", ""),
        "doi": record_meta.get("doi", ""),
        "authors": record_meta.get("authors", []),
    }
    # 解析发布日期为 {year, month}
    published = parse_year_month(record_meta.get("publication_date"))
    if published:
        item["published"] = published
    # 附加一些有用字段（主程序加载会忽略不认识的字段）
    # 保留记录 ID（可选字段，不用于下载），以便后续定位
    item["record_id"] = record_meta.get("record_id")
    item["inspire_url"] = record_meta.get("inspire_url")
    item["citations_count"] = record_meta.get("citations", 0)
    if role:
        item["role"] = role  # main/reference/citation
    return item


# ---------------------------
# 年轻作者判定
# ---------------------------

AUTHOR_FIRST_YEAR_CACHE: Dict[str, Optional[int]] = {}


def extract_year_from_inspire_metadata(md: Dict[str, Any]) -> Optional[int]:
    """从 INSPIRE 原始 metadata 中尽可能提取年份。"""
    # 1) preprint_date: 'YYYY' or 'YYYY-MM' etc
    preprint = md.get("preprint_date")
    ym = parse_year_month(preprint)
    if "year" in ym:
        return ym["year"]
    # 2) publication_info[].year
    pub_infos = md.get("publication_info", []) or []
    if pub_infos and isinstance(pub_infos, list):
        year = pub_infos[0].get("year")
        if isinstance(year, int):
            return year
        if isinstance(year, str) and year.isdigit():
            return int(year)
    # 3) earliest_date / earliest_date: 'YYYY-MM-DD'
    earliest = md.get("earliest_date") or md.get("earliestdate")
    ym2 = parse_year_month(earliest)
    if "year" in ym2:
        return ym2["year"]
    return None


def get_author_first_year(client: Any, author_name: str) -> Optional[int]:
    """粗略获取作者首发年份：搜索作者文献，取最早年份。
    注：作者歧义可能导致噪声，本实现尽量取较小年份。
    结果加入缓存以减少请求。
    """
    if author_name in AUTHOR_FIRST_YEAR_CACHE:
        return AUTHOR_FIRST_YEAR_CACHE[author_name]
    min_year: Optional[int] = None
    try:
        # 使用 author: 精确字段；取前若干条记录
        results = client.search_literature(f"author:\"{author_name}\"", size=25)
        hits = results.get("hits", {}).get("hits", [])
        for h in hits:
            md = h.get("metadata", {})
            y = extract_year_from_inspire_metadata(md)
            if y is not None:
                if min_year is None or y < min_year:
                    min_year = y
        # 回退策略：find a 语法
        if min_year is None:
            results2 = client.search_literature(f"find a {author_name}", size=25)
            hits2 = results2.get("hits", {}).get("hits", [])
            for h in hits2:
                md = h.get("metadata", {})
                y = extract_year_from_inspire_metadata(md)
                if y is not None:
                    if min_year is None or y < min_year:
                        min_year = y
    except Exception:
        min_year = None
    AUTHOR_FIRST_YEAR_CACHE[author_name] = min_year
    return min_year


def compute_young_author_fields(client: Any, authors: List[str], pub_year: Optional[int], years_window: int) -> Dict[str, Any]:
    """计算年轻作者相关字段。
    young_scholar_index: 若存在至少一位作者满足 pub_year - first_year <= years_window 则为 1，否则 -1。
    附带 young_authors 列表与 author_first_years 映射，便于调试或后续处理。
    """
    result = {
        "young_scholar_index": -1,
        "young_authors": [],
        "author_first_years": {},
        "young_author_years_window": years_window,
    }
    if not authors or pub_year is None:
        return result
    young_any = False
    for name in authors:
        fy = get_author_first_year(client, name)
        if fy is not None:
            result["author_first_years"][name] = fy
            if 0 <= (pub_year - fy) <= years_window:
                young_any = True
                result["young_authors"].append(name)
    result["young_scholar_index"] = 1 if young_any else -1
    return result


def fetch_related_ids(client: Any, record_id: str, kind: str, limit: int) -> List[str]:
    """获取相关文献的记录 ID 列表。
    kind: "references" 或 "citations"
    """
    ids: List[str] = []
    try:
        if kind == "references":
            # 直接从记录元数据里解析 references
            record = client.get_record(record_id)
            refs = (record.get('metadata', {}) or {}).get('references', []) or []
            for ref in refs:
                rec = ref.get('record') if isinstance(ref, dict) else None
                if isinstance(rec, dict):
                    ref_url = rec.get('$ref') or rec.get('$REF') or rec.get('url')
                    if isinstance(ref_url, str) and '/literature/' in ref_url:
                        try:
                            rid = ref_url.rstrip('/').split('/')[-1]
                            if rid:
                                ids.append(str(rid))
                                if len(ids) >= limit:
                                    break
                            continue
                        except Exception:
                            pass
                    cn = rec.get('control_number') or rec.get('controlNumber')
                    if cn:
                        ids.append(str(cn))
                        if len(ids) >= limit:
                            break
        else:
            # 首选 citations 端点
            data = client.get_citations(record_id, size=limit)
            hits = (data.get('hits', {}) or {}).get('hits', []) or []
            for h in hits:
                rid = h.get('id') or (h.get('metadata', {}) or {}).get('control_number')
                if rid:
                    ids.append(str(rid))
                if len(ids) >= limit:
                    break
            # 回退：搜索语法 refersto:recid {id}
            if not ids:
                try:
                    results = client.search_literature(f"refersto:recid {record_id}", size=limit)
                    hits2 = (results.get('hits', {}) or {}).get('hits', []) or []
                    for h in hits2:
                        rid = h.get('id') or (h.get('metadata', {}) or {}).get('control_number')
                        if rid:
                            ids.append(str(rid))
                        if len(ids) >= limit:
                            break
                except Exception:
                    pass
    except Exception as e:
        print(f"⚠️ 获取{kind}失败: {e}")
    out = ids[:limit]
    # 可选调试：设置环境变量 IHD_DEBUG_RELATED=1 以记录解析情况
    try:
        if os.getenv('IHD_DEBUG_RELATED'):
            log_dir = PROJ_ROOT / 'log'
            log_dir.mkdir(parents=True, exist_ok=True)
            with open(log_dir / 'related_debug.txt', 'a', encoding='utf-8') as lf:
                lf.write(f"record={record_id} kind={kind} count={len(out)} ids={out[:10]}\n")
    except Exception:
        pass
    return out


# ---------------------------
# PDF URL 提取与下载（通过 DOI 或 直链 URL）
# ---------------------------

def _pdf_url_from_inspire_metadata_raw(md_raw: Dict[str, Any]) -> Optional[str]:
    # documents[].key 以 .pdf 结尾优先
    docs = md_raw.get("documents", []) or []
    for doc in docs:
        key = (doc.get("key") or "").lower()
        url = doc.get("url") or doc.get("source")
        if key.endswith(".pdf") and url:
            return url
        # 有些记录没有 .pdf 后缀，但给了 url 指向 pdf
        if url and str(url).lower().endswith('.pdf'):
            return url
    # 回退 arXiv eprint
    eprints = md_raw.get("arxiv_eprints", []) or []
    if eprints:
        arxiv_id = eprints[0].get("value")
        if arxiv_id:
            return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    return None


def download_pdf_by_url(client: Any, url: str, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    client.download_file(url, output_path)


def _sanitize_dir_name(name: str) -> str:
    return (
        name.replace('/', '_')
        .replace('\\', '_')
        .replace(':', '_')
        .replace('?', '_')
        .replace('*', '_')
        .replace('"', "'")
        .replace('<', '_')
        .replace('>', '_')
        .replace('|', '_')
    )


def dir_name_from_metadata(meta_norm: Dict[str, Any]) -> str:
    doi = meta_norm.get('doi')
    if doi:
        return _sanitize_dir_name(doi)
    # 回退 arxiv_id
    aid = meta_norm.get('arxiv_id')
    if aid:
        return _sanitize_dir_name(aid)
    # 最后回退 record_id（不用于下载，仅作为文件夹名）
    rid = meta_norm.get('record_id') or 'unknown'
    return _sanitize_dir_name(str(rid))


def process_one_by_doi(client: Any, doi: str, out_dir: str, download: bool = True, years_window: Optional[int] = None, *, compute_young: bool = True) -> Dict[str, Any]:
    """基于 DOI 处理单篇：优先用 DOI 或 URL 下载 PDF，不依赖 record_id 作为输入。"""
    ensure_dir(out_dir)
    # 命中记录（含原始 metadata，可直接提取 PDF URL）
    hit = client.find_record_by_doi(doi)
    if not hit:
        raise ValueError(f"未找到 DOI={doi} 的记录")
    rid = str(hit.get('id'))  # 仅用于获取规范化元数据与相关关系
    md_raw = hit.get('metadata', {}) or {}

    # 写入元数据（规范化）
    meta_norm = client.get_metadata(rid)
    item = to_items_metadata(meta_norm)

    # 目录名基于 DOI/ArXiv/rid
    # 注意：传入的 out_dir 已是目标目录；上层确保按 dir_name_from_metadata 命名
    # 下载 PDF（可选）
    pdf_filename = f"{_sanitize_dir_name(doi)}.pdf"
    pdf_path = os.path.join(out_dir, pdf_filename)
    if download:
        pdf_url = _pdf_url_from_inspire_metadata_raw(md_raw)
        if pdf_url:
            try:
                # 优先走 client 下载（保持统一），若失败则直接 HTTP 下载
                try:
                    download_pdf_by_url(client, pdf_url, pdf_path)
                except Exception:
                    _download_binary(pdf_url, pdf_path)
            except Exception as e:
                print(f"警告: 无法下载 PDF ({pdf_url}): {e}")
    # 仅在存在 PDF 时写入 metadata；否则删除残留的 metadata
    meta_path = os.path.join(out_dir, f"{_sanitize_dir_name(doi)}_metadata.json")
    if os.path.exists(pdf_path):
        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(meta_norm, f, ensure_ascii=False, indent=2)
    else:
        try:
            if os.path.exists(meta_path):
                os.remove(meta_path)
        except Exception:
            pass

    # 年轻作者增强（可关闭以加速）
    if compute_young:
        if years_window is None:
            years_window = get_young_author_years()
        pub_year = None
        if "published" in item and isinstance(item["published"], dict):
            pub_year = item["published"].get("year")
        ya = compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
        item.update(ya)
    return item


def process_one_by_record_id_using_url(client: Any, record_id: str, out_dir: str, download: bool = True, years_window: Optional[int] = None, *, compute_young: bool = False) -> Dict[str, Any]:
    """用于关联文献：由 record_id 获取原始 metadata，提取 URL/DOI 后按 URL/DOI 下载 PDF。"""
    ensure_dir(out_dir)
    rec = client.get_record(record_id)
    md_raw = rec.get('metadata', {}) or {}
    meta_norm = client.get_metadata(record_id)
    item = to_items_metadata(meta_norm)

    # 准备文件名（无论是否下载）
    base_name = dir_name_from_metadata(meta_norm)
    pdf_path = os.path.join(out_dir, f"{base_name}.pdf")
    meta_path = os.path.join(out_dir, f"{base_name}_metadata.json")
    # 下载 PDF 优先 URL（documents/arXiv）
    if download:
        pdf_url = _pdf_url_from_inspire_metadata_raw(md_raw)
        if pdf_url:
            try:
                try:
                    download_pdf_by_url(client, pdf_url, pdf_path)
                except Exception:
                    _download_binary(pdf_url, pdf_path)
            except Exception as e:
                print(f"警告: 关联文献 PDF 下载失败 ({pdf_url}): {e}")
    # 仅在存在 PDF 时写元数据；否则删除残留的元数据
    if os.path.exists(pdf_path):
        with open(meta_path, 'w', encoding='utf-8') as f:
            json.dump(meta_norm, f, ensure_ascii=False, indent=2)
    else:
        try:
            if os.path.exists(meta_path):
                os.remove(meta_path)
        except Exception:
            pass

    # 年轻作者增强（默认关闭以加速）
    if compute_young:
        if years_window is None:
            years_window = get_young_author_years()
        pub_year = None
        if "published" in item and isinstance(item["published"], dict):
            pub_year = item["published"].get("year")
        ya = compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
        item.update(ya)
    return item


def _pdf_exists_for_metadata(meta_path: Path) -> bool:
    """判断与 *_metadata.json 同名的 .pdf 是否已存在。"""
    stem = meta_path.name[:-len("_metadata.json")] if meta_path.name.endswith("_metadata.json") else meta_path.stem
    pdf_path = meta_path.parent / f"{stem}.pdf"
    return pdf_path.exists()


def _download_pdf_for_metadata(client: Any, meta_path: Path) -> Tuple[bool, str]:
    """给定 *_metadata.json，尝试下载对应 PDF 到同目录。

    返回 (success, message)。
    """
    try:
        with open(meta_path, "r", encoding="utf-8") as f:
            meta_norm = json.load(f)
        # 解析 record_id；若无则尝试从 inspire_url 或 doi 推断
        rid = meta_norm.get("record_id")
        if not rid:
            ins_url = meta_norm.get("inspire_url")
            if isinstance(ins_url, str) and "/literature/" in ins_url:
                rid = ins_url.rstrip("/").split("/")[-1]
        if not rid:
            doi = meta_norm.get("doi")
            if doi:
                hit = InspireHEPClient().find_record_by_doi(doi)
                if hit:
                    rid = str(hit.get("id"))
        if not rid:
            return False, "缺少 record_id/doi，无法定位记录"

        # 获取原始 metadata 以提取 PDF URL
        client2 = InspireHEPClient()
        rec = client2.get_record(str(rid))
        md_raw = rec.get("metadata", {}) or {}
        url = _pdf_url_from_inspire_metadata_raw(md_raw)
        if not url:
            return False, "未找到 PDF URL"
        # 输出文件名与目录
        base = meta_path.name[:-len("_metadata.json")] if meta_path.name.endswith("_metadata.json") else meta_path.stem
        out_pdf = meta_path.parent / f"{base}.pdf"
        download_pdf_by_url(client2, url, str(out_pdf))
        return True, f"下载完成: {out_pdf}"
    except Exception as e:
        return False, f"下载失败: {e}"


def _walk_metadata_jsons(data_root: Path, teacher: str, subdirs: Optional[List[str]]) -> List[Path]:
    t_root = data_root / teacher
    found: List[Path] = []
    if not t_root.exists():
        return found
    targets = subdirs or ["main", "ref1", "cited"]
    for sd in targets:
        base = t_root / sd
        if not base.exists():
            continue
        # 递归查找 *_metadata.json
        found.extend(base.rglob("*_metadata.json"))
    return found


def _run_from_data(args: argparse.Namespace) -> int:
    data_root = Path(args.data_root).resolve()
    teacher = args.teacher
    subdirs = [s.strip() for s in (args.subdirs.split(",") if args.subdirs else []) if s.strip()] or None

    metas = _walk_metadata_jsons(data_root, teacher, subdirs)
    if not metas:
        print(f"未在 {data_root / teacher} 下找到任何 *_metadata.json")
        return 0

    # 过滤已存在 PDF 的条目
    pending = [m for m in metas if not _pdf_exists_for_metadata(m)]
    print(f"共发现元数据 {len(metas)} 个；待下载 PDF {len(pending)} 个（并发 {args.workers}）")
    if not pending:
        return 0

    def task(meta_path: Path) -> str:
        ok, msg = _download_pdf_for_metadata(InspireHEPClient(), meta_path)
        prefix = "✓" if ok else "✗"
        return f"{prefix} {meta_path.parent.name}/{meta_path.name}: {msg}"

    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for res in pool.map(task, pending):
            print(res)
    return 0


def main():
    parser = argparse.ArgumentParser(description="根据 DOI 下载论文及其相关文献，或根据 data/<老师> 下的 *_metadata.json 批量补全 PDF（INSPIRE-HEP）")

    mx = parser.add_mutually_exclusive_group(required=True)
    mx.add_argument("--doi", help="论文 DOI，例如 10.1234/abc")
    mx.add_argument("--from-data", action="store_true", help="根据 data/<老师> 下的 *_metadata.json 补齐缺失的 PDF")

    parser.add_argument("-o", "--output-dir", default=".", help="输出目录（默认当前目录）；仅 --doi 模式使用")
    parser.add_argument("--related-limit", type=int, default=10, help="每类相关文献（被引/参考）的最大数量；仅 --doi 模式使用")
    parser.add_argument("--no-related-downloads", action="store_true", help="不下载相关文献的 PDF/元数据，只做索引；仅 --doi 模式使用")

    # from-data 模式参数
    parser.add_argument("--data-root", default=str(PROJ_ROOT / "data"), help="data 根目录（包含 <老师>/main|ref1|cited）")
    parser.add_argument("--teacher", default=None, help="老师名（必填，用于 --from-data 模式）")
    parser.add_argument("--subdirs", default=None, help="限定子目录，逗号分隔（如 main,ref1,cited）；不填则三者都扫")
    parser.add_argument("--workers", type=int, default=6, help="并发下载 PDF 线程数（--from-data 模式）")

    args = parser.parse_args()

    if args.from_data:
        if not args.teacher:
            print("--from-data 模式下必须提供 --teacher")
            return 1
        return _run_from_data(args)

    # --doi 模式
    client = InspireHEPClient()

    # 1) 通过 DOI 定位记录
    hit = client.find_record_by_doi(args.doi)
    if not hit:
        print(f"未找到 DOI={args.doi} 对应的 INSPIRE 记录。")
        return 1

    record_id = str(hit.get("id"))
    print(f"找到记录 ID: {record_id}")

    root_out = os.path.abspath(args.output_dir)
    ensure_dir(root_out)

    # 2) 下载主文献（按 DOI/URL 路径，不依赖 record_id 下载 PDF）
    years_window = get_young_author_years()
    main_dir = os.path.join(root_out, _sanitize_dir_name(args.doi))
    main_item = process_one_by_doi(client, args.doi, main_dir, download=True, years_window=years_window)
    main_item["role"] = "main"

    # 3) 索引并（可选）下载被引与参考
    items: List[Dict[str, Any]] = [main_item]

    # references
    ref_ids = fetch_related_ids(client, record_id, kind="references", limit=args.related_limit)
    if ref_ids:
        refs_dir = os.path.join(main_dir, "references")
        ensure_dir(refs_dir)
        for rid in ref_ids:
            print(f"处理参考文献 {rid} ...")
            try:
                item = process_one_by_record_id_using_url(client, rid, os.path.join(refs_dir, str(rid)), download=not args.no_related_downloads, years_window=years_window)
                item["role"] = "reference"
                items.append(item)
            except Exception as e:
                print(f"⚠️ 处理参考文献 {rid} 失败: {e}")

    # citations
    cit_ids = fetch_related_ids(client, record_id, kind="citations", limit=args.related_limit)
    if cit_ids:
        cits_dir = os.path.join(main_dir, "citations")
        ensure_dir(cits_dir)
        for rid in cit_ids:
            print(f"处理被引文献 {rid} ...")
            try:
                item = process_one_by_record_id_using_url(client, rid, os.path.join(cits_dir, str(rid)), download=not args.no_related_downloads, years_window=years_window)
                item["role"] = "citation"
                items.append(item)
            except Exception as e:
                print(f"⚠️ 处理被引文献 {rid} 失败: {e}")

    # 4) 生成与主程序一致的元数据（items 数组）
    items_manifest = {"items": items}
    manifest_path = os.path.join(main_dir, "metadata_items.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(items_manifest, f, ensure_ascii=False, indent=2)
    print(f"✓ 元数据清单已保存: {manifest_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
