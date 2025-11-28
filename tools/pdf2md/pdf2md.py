import argparse
import requests
import os
from pathlib import Path
import uuid
import time
import zipfile
import shutil
import json
from collections import defaultdict
import hashlib


def _build_header(token: str) -> dict:
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }


def _converted_stems(output_dir: Path) -> set[str]:
    """返回已转换完成（或已下载结果包）的文件 stem 集合，用于跳过重复转换。

    规则：
    - 存在同名 .md 视为已完成
    - 或者存在同名 .zip（API 返回的结果包）也视为已完成
    """
    output_dir = Path(output_dir)
    md_set = {p.stem for p in output_dir.rglob("*.md")}
    zip_set = {p.stem for p in output_dir.rglob("*.zip")}
    return md_set | zip_set


def new_files(file_dir: str | Path, output_dir: str | Path) -> dict[str, list[str]]:
    file_dir = Path(file_dir)
    output_dir = Path(output_dir)
    converted = _converted_stems(output_dir)
    candidates = [p for p in file_dir.rglob("*.pdf") if p.stem not in converted]
    uniq: dict[str, list[str]] = defaultdict(list)
    for p in candidates:
        uniq[p.stem].append(str(p.relative_to(file_dir)))
    return dict(uniq)


def files(file_dir: str | Path) -> dict[str, list[str]]:
    file_dir = Path(file_dir)
    all_files = [p for p in file_dir.rglob("*.pdf")]
    uniq: dict[str, list[str]] = defaultdict(list)
    for p in all_files:
        uniq[p.stem].append(str(p.relative_to(file_dir)))
    return dict(uniq)


def _file_signature(path: Path, sample_bytes: int = 4 * 1024 * 1024) -> str:
    """计算 PDF 的签名用于去重：size + sha1(前 sample_bytes)。"""
    try:
        size = path.stat().st_size
        h = hashlib.sha1()
        with open(path, 'rb') as f:
            chunk = f.read(sample_bytes)
            h.update(chunk)
        return f"{size}-" + h.hexdigest()
    except Exception:
        return f"0-err-{path.name}"


def _is_converted_rel(output_dir: Path, rel_pdf: Path) -> bool:
    md_path = output_dir / rel_pdf.with_suffix('.md')
    zip_path = output_dir / rel_pdf.with_suffix('.zip')
    return md_path.exists() or zip_path.exists()


def _gather_candidates_and_duplicates(file_dir: Path, output_dir: Path, subdirs: list[str] | None) -> tuple[dict[str, list[str]], dict[str, str]]:
    """收集未转换的候选 PDF（去重后）与重复映射。

    返回：
    - uniques: {stem: [rel_pdf_path]} 仅包含每个签名的首要条目，用于上传与转换
    - duplicates_map: {dup_rel: primary_rel} 将重复 PDF 的相对路径映射到首要条目相对路径
    规则：
    - 仅考虑尚未在 output_dir 生成 .md 或 .zip 的条目为候选；
    - 以内容签名（大小+sha1(前4MB)）为分组，优先选择已转换过的路径为主（若组内存在），否则选择组内第一个；
    - 其余同签名的路径加入 duplicates_map。
    """
    # 1) 列举目标范围的全部 PDF 相对路径
    rel_pdfs: list[Path] = []
    if subdirs:
        for sd in subdirs:
            sd_root = file_dir / sd
            if not sd_root.exists():
                continue
            for p in sd_root.rglob('*.pdf'):
                rel_pdfs.append(Path(sd) / p.relative_to(sd_root))
    else:
        for p in (file_dir.rglob('*.pdf')):
            rel_pdfs.append(p.relative_to(file_dir))

    # 2) 根据签名分组（只对未转换者考虑去重；但选择主项时优先用已转换者，以便后续复制）
    groups: dict[str, list[Path]] = defaultdict(list)
    sig_cache: dict[Path, str] = {}
    for rel in rel_pdfs:
        abs_pdf = file_dir / rel
        sig = _file_signature(abs_pdf)
        sig_cache[rel] = sig
        groups[sig].append(rel)

    uniques: dict[str, list[str]] = {}
    duplicates_map: dict[str, str] = {}
    for sig, rel_list in groups.items():
        # 组内若某路径已转换，则选择其为主；否则选择首个未转换的路径为主
        primary_rel: Path | None = None
        # 优先：已经转换的（这样本次无需上传，后续直接复制）
        for rel in rel_list:
            if _is_converted_rel(output_dir, rel):
                primary_rel = rel
                break
        # 其次：第一个未转换的
        if primary_rel is None:
            for rel in rel_list:
                if not _is_converted_rel(output_dir, rel):
                    primary_rel = rel
                    break
        if primary_rel is None:
            # 整组都已转换，标记其余为重复复制即可
            primary_rel = rel_list[0]
        # 记录 duplicates_map（组内其他路径 -> 主路径）
        for rel in rel_list:
            if rel != primary_rel:
                duplicates_map[str(rel)] = str(primary_rel)
        # 若主路径尚未转换，加入 uniques 参与上传
        if not _is_converted_rel(output_dir, primary_rel):
            stem = primary_rel.stem
            uniques.setdefault(stem, []).append(str(primary_rel))

    return uniques, duplicates_map


