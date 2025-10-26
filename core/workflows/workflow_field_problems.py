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
import time
import re
from collections import defaultdict
from typing import List, Dict, Any

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from .. import config
from .cache_manager import CacheManager

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
            temperature=config.LLM_TEMPERATURE
        )
        
        # 初始化备用 LLM
        self.fallback_llm = None
        if config.DASHSCOPE_API_KEY:
            try:
                self.fallback_llm = ChatTongyi(
                    model=config.LLM_FALLBACK_MODEL,
                    dashscope_api_key=config.DASHSCOPE_API_KEY,
                    temperature=config.LLM_TEMPERATURE
                )
                print("  -> Fallback LLM (DashScope) initialized.")
            except Exception as e:
                print(f"  ⚠️ Could not initialize Fallback LLM. Reason: {e}")
                self.fallback_llm = None
        else:
            print("  -> Fallback LLM not configured (DASHSCOPE_API_KEY not found).")
            
        self.cache = None

    def _load_paper_content(self, file_path: str) -> str:
        """加载指定路径的 Markdown 文件内容。"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"    ⚠️ Error loading file {file_path}: {e}")
            return ""

    def _invoke_llm_with_fallback(self, chain, paper_content):
        """
        调用LLM，如果主LLM失败，则尝试备用LLM。
        """
        try:
            print("      -> Attempting main LLM...")
            result = chain.invoke({"paper_content": paper_content[:12000]})
            return result
        except (OutputParserException, json.JSONDecodeError) as e:
            print(f"      ⚠️ Main LLM output parsing failed: {e}. Retrying with main LLM...")
            try:
                result = chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception as final_e:
                print(f"      ⚠️ Main LLM retry failed: {final_e}.")
        except Exception as e:
            print(f"      ⚠️ Main LLM failed: {e}")

        if self.fallback_llm:
            try:
                print("      -> Attempting fallback LLM...")
                fallback_chain = chain.with_components(llm=self.fallback_llm)
                result = fallback_chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception as e:
                print(f"      ⚠️ Fallback LLM also failed: {e}")
        
        raise RuntimeError("Both main and fallback LLMs failed to process the paper.")

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

        rating_result = self._invoke_llm_with_fallback(chain, paper_content)
        time.sleep(1) # Add a delay to avoid rate limiting
        
        return rating_result

    def _group_papers_by_problem(self, papers: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        (Map Step) 根据识别出的问题对论文进行分组。
        使用简单的关键词匹配来聚合相似问题。
        """
        print("      -> Grouping papers by identified problem...")
        
        # 提取核心词作为分组依据，忽略常见的、非描述性的词语
        stop_words = {'and', 'the', 'of', 'in', 'a', 'for', 'with', 'on', 'to', 'from', 'by'}
        
        def get_group_key(problem_phrase: str) -> str:
            # 转换为小写，移除标点
            normalized = re.sub(r'[^\w\s]', '', problem_phrase.lower())
            # 分词并移除停用词，然后排序，确保顺序不影响key
            keywords = sorted([word for word in normalized.split() if word not in stop_words])
            # 如果没有关键词，则返回原始短语
            return ' '.join(keywords) if keywords else problem_phrase

        groups = defaultdict(list)
        for paper in papers:
            problem = paper.get("identified_problem", "Uncategorized")
            group_key = get_group_key(problem)
            groups[group_key].append(paper)
        
        print(f"      -> Grouped into {len(groups)} topics.")
        return groups

    def _summarize_group(self, group_key: str, group_papers: List[Dict[str, Any]]) -> str:
        """
        (Reduce Step) 对单个论文小组进行总结。
        """
        print(f"        -> Summarizing group '{group_key}' with {len(group_papers)} papers...")

        prompt = ChatPromptTemplate.from_template("""You are a research analyst summarizing a cluster of papers that address a similar problem.

The problem area is: "{group_key}"
The papers in this group are:
{papers_json}

Your task is to write a concise summary for this specific group. Your summary MUST:
1.  Start by clearly stating the core problem this group addresses.
2.  Summarize the common approaches or findings within the group.
3.  **Crucially, highlight any unique, novel, or outlier ideas, methods, or findings.** Do not let these unique points get lost. Mention them explicitly, for example: "While most papers focused on X, one paper uniquely proposed Y..."
4.  Keep the summary for this group to about 100-150 words.

Group Summary:""")
        
        chain = prompt | self.llm
        papers_json_str = json.dumps(group_papers, indent=2, ensure_ascii=False)

        # 限制传入的JSON字符串长度，以防万一
        max_length = 12000
        if len(papers_json_str) > max_length:
            # 一个简单的截断策略
            papers_to_include = []
            current_length = 0
            for paper in group_papers:
                paper_str = json.dumps(paper, ensure_ascii=False)
                if current_length + len(paper_str) > max_length:
                    break
                papers_to_include.append(paper)
                current_length += len(paper_str)
            papers_json_str = json.dumps(papers_to_include, indent=2, ensure_ascii=False)


        summary = chain.invoke({
            "group_key": group_key,
            "papers_json": papers_json_str
        }).content
        time.sleep(1) # Add a delay
        return summary

    def _synthesize_final_summary(self, group_summaries: List[str]) -> str:
        """
        (Final Synthesis Step) 基于所有小组的总结，生成最终的综合报告。
        """
        print("    -> Synthesizing final summary from group summaries...")
        prompt = ChatPromptTemplate.from_template("""You are a senior research analyst. You have been given summaries from several clusters of research papers. Your task is to synthesize these into a single, coherent overview of the field's hot topics.

The summaries for each research cluster are provided below:
---
{group_summaries_text}
---

Your final synthesis should:
1.  Identify and list 2-4 main hot topics or core problems that emerge from the collective summaries.
2.  Provide a brief, coherent narrative explaining what these hot topics are, how they relate to each other, and why they are important for the field.
3.  **Integrate insights from the summaries, preserving any mentioned novel or unique points.** For instance, if a summary mentions an outlier idea, ensure it is reflected in the final report as a potential emerging trend.
4.  Be about 200-250 words.

Synthesized Summary of Hot Topics:""")

        chain = prompt | self.llm
        
        summaries_text = "\n\n".join(f"Cluster Summary {i+1}:\n{summary}" for i, summary in enumerate(group_summaries))

        synthesis_result = chain.invoke({"group_summaries_text": summaries_text})
        return synthesis_result.content

    def run(self, professor_name: str, main_papers: List[Dict[str, Any]], ref1_papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        执行分析领域热点问题的完整流程。
        """
        self.cache = CacheManager(professor_name, "field_problems_analysis")
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
            paper_id = paper['id']
            cached_result = self.cache.get(paper_id)

            if cached_result:
                print(f"    -> Found cached rating for paper: {paper['title']}")
                rating = cached_result
            else:
                print(f"    -> Rating paper: {paper['title']}")
                content = self._load_paper_content(paper['md_filename'])
                if not content:
                    continue
                
                rating = self._rate_single_paper(content)
                self.cache.set(paper_id, rating)

            rating['paper_id'] = paper_id
            rating['title'] = paper['title']
            all_rated_papers.append(rating)

        # 步骤2: 筛选高分论文
        high_score_threshold = 7
        high_score_papers = [p for p in all_rated_papers if p.get("problem_representativeness_score", 0) >= high_score_threshold]
        print(f"    -> Found {len(high_score_papers)} papers with score >= {high_score_threshold}.")

        # 步骤3: Map-Reduce综合高分论文，提炼热点问题
        if high_score_papers:
            # Map: 将论文按问题分组
            paper_groups = self._group_papers_by_problem(high_score_papers)
            
            # Reduce: 对每个小组进行总结
            group_summaries = []
            # 为保证输出稳定性，对group key排序
            sorted_group_keys = sorted(paper_groups.keys())
            for group_key in sorted_group_keys:
                group_papers = paper_groups[group_key]
                # 如果一个小组论文太少，可能只是措辞差异，直接用其分析结果，不单独总结
                if len(group_papers) <= 2:
                    # 直接将论文的justification作为小组总结
                    combined_justification = ". ".join([p['justification'] for p in group_papers])
                    group_summary = f"A small cluster focused on '{group_key}'. The key idea is: {combined_justification}"
                    group_summaries.append(group_summary)
                else:
                    group_summary = self._summarize_group(group_key, group_papers)
                    group_summaries.append(group_summary)

            # Final Synthesis: 综合所有小组的总结
            if group_summaries:
                summary = self._synthesize_final_summary(group_summaries)
            else:
                summary = "Could not generate group summaries, unable to synthesize hot topics."

            hot_topics = list(paper_groups.keys())
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
