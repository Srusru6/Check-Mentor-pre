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

	Downloads_pdf/
		老师名字/
			main/   # 原文
			ref1/   # 一级引用
            cited/   # 一二级引用中的筛选年轻作者文章
2) MinerU Token（PDF → Markdown 服务）：

将 `MINERU_TOKEN` 设为环境变量，或在运行 `pdf2md` 子命令时通过 `--token` 传入。

3) `config.ini`（可选，仅 DOIdownloader 使用）：可配置下载策略，例如 Top-N、近几年筛选等。

## 数据目录结构

下载与转换阶段：

	Downloads_md/
		老师名字/
			main/   # 原文
			ref1/   # 一级引用
            cited/   # 一二级引用中的筛选年轻作者文章
# 学术开盒 Demo (Academic Insight Extractor)
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
.
├── cache/                  # 缓存目录，存储工作流的中间结果
├── core/                   # 核心逻辑模块
│   ├── workflows/          # 各个问题的工作流
│   │   ├── workflow_contribution.py
│   │   ├── workflow_field_problems.py
│   │   └── workflow_undergrad_projects.py
│   ├── config.py           # 从 .env 加载配置
│   ├── data_manager.py     # 管理 JSON 格式的缓存数据
│   ├── metadata_manager.py # 论文元数据管理 (NEW!)
│   ├── final_analysis.py   # 生成最终综合报告
│   └── workflow_orchestrator.py # 工作流编排器
├── data/                   # 输入数据
│   ├── metadata_example.json # 元数据格式示例 (NEW!)
│   └── 王剑威/             # 按教授姓名组织
│       ├── main/           # 教授代表作
│       │   └── metadata.json # 论文元数据 (可选)
│       ├── ref1/           # 关键参考文献
│       │   └── metadata.json # 论文元数据 (可选)
│       └── cited/           # 潜在项目文献
│           └── metadata.json # 论文元数据 (可选)
├── output/                 # 输出目录
│   └── ..._final_report.md # 最终生成的 Markdown 报告
├── .env.example            # 环境变量示例文件
├── .venv/                  # Python 虚拟环境
├── main.py                 # 项目主入口点
├── metadata_tools.py       # 元数据管理工具 (NEW!)
├── METADATA_README.md      # 元数据功能详细文档 (NEW!)
├── METADATA_QUICKSTART.md  # 元数据功能快速入门 (NEW!)
├── README.md               # 项目说明文件
└── requirements.txt        # Python 依赖列表
```

## 安装与配置

1.  **克隆仓库**
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  **创建并激活 Python 虚拟环境**
    ```bash
    # 创建虚拟环境
    python -m venv .venv

    # 激活虚拟环境 (Windows PowerShell)
    ./.venv/Scripts/Activate.ps1
    
    # 激活虚拟环境 (macOS/Linux)
    # source .venv/bin/activate
    ```

3.  **安装依赖**
    ```bash
    pip install -r requirements.txt
    ```

4.  **配置环境变量**
    - 将 `.env.example` 文件复制一份并重命名为 `.env`。
    - 打开 `.env` 文件，填入你的 API 密钥和终结点（Base URL）。
      ```env
      OPENAI_API_KEY="YOUR_API_KEY_HERE"
      OPENAI_API_BASE="YOUR_API_BASE_URL_HERE"

      # 可选：配置备用LLM（阿里云百炼）以增强稳定性
      DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY_HERE"
      ```

## 如何运行

1.  **准备数据**
    - 在 `data/` 目录下，以目标教授的姓名创建一个新的文件夹，例如 `data/王剑威/`。
    - 在新创建的教授文件夹内，建立三个子目录：`main`, `ref1`, `cited`。
      - `main/`: 存放教授的**核心代表作**。
      - `ref1/`: 存放用于分析**领域热点**的关键参考文献。
          - `ref2/`: 存放用于启发**本科生项目**的复杂度适中的论文。
    - 将整理好的论文（`.md` 格式）放入对应的文件夹中。
    - **[可选]** 添加论文元数据以提升分析质量（详见下方"元数据功能"部分）。

2.  **执行程序**
    - 在项目根目录下，通过命令行运行 `main.py`，并使用 `--target` 参数指定目标教授的姓名。
    - 最终报告将生成在 `output/` 目录下，并命名为 `[教授姓名]_final_report.md`。

    **完整命令示例:**
    ```bash
    python main.py --target "王剑威"
    ```

    **测试模式:**
    - 如果你只想快速验证程序流程，可以添加 `--test-mode` 标志。该模式下，程序将只处理每个数据文件夹下的少量论文。
    ```bash
    python main.py --target "王剑威" --test-mode
    ```

## 工作原理简介

本程序的工作流程如下：

1.  **数据加载**: 程序首先根据你提供的教授姓名，在 `data/` 目录中找到对应的论文文件（`.md` 格式）。
2.  **工作流编排**: `WorkflowOrchestrator` 启动，依次执行三个核心分析工作流：
    - **贡献分析**: 分析 `main/` 目录下的论文，总结教授的核心研究贡献。
    - **领域问题分析**: 分析 `main/` 和 `ref1/` 目录下的论文，识别该领域的前沿热点。
    - **本科生项目分析**: 分析 `ref1/` 和 `cited/` 目录下的论文，提出适合本科生参与的项目建议。
3.  **LLM 分析**: 每个工作流将论文内容发送给大型语言模型（LLM），并根据精心设计的指令（Prompt）提取结构化信息。
4.  **缓存机制**: 所有 LLM 的分析结果都会被缓存在 `cache/` 目录下的 JSON 文件中。当再次运行程序时，已分析过的论文将被跳过，从而节省时间和 API 调用成本。
5.  **报告生成**: 所有工作流完成后，`FinalAnalyzer` 会将各部分的分析结果汇总，生成一份结构清晰、内容连贯的 Markdown 格式报告，并将其翻译为中文。

这个架构使得分析流程模块化，并且易于扩展和维护。

    - **完整运行**:
      使用 `--target` 参数指定要分析的教授姓名。程序将处理该教授对应的所有数据。
      ```bash
      # 示例：完整分析 "王剑威" 教授
      python main.py --target "王剑威"
      ```

    - **测试模式运行**:
      在完整运行的基础上，添加 `--test-mode` 标志。程序将只处理每个数据源下的少量（默认为2篇）论文，以便快速验证流程。
      ```bash
      # 示例：以测试模式分析 "王剑威" 教授
      python main.py --target "王剑威" --test-mode
      ```

## 输出说明

- 程序执行完毕后，一份详细的 Markdown 格式分析报告将保存在 `output/` 目录下，文件名类似于 `王剑威_final_report.md`。

## 元数据功能 (NEW! ✨)

本项目现已支持论文元数据，可以显著提升分析质量！

### 什么是元数据？

每篇论文的元数据包含：
- **DOI**: 论文的唯一标识符
- **作者列表**: 完整的作者信息
- **发布时间**: 论文的发布日期
- **青年学者索引**: 标识第一位青年学者在作者列表中的位置

### 元数据的作用

1. **智能排序**: 更新的论文会被优先分析，确保关注最新研究动态
2. **时效性评分**: 自动计算论文的时效性得分（0-1），近期论文得分更高
3. **青年学者识别**: 识别有青年学者参与的论文
4. **完整作者信息**: 为未来的合作网络分析打下基础

### 快速开始

1. **生成元数据模板**:
   ```bash
   python metadata_tools.py generate data/王剑威/main/metadata.json --paper-dir data/王剑威/main
   ```

2. **填写论文信息**: 编辑生成的 `metadata.json` 文件

3. **验证格式**:
   ```bash
   python metadata_tools.py validate data/王剑威/main/metadata.json
   ```

4. **正常运行程序**: 系统会自动检测并使用元数据

### 详细文档

- 📖 [元数据详细文档](log/metadata_feature/METADATA_README.md) - 完整的技术说明和API文档
- 🚀 [快速入门指南](log/metadata_feature/METADATA_QUICKSTART.md) - 分步骤的使用教程
- 📝 [元数据示例](data/metadata_example.json) - JSON格式示例
- 📊 [权重应用总结](log/metadata_feature/METADATA_WEIGHTS_SUMMARY.md) - 元数据权重在工作流中的应用

### 兼容性

✅ **完全向后兼容**: 没有元数据文件时，程序仍可正常运行
✅ **渐进式采用**: 可以只为部分论文添加元数据
✅ **零学习成本**: 使用工具脚本自动生成模板

---

## 智能聚类功能 (NEW! 🔥)

当论文数量过多时，系统会自动进行语义聚类和代表性采样，确保分析质量。

### 功能特点

1. **自动触发**: 当论文数量超过阈值（10篇）时自动启用
2. **语义聚类**: 使用LLM理解论文间的语义关系，自动分组为3-5个主题
3. **代表性采样**: 从每个主题中选择最具代表性的论文
4. **智能降维**: 10+ 篇论文 → 3-5 个主题 → 3-5 篇代表性论文

### 三个工作流的聚类策略

| 工作流 | 聚类依据 | 代表性标准 | 目标 |
|--------|----------|------------|------|
| **教授贡献分析** | 研究领域 + 核心贡献 | 时效性最高 | 展示最新研究方向 |
| **领域热点问题** | 识别的问题 | 得分最高 | 识别最重要问题 |
| **本科生项目** | 项目创意 | 综合得分最高 | 推荐最佳项目 |

### 效果

- ✅ **处理大规模论文集**: 即使20-30篇论文也能高效分析
- ✅ **避免信息过载**: 减少50-80%的token消耗
- ✅ **保证覆盖全面**: 每个主题都有代表性论文
- ✅ **提升分析质量**: 去除重复信息，保留关键内容

### 详细文档

- 📋 [聚类功能实现报告](log/CLUSTERING_FEATURE_IMPLEMENTATION.md) - 完整的技术实现文档

---

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
