# Check-Mentor

一条龙的学术开盒工具：从 DOI 下载论文、批量 PDF → Markdown 转换、合并元数据、到 LLM 驱动的三大工作流分析（核心贡献、领域热点、本科生项目建议），最终输出中英文报告。

本仓库已将所有程序运行整合到 `main.py`，可通过子命令统一调用。

## 依赖安装

Windows PowerShell 中执行（已内置 Python 环境请替换为对应解释器）：

```powershell
python -m pip install -r requirements.txt
```

主要依赖：
- LangChain 及 OpenAI 接口（analysis 使用）
- requests、beautifulsoup4（下载器）
- python-Levenshtein（标题相似度校验）

## 环境变量与配置

1) 在项目根目录创建 `.env`（用于分析阶段 LLM 调用）：

```
OPENAI_API_KEY=你的OpenAIKey
OPENAI_API_BASE=https://api.openai.com/v1
LLM_MODEL=DeepSeek-V3

# 可选：备用模型（阿里通义）
DASHSCOPE_API_KEY=你的DashScopeKey
LLM_FALLBACK_MODEL=qwen-plus
```

2) MinerU Token（PDF → Markdown 服务）：

将 `MINERU_TOKEN` 设为环境变量，或在运行 `pdf2md` 子命令时通过 `--token` 传入。

3) `config.ini`（可选，仅 DOIdownloader 使用）：可配置下载策略，例如 Top-N、近几年筛选等。

## 数据目录结构

下载与转换阶段：

```
Downloads_pdf/
  老师名字/
    main/
    ref1/
    ref2/
    cited/

Downloads_md/
  老师名字/
    main/
    ref1/
    ref2/
```

分析阶段默认直接读取 `Downloads_md/老师名字/` 下的 `main/ref1/ref2`。如需自定义数据位置，可通过 `--data-root` 覆盖。

每个层级目录都会维护 `history.json`（下载/合并时生成/更新），包含标题、DOI、作者、出版年月、（可选）年轻作者标识等。

## 一体化命令（main.py）

所有命令均在项目根目录执行，示例基于 Windows PowerShell：

1) 下载 PDF（封装 `DOIdownloader/download.py`）

```powershell
python .\main.py download --from-results AUTO --workers 6 --depth 1 --pdf-root .\Downloads_pdf
# 或按DOI手动指定
python .\main.py download --doi "10.xxxx/aaaa,10.yyyy/bbbb" --teacher "张三" --depth 1 --workers 4
```

2) PDF → Markdown（封装 `pdf2md/pdf2md.py`）

```powershell
python .\main.py pdf2md --teacher "张三" --pdf-root .\Downloads_pdf --md-root .\Downloads_md --subdirs main,ref1,ref2 --token $env:MINERU_TOKEN
```

3) 合并 history.json（封装 `DOIdownloader/merge_history_to_md.py`）

```powershell
python .\main.py merge-history --teacher "张三" --subdir main
python .\main.py merge-history --teacher "张三" --subdir ref1
python .\main.py merge-history --teacher "张三" --subdir ref2
```

4) 分析并生成报告（默认读取 `Downloads_md/张三`）

```powershell
python .\main.py analyze --target "张三" --test-mode
# 或使用自定义数据根目录
python .\main.py analyze --target "张三" --data-root d:\data\z3_md
```

5) 一条龙流程（PDF→MD→合并→分析）

```powershell
python .\main.py run-all --target "张三" --token $env:MINERU_TOKEN --test-mode
```

运行完成后，最终报告会输出到：`output/张三_final_report.md`。

## 模块说明

- `DOIdownloader/download.py`：支持从 `results.txt` 读取教师与 DOIs 映射，按层级下载 PDF（含可选被引 cited）。
- `pdf2md/pdf2md.py`：调用 MinerU API 批量转换 PDF → Markdown，并保留 full.json 与图片。
- `DOIdownloader/merge_history_to_md.py`：将 PDF 端与 MD 端历史合并至 `Downloads_md`，便于统一查看。
- `core/*`：三大工作流与最终报告整合、翻译输出。

## 常见问题

- 缺少依赖（如 langchain_*）提示：请先 `pip install -r requirements.txt`。
- MinerU Token 未设置：`pdf2md` 子命令需 `--token` 或环境变量 `MINERU_TOKEN`。
- 未找到数据：`analyze` 默认读取 `Downloads_md/<教师>`；若你将 MD 放在其他路径，请使用 `--data-root` 指定。

## 质量门（快速结论）

- Build（语法检查）：PASS（仓库内关键脚本语法有效；第三方依赖需安装后方可解析导入）
- Lint/Typecheck：未强制执行（LangChain/依赖项安装后建议本地运行 linters）
- Tests：暂无自动化测试（建议使用小样本数据进行手动验证）

---

示例：
- 类 `WorkflowOrchestrator` 在 `core/workflow_orchestrator.py`
- 最终报告写入 `output/` 目录
- 可选配置位于根目录 `config.ini`