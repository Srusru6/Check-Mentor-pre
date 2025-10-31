# DOI 下载器（学术爬虫）

一个可配置的 DOI 学术论文下载器：支持下载原文、按层并发地递归下载引用（ref1/ref2/...），并默认下载“被引”（cited-by）论文；可在指定层筛选“年轻作者”；内置重试、限速、持久化历史与丰富的命令行参数。

提示：默认会将 ref1 层中被判定为“年轻作者”的文章复制一份到 ref2 目录，便于集中查看（与是否开启 `--young` 无关）。可用 `--no-copy-ref1-young-to-ref2` 关闭此行为。且当设置 `--save-only-depth` 且不为 2 时，该复制不会发生。

## 默认行为（不带参数）

直接运行脚本时将：

1) 尝试从脚本同目录的 `results.txt` 读取每位老师的 DOI 列表，并按老师名输出到 `Downloads_pdf/<老师名>/(main|ref1|ref2|cited)`（默认会额外抓取每个根 DOI 的“被引”论文到 `cited/`）。

2) 若 `results.txt` 解析不到任何 DOI，则回退到示例任务：
	 - 自动开启生产模式（精简输出）
	 - 使用示例 DOI `10.1038/nphys4074`
	 - 递归深度为 2（main/ref1/ref2），在第 2 层启用“年轻作者”筛选，并默认开启“ref1 年轻作者复制到 ref2”的汇总。
	 - 保存到：`Downloads_pdf/sample/main|ref1|ref2`

与旧版描述不同：仅在“回退到示例任务”时才默认开启生产模式；正常读取 `results.txt` 时不会自动加 `--prod`。

## 环境要求

- Python 3.9+
- 可访问 DOI 落地页、CrossRef API；如需使用 Sci-Hub，需能访问至少一个镜像域名（可通过参数自定义）。

## 安装依赖

建议在虚拟环境中安装：

```powershell
pip install requests beautifulsoup4 python-Levenshtein
```

## 使用方法（CLI）

```text
python download.py [--prod] [--doi DOI1,DOI2] [--teacher NAME]
							 [--from-results [PATH]] [--pdf-root PATH]
							 [--depth N] [--workers K] [--save-only-depth D]
							 [--young] [--young-depth L] [--young-keywords KW1,KW2]
							 [--no-copy-ref1-young-to-ref2]
					 [--rps R] [--retries T] [--backoff B] [--timeout S] [--pool-maxsize P]
							 [--unpaywall-email you@domain] [--openalex-email you@domain]
				 [--scihub-domains URL1,URL2] [--no-cited] [--only-ref1-cited]
				 [--verify strict|light|off] [--no-rank-main]
```

