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
# 学术开盒 Demo (Academic Insight Extractor)

本项目是一个演示程序，旨在通过分析一位教授的多篇学术论文，自动回答本科生在选择科研导师前最关心的几个核心问题。它利用大型语言模型（LLM）对非结构化的论文文本进行批量分析、提取与信息合成。

## 核心目标

本项目的核心是自动回答以下三个问题，帮助学生全面了解一位学者的研究画像：

1.  **教授的核心贡献**:
    - *老师对哪些方向感兴趣，他对此有哪些贡献？*
    - 通过分析其代表作，提炼核心研究方向和具体贡献。

2.  **领域的热点问题**:
    - *这些方向的学者们都在关心什么问题？*
    - 通过分析其代表作和关键参考文献，描绘出该领域的前沿和热点。

3.  **本科生的切入点**:
    - *这些方向有哪些本科生可以参与的项目？*
    - 通过分析相关领域的论文，评估其复杂度与可行性，为本科生提供潜在的科研项目建议。

## 技术栈
- **语言**: Python 3.10+
- **核心框架**: LangChain (用于编排 LLM 工作流)
- **语言模型**:
  - 主要模型: OpenAI GPT 系列或任何兼容 OpenAI API 接口的模型 (如 DeepSeek)。
  - 备用模型: 阿里云通义千问 (通过 DashScope)。
- **核心库**: `langchain`, `openai`, `dashscope`, `python-dotenv`, `tqdm`

## 项目结构

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
│   ├── final_analysis.py   # 生成最终综合报告
│   └── workflow_orchestrator.py # 工作流编排器
├── data/                   # 输入数据
│   └── 王剑威/             # 按教授姓名组织
│       ├── main/           # 教授代表作
│       ├── ref1/           # 关键参考文献
│       └── ref2/           # 潜在项目文献
├── output/                 # 输出目录
│   └── ..._final_report.md # 最终生成的 Markdown 报告
├── .env.example            # 环境变量示例文件
├── .venv/                  # Python 虚拟环境
├── main.py                 # 项目主入口点
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
    - 在新创建的教授文件夹内，建立三个子目录：`main`, `ref1`, `ref2`。
      - `main/`: 存放教授的**核心代表作**。
      - `ref1/`: 存放用于分析**领域热点**的关键参考文献。
      - `ref2/`: 存放用于启发**本科生项目**的复杂度适中的论文。
    - 将整理好的论文（`.md` 格式）放入对应的文件夹中。

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
    - **本科生项目分析**: 分析 `ref1/` 和 `ref2/` 目录下的论文，提出适合本科生参与的项目建议。
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
