# Check-Mentor

Check Mentor

## 工作流程

### 老师名单获取与文章doi下载

输出：

results.txt

### doi 到 pdf 下载工序

输入：

从 results.txt 自动读取（推荐）

输出格式：

	Downloads_pdf/
		老师名字/
			main/   # 原文
			ref1/   # 一级引用
			ref2/   # 一二级引用中的筛选年轻作者文章

### pdf转markdown

输入：

Downloads_pdf

输出格式：

	Downloads_md/
		老师名字/
			main/   # 原文
			ref1/   # 一级引用
			ref2/   # 一二级引用中的筛选年轻作者文章

### 根据 DOI 查找“被引”文章的 DOI（反向引用）

有时需要知道“一篇论文被哪些论文引用了”。仓库已提供脚本，基于 OpenAlex 开放接口，无需 API Key：

- 脚本位置：`DOIdownloader/cited_by_from_doi.py`
- 功能：输入一个或多个 DOI，输出所有“引用了该 DOI 的论文”的 DOI 列表（去除无 DOI 的记录）。
- 依赖：`requests`（已在根目录 `requirements.txt` 中列出）。

用法（Windows PowerShell）：

```powershell
# 1) 单个 DOI，结果打印到控制台（每行一个 DOI）
python DOIdownloader/cited_by_from_doi.py --doi 10.1038/nature12373

# 2) 从文件批量读取（每行一个 DOI；支持注释行以 # 开头），保存到 CSV
python DOIdownloader/cited_by_from_doi.py --input d:\path\to\dois.txt --out d:\path\to\citing.csv

# 3) 推荐：提供联系邮箱以礼貌使用 OpenAlex（用于 mailto 参数）
python DOIdownloader/cited_by_from_doi.py --doi 10.1038/nature12373 --email you@example.com
```

输出 CSV 列：`source_doi, citing_doi, citing_openalex_id, year`

说明：
- 脚本先把输入 DOI 解析为 OpenAlex 的工作条目 ID（W 开头），再用 `filter=cites:W...` 获取所有“被引者”。
- 仅保留有 DOI 的引用条目（部分条目在 OpenAlex 中可能无 DOI）。
- 若网络较慢或请求较多，脚本自带重试与退避；可适当分批处理或加入 `--email` 以提高稳定性。