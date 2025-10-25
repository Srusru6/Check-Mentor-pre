"""
Workflow 2: 分析领域的热点问题

该工作流的目标是回答第二个核心问题：
"这个领域主要在关心什么问题？"

它通过以下步骤实现：
1. 接收教授的代表作（main_papers）和关键参考文献（ref1_papers）作为输入。
2. 设计一个AI评分机制，评估每篇论文对于“领域问题代表性”的得分。
3. 基于得分较高的论文，综合分析出该领域当前关注的核心问题和技术趋势。
"""
import json
from typing import List, Dict, Any

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from .. import config

class FieldProblemsWorkflow:
    """
    分析领域热点问题的工作流。
    """
    def __init__(self):
        """
        初始化工作流。
        """
        print("  -> FieldProblemsWorkflow initialized.")
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            openai_api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE,
            temperature=0.3
        )

    def _load_paper_content(self, file_path: str) -> str:
        """加载指定路径的 Markdown 文件内容。"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"    ⚠️ Error loading file {file_path}: {e}")
            return ""

    def _rate_single_paper(self, paper_content: str) -> Dict[str, Any]:
        """
        使用 LLM 评估单篇论文，判断其“领域问题代表性”并打分。
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert academic reviewer. Your task is to evaluate a research paper based on its relevance to core problems in its field.
Provide a JSON response with the following structure:
{{
  "problem_representativeness_score": <An integer score from 1 (not representative) to 10 (highly representative)>,
  "justification": "<A brief justification for your score, explaining what core problem the paper addresses.>",
  "identified_problem": "<A concise phrase identifying the core problem or question, e.g., 'scalable quantum entanglement', 'reducing photonic circuit loss'>"
}}"""),
            ("user", "Please evaluate the following paper content and provide the structured JSON output:\n\n---\n{paper_content}\n---")
        ])
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        # 为了避免 API 调用，暂时注释掉并返回占位符
        # rating_result = chain.invoke({"paper_content": paper_content[:12000]})
        rating_result = {
            "problem_representativeness_score": 8, # 占位分数
            "justification": "占位理由：该论文直接解决了其领域内的一个关键挑战。",
            "identified_problem": "占位符问题"
        }
        
        return rating_result

    def _synthesize_hot_topics(self, rated_papers: List[Dict[str, Any]]) -> str:
        """
        基于高分论文，综合分析出领域的热点问题。
        """
        prompt = ChatPromptTemplate.from_template("""You are a senior research analyst. Based on a list of highly-rated papers, identify and summarize the key research problems and hot topics in this field.

The analyses of the papers are provided below:
{papers_json}

Your summary should:
1. List 2-4 main hot topics or core problems identified from these papers.
2. Provide a brief, coherent narrative explaining what these hot topics are and why they are important.
3. Be about 150-200 words.

Synthesized Summary of Hot Topics:""")

        chain = prompt | self.llm

        papers_json_str = json.dumps(rated_papers, indent=2, ensure_ascii=False)

        # 为了避免 API 调用，暂时注释掉并返回占位符
        # synthesis_result = chain.invoke({"papers_json": papers_json_str})
        # return synthesis_result.content
        return "此部分为热点问题综合总结占位符。基于对高分论文的分析，当前该领域的热点问题包括 [占位符热点1] 和 [占位符热点2]。这些问题之所以重要，是因为 [占位符原因总结]。"

    def run(self, main_papers: List[Dict[str, Any]], ref1_papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        执行分析领域热点问题的完整流程。
        """
        all_papers = main_papers + ref1_papers
        print(f"  -> Running FieldProblemsWorkflow on {len(all_papers)} papers.")

        if not all_papers:
            print("  -> No papers provided. Skipping workflow.")
            return {
                "summary": "没有提供任何论文，无法分析领域热点问题。",
                "hot_topics": [],
                "rated_papers": []
            }

        # 步骤1: 对每篇论文进行评分
        all_rated_papers = []
        for paper in all_papers:
            print(f"    -> Rating paper: {paper['title']}")
            content = self._load_paper_content(paper['md_filename'])
            if not content:
                continue
            
            rating = self._rate_single_paper(content)
            rating['paper_id'] = paper['id']
            rating['title'] = paper['title']
            all_rated_papers.append(rating)

        # 步骤2: 筛选高分论文
        high_score_threshold = 7
        high_score_papers = [p for p in all_rated_papers if p.get("problem_representativeness_score", 0) >= high_score_threshold]
        print(f"    -> Found {len(high_score_papers)} papers with score >= {high_score_threshold}.")

        # 步骤3: 综合高分论文，提炼热点问题
        if high_score_papers:
            print("    -> Synthesizing hot topics from high-score papers...")
            summary = self._synthesize_hot_topics(high_score_papers)
            hot_topics = list(set(p.get("identified_problem", "N/A") for p in high_score_papers))
        else:
            print("    -> No high-score papers found. Cannot synthesize hot topics.")
            summary = "没有发现具有足够领域问题代表性的论文，无法总结出当前的热点问题。"
            hot_topics = []

        # 步骤4: 格式化最终输出
        final_result = {
            "summary": summary,
            "hot_topics": hot_topics,
            "rated_papers": [
                {
                    "paper_id": p['paper_id'],
                    "title": p['title'],
                    "score": p.get('problem_representativeness_score', 'N/A'),
                    "justification": p.get('justification', 'N/A')
                }
                for p in all_rated_papers
            ]
        }

        return final_result
