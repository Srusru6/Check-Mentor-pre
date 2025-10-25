# 学术开盒 Demo (Academic Insight Extractor)

本项目是一个演示程序，旨在通过分析一位教授的多篇学术论文，自动回答本科生在选择科研导师前最关心的几个核心问题。它利用大型语言模型（LLM）和检索增强生成（RAG）技术，从非结构化的论文文本中提取、分析并合成有价值的信息。

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
- **核心框架**: LangChain (用于构建 RAG 流程)
- **语言模型**: OpenAI GPT 系列或任何兼容 OpenAI API 接口的模型

## 项目结构

```
.
├── core/                   # 核心逻辑模块
│   ├── workflows/          # 各个问题的工作流
│   │   ├── workflow_contribution.py
│   │   ├── workflow_field_problems.py
│   │   └── workflow_undergrad_projects.py
│   ├── config.py           # 从 .env 加载配置
│   ├── data_manager.py     # 管理 JSON 数据的读写
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
    .\.venv\Scripts\Activate.ps1
    
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
      ```

## 如何运行

1.  **准备论文**: 将需要分析的教授论文（目前支持 Markdown `.md` 格式）放入 `data/sample/main/` 文件夹内。
2.  **执行程序**: 在项目根目录下，运行以下命令：
    ```bash
    python main.py
    ```

## 输出说明

- 程序执行完毕后，所有处理结果和生成的报告都会被保存在 `output/` 目录下的一个 JSON 文件中（例如 `测试教授_research_data.json`）。
- 最终的综合报告也会在程序运行结束时直接打印在控制台中。
- 你可以查阅 JSON 文件以获取包括论文摘要、各问题详细分析在内的所有中间数据。
