# Convert PDF to Markdown

## use api from MinerU
https://mineru.net/apiManage/docs

## 本仓库脚本使用说明（pdf2md.py）

该脚本会将 `Downloads_pdf/曹庆宏/` 下的 PDF 批量上传至 MinerU，等待解析完成后自动下载 ZIP，解包生成对应的 Markdown（.md）文件与 images 目录到 `Downloads_md/曹庆宏/` 下，并为同名（不同路径）PDF 复制一份同样的 Markdown 结果。

步骤（Windows PowerShell）：

1. 安装依赖

    ```powershell
    pip install -r .\requirements.txt
    ```

2. 准备 MinerU API Token（在官网申请），设置到当前会话：

    ```powershell
    $env:MINERU_TOKEN = "<你的token>"
    ```

3. 将待转换的 PDF 放到 `Downloads_pdf/曹庆宏/`（可含子目录）。输出会写入 `Downloads_md/曹庆宏/`。

4. 运行脚本：

    ```powershell
    python .\pdf2md\pdf2md.py
    ```

脚本默认行为与注意事项：

- 仅处理“新增”PDF：会跳过已经在输出目录存在同名 .md 的文件；若想强制重跑，可删除对应的 .md 或修改脚本将 `unique_dict = new_files()` 改为 `files()`。
- 单次最多处理 199 个文件（可在代码中调整 `file_names = ...[:199]`）。
- API 参数：开启公式与表格识别（`enable_formula=True, enable_table=True`），`is_ocr=False`（如需 OCR，可在代码里改为 True）。
- 解析完成后会生成与 PDF 相同相对路径的 `.zip`、对应的 `.md`、同名 `.json`（当返回 `full.json` 时）与 `images/` 目录；若 ZIP 中无 `full.md` 会提示警告。
-- 若存在同名（不同路径）的 PDF，脚本会把生成的 `.md` 复制到每个同名目标路径；若存在同名 `.json` 也会一并复制。

常见问题：

- 401/鉴权失败：检查 MINERU_TOKEN 是否正确且未过期。
- 长时间无结果：脚本每 2 秒轮询一次，最多约 6 分钟；可根据需要调整 `max_retry`。
- 批量 >199：分批运行或修改切片上限。

### Batch File Upload and Parsing

example
```python
import requests

token = "官网申请的api token"
url = "https://mineru.net/api/v4/file-urls/batch"
header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}
data = {
    "enable_formula": True,
    "language": "ch",
    "enable_table": True,
    "files": [
        {"name":"demo.pdf", "is_ocr": True, "data_id": "abcd"}
    ]
}
file_path = ["demo.pdf"]
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
        else:
            print('apply upload url failed,reason:{}'.format(result.msg))
    else:
        print('response not success. status:{} ,result:{}'.format(response.status_code, response))
except Exception as err:
    print(err)
```

### Batch Retrieve Task Results

example
```python
import requests

token = "官网申请的api token"
url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

res = requests.get(url, headers=header)
print(res.status_code)
print(res.json())
print(res.json()["data"])
```

