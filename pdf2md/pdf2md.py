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


def _build_header(token: str) -> dict:
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }


def new_files(file_dir: str | Path, output_dir: str | Path) -> dict[str, list[str]]:
    file_dir = Path(file_dir)
    output_dir = Path(output_dir)
    converted = {p.stem for p in output_dir.rglob("*.md")}
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
    for title, paths in file_dict.items():
        path_objects = [Path(output_dir) / Path(p).with_suffix(".md") for p in paths]
        existing_file = next((p for p in path_objects if p.exists()), None)
        if existing_file is None:
            print(f"⚠️ 未找到 '{title}' 的任何源文件！")
            continue
        # 复制到目标路径
        for target_path in path_objects:
            if target_path == existing_file:
                continue
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(existing_file, target_path)
        # 同步JSON
        existing_json = existing_file.with_suffix('.json')
        if existing_json.exists():
            for target_path in path_objects:
                if target_path == existing_file:
                    continue
                target_json = target_path.with_suffix('.json')
                target_json.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(existing_json, target_json)


def convert_pdfs_to_md(teacher: str, pdf_root: str | Path, md_root: str | Path, token: str, subdirs: list[str] | None = None, limit: int | None = None):
    pdf_root = Path(pdf_root)
    md_root = Path(md_root)
    file_dir = pdf_root / teacher
    output_dir = md_root / teacher
    if subdirs:
        # 仅在这些子目录内转换
        pdf_paths = []
        for sd in subdirs:
            pdf_paths.append(file_dir / sd)
        # 临时聚合目录到一个 temp 根以便 new_files 逻辑
        # 这里直接针对每个子目录分别处理
        uniques: dict[str, list[str]] = {}
        for sd in subdirs:
            u = new_files(file_dir / sd, output_dir / sd)
            uniques.update({k: [str(Path(sd) / Path(v[0]))] for k, v in u.items()})
    else:
        uniques = new_files(file_dir, output_dir)

    if not uniques:
        print("没有新的PDF需要转换。")
        return

    # 按需要限制数量
    file_names = list(uniques.keys())
    if limit is not None and limit > 0:
        file_names = file_names[:limit]

    # 记录任务
    try:
        with open("task.json", "w", encoding="utf-8") as file:
            json.dump(uniques, file, ensure_ascii=False, indent=4)
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


def main():
    ap = argparse.ArgumentParser(description="批量将 Downloads_pdf/<教师> 下的PDF转换为Markdown到 Downloads_md/<教师>")
    ap.add_argument('--teacher', required=True, help='教师名称（用于文件夹名）')
    ap.add_argument('--pdf-root', default=str(Path(__file__).resolve().parents[1] / 'Downloads_pdf'), help='PDF根目录，默认 ../Downloads_pdf')
    ap.add_argument('--md-root', default=str(Path(__file__).resolve().parents[1] / 'Downloads_md'), help='MD输出根目录，默认 ../Downloads_md')
    ap.add_argument('--token', default=os.getenv('MINERU_TOKEN', ''), help='MinerU API Token，默认读环境变量 MINERU_TOKEN')
    ap.add_argument('--subdirs', default=None, help='仅处理这些子目录，逗号分隔，例如 main,ref1,ref2')
    ap.add_argument('--limit', type=int, default=None, help='最多处理的文件数（可选）')
    args = ap.parse_args()

    if not args.token:
        print('缺少 MinerU Token，请通过 --token 或环境变量 MINERU_TOKEN 提供。')
        return

    subdirs = [s.strip() for s in args.subdirs.split(',')] if args.subdirs else None
    convert_pdfs_to_md(args.teacher, args.pdf_root, args.md_root, args.token, subdirs=subdirs, limit=args.limit)


if __name__ == '__main__':
    main()