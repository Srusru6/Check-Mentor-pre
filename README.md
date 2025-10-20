# Check-Mentor

Check Mentor

## 工作流程

### 老师名单获取与文章doi下载

输出：

doi.xlsx

### doi 到 pdf 下载工序

输入：

doi.xlsx

输出格式：

	Downloads_pdf/
		老师名字/
			main/   # 原文
			ref1/   # 一级引用
			ref2/   # 二级引用（筛选年轻作者）

### pdf转markdown

输入：

Downloads_pdf

输出格式：

	Downloads_md/
		老师名字/
			main/   # 原文
			ref1/   # 一级引用
			ref2/   # 二级引用（筛选年轻作者）