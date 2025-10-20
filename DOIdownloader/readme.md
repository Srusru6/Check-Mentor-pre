# DOI 下载器（学术爬虫）

一个可配置的 DOI 学术论文下载器：支持下载原文、递归下载一二级引用，第二层可筛选“年轻作者”文章；带并发、重试、限速、持久化历史与命令行参数。

提示：当启用“年轻作者”筛选时，`ref1` 层中被判定为“年轻作者”的文章会默认复制一份到 `ref2` 目录，便于集中查看。可用 `--no-copy-ref1-young-to-ref2` 关闭此行为。

## 默认行为（开箱即用）

不带任何参数直接运行脚本时：

- 自动开启生产模式（精简输出）
- 以示例 DOI `10.1126/science.177.4047.393` 为入口
- 下载：原文 + 一级引用 + 二级引用
- 在第二层对“年轻作者”进行筛选（通过 CrossRef 作者单位关键词近似识别）
- 保存路径：`Downloads_pdf/sample/main`（原文）与 `Downloads_pdf/sample/ref1`、`Downloads_pdf/sample/ref2`（引用）

## 环境要求

- Python 3.9+
- 网络可访问 DOI 落地页、CrossRef，以及默认的 Sci-Hub 镜像（脚本内置多个域名自动尝试）

## 安装依赖

建议在虚拟环境中安装：

```powershell
pip install requests beautifulsoup4 python-Levenshtein
```

## 使用方法（CLI）

```text
python download.py [--prod] [--doi DOI1,DOI2] [--depth N] [--workers K]
									 [--young] [--young-depth D] [--young-keywords KW1,KW2]
							   [--rps R] [--retries T] [--backoff B] [--timeout S]
									   [--unpaywall-email you@domain] [--scihub-domains URL1,URL2]
							   [--no-copy-ref1-young-to-ref2]
```

- --prod：开启生产模式（精简日志）。默认行为下已自动开启。
- --doi：一个或多个 DOI（逗号或空格分隔）。若不提供，将运行默认示例 DOI。
- --depth：引用递归深度（>=0）。例如 2 表示原文+一级+二级引用。
- --workers：每一层的并发下载线程数。
- --young：启用“年轻作者”筛选（基于作者单位关键词）。
- --young-depth：在哪一层应用年轻作者筛选，默认 2。
- --young-keywords：自定义判定“年轻/学生”作者的单位关键词，逗号分隔（默认内置常见词，如 student、undergraduate、bachelor 等）。
- --no-copy-ref1-young-to-ref2：关闭“将 ref1 层年轻作者文章复制到 ref2 目录”的默认行为。
- --rps：全局限速（每秒请求数），0 表示不限制。
- --retries：HTTP 重试次数（覆盖内置默认）。
- --backoff：HTTP 重试退避因子（覆盖内置默认）。
- --timeout：HTTP 请求超时时间（秒，覆盖内置默认）。
- --unpaywall-email：用于调用 Unpaywall API 的联系邮箱（获取开放获取 PDF 的优先通道）。
- --scihub-domains：自定义 Sci-Hub 镜像列表，逗号分隔，按顺序尝试（绕过被封锁的域名）。

### 示例

1) 使用默认行为（生产模式 + 示例 DOI + 二层年轻作者筛选）：

```powershell
python download.py
```

2) 指定 DOI，深度为 2，并发 6，保留第二层年轻作者筛选：

```powershell
python download.py --doi 10.1038/s41586-024-00000-0 --depth 2 --workers 6 --young --young-depth 2
```

3) 多个 DOI（逗号或空格分隔），关闭年轻作者筛选：

```powershell
python download.py --doi "10.1038/xxxx, 10.1126/yyyy" --depth 1 --workers 4
```

4) 指定 Unpaywall 邮箱和自定义 Sci-Hub 镜像：

```powershell
python download.py --doi 10.1126/science.177.4047.393 --depth 0 --unpaywall-email you@domain.com --scihub-domains https://sci-hub.se,https://sci-hub.st,https://sci-hub.ru
```

## 功能说明

- 多来源解析：优先尝试出版社直链下载，失败则自动回退至 Sci-Hub；对 Sci-Hub 页面尝试解析出 PDF 直链。
- 参考文献抽取：从落地页解析 DOI，辅以正则与多种 HTML 结构启发式，统一规范化去重。
- 并发与 BFS：按层并发下载，控制每层线程数；下载历史持久化，避免重复工作。
- 标题校验：CrossRef 官方标题 + 页面标题，利用 Levenshtein 相似度做轻量验证。
- 网络鲁棒性：全局 Session + 重试 + 限速 + 超时控制，CLI 可调。

## 故障排查

- 出版社 403/401：多数出版社需要校内网或机构访问（VPN/代理）。可尝试：
	- 在校/图书馆 VPN 环境运行
	- 启用 Unpaywall：`--unpaywall-email you@domain.com`（若该 DOI 有 OA 版本）
	- 改用开放获取 DOI 测试，如 `10.48550/arXiv.1706.03762`
- Sci-Hub 无法解析（DNS 失败）：本地网络可能屏蔽域名。可尝试：
	- 指定可用镜像：`--scihub-domains https://sci-hub.se,https://sci-hub.st,https://sci-hub.ru`
	- 更换网络/DNS，或使用 VPN
- 仍未下载但无报错：默认生产模式日志精简。请去掉 `--prod` 以查看详细日志并反馈报错信息。

## 目录结构

```
Downloads_pdf/
	sample/
		main/   # 原文
		ref1/   # 一级引用
	ref2/   # 二级引用（可筛选）；若开启年轻作者筛选，这里也会汇总一份来自 ref1 的“年轻作者”副本
```

## 注意事项与建议

- 学术资源请遵循相应的版权与使用政策，仅用于个人学习研究。
- Sci-Hub 页面结构可能变化，已做多种选择器兜底；如失效，可反馈或更新解析逻辑。
- CrossRef 元数据缓存为内存 LRU，后续可扩展为磁盘缓存以减少重复请求。

