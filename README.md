# Check-Mentor

统一的学术开盒流水线：从 DOI 下载 → PDF 转 Markdown → 合并元数据 → LLM 工作流分析（核心贡献 / 领域热点 / 本科生项目），生成中/英文报告。

本项目已将所有命令整合到 `main.py`（Windows PowerShell 示例）。

## 安装

```powershell
python -m pip install -r requirements.txt
```

主要依赖：
- LangChain + OpenAI（分析），DashScope 可选（备用模型）
- requests、beautifulsoup4（下载）
- python-Levenshtein（标题相似度）

## 配置

- 在根目录复制 `.env.example` 为 `.env`，填入 LLM 信息（用于分析阶段）：
    - OPENAI_API_KEY、OPENAI_API_BASE、LLM_MODEL
    - 可选：DASHSCOPE_API_KEY、LLM_FALLBACK_MODEL
- MinerU Token（PDF→MD）：设置环境变量 `MINERU_TOKEN` 或在命令中通过 `--token` 传入
- 可选 `config.ini`（仅下载器使用）：Top-N、近几年筛选、refs/cited 抽样等
    - `[download].sample_threshold` 与 `[download].sample_size`：当某主文献的参考文献（refs）或被引（cited）数量超过阈值时，随机抽样指定数量进行处理；留空或 ≤0 表示不启用。

## 数据目录

```
Downloads_pdf/
    老师/
        main/ ref1/ cited/

data/
    老师/
        main/ ref1/ cited/
```

分析默认读取 `data/老师/` 的 `main/ref1/cited`。下载历史会写入各层 `history.json`。

本仓库已附带样例：
- `DOIdownloader/results.txt`：示例教师与 DOI 列表
- `data/示例老师/`：包含一个示例 Markdown 论文

## 一体化命令

1) 下载 PDF（封装 `DOIdownloader/download.py`）
```powershell
python .\main.py download --from-results AUTO --workers 6 --depth 1 --pdf-root .\Downloads_pdf
# 或手动指定DOI
python .\main.py download --doi "10.1038/nphys4074" --teacher "示例老师" --depth 1 --workers 4
```

2) PDF → Markdown（封装 `tools/pdf2md/pdf2md.py`）
```powershell
python .\main.py pdf2md --teacher "示例老师" --pdf-root .\Downloads_pdf --md-root .\data --subdirs main,ref1,cited --token $env:MINERU_TOKEN
```

3) 合并下载历史到 data（封装 `DOIdownloader/merge_history_to_md.py`）
```powershell
python .\main.py merge-history --teacher "示例老师" --subdir main
python .\main.py merge-history --teacher "示例老师" --subdir ref1
python .\main.py merge-history --teacher "示例老师" --subdir cited
```

4) 分析并生成报告（默认读 `data/示例老师`）
```powershell
python .\main.py analyze --target "示例老师" --test-mode
# 或自定义数据根：
python .\main.py analyze --target "示例老师" --data-root D:\data\示例老师
```

5) 一条龙（PDF→MD→合并→分析）
```powershell
python .\main.py run-all --target "示例老师" --token $env:MINERU_TOKEN --test-mode
```

6) InspireHEP 下载器 (NEW! ⚛️)

针对高能物理领域，支持从 InspireHEP 批量下载论文及其引用/被引文献，并自动整理为本项目所需的目录结构。

**特点：**
- 自动下载 PDF 和元数据
- 自动计算年轻学者指数
- 支持从 `mid.txt` 批量导入或命令行直接指定
- **注意**：如果 InspireHEP 上没有提供 PDF 下载链接，程序将自动跳过该文献的下载。

**命令示例：**

从 `mid.txt` 批量下载：
```powershell
python .\main.py meta-pack --mid-file .\inspirehep_source\pre-process\mid.txt --k 5 --verbose
```

直接指定老师和 DOI：
```powershell
python .\main.py meta-pack --teacher "曹庆宏" --dois "10.1103/PhysRevLett.116.061102" --k 3
```

报告输出：`output/示例老师_final_report.md`

## 模块

- `DOIdownloader/download.py`：从 `results.txt` 读取教师与 DOI，按层级下载（含可选被引 cited）
- `tools/pdf2md/pdf2md.py`：调用 MinerU API 批量转换 PDF→Markdown，保留 full.json、图片
- `DOIdownloader/merge_history_to_md.py`：将 PDF 端与 MD 端历史合并至 `data`
- `core/*`：三大工作流与最终报告整合/翻译

## 常见问题

- 缺少 langchain/openai 等依赖：先执行 `pip install -r requirements.txt`
- 未设置 MinerU Token：`pdf2md` 子命令需 `--token` 或环境变量 `MINERU_TOKEN`
- 分析需 LLM Key：`analyze` 会校验 OPENAI_API_KEY

## 质量门（快速结论）

- Build：PASS（CLI 帮助可用；分析需依赖已安装）
- Lint/Typecheck：未强制（建议本地执行）
- Tests：无（建议用样例教师快速试跑）
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
      - `cited/`: 存放用于启发**本科生项目**的复杂度适中的论文。
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
- `tools/pdf2md/pdf2md.py`：调用 MinerU API 批量转换 PDF → Markdown，并保留 full.json 与图片。
- `DOIdownloader/merge_history_to_md.py`：将 PDF 端与 MD 端历史合并至 `data`，便于统一查看。
- `core/*`：三大工作流与最终报告整合、翻译输出。

## 常见问题

- 缺少依赖（如 langchain_*）提示：请先 `pip install -r requirements.txt`。
- MinerU Token 未设置：`pdf2md` 子命令需 `--token` 或环境变量 `MINERU_TOKEN`。
- 未找到数据：`analyze` 默认读取 `data/<教师>`；若你将 MD 放在其他路径，请使用 `--data-root` 指定。

## 质量门（快速结论）

- Build（语法检查）：PASS（仓库内关键脚本语法有效；第三方依赖需安装后方可解析导入）
- Lint/Typecheck：未强制执行（LangChain/依赖项安装后建议本地运行 linters）
- Tests：暂无自动化测试（建议使用小样本数据进行手动验证）

---

示例：
- 类 `WorkflowOrchestrator` 在 `core/workflow_orchestrator.py`
- 最终报告写入 `output/` 目录
- 可选配置位于根目录 `config.ini`
