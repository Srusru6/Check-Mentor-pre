"""
Workflow 3: 分析本科生可参与的项目

该工作流的目标是回答第三个核心问题：
"有哪些适合本科生参与的科研项目？"

它通过以下步骤实现：
1. 接收关键参考文献（ref1_papers）和潜在项目文献（ref2_papers）作为输入。
2. 设计一个AI评估机制，从“工作复杂度”和“本科生友好度”两个维度对每篇论文进行打分。
3. 基于得分适中的论文，提炼出潜在的、可操作性强的本科生科研项目点。
"""
import json
import time
from typing import List, Dict, Any
from tqdm import tqdm

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from .. import config
from .cache_manager import CacheManager

class UndergradProjectsWorkflow:
    """
    分析本科生可参与项目的工作流。
    """
    def __init__(self, main_llm, fallback_llm=None):
        """
        初始化工作流，接收外部传入的LLM实例。
        """
        print("  -> UndergradProjectsWorkflow initialized.")
        self.llm = main_llm
        self.fallback_llm = fallback_llm
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
            # print("      -> Attempting main LLM...")
            result = chain.invoke({"paper_content": paper_content[:12000]})
            return result
        except (OutputParserException, json.JSONDecodeError) as e:
            # print(f"      ⚠️ Main LLM output parsing failed: {e}. Retrying with main LLM...")
            try:
                result = chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception as final_e:
                # print(f"      ⚠️ Main LLM retry failed: {final_e}.")
                pass
        except Exception as e:
            # print(f"      ⚠️ Main LLM failed: {e}")
            pass

        if self.fallback_llm:
            try:
                # print("      -> Attempting fallback LLM...")
                fallback_chain = chain.with_components(llm=self.fallback_llm)
                result = fallback_chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception as e:
                # print(f"      ⚠️ Fallback LLM also failed: {e}")
                pass
        
        return {"error": "Both main and fallback LLMs failed."}

    def _evaluate_single_paper(self, paper_content: str) -> Dict[str, Any]:
        """
        使用 LLM 评估单篇论文，判断其“工作复杂度”和“本科生友好度”。
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an experienced professor evaluating research papers for potential undergraduate projects.
Provide a JSON response with the following structure:
{{
  "complexity_score": <An integer score from 1 (very simple) to 10 (very complex) for the overall technical difficulty>,
  "friendliness_score": <An integer score from 1 (very unfriendly) to 10 (very friendly) for undergraduate involvement, considering required background knowledge and feasibility>,
  "project_idea": "<A concrete, one-sentence project idea for an undergraduate based on this paper. If not suitable, state 'Not suitable'.>"
}}"""),
            ("user", "Please evaluate the following paper content for undergraduate project suitability and provide the structured JSON output:\n\n---\n{paper_content}\n---")
        ])
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        evaluation_result = self._invoke_llm_with_fallback(chain, paper_content)
        # time.sleep(1) # Delay moved to the main loop
        
        return evaluation_result

    def _synthesize_project_suggestions(self, suitable_papers: List[Dict[str, Any]]) -> str:
        """
        基于筛选出的论文，综合生成一份项目建议总结。
        """
        prompt = ChatPromptTemplate.from_template("""You are a helpful academic advisor. Based on a list of papers suitable for undergraduates, create a summary of potential research project areas.

The evaluated papers are provided below:
{papers_json}

Your summary should:
1. Group the project ideas into 2-3 thematic areas.
2. Provide a brief, encouraging narrative about why these areas are exciting for undergraduate research.
3. Be about 150-200 words.

Synthesized Summary of Project Suggestions:""")

        chain = prompt | self.llm

        papers_json_str = json.dumps(suitable_papers, indent=2, ensure_ascii=False)

        synthesis_result = chain.invoke({"papers_json": papers_json_str})
        return synthesis_result.content

    def run(self, professor_name: str, ref2_papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        执行分析本科生项目的完整流程。
        """
        self.cache = CacheManager(professor_name, "undergrad_projects_analysis")
        all_papers = ref2_papers
        print(f"  -> Running UndergradProjectsWorkflow on {len(all_papers)} papers (ref2 only).")

        if not all_papers:
            print("  -> No papers provided. Skipping workflow.")
            return {
                "summary": "没有提供任何论文，无法分析本科生可参与的项目。",
                "project_ideas": [],
                "rated_papers": []
            }

        # 步骤1: 对每篇论文进行评估
        all_evaluated_papers = []
        for paper in tqdm(all_papers, desc="  -> Evaluating undergrad projects"):
            paper_id = paper['id']
            cached_result = self.cache.get(
                paper_id,
                required_keys=["paper_id", "title", "project_idea", "complexity_score", "friendliness_score"]
            )

            if cached_result:
                evaluation = cached_result
            else:
                content = self._load_paper_content(paper['md_filename'])
                if not content:
                    continue
                
                evaluation_result = self._evaluate_single_paper(content)

                if evaluation_result.get("error"):
                    tqdm.write(f"    ⚠️ Skipped paper '{paper['title']}' due to LLM failure.")
                    continue

                # 构建完整的评估对象并缓存
                evaluation = {
                    **evaluation_result,
                    'paper_id': paper_id,
                    'title': paper['title']
                }
                self.cache.set(paper_id, evaluation)
                time.sleep(1) # Delay after successful API call

            all_evaluated_papers.append(evaluation)

        if not all_evaluated_papers:
            print("\n  -> No papers were successfully evaluated. Skipping synthesis.")
            return {
                "summary": "所有论文均未能成功评估，无法分析本科生可参与的项目。",
                "project_ideas": [],
                "rated_papers": []
            }

        # 步骤2: 筛选合适的论文 (复杂度适中，友好度较高)
        suitable_papers = [
            p for p in all_evaluated_papers 
            if 4 <= p.get("complexity_score", 0) <= 8 
            and p.get("friendliness_score", 0) >= 6
        ]
        print(f"\n    -> Found {len(suitable_papers)} suitable papers for undergraduate projects.")

        # 步骤3: 综合项目建议
        if suitable_papers:
            print("    -> Synthesizing project suggestions...")
            summary = self._synthesize_project_suggestions(suitable_papers)
            project_ideas = [
                {
                    "paper_id": p['paper_id'],
                    "title": p['title'],
                    "idea": p.get("project_idea")
                }
                for p in suitable_papers if "Not suitable" not in p.get("project_idea", "")
            ]
        else:
            print("    -> No suitable papers found. Cannot synthesize project suggestions.")
            summary = "没有发现难度适中且适合本科生参与的论文，无法提供具体的项目建议。"
            project_ideas = []

        # 步骤4: 格式化最终输出
        final_result = {
            "summary": summary,
            "project_ideas": project_ideas,
            "rated_papers": [
                {
                    "paper_id": p['paper_id'],
                    "title": p['title'],
                    "complexity_score": p.get('complexity_score', 'N/A'),
                    "friendliness_score": p.get('friendliness_score', 'N/A')
                }
                for p in all_evaluated_papers
            ]
        }

        return final_result
