import requests
import os
from pathlib import Path
import uuid
import time
import zipfile
import tempfile
import shutil


file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Downloads_pdf")
file_path = [str(p) for p in Path(file_dir).rglob("*.pdf")]
output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Downloads_md")

token = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIwMzA2OTgiLCJyb2wiOiJST0xFX1JFR0lTVEVSLFJPTEVfREFUQVNFVCIsImlzcyI6Ik9wZW5YTGFiIiwiaWF0IjoxNzM2NDc2NTM0LCJjbGllbnRJZCI6IjRtMndvbmVta3Yycm0zN253ZW44IiwicGhvbmUiOiIiLCJ1dWlkIjoiOGFmYmY3YzUtYzQ4NS00ODg5LWFlZjQtZDczZDM5ZmZmZGRjIiwiZW1haWwiOiJPcGVuRGF0YUxhYkBwamxhYi5vcmcuY24iLCJleHAiOjE4OTQxNTY1MzR9.zsobQWe9Wn5XpWdVrBUdZOVfkWLSXOiWUfwUtgnUuqcrY5BUsgtsgsFhKNd8en79Ho_2QzxNySYYHuSrEiRGFQ"
header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}
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
                "name": str(Path(file).relative_to(Path(file_dir))),
                "data_id": str(uuid.uuid4())
            }
            for file in file_path
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
                    with open(file_path[i], 'rb') as f:
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
    done = False
    done_files = set([])
    url = f"https://mineru.org.cn/api/v4/extract-results/batch/{batch_id}"
    os.makedirs(output_dir, exist_ok=True)
    while not done:
        res = requests.get(url, headers=header)
        result = res.json()["data"]["extract_result"]
        if all(file["state"] == "done" for file in result):
            done = True
            print("all files done")
        for item in result:
            file = Path(item["file_name"]).with_suffix(".zip")
            if str(file) not in done_files and item["state"] == "done":
                done_files.add(str(file))
                zip_url = item["full_zip_url"]
                response = requests.get(zip_url, stream=True)
                response.raise_for_status()
                file_path = Path(output_dir) / file
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"文件已下载并保存至: {file_path}")
        time.sleep(1)

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