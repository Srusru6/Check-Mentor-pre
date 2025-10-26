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
import time
from typing import List, Dict, Any

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from .. import config
from .cache_manager import CacheManager

class ContributionWorkflow:
    """
    分析教授核心贡献的工作流。
    """
    def __init__(self, main_llm, fallback_llm=None):
        """
        初始化工作流，接收外部传入的LLM实例。
        """
        print("  -> ContributionWorkflow initialized.")
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
        这是一个通用的调用逻辑，适用于所有单篇论文分析。
        """
        try:
            # 尝试主LLM
            print("      -> Attempting main LLM...")
            result = chain.invoke({"paper_content": paper_content[:12000]})
            return result
        except (OutputParserException, json.JSONDecodeError) as e:
            print(f"      ⚠️ Main LLM output parsing failed: {e}. Retrying with main LLM...")
            # 有时解析失败是暂时的，重试一次
            try:
                result = chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception as final_e:
                print(f"      ⚠️ Main LLM retry failed: {final_e}.")
                # fall through to fallback
        except Exception as e:
            print(f"      ⚠️ Main LLM failed: {e}")

        # 如果主LLM失败，且备用LLM已配置，则尝试备用LLM
        if self.fallback_llm:
            try:
                print("      -> Attempting fallback LLM...")
                fallback_chain = chain.with_components(llm=self.fallback_llm)
                result = fallback_chain.invoke({"paper_content": paper_content[:12000]})
                return result
            except Exception as e:
                print(f"      ⚠️ Fallback LLM also failed: {e}")
        
        # 如果都失败了，则抛出异常
        raise RuntimeError("Both main and fallback LLMs failed to process the paper.")


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

        analysis_result = self._invoke_llm_with_fallback(chain, paper_content)
        time.sleep(1) # Add a delay to avoid rate limiting
        
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

        synthesis_result = chain.invoke({"analyses_json": analyses_json_str})
        return synthesis_result.content


    def run(self, professor_name: str, main_papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        执行分析教授核心贡献的完整流程。
        """
        self.cache = CacheManager(professor_name, "contribution_analysis")
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
            paper_id = paper['id']
            cached_result = self.cache.get(paper_id)

            if cached_result:
                print(f"    -> Found cached analysis for paper: {paper['title']}")
                single_analysis = cached_result
            else:
                print(f"    -> Analyzing paper: {paper['title']}")
                content = self._load_paper_content(paper['md_filename'])
                if not content:
                    continue
                
                single_analysis = self._analyze_single_paper(content)
                self.cache.set(paper_id, single_analysis)

            single_analysis['paper_id'] = paper_id
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
