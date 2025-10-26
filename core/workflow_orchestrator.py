"""
工作流编排器 (Workflow Orchestrator)

该模块是新架构的核心，负责：
1. 接收分离后的数据源（main_papers, ref1_papers, ref2_papers）。
2. 初始化并调用三个独立的工作流，分别处理三个核心问题。
3. 收集每个工作流的分析结果。
4. 将整合后的结果返回给主流程，用于最终报告的生成。
"""
from typing import List, Dict, Any
import json

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi

from . import config
from .workflows.workflow_contribution import ContributionWorkflow
from .workflows.workflow_field_problems import FieldProblemsWorkflow
from .workflows.workflow_undergrad_projects import UndergradProjectsWorkflow

class WorkflowOrchestrator:
    """
    负责调度和执行所有分析工作流的中心控制器。
    """
    def __init__(self):
        """
        初始化所有LLM实例和需要的工作流。
        """
        print("⚙️ Workflow Orchestrator initialized.")
        
        # 1. 统一初始化LLM实例
        main_llm = ChatOpenAI(
            model=config.LLM_MODEL,
            openai_api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE,
            temperature=config.LLM_TEMPERATURE
        )
        
        fallback_llm = None
        if config.DASHSCOPE_API_KEY:
            try:
                fallback_llm = ChatTongyi(
                    model=config.LLM_FALLBACK_MODEL,
                    dashscope_api_key=config.DASHSCOPE_API_KEY,
                    temperature=config.LLM_TEMPERATURE
                )
                print("  -> Fallback LLM (DashScope) initialized successfully.")
            except Exception as e:
                print(f"  ⚠️ Could not initialize Fallback LLM. Reason: {e}")
                fallback_llm = None
        else:
            print("  -> INFO: Fallback LLM not configured (DASHSCOPE_API_KEY not found). The program will run with the main LLM only.")

        # 2. 将LLM实例注入到各个工作流中
        self.contribution_workflow = ContributionWorkflow(main_llm, fallback_llm)
        self.field_problems_workflow = FieldProblemsWorkflow(main_llm, fallback_llm)
        self.undergrad_projects_workflow = UndergradProjectsWorkflow(main_llm, fallback_llm)

    def run(
        self,
        professor_name: str,
        main_papers: List[Dict[str, Any]],
        ref1_papers: List[Dict[str, Any]],
        ref2_papers: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        执行完整的分析流程。

        Args:
            professor_name: 教授姓名，用于缓存。
            main_papers: 教授的代表作列表。
            ref1_papers: 引用文献列表。
            ref2_papers: 潜在本科生项目相关的文献列表。

        Returns:
            一个包含所有分析结果的字典。
        """
        print("\n--- 开始执行工作流编排 ---\n")
        
        all_results = {}

        # --- 工作流1: 分析教授的核心贡献 ---
        print("\n➡️ [Workflow 1/3] 分析教授的核心贡献...")
        contribution_results = self.contribution_workflow.run(professor_name, main_papers)
        # print(json.dumps(contribution_results, indent=2, ensure_ascii=False))
        all_results['contribution_analysis'] = contribution_results


        # --- 工作流2: 分析领域的热点问题 ---
        print("\n➡️ [Workflow 2/3] 分析领域的热点问题...")
        field_problems_results = self.field_problems_workflow.run(professor_name, main_papers, ref1_papers)
        # print(json.dumps(field_problems_results, indent=2, ensure_ascii=False))
        all_results['field_problems_analysis'] = field_problems_results


        # --- 工作流3: 分析本科生可参与的项目 ---
        print("\n➡️ [Workflow 3/3] 分析本科生可参与的项目...")
        undergrad_projects_results = self.undergrad_projects_workflow.run(professor_name, ref2_papers)
        # print(json.dumps(undergrad_projects_results, indent=2, ensure_ascii=False))
        all_results['undergrad_projects_analysis'] = undergrad_projects_results


        print("\n--- 所有工作流执行完毕 ---\n")
        
        return all_results
