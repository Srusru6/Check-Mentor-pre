import requests
import os
from pathlib import Path
import uuid
import time


file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Downloads_pdf")
file_path = [str(p) for p in Path(file_dir).rglob("*.pdf")]
output_dir = os.path.join(os.path.dirname(__file__), "output")

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
                "name": Path(file).name,
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
        for file in result:
            name = Path(file["file_name"]).stem
            if name not in done_files and file["state"] == "done":
                done_files.add(name)
                zip_url = file["full_zip_url"]
                response = requests.get(zip_url, stream=True)
                response.raise_for_status()
                file_path = os.path.join(output_dir, f"{name}.zip")
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"✅ 文件已下载并保存至: {file_path}")
        time.sleep(1)

batch_id = batch_upload()
print(batch_id)

batch_retrieve(batch_id)