def _replicate_duplicates(duplicates_map: dict[str, str], output_dir: Path):
    """将主路径的 .md/.json 复制到重复路径对应位置。忽略缺失的主文件。"""
    for dup_rel, primary_rel in duplicates_map.items():
        dup_md = output_dir / Path(dup_rel).with_suffix('.md')
        dup_json = output_dir / Path(dup_rel).with_suffix('.json')
        pri_md = output_dir / Path(primary_rel).with_suffix('.md')
        pri_json = output_dir / Path(primary_rel).with_suffix('.json')
        # 复制 MD
        if pri_md.exists():
            dup_md.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy(pri_md, dup_md)
            except Exception as e:
                print(f"复制重复MD失败 {pri_md} -> {dup_md}: {e}")
        # 复制 JSON（若存在）
        if pri_json.exists():
            dup_json.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy(pri_json, dup_json)
            except Exception as e:
                print(f"复制重复JSON失败 {pri_json} -> {dup_json}: {e}")


def batch_upload(file_names: list[str], unique_dict: dict[str, list[str]], file_dir: Path, header: dict) -> str | None:
    url = "https://mineru.org.cn/api/v4/file-urls/batch"
    data = {
        "is_ocr": False,
        "enable_formula": True,
        "enable_table": True,
        "model_version": "vlm",
        "language": None,
        "is_chem": False,
        "files": [
            {"name": f"{filename}.pdf", "data_id": str(uuid.uuid4())}
            for filename in file_names
        ]
    }

    try:
        response = requests.post(url, headers=header, json=data)
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                for i in range(0, len(urls)):
                    with open(file_dir / Path(unique_dict[file_names[i]][0]), 'rb') as f:
                        res_upload = requests.put(urls[i], data=f)
                        if res_upload.status_code == 200:
                            print(f"Uploaded: {file_names[i]}")
                        else:
                            print(f"Upload failed for: {file_names[i]}")
                return batch_id
            else:
                print(f"Apply upload url failed: {result}")
        else:
            print(f"HTTP {response.status_code}: {response.text}")
    except Exception as err:
        print(err)
    return None


def batch_retrieve(batch_id: str, unique_dict: dict[str, list[str]], file_dir: Path, output_dir: Path, header: dict):
    max_retry = 180
    retry = 0
    done = False
    done_files = set()
    url = f"https://mineru.org.cn/api/v4/extract-results/batch/{batch_id}"
    os.makedirs(output_dir, exist_ok=True)
    while not done:
        res = requests.get(url, headers=header)
        res.raise_for_status()
        payload = res.json()
        result = ((payload or {}).get("data") or {}).get("extract_result") or []
        if retry > max_retry:
            print([file for file in result if file.get("state") != "done"])
        if result and all(file.get("state") == "done" for file in result):
            done = True
            print(f"{len(result)} all files done")
        for item in result:
            file = Path(item.get("file_name", "")).with_suffix(".zip")
            if str(file) not in done_files and item.get("state") == "done":
                done_files.add(str(file))
                zip_url = item.get("full_zip_url")
                if not zip_url:
                    continue
                response = requests.get(zip_url, stream=True)
                response.raise_for_status()
                stem = Path(item.get("file_name", "")).stem
                path = unique_dict.get(stem, [stem])[0]
                file_path = output_dir / Path(path).with_suffix(".zip")
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                print(f"下载完成: {file_path}")
        print("Polling...")
        time.sleep(2)
        retry += 1