- --prod：开启生产模式（精简日志）。
- --doi：一个或多个 DOI（逗号或空格分隔）。若不提供，则使用 `--from-results` 模式。
- --from-results：从 results.txt 读取 DOI 并按“老师名/main|ref1|ref2”目录保存；可选自定义路径；不传或传 `AUTO` 时默认读取脚本同目录下 `results.txt`。当未提供 `--doi` 时，默认启用该模式。
- --teacher：与 `--doi` 搭配使用，指定输出的老师名目录（默认 `sample`）。
- --pdf-root：PDF 输出根目录，默认 `./Downloads_pdf`。
- --depth：引用递归深度（>=0）。例如 2 表示原文 + ref1 + ref2。
- --save-only-depth：仅在指定深度保存 PDF（0=main, 1=ref1, 2=ref2, ...）。用于快速收集某一层文件。
- --workers：每一层的并发下载线程数。
- --young：启用“年轻作者”筛选（基于 CrossRef 作者单位关键词）。只对进入“指定层”的队列起过滤作用。
- --young-depth：在哪一层应用年轻作者筛选，默认 2。
- --young-keywords：自定义判定“年轻/学生”作者的单位关键词（逗号分隔）。默认内置常见关键词（如 student、phd、硕士、研究生 等）。
- --no-copy-ref1-young-to-ref2：关闭“将 ref1 层年轻作者文章复制到 ref2 目录”的默认行为（默认开启，且与 `--young` 无关）。
- --rps：全局限速（每秒请求数），0 表示不限制。
- --retries：HTTP 重试次数（覆盖内置默认）。
- --backoff：HTTP 重试退避因子（覆盖内置默认）。
- --timeout：HTTP 请求超时时间（秒，覆盖内置默认）。
- --pool-maxsize：HTTP 连接池大小（默认 ≈ workers×4）。增大可提升并发下载时的吞吐。
- --unpaywall-email：用于调用 Unpaywall API 的联系邮箱（优先寻找 OA PDF）。
- --openalex-email：用于调用 OpenAlex API（用于“被引”DOI 查询）的 mailto 邮箱。
- --scihub-domains：自定义 Sci-Hub 镜像列表（逗号分隔），按顺序尝试。
- --no-cited：关闭默认的“被引”下载（默认开启）。
- --only-ref1-cited：先筛选 main（应用近 M 年与 Top-N），不下载 main 层 PDF；仅下载 ref1 与 cited 的筛选结果。
- --top-n：对 ref1 与 cited 的候选文章按“被引用次数”（Crossref 的 is-referenced-by-count）排序后取前 N。
- --recent-years：只保留近 M 年的文章（ref1 与 cited 候选）。
 - --verify：下载校验策略。
	 - strict（默认）：优先访问 DOI 落地页获取标题，再比对 Crossref 官方标题（较慢但更严格）。
	 - light：优先使用 Crossref 标题与参考文献（更快，通常足够）。
	 - off：关闭标题校验（最快，可能增加误判风险）。
 - --no-rank-main：main 层不按被引次数排序（可显著减少 Crossref 请求，从而加速）。

可选分层 Top-N 参数（如不提供则读取 config.ini）：
- --top-n-main：main 层（根 DOI）按被引次数排序选前 N。
- --top-n-ref：ref1 层（每个根条目的参考文献）按被引次数排序选前 N。
- --top-n-cited：cited 层（每个根条目的被引）按被引次数排序选前 N。

### 常用示例（Windows PowerShell）

1) 从 `results.txt` 批量下载，按老师分目录保存（默认会在 `cited/` 目录下载根 DOI 的“被引”论文）：

```powershell
python download.py --depth 1 --workers 4
# 或自定义 results.txt 路径与输出根目录
python download.py --from-results d:\programs\checkmentor\Check-Mentor\DOIdownloader\results.txt --pdf-root d:\data\Downloads_pdf --depth 2 --workers 6 --prod
```

`results.txt` 支持如下结构（非 DOI 行会自动忽略）：

```
--- 姓名 (机构) ---
OpenAlex Profile: https://openalex.org/...
Combined DOIs (10 found):
1. 10.1007/jhep08(2011)018
2. 10.1016/j.physletb.2009.02.015
...
```

同一老师名下可列多行 DOI，解析器会从任何含 DOI 的行中提取。

Top-N 选择说明：
- 本工具中“影响因子”即指“文章被引用次数”（Crossref 字段 is-referenced-by-count），不使用期刊影响因子。
- 选择顺序为：先按年份过滤（近 M 年），再按被引次数排序取 Top-N。

配置项（config.ini -> [download]）：
- top_n_main：main 层 Top-N（默认 10）
- top_n_ref：ref1 层 Top-N（默认 100）
- top_n_cited：cited 层 Top-N（默认 100）
- recent_years：近 M 年（默认 3）
- impact_factors：期刊影响因子映射（当前版本已忽略，可留空）

2) 仅下载 ref1 与 cited（不下载 main PDF），先对 main 进行筛选后展开：

```powershell
python download.py --from-results AUTO --depth 1 --only-ref1-cited --workers 4
```

3) 指定单个 DOI，深度为 2，并发 6，在第 2 层进行年轻作者筛选：

```powershell
python download.py --doi 10.1038/s41586-024-00000-0 --teacher 王剑威 --depth 2 --workers 6 --young --young-depth 2
```

4) 多个 DOI（逗号或空格均可），关闭年轻作者筛选：

```powershell
python download.py --doi "10.1038/xxxx, 10.1126/yyyy" --teacher sample --depth 1 --workers 4
```

5) 指定 Unpaywall 邮箱和自定义 Sci-Hub 镜像：

