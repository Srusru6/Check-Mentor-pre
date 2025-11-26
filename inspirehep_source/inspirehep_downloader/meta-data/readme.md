用法示例（默认包含“参考 ref1 + 被引 cited”）

- 基于 mid 批处理（单老师，下载主文献 + 参考 + 被引）：
	D:/programs/checkmentor/Check-Mentor/.venv/Scripts/python.exe d:\programs\checkmentor\Check-Mentor\inspirehep_source\inspirehep_downloader\meta-data\run_meta_pack.py --mid-file d:\programs\checkmentor\Check-Mentor\inspirehep_source\pre-process\mid_batch.json --teacher 朱华星 --k 10 --verbose --pdf-root d:\programs\checkmentor\Check-Mentor\Downloads_pdf

- 并发处理多位老师（下载主文献 + 参考 + 被引）：
	D:/programs/checkmentor/Check-Mentor/.venv/Scripts/python.exe d:\programs\checkmentor\Check-Mentor\inspirehep_source\inspirehep_downloader\meta-data\run_meta_pack.py --mid-file d:\programs\checkmentor\Check-Mentor\inspirehep_source\pre-process\mid_batch.json --k 10 --workers-teachers 2 --verbose --pdf-root d:\programs\checkmentor\Check-Mentor\Downloads_pdf

可选行为

- 仅索引关联（不下载参考/被引 PDF 与元数据）：在命令中追加 `--no-related-downloads`。
  例如：
  D:/programs/checkmentor/Check-Mentor/.venv/Scripts/python.exe d:\programs\checkmentor\Check-Mentor\inspirehep_source\inspirehep_downloader\meta-data\run_meta_pack.py --mid-file d:\programs\checkmentor\Check-Mentor\inspirehep_source\pre-process\mid_batch.json --teacher 朱华星 --k 10 --no-related-downloads --verbose --pdf-root d:\programs\checkmentor\Check-Mentor\Downloads_pdf

调优建议

- 老师级并发：通过 `--workers-teachers` 控制（建议 2-4，根据网络与 API 限速调整）。
- 主/相关文献并发：编辑项目根 `config.ini` 中 `[download] workers_main` 与 `workers_related`。
- 大量 refs/cited 时：在 `config.ini` 的 `[download]` 段设置 `sample_threshold` 与 `sample_size` 以开启随机抽样。