# 学术开盒 Demo (Academic Insight Extractor)

本项目是一个演示程序，旨在通过分析一位教授的多篇学术论文，自动回答本科生在选择科研导师前最关心的几个核心问题。它利用大型语言模型（LLM）和检索增强生成（RAG）技术，从非结构化的论文文本中提取、分析并合成有价值的信息。

## 核心功能

- **论文总结**: 对指定的每一篇论文生成简洁、结构化的摘要。
- **核心问题分析**: 针对一组预设的核心问题（如“教授的研究兴趣”、“领域内的主要问题”、“本科生可参与的项目”），评估每篇论文与这些问题的相关性，并给出评分和详细解释。
- **综合报告生成**: 汇总所有论文的分析结果，生成一份关于该教授研究方向的最终综合报告，为学生提供决策支持。

## 技术栈

- **语言**: Python 3.10+
- **核心框架**: LangChain (用于构建 RAG 流程)
- **语言模型**: OpenAI GPT 系列或任何兼容 OpenAI API 接口的模型
- **向量数据库**: ChromaDB (用于文本块的向量化存储与检索)
- **文本处理**: `langchain-text-splitters`, `unstructured`

## 项目结构

```
.
├── core/                   # 核心逻辑模块
│   ├── config.py           # 从 .env 加载配置
│   ├── core_questions.py   # 定义核心问题集
│   ├── data_manager.py     # 管理 JSON 数据的读写
│   ├── final_analysis.py   # 生成最终综合报告
│   └── rag_processor.py    # RAG 核心处理器（加载、分割、向量化、分析）
├── data/                   # 输入数据
│   └── sample/main/        # 存放待分析的论文 (.md 格式)
├── output/                 # 输出目录
│   └── ..._research_data.json # 包含所有结果的 JSON 文件
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