```powershell
python download.py --doi 10.1126/science.177.4047.393 --depth 0 --unpaywall-email you@domain.com --scihub-domains https://sci-hub.se,https://sci-hub.st,https://sci-hub.ru
```

5) 只保存 ref2 层（例如仅收集二级引用 PDF）：

```powershell
python download.py --doi 10.1038/nphys4074 --depth 2 --save-only-depth 2
```

## 反向引用（根据 DOI 下载“被引”论文）

已合并至 `download.py`，默认开启。对于每个根 DOI，会通过 OpenAlex 查询其“被引”DOI，并将对应论文下载到 `cited/` 目录。如需关闭，请加 `--no-cited`。

## ref2 生成逻辑（关键点）

- 层级与目录：depth=0 → `main`，depth=1 → `ref1`，depth=2 → `ref2`。
- BFS 递归：处理第 d 层时解析到的参考文献会进入第 d+1 层队列；当 `--depth >= 2` 时会实际下载到 `ref2/`。
- 年轻作者副本：默认会在处理 `ref1`（d=1）时，把被判定为“年轻作者”的论文从 `ref1` 复制一份到 `ref2` 进行汇总；该行为与是否开启 `--young` 无关，但会受 `--save-only-depth` 限制（仅当未限制或等于 2 时复制）。
- 过滤与复制的区别：
	- 过滤（`--young` + `--young-depth`）影响“进入下一层队列的 DOI 是否保留”。
	- 复制（`--no-copy-ref1-young-to-ref2` 开关）只是在已有下载的前提下把 `ref1` 的年轻作者论文“再放一份”到 `ref2`，不影响队列。

## 功能说明

- 多来源解析：优先尝试出版社直链下载，失败则尝试 Unpaywall（若提供邮箱），仍失败再回退至 Sci-Hub；对页面解析出 PDF 直链。
- 参考文献抽取：从落地页与元数据中解析 DOI，辅以正则与多种 HTML 结构启发式，统一规范化去重。
- 并发与 BFS：按层并发下载，控制每层线程数；下载历史持久化，跨老师去重（同一 DOI 二次复制时复用历史）。
- 标题校验：用 CrossRef 官方标题对比页面标题，基于 Levenshtein 相似度做轻量验证。
- 网络鲁棒性：全局 Session + 重试 + 限速 + 超时控制，CLI 可调。

## 故障排查

- 出版社 403/401：多数出版社需要校内网或机构访问（VPN/代理）。可尝试：
	- 在校/图书馆 VPN 环境运行
	- 启用 Unpaywall：`--unpaywall-email you@domain.com`（若该 DOI 有 OA 版本）
	- 改用开放获取 DOI 测试，如 `10.48550/arXiv.1706.03762`
- Sci-Hub 无法解析（DNS 失败）：本地网络可能屏蔽域名。可尝试：
	- 指定可用镜像：`--scihub-domains https://sci-hub.se,https://sci-hub.st,https://sci-hub.ru`
	- 更换网络/DNS，或使用 VPN
- 无下载但无报错：去掉 `--prod` 查看详细日志；或提高 `--timeout`，减小 `--workers`。

## 目录结构

```
Downloads_pdf/
	老师名字/
		main/  # 原文
		ref1/  # 一级引用
		ref2/  # 二级引用；默认也会汇总一份来自 ref1 的“年轻作者”副本（可关闭）
		cited/ # 根 DOI 的“被引”论文（默认启用；可 --no-cited 关闭）

每个层级目录（main/ref1/cited）会维护一个 `history.json`，记录已下载论文的：标题、DOI、引用（references）、被引（cited_by）、作者列表、出版年月（year/month）以及“年轻作者”名单。该文件在并发下载时线程安全地增量更新，自动去重（按 DOI 覆盖更新）。
```

## 注意事项与建议

- 学术资源请遵循相应的版权与使用政策，仅用于个人学习研究。
- Sci-Hub 页面结构可能变化，代码已做多种选择器兜底；如失效，可反馈或更新解析逻辑。
- CrossRef 元数据缓存为内存 LRU；可通过 `--no-rank-main` 显著减少排序请求；并可适当增大 `--workers` 与 `--pool-maxsize` 提升吞吐（视网络环境与站点限流而定）。

