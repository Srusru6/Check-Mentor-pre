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
from typing import List, Dict, Any
from tqdm import tqdm

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from .cache_manager import CacheManager

class FieldProblemsWorkflow:
    """
    分析领域热点问题的工作流。
    """
    def __init__(self, main_llm, fallback_llm=None):
        """
        初始化工作流，接收外部传入的LLM实例。
        """
        print("  -> FieldProblemsWorkflow initialized.")
        self.llm = main_llm
        self.fallback_llm = fallback_llm
        self.cache = None

    def _print_section_header(self, title: str, level: int = 1):
        """打印带样式的章节标题"""
        if level == 1:
            print(f"\n{'='*70}\n🎓 {title}\n{'='*70}")
        elif level == 2:
            print(f"\n--- {title} ---")

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
            result = chain.invoke({"paper_content": paper_content[:12000]})
            return result
        except (OutputParserException, json.JSONDecodeError):
            try:
                result = chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception:
                pass
        except Exception:
            pass

        if self.fallback_llm:
            try:
                fallback_chain = chain.with_llm(self.fallback_llm)
                result = fallback_chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception:
                pass
        
        return {"error": "Both main and fallback LLMs failed."}

    def _rate_single_paper(self, paper_content: str) -> Dict[str, Any]:
        """
        使用 LLM 评估单篇论文，基于四维模型进行打分。
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a top-tier, discerning academic reviewer, known for your critical judgment and ability to differentiate between good and truly exceptional work. Your reputation depends on it. **You must avoid grade inflation.** Use the entire 0.0 to 1.0 scale meaningfully. A score of 0.9 or higher should be reserved only for papers that are genuine landmarks in their field.

You will provide a multi-dimensional evaluation based on the following four criteria. Each score MUST be a float between 0.0 and 1.0.

**Evaluation Criteria & Weights:**

1.  **Significance (Weight: 30%)**: How important is the core problem this paper addresses?
    - 1.0: A foundational, field-defining problem (e.g., demonstrating quantum supremacy, solving a major open question).
    - 0.7: A known, important sub-problem that unlocks significant progress.
    - 0.4: A niche or incremental issue with limited impact.
    - 0.1: A minor or solved problem.

2.  **Novelty (Weight: 10%)**: How original is the paper's proposed SOLUTION or METHOD?
    - 1.0: A completely new paradigm or technique that changes how the field works.
    - 0.7: A clever and non-obvious combination or improvement of existing methods.
    - 0.4: A standard, incremental improvement.
    - 0.1: A routine application of well-known methods.
    - **Note for Review Papers**: For a review, this score is expected to be low. Do not penalize it for this.

3.  **Clarity (Weight: 30%)**: How clearly is the problem, its context, and the proposed solution/synthesis presented?
    - 1.0: A masterclass in scientific communication. A new student could grasp the field's landscape from this paper alone. The structure is flawless.
    - 0.7: Well-written and structured, understandable by experts with some effort.
    - 0.4: Generally understandable, but key parts are confusing, poorly structured, or buried in jargon.
    - 0.1: Poorly written, illogical, and hard to understand.
    - **Note for Review Papers**: A well-organized review that clarifies the state of the art and provides a coherent narrative should score very highly here. This is a primary metric for a good review.

4.  **Potential (Weight: 30%)**: How likely is this work to inspire or enable significant future research?
    - 1.0: Opens up entirely new research avenues or provides a critical enabling tool that will be widely adopted.
    - 0.7: Likely to lead to a flurry of direct follow-up studies and citations.
    - 0.4: May be cited or lead to a few incremental studies.
    - 0.1: Unlikely to have a significant impact on the field.
    - **Note for Review Papers**: A comprehensive and insightful review that successfully maps out future challenges and opportunities should score very highly here. This is a primary metric for a good review.

You MUST provide a JSON response with the following structure:
{{
  "significance_score": <float between 0.0 and 1.0>,
  "novelty_score": <float between 0.0 and 1.0>,
  "clarity_score": <float between 0.0 and 1.0>,
  "potential_score": <float between 0.0 and 1.0>,
  "justification": "<A concise, critical justification for your scores, referencing the criteria above. Explain WHY you gave these specific scores.>",
  "identified_problem": "<A short, precise phrase identifying the core problem the paper tackles.>"
}}"""),
            ("user", "Please analyze the following paper content and provide the structured JSON output:\n\n---\n{paper_content}\n---")
        ])
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        analysis_result = self._invoke_llm_with_fallback(chain, paper_content)
        
        if "error" in analysis_result:
            return analysis_result
            
        required_keys = ["significance_score", "novelty_score", "clarity_score", "potential_score"]
        if not all(key in analysis_result for key in required_keys):
            return {"error": "LLM response was missing one or more required score keys."}

        return analysis_result

    def _summarize_hot_topics(self, synthesis_context: str) -> Dict[str, Any]:
        """
        (New) Synthesizes hot topics directly from a list of top-rated papers.
        This replaces the more complex map-reduce logic for simplicity and robustness.
        """
        print("    -> Synthesizing hot topics from top-rated papers...")

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a senior research analyst. You have been given a list of top-rated papers from a specific field. Your task is to synthesize this information into a coherent overview of the field's hot topics.

The papers are provided below, each with a title, the core problem it addresses, and a justification for its high rating.
---
{synthesis_context}
---

Your final output MUST be a JSON object with the following structure:
{{
  "summary": "<A brief, coherent narrative (about 200-250 words) explaining what these hot topics are, how they relate to each other, and why they are important for the field. Integrate insights from the paper justifications, preserving any mentioned novel or unique points.>",
  "hot_topics": [
    {{
      "topic_name": "<The name of the first main hot topic, derived from the papers>",
      "challenge": "<A brief description of the core challenge or question for this topic.>",
      "related_papers": ["<Title of paper 1>", "<Title of paper 2>"]
    }}
  ]
}}

