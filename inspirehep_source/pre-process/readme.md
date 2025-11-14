预处理：从 mid.txt 解析老师及其 recent/引用排序的 DOI 列表，并生成 mid_batch.json，供 downstream 下载器使用。

使用说明

- 将一位或多位老师的条目写入同一个 `mid.txt` 中，示例结构：
  
	曹某某
	时间排序：
	@article{... doi = "10.x/..." }
	...
  
	引用排序：
	@article{... doi = 10.y/... }
	...
  
	另一位老师
	时间排序
	...
	引用排序
	...

- 运行脚本生成批处理计划：

	PowerShell（Windows）：
	& .venv\Scripts\python.exe inspirehep_source\pre-process\convert_mid_to_batch.py

输出

- 生成 `inspirehep_source/pre-process/mid_batch.json`，格式：
	{
		"老师A": {"recent": ["10.x"...], "cited": ["10.y"...]},
		"老师B": { ... }
	}

后续

- 结合打包式下载器：
	& .venv\Scripts\python.exe inspirehep_source\inspirehep_downloader\meta-data\run_meta_pack.py --mid-file inspirehep_source\pre-process\mid_batch.json --k 10 --verbose --pdf-root Downloads_pdf

备注

- 支持“时间排序/引用排序”标题含或不含中文冒号（：）。
- 仅从条目中提取包含 `doi=` 字段的记录；重复 DOI 自动去重并保持顺序。
