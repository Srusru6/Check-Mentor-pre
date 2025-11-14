# 元数据功能详细文档

## 1. 概述

元数据（Metadata）是对论文数据的结构化描述。在 Check-Mentor 项目中，引入元数据旨在通过提供更丰富的上下文信息（如发表时间、作者信息等），显著提升分析流程的智能化程度和分析结果的深度与准确性。

本系统设计为**完全向后兼容**，即使不存在元数据文件，核心分析功能依然可以正常运行。但提供元数据将解锁更高级的功能。

## 2. 元数据文件结构

元数据以 `metadata.json` 的形式存储在每个论文子目录中（例如 `data/教师姓名/main/metadata.json`）。它是一个包含多个对象的 JSON 数组，每个对象对应一篇论文。

### 2.1. 字段详解

每个论文条目包含以下字段：

| 字段名 | 类型 | 是否必须 | 描述 |
| :--- | :--- | :--- | :--- |
| `filename` | String | 是 | 论文的文件名（例如 `paper1.md`），用于将元数据与文件关联。 |
| `doi` | String | 否 | 论文的数字对象标识符（Digital Object Identifier）。建议填写，用于唯一标识。 |
| `authors` | Array[String] | 否 | 作者列表，按原文顺序排列。 |
| `publication_date` | String | 否 | 论文的发表日期，格式为 `YYYY-MM-DD`。这是计算时效性得分的关键。 |
| `young_scholar_index` | Integer | 否 | **青年学者索引**。标记第一位青年学者在 `authors` 数组中的位置（从0开始）。若无青年学者或不确定，则为 `-1`。 |

### 2.2. 示例

```json
[
    {
        "filename": "sample_paper_1.md",
        "doi": "10.1038/nature12345",
        "authors": [
            "John Doe",
            "Jane Smith",
            "Peter Jones"
        ],
        "publication_date": "2023-05-20",
        "young_scholar_index": 1
    },
    {
        "filename": "sample_paper_2.md",
        "doi": "10.1126/science.abc6789",
        "authors": [
            "Alice Williams",
            "Bob Brown"
        ],
        "publication_date": "2021-11-10",
        "young_scholar_index": -1
    }
]
```

## 3. 核心功能

元数据驱动了以下核心功能，使分析更智能、更具洞察力。

### 3.1. 智能排序与时效性评分

- **排序**: 在进行分析前，系统会根据 `publication_date` 对论文进行降序排序，确保**最新的研究成果被优先处理**。
- **时效性得分 (Recency Score)**: 系统会根据发表日期自动计算一个 `recency_score`（范围 0-1）。该分数随时间推移而衰减，最近发表的论文得分接近1，而 오래된 论文得分接近0。这个分数是后续权重计算和代表性采样中的一个重要因子。

### 3.2. 青年学者识别

通过 `young_scholar_index` 字段，系统能够：
- 识别出有青年学者（特别是第一作者或通讯作者）参与的研究。
- 在“本科生项目建议”等工作流中，可能会对这类论文赋予更高权重，因为它们可能更适合作为入门研究的参考。

### 3.3. 数据完整性与未来扩展

- **DOI**: 确保了每篇论文的唯一性，为未来实现更高级的功能（如自动抓取引用、构建引文网络）打下基础。
- **作者列表**: 完整的作者信息是进行学者合作网络分析的前提。

## 4. `metadata_tools.py` 工具集

为了简化元数据的创建和管理，项目提供了 `metadata_tools.py` 脚本。

### 4.1. `generate` - 生成元数据模板

此命令会自动扫描指定目录下的所有 `.md` 文件，并生成一个包含这些文件条目的 `metadata.json` 模板。

**使用方法:**
```bash
python metadata_tools.py generate [输出路径] --paper-dir [论文目录]
```

**示例:**
```bash
# 为 data/王剑威/main/ 目录下的论文生成元数据模板
python metadata_tools.py generate data/王剑威/main/metadata.json --paper-dir data/王剑威/main
```
执行后，`data/王剑威/main/metadata.json` 文件会被创建，你只需填充其中的 `doi`、`authors` 等字段即可。

### 4.2. `validate` - 验证元数据格式

在手动编辑 `metadata.json` 后，使用此命令可以检查文件格式是否正确，确保程序能够顺利解析。

**验证内容:**
- JSON 格式是否合法。
- `filename` 对应的文件是否存在于指定目录。
- `publication_date` 是否为 `YYYY-MM-DD` 格式。
- `young_scholar_index` 是否为整数。

**使用方法:**
```bash
python metadata_tools.py validate [元数据文件路径]
```

**示例:**
```bash
python metadata_tools.py validate data/王剑威/main/metadata.json
```

## 5. 与核心工作流的集成

1. **数据加载**: `DataManager` 在加载论文时，会自动检测并解析对应的 `metadata.json` 文件，将元数据附加到每篇论文对象上。
2. **工作流编排**: `WorkflowOrchestrator` 在启动三大工作流（贡献、热点、本科生项目）之前，会利用元数据对论文进行排序。
3. **智能聚类**: 在论文数量过多触发聚类时，元数据（特别是时效性得分）是挑选**代表性论文**的关键依据，确保选出的论文既有代表性，又能反映最新趋势。

通过这种方式，元数据无缝地融入了从数据准备到最终分析的整个生命周期。