Instructions:
1.  Read through all the provided paper details.
2.  Identify 2-4 overarching themes or "hot topics" that emerge from the collective 'Identified Problem' fields.
3.  For each topic, formulate a concise `topic_name` and `challenge`.
4.  Group the paper titles under the most relevant `hot_topics` they belong to. A paper can be listed under multiple topics if it's relevant.
5.  Write the final `summary` narrative based on all the information.
"""),
            ("user", "The context containing the top-rated papers is provided above. Please generate the JSON output.")
        ])

        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        try:
            synthesis_result = chain.invoke({
                "synthesis_context": synthesis_context
            })
            return synthesis_result
        except Exception as e:
            print(f"    ⚠️ Error during final synthesis: {e}")
            return {
                "summary": "Failed to synthesize final summary due to an error.",
                "hot_topics": []
            }

    def run(self, main_papers: List[Dict[str, Any]], ref1_papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        执行工作流，分析所有论文并识别领域热点问题。
        """
        self._print_section_header("Workflow 2: Analyzing Field Problems", level=2)
        
        if not main_papers:
             print("  -> No main papers provided. Cannot determine professor name for cache.")
             cache_filename = "default_field_problems_analysis_cache.json"
        else:
            cache_filename = f"{main_papers[0]['authors'][0]}_field_problems_analysis_cache.json"
        self.cache = CacheManager(cache_filename)
        print(f"  -> Cache file set to: {self.cache.cache_path}")

        all_papers = main_papers + ref1_papers
        
        if not all_papers:
            print("  -> No papers provided. Skipping workflow.")
            return {
                "summary": "没有提供任何论文，无法分析领域热点问题。",
                "hot_topics": [],
                "analyzed_papers": [],
            }

        # 1. 评估所有论文的“领域问题代表性”
        print(f"\n  [Step 1/2] Evaluating {len(all_papers)} papers for field relevance...")
        
        rated_papers = []
        
        with tqdm(total=len(all_papers), desc="  Rating papers") as pbar:
            for paper in all_papers:
                paper_id = paper["id"]
                
                cached_result = self.cache.get(paper_id)
                if cached_result:
                    pbar.update(1)
                    pbar.set_postfix_str("Cached")
                    if all(k in cached_result for k in ['significance_score', 'novelty_score', 'clarity_score', 'potential_score']):
                        # 将缓存结果与元数据合并
                        full_cached_result = {**cached_result, 'paper_id': paper_id, 'title': paper['title']}
                        rated_papers.append(full_cached_result)
                        continue
                    else:
                        pbar.set_postfix_str("Invalid Cache, Re-analyzing")

                paper_content = self._load_paper_content(paper["md_filename"])
                if not paper_content:
                    pbar.update(1)
                    pbar.set_postfix_str("Skipped (no content)")
                    continue

                analysis_result = self._rate_single_paper(paper_content)
                
                if "error" in analysis_result:
                    pbar.update(1)
                    pbar.set_postfix_str(f"Error ({analysis_result['error']})")
                    continue

                s_score = analysis_result.get('significance_score', 0)
                n_score = analysis_result.get('novelty_score', 0)
                c_score = analysis_result.get('clarity_score', 0)
                p_score = analysis_result.get('potential_score', 0)
                
                weighted_score = (s_score * 0.3) + (n_score * 0.1) + (c_score * 0.3) + (p_score * 0.3)
                analysis_result["weighted_score"] = round(weighted_score, 2)

                full_result = {**analysis_result, "paper_id": paper_id, "title": paper["title"]}
                
                rated_papers.append(full_result)
                self.cache.set(paper_id, analysis_result)
                
                pbar.update(1)
                pbar.set_postfix_str(f"Score: {weighted_score:.2f}")
                time.sleep(0.1)
        
        if not rated_papers:
            print("\n  -> No papers were successfully rated. Skipping synthesis.")
            return {
                "summary": "所有论文均未能成功评分，无法分析领域热点问题。",
                "hot_topics": [],
                "analyzed_papers": [],
            }

        # 2. 基于高分论文，综合分析热点问题
        print("\n  [Step 2/2] Synthesizing hot topics from top-rated papers...")
        
        rated_papers.sort(key=lambda x: x.get("weighted_score", 0), reverse=True)
        
        top_n = min(len(rated_papers), 10)
        top_papers = rated_papers[:top_n]

        if not top_papers:
            print("    ⚠️ No high-score papers found. Cannot synthesize hot topics.")
            return {
                "summary": "未能成功评估任何论文，无法生成领域热点问题总结。",
                "hot_topics": [],
                "analyzed_papers": []
            }

        synthesis_context = "Here are the top-rated papers identified as most representative of the field's key problems:\n\n"
        for i, paper in enumerate(top_papers, 1):
            synthesis_context += f"--- Paper {i} ---\n"
            synthesis_context += f"Title: {paper.get('title', 'N/A')}\n"
            synthesis_context += f"Identified Problem: {paper.get('identified_problem', 'N/A')}\n"
            synthesis_context += f"Justification: {paper.get('justification', 'N/A')}\n"
            synthesis_context += f"Weighted Score: {paper.get('weighted_score', 0):.2f}\n\n"

        summary_result = self._summarize_hot_topics(synthesis_context)

        final_result = {
            "summary": summary_result.get("summary", "Could not generate summary."),
            "hot_topics": summary_result.get("hot_topics", []),
            "analyzed_papers": [p["title"] for p in top_papers],
        }

        print("✅ Workflow 2 completed successfully.")
        return final_result
