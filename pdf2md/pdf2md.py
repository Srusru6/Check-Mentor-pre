import requests
import os
from pathlib import Path
import uuid
import time
import zipfile
import tempfile
import shutil
import json
from collections import defaultdict


file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Downloads_pdf", "王剑威")
output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Downloads_md", "王剑威")

token = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIwMzA2OTgiLCJyb2wiOiJST0xFX1JFR0lTVEVSLFJPTEVfREFUQVNFVCIsImlzcyI6Ik9wZW5YTGFiIiwiaWF0IjoxNzM2NDc2NTM0LCJjbGllbnRJZCI6IjRtMndvbmVta3Yycm0zN253ZW44IiwicGhvbmUiOiIiLCJ1dWlkIjoiOGFmYmY3YzUtYzQ4NS00ODg5LWFlZjQtZDczZDM5ZmZmZGRjIiwiZW1haWwiOiJPcGVuRGF0YUxhYkBwamxhYi5vcmcuY24iLCJleHAiOjE4OTQxNTY1MzR9.zsobQWe9Wn5XpWdVrBUdZOVfkWLSXOiWUfwUtgnUuqcrY5BUsgtsgsFhKNd8en79Ho_2QzxNySYYHuSrEiRGFQ"
header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

def new_files():
    converted = [p.stem for p in Path(output_dir).rglob("*.md")]
    new_files = [p for p in Path(file_dir).rglob("*.pdf") if p.stem not in converted]
    unique_dict = defaultdict(list)
    for p in new_files:
        unique_dict[p.stem].append(str(p.relative_to(Path(file_dir))))
    return unique_dict

def files():
    all_files = [p for p in Path(file_dir).rglob("*.pdf")]
    unique_dict = defaultdict(list)
    for p in all_files:
        unique_dict[p.stem].append(str(p.relative_to(Path(file_dir))))
    return unique_dict

unique_dict = new_files()
with open("task.json", "w", encoding="utf-8") as file:
    json.dump(dict(unique_dict), file, ensure_ascii=False, indent=4)
file_names = list(dict(unique_dict).keys())[:199]
print(len(file_names))

def batch_upload():
    url = "https://mineru.org.cn/api/v4/file-urls/batch"
    data = {
        "is_ocr": False,
        "enable_formula": True,
        "enable_table": True,
        "model_version": "vlm",
        "language": None,
        "is_chem": False,
        "files": [
            {
                "name": f"{filename}.pdf",
                "data_id": str(uuid.uuid4())
            }
            for filename in file_names
        ]
    }
    
    try:
        response = requests.post(url,headers=header,json=data)
        if response.status_code == 200:
            result = response.json()
            print('response success. result:{}'.format(result))
            if result["code"] == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                print('batch_id:{},urls:{}'.format(batch_id, urls))
                for i in range(0, len(urls)):
                    with open(Path(file_dir) / Path(unique_dict[file_names[i]][0]), 'rb') as f:
                        res_upload = requests.put(urls[i], data=f)
                        if res_upload.status_code == 200:
                            print(f"{urls[i]} upload success")
                        else:
                            print(f"{urls[i]} upload failed")
                return batch_id
            else:
                print('apply upload url failed,reason:{}'.format(result.msg))
        else:
            print('response not success. status:{} ,result:{}'.format(response.status_code, response.text))
    except Exception as err:
        print(err)

def batch_retrieve(batch_id):
    max_retry = 180
    retry = 0
    done = False
    done_files = set([])
    url = f"https://mineru.org.cn/api/v4/extract-results/batch/{batch_id}"
    os.makedirs(output_dir, exist_ok=True)
    while not done:
        res = requests.get(url, headers=header)
        result = res.json()["data"]["extract_result"]
        if retry > max_retry:
            print([file for file in result if file["state"] != "done"])
        if all(file["state"] == "done" for file in result):
            done = True
            print(f"{len(result)} all files done")
        for item in result:
            file = Path(item["file_name"]).with_suffix(".zip")
            if str(file) not in done_files and item["state"] == "done":
                done_files.add(str(file))
                zip_url = item["full_zip_url"]
                response = requests.get(zip_url, stream=True)
                response.raise_for_status()
                path = unique_dict[Path(item["file_name"]).stem][0]
                file_path = Path(output_dir) / Path(path).with_suffix(".zip")
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"文件已下载并保存至: {file_path}")
        print("new query...")
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
            for info in members:
                filename = info.filename.strip('/')

                if filename == 'full.md':
                    md_target = parent_dir / f"{stem_name}.md"
                    if not md_target.exists():
                        with zf.open(info) as src, open(md_target, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                        print(f"生成: {md_target}")
                    has_full_md = True
                elif filename.startswith('images/') or filename.startswith('./images/'):
                    rel_path = Path(filename.replace('\\', '/').lstrip('./'))
                    if rel_path.parts[0] == 'images':
                        target_file = images_output / '/'.join(rel_path.parts[1:])
                        target_file.parent.mkdir(parents=True, exist_ok=True)

                        with zf.open(info) as src, open(target_file, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                        print(f"添加图片: {target_file}")
            if not has_full_md:
                print(f"警告: {zip_path} 不包含 full.md")

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

batch_id = batch_upload()
print(batch_id)
batch_retrieve(batch_id)

process_all_zips(Path(output_dir))


def replicate_files(file_dict: dict):
    for title, paths in file_dict.items():
        path_objects = [Path(output_dir) / Path(p).with_suffix(".md") for p in paths]
        
        # 查找哪个文件真实存在
        existing_file = None
        for p in path_objects:
            if p.exists():
                existing_file = p
                break
        
        if existing_file is None:
            print(f"⚠️ 未找到 '{title}' 的任何源文件！")
            continue

        print(f"✅ 源文件: {existing_file}")
        
        # 创建父目录（如果不存在），并将源文件复制到所有目标路径
        for target_path in path_objects:
            if target_path == existing_file:
                continue  # 跳过已存在的源文件
            
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(existing_file, target_path)
            print(f"   🔖 复制到: {target_path}")

replicate_files(files())

"""
def check():
    files = [p for p in Path(file_dir).rglob("*.pdf")]
    file_dict = {}
    for item in files:
        if item.stem not in file_dict:
            file_dict[item.stem] = []
        file_dict[item.stem].append(str(item.relative_to(Path(file_dir))))
    same = {}
    for key, value in file_dict.items():
        if len(value) > 1:
            same[key] = value
    print(len(same.keys()))
    with open("result.json", mode='w', encoding="utf-8") as file:
        json.dump(same, file, ensure_ascii=False, indent=4)
check()
"""