# 元数据功能快速入门指南

本指南将引导你完成为论文添加元数据的完整流程，以提升 Check-Mentor 的分析质量。

## 步骤 1: 准备论文文件

确保你的 `.md` 格式的论文文件已经放置在正确的目录结构下。

例如，对于教授“王剑威”，目录结构应如下：
```
data/
└── 王剑威/
    ├── main/
    │   ├── paper1.md
    │   └── paper2.md
    ├── ref1/
    └── cited/
```

## 步骤 2: 生成元数据模板

使用 `metadata_tools.py` 脚本为特定目录（例如 `main` 目录）下的所有论文自动生成一个 `metadata.json` 模板文件。

打开终端，执行以下命令：

```bash
# 语法: python metadata_tools.py generate [输出文件名] --paper-dir [论文所在目录]
# 示例:
python metadata_tools.py generate data/王剑威/main/metadata.json --paper-dir data/王剑威/main
```

执行后，你会在 `data/王剑威/main/` 目录下看到一个新文件 `metadata.json`。其内容如下：

```json
[
    {
        "filename": "paper1.md",
        "doi": "",
        "authors": [],
        "publication_date": "YYYY-MM-DD",
        "young_scholar_index": -1
    },
    {
        "filename": "paper2.md",
        "doi": "",
        "authors": [],
        "publication_date": "YYYY-MM-DD",
        "young_scholar_index": -1
    }
]
```
该模板已自动为你填充了 `filename` 字段。

## 步骤 3: 填写元数据信息

现在，打开 `metadata.json` 文件，并手动填写每篇论文的详细信息。

- **`doi`**: 论文的唯一标识符。
- **`authors`**: 一个包含所有作者姓名的数组。
- **`publication_date`**: 论文的发表日期，**严格遵循 `YYYY-MM-DD` 格式**。
- **`young_scholar_index`**: 如果作者中有青年学者，填写其在 `authors` 数组中的索引（从0开始）；否则保持 `-1`。

**填写完成后的示例：**
```json
[
    {
        "filename": "paper1.md",
        "doi": "10.1038/nature12345",
        "authors": ["John Doe", "Jane Smith", "Peter Jones"],
        "publication_date": "2023-05-20",
        "young_scholar_index": 1
    },
    {
        "filename": "paper2.md",
        "doi": "10.1126/science.abc6789",
        "authors": ["Alice Williams", "Bob Brown"],
        "publication_date": "2021-11-10",
        "young_scholar_index": -1
    }
]
```

> **提示**: 你可以为 `ref1` 和 `cited` 目录重复以上步骤，创建它们各自的 `metadata.json` 文件。

## 步骤 4: 验证元数据（可选但推荐）

为了确保你填写的信息格式正确，可以使用 `validate` 命令进行检查。

```bash
# 语法: python metadata_tools.py validate [元数据文件路径]
# 示例:
python metadata_tools.py validate data/王剑威/main/metadata.json
```

如果格式完全正确，你会看到成功提示。如果存在错误（如日期格式不正确、文件名不匹配等），脚本会给出明确的错误信息，方便你修正。

## 步骤 5: 正常运行分析程序

完成以上步骤后，你无需做任何额外操作。只需像往常一样运行 `main.py`。

```bash
python main.py --target "王剑威"
```

系统会自动检测到 `metadata.json` 文件，加载其中的信息，并在分析过程中利用这些元数据来**智能排序论文、计算时效性得分、识别青年学者**等，从而产出更高质量的分析报告。

---

**总结**:
1. **生成模板**: `python metadata_tools.py generate ...`
2. **填写信息**: 手动编辑 `metadata.json`。
3. **验证格式**: `python metadata_tools.py validate ...`
4. **运行分析**: `python main.py --target "..."`

现在，你的分析流程已经获得了元数据的加持！
