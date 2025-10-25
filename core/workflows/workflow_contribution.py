"""
Workflow 1: 分析教授的核心贡献

该工作流的目标是回答第一个核心问题：
"老师对哪些方向感兴趣，他对此有哪些贡献？"

它通过以下步骤实现：
1. 接收教授的代表作列表（main_papers）作为输入。
2. 对每一篇代表作进行内容总结，提取其核心研究方向和贡献。
3. 将所有论文的分析结果进行综合，形成一个关于教授整体研究方向和贡献的结构化报告。
"""
import json
from typing import List, Dict, Any

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from .. import config

class ContributionWorkflow:
    """
    分析教授核心贡献的工作流。
    """
    def __init__(self):
        """
        初始化工作流，包括初始化 LLM 客户端。
        """
        print("  -> ContributionWorkflow initialized.")
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

    def _analyze_single_paper(self, paper_content: str) -> Dict[str, Any]:
        """
        使用 LLM 分析单篇论文的内容，提取研究领域和核心贡献。
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert academic analyst. Your task is to extract the key information from a research paper.
Provide a JSON response with the following structure:
{{
  "research_area": "<The primary research area or sub-field of this paper, e.g., 'Quantum Computing', 'Photonic Integrated Circuits'>",
  "core_contribution": "<A concise, one-sentence summary of the paper's main contribution.>"
}}"""),
            ("user", "Please analyze the following paper content and provide the structured JSON output:\n\n---\n{paper_content}\n---")
        ])
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        # 为了避免 API 调用，暂时注释掉并返回占位符
        # analysis_result = chain.invoke({"paper_content": paper_content[:12000]})
        analysis_result = {
            "research_area": "占位符研究领域",
            "core_contribution": "占位符核心贡献：提出了一种新的方法/模型/理论。"
        }
        
        return analysis_result

    def _synthesize_results(self, all_analyses: List[Dict[str, Any]]) -> str:
        """
        综合所有单篇论文的分析结果，生成一份整体总结。
        """
        prompt = ChatPromptTemplate.from_template("""You are a senior research analyst. Based on the analyses of a professor's key papers, synthesize a comprehensive summary of their research interests and main contributions.

The analyses of individual papers are provided below in JSON format:
{analyses_json}

Your summary should:
1. Identify and list the main research areas (2-4 distinct areas).
2. Provide a coherent narrative summarizing the professor's overall contributions and impact.
3. Be about 150-200 words.

Synthesized Summary:""")

        chain = prompt | self.llm

        analyses_json_str = json.dumps(all_analyses, indent=2, ensure_ascii=False)

        # 为了避免 API 调用，暂时注释掉并返回占位符
        # synthesis_result = chain.invoke({"analyses_json": analyses_json_str})
        # return synthesis_result.content
        return "此部分为综合总结占位符。基于对多篇代表作的分析，该教授的核心研究领域似乎集中在 [占位符领域1] 和 [占位符领域2]。他/她的主要贡献在于 [占位符贡献总结]。"


    def run(self, main_papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        执行分析教授核心贡献的完整流程。
        """
        print(f"  -> Running ContributionWorkflow on {len(main_papers)} main papers.")

        if not main_papers:
            print("  -> No main papers provided. Skipping workflow.")
            return {
                "summary": "没有提供教授的代表作，无法分析其核心贡献。",
                "research_areas": [],
                "key_contributions": []
            }

        # 步骤1: 对每篇论文进行单独分析
        all_single_analyses = []
        for paper in main_papers:
            print(f"    -> Analyzing paper: {paper['title']}")
            content = self._load_paper_content(paper['md_filename'])
            if not content:
                continue
            
            single_analysis = self._analyze_single_paper(content)
            single_analysis['paper_id'] = paper['id']
            single_analysis['title'] = paper['title']
            all_single_analyses.append(single_analysis)

        # 步骤2: 综合所有分析结果
        print("    -> Synthesizing all results...")
        final_summary = self._synthesize_results(all_single_analyses)

        # 步骤3: 格式化最终输出
        final_result = {
            "summary": final_summary,
            "research_areas": list(set(analysis.get("research_area", "N/A") for analysis in all_single_analyses)),
            "key_contributions": [
                {
                    "paper_id": analysis['paper_id'],
                    "title": analysis['title'],
                    "contribution": analysis['core_contribution']
                }
                for analysis in all_single_analyses
            ]
        }

        return final_result
