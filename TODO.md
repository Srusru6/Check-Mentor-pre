# TODO List

## 本部分任务

任务一：对于每篇论文，对它进行总结

任务二：根据核心问题集，对于每篇论文，返回其“相关系数”列表。

任务三：汇总所有论文的信息，生成最终报告。

## 主要实现方式

利用LangChain提供的RAG框架，在其VectorStore环节集成Chroma库，以实现向量存储与检索。

下面这个文档有助于理解我们实现的架构，以及介绍调用LangChain时的函数语法：

[构建检索增强生成 (RAG) 应用：第一部分 | 🦜️🔗 LangChain 框架](https://python.langchain.ac.cn/docs/tutorials/rag/)



注意到，实际上任务二、任务三的联系紧密，它们甚至会用到同一个Chroma库。因此，我们着重分解一下任务二、任务三，以便统一接口语法等问题。

## 任务分解

#### 1、加载论文

LangChain自带文档加载器；也可以外接别的库。

#### 2、使用文本分割器将文档分割成块

注意，我们希望保留文档的一些元数据（metadata），比如论文id、标题、作者、年份等信息。

#### 3、**文本块**向量化

使用Embedding模型，为每个文本块都创建向量。这里需要用到对应模型的api

这意味着我们将为每篇论文创建多个嵌入。

#### 4、使用Chroma库，存储这些向量

（我希望针对所有论文构建一个大的向量库，这样方便于后续统一处理）

#### 5、核心问题分析

我们有若干核心问题，对于每个问题，我们检索一篇论文里最相关的块，然后让模型判断相关度（比如，给出一个Score，并输出理由。这里会涉及一点Prompt工程）。

请注意，你最好将“核心问题”写在一个文件里（比如core_questions.py），而非直接插入在检索程序内；并且，我希望该文件内定义一个字典类Core_Questions，其key描述该问题涉及的方面（比如"research_domain"），其value是自然语言表述的问题（比如“该教授的主要研究领域是什么？”，或者对应的英文版问题）

这一环节最终需要输出一个字典relevance_analysis，它的key对应Core_Questions的key，而value则需要包含相关性评分、确信度、证据、推理过程等。

例如：

```python
relevance_analysis = {
	"research_domain": {
    "score": 0,
    "confidence": 0,
    "evidence": "",
    "reasoning": ""
	}
}
```

**Hint：**

首先，我们检索时，需要针对每篇论文都提供一个输出，因此请注意检索按论文过滤；

其次，Chroma在检索过程中，会返回一个“相似度分数”，我们也可以将其作为“相关度”的一部分，赋予一定权重。

另外，我们的“问题相关”检索是一个复杂的逻辑实现，可以采取更多的检索技巧。参考：

[检索 | 🦜️🔗 LangChain 框架](https://python.langchain.ac.cn/docs/concepts/retrieval/)

#### 6、最终报告生成

我们需要使用一个Chain将检索后的文本块和问题分析传给大模型。

因此，本部分需要访问：每篇论文的总结、每篇论文对每个核心问题的帮助分析，以及量化的相关度作为参数。



从前程序的结果最终存储在一个.json文件中。其文件整体结构为：

```json
{
  "metadata": {},
  "professor_info": {},
  "papers": [],
  "analysis_results": {},
  "correlation_data": {},
  "report_cache": {}
}
```

其中metadata项存储项目元数据，比如：

```json
{
  "metadata": {
    "project_version": "1.0",
    "created_date": "2025-10-01",
    "last_updated": "2025-10-20",
    "total_papers": 100,
    "analysis_model": "gpt-4",
    "embedding_model": "qwen3-embedding-8b",
    "data_sources": [
      "arXiv",
      "Google Scholar", 
    ]
  }
}
```

professor_info项则存储教授数据，包括名字、所在系所等。

papers列表存储了论文元数据（id、标题、作者等），任务一完成的总结，以及爬虫痕迹。

analysis_results项是重点，其key为论文id，value为“5、核心问题分析”输出的relevance_analysis，比如：

```json
{
  "analysis_results": {
    "paper_001": {
        "research_domain": {
          "score": 0.92,
          "confidence": 0.88,
          "evidence": "论文明确提到了量子纠缠在凝聚态系统中的应用",
          "reasoning": "该论文直接解决了教授核心研究领域的问题"
        },
        "technical_approach": {
          "score": 0.85,
          "confidence": 0.91, 
          "evidence": "使用了密度泛函理论和量子蒙特卡洛方法",
          "reasoning": "这些方法是教授实验室的典型技术路线"
        },
        "novelty": {
          "score": 0.78,
          "confidence": 0.82,
          "evidence": "提出了新的纠缠度量方法",
          "reasoning": "该方法在领域内具有创新性"
        },
        "beginner_friendly": {
          "score": 0.65,
          "confidence": 0.75,
          "evidence": "代码已开源，有详细文档",
          "reasoning": "适合初学者复现和扩展"
        }
    }
  }
}
```
请注意，这里举例的问题并非实际问题；真正的core_question

correlation_data和report_cache则是这部分产生的数据缓存。
