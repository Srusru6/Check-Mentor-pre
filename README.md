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
			cited/  # 根 DOI 的“被引”论文（默认启用；可 --no-cited 关闭）

说明：每个层级目录会维护一个 `history.json`，包含已下载论文的标题、DOI、引用（references）、被引（cited_by）、作者、出版年月（year/month）及“年轻作者”名单，便于后续分析与复用。

### pdf转markdown

输入：

Downloads_pdf

输出格式：

	Downloads_md/
		老师名字/
			main/   # 原文
			ref1/   # 一级引用
			ref2/   # 一二级引用中的筛选年轻作者文章