def process_zip_file(zip_path: Path):
    parent_dir = zip_path.parent
    stem_name = zip_path.stem
    images_output = parent_dir / "images"
    images_output.mkdir(exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            members = [info for info in zf.infolist() if not info.is_dir()]

            has_full_md = False
            has_full_json = False
            for info in members:
                filename = info.filename.strip('/')

                if filename == 'full.md':
                    md_target = parent_dir / f"{stem_name}.md"
                    if not md_target.exists():
                        with zf.open(info) as src, open(md_target, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                        print(f"生成: {md_target}")
                    has_full_md = True
                elif filename == 'full.json':
                    json_target = parent_dir / f"{stem_name}.json"
                    if not json_target.exists():
                        with zf.open(info) as src, open(json_target, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                        print(f"生成JSON: {json_target}")
                    has_full_json = True
                elif filename.startswith('images/') or filename.startswith('./images/'):
                    rel_path = Path(filename.replace('\\', '/').lstrip('./'))
                    if rel_path.parts and rel_path.parts[0] == 'images':
                        target_file = images_output / '/'.join(rel_path.parts[1:])
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        with zf.open(info) as src, open(target_file, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                        print(f"添加图片: {target_file}")
            if not has_full_md:
                print(f"警告: {zip_path} 不包含 full.md")
            # full.json 可选
    except Exception as e:
        print(f"失败 {zip_path}: {e}")


def process_all_zips(root_dir: Path):
    root_dir = Path(root_dir)
    if not root_dir.exists():
        raise FileNotFoundError(f"目录不存在: {root_dir}")
    zip_files = sorted(root_dir.rglob("*.zip"))
    if not zip_files:
        print("没有找到任何 .zip 文件")
        return
    for zip_path in zip_files:
        print(f"\n正在处理: {zip_path}")
        process_zip_file(zip_path)


def replicate_files(file_dict: dict[str, list[str]], output_dir: Path):
    """将已生成的 .md 和识别到的 .json 按相同相对路径复制到 data 对应位置。

    行为：
    - 若存在某一相对路径对应的 .md，则以该 .md 为源复制到同 stem 的其他目标路径。
    - 若不存在 .md 但存在 .json（识别结果），也会以该 .json 为源复制到同 stem 的其他目标路径。
    - 当 .md 存在时，仍会同步其旁边的 .json（若有）。
    """
    for title, paths in file_dict.items():
        md_candidates = [Path(output_dir) / Path(p).with_suffix(".md") for p in paths]
        json_candidates = [Path(output_dir) / Path(p).with_suffix(".json") for p in paths]

        # 源优先选择：md > json
        existing_md = next((p for p in md_candidates if p.exists()), None)
        existing_json = next((p for p in json_candidates if p.exists()), None)
        if not existing_md and not existing_json:
            print(f"⚠️ 未找到 '{title}' 的任何已转换文件（.md 或 .json）！")
            continue

        # 复制 MD（若存在）
        if existing_md:
            for target_md in md_candidates:
                if target_md == existing_md:
                    continue
                target_md.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(existing_md, target_md)

        # 同步 JSON：
        # 1) 优先使用与 existing_md 同目录同名的 .json；
        # 2) 若不存在，则回退到任一已存在的 json（existing_json）。
        src_json = None
        md_side_json = existing_md.with_suffix('.json') if existing_md else None
        if md_side_json and md_side_json.exists():
            src_json = md_side_json
        elif existing_json and existing_json.exists():
            src_json = existing_json

        if src_json:
            for target_json in json_candidates:
                if target_json == src_json:
                    continue
                target_json.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.copy(src_json, target_json)
                except Exception as e:
                    print(f"复制 JSON 失败 {src_json} -> {target_json}: {e}")


def convert_pdfs_to_md(teacher: str, pdf_root: str | Path, md_root: str | Path, token: str, subdirs: list[str] | None = None, limit: int | None = None):
    pdf_root = Path(pdf_root)
    md_root = Path(md_root)
    file_dir = pdf_root / teacher
    output_dir = md_root / teacher
    uniques, duplicates_map = _gather_candidates_and_duplicates(file_dir, output_dir, subdirs)

    if not uniques:
        print("没有新的PDF需要转换。")
        return

    # 按需要限制数量
    file_names = list(uniques.keys())
    if limit is not None and limit > 0:
        file_names = file_names[:limit]

    # 记录任务与重复映射
    try:
        with open("task.json", "w", encoding="utf-8") as file:
            json.dump(uniques, file, ensure_ascii=False, indent=4)
        with open("duplicates.json", "w", encoding="utf-8") as fdup:
            json.dump(duplicates_map, fdup, ensure_ascii=False, indent=2)
    except Exception:
        pass

    header = _build_header(token)
    batch_id = batch_upload(file_names, uniques, file_dir, header)
    if not batch_id:
        print("申请上传批次失败，已中止。")
        return

    print(f"BatchId: {batch_id}")
    batch_retrieve(batch_id, uniques, file_dir, output_dir, header)
    process_all_zips(output_dir)
    replicate_files(files(file_dir), output_dir)
    # 将主路径转换结果复制到重复路径
    _replicate_duplicates(duplicates_map, output_dir)


def resume_with_batch(batch_id: str, teacher: str, pdf_root: str | Path, md_root: str | Path, token: str, task_file: str = "task.json"):
    """根据上次保存的 task.json（stem -> 相对路径）恢复批次结果下载与解包。"""
    pdf_root = Path(pdf_root)
    md_root = Path(md_root)
    file_dir = pdf_root / teacher
    output_dir = md_root / teacher
    header = _build_header(token)
    try:
        with open(task_file, "r", encoding="utf-8") as f:
            uniques = json.load(f)
    except Exception as e:
        print(f"无法读取任务文件 {task_file}：{e}")
        return
    # 尝试读取重复映射
    duplicates_map: dict[str, str] = {}
    try:
        with open("duplicates.json", "r", encoding="utf-8") as fdup:
            duplicates_map = json.load(fdup)
    except Exception:
        duplicates_map = {}
    batch_retrieve(batch_id, uniques, file_dir, output_dir, header)
    process_all_zips(output_dir)
    replicate_files(files(file_dir), output_dir)
    _replicate_duplicates(duplicates_map, output_dir)


def main():
    ap = argparse.ArgumentParser(description="批量将 data/<教师> 下的PDF转换为Markdown到 data/<教师>")
    ap.add_argument('--teacher', required=True, help='教师名称（用于文件夹名）')
    ap.add_argument('--pdf-root', default=str(Path(__file__).resolve().parents[2] / 'data'), help='PDF根目录，默认 ../../data')
    ap.add_argument('--md-root', default=str(Path(__file__).resolve().parents[2] / 'data'), help='MD输出根目录，默认 ../../data')
    ap.add_argument('--token', default=os.getenv('MINERU_TOKEN', ''), help='MinerU API Token，默认读环境变量 MINERU_TOKEN')
    ap.add_argument('--subdirs', default=None, help='仅处理这些子目录，逗号分隔，例如 main,ref1,cited')
    ap.add_argument('--limit', type=int, default=None, help='最多处理的文件数（可选）')
    ap.add_argument('--resume-batch', default=None, help='仅恢复指定 batch_id 的结果下载（依赖 task.json）')
    args = ap.parse_args()

    if not args.token:
        print('缺少 MinerU Token，请通过 --token 或环境变量 MINERU_TOKEN 提供。')
        return

    subdirs = [s.strip() for s in args.subdirs.split(',')] if args.subdirs else None
    if args.resume_batch:
        resume_with_batch(args.resume_batch, args.teacher, args.pdf_root, args.md_root, args.token)
    else:
        convert_pdfs_to_md(args.teacher, args.pdf_root, args.md_root, args.token, subdirs=subdirs, limit=args.limit)


if __name__ == '__main__':
    main()
