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

# 在后续步骤中，我们将从这里导入具体的工作流实现
from .workflows.workflow_contribution import ContributionWorkflow
from .workflows.workflow_field_problems import FieldProblemsWorkflow
from .workflows.workflow_undergrad_projects import UndergradProjectsWorkflow

class WorkflowOrchestrator:
    """
    负责调度和执行所有分析工作流的中心控制器。
    """
    def __init__(self):
        """
        初始化所有需要的工作流。
        """
        print("⚙️ Workflow Orchestrator initialized.")
        self.contribution_workflow = ContributionWorkflow()
        self.field_problems_workflow = FieldProblemsWorkflow()
        self.undergrad_projects_workflow = UndergradProjectsWorkflow()

    def run(
        self,
        main_papers: List[Dict[str, Any]],
        ref1_papers: List[Dict[str, Any]],
        ref2_papers: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        执行完整的分析流程。

        Args:
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
        contribution_results = self.contribution_workflow.run(main_papers)
        # print(json.dumps(contribution_results, indent=2, ensure_ascii=False))
        all_results['contribution_analysis'] = contribution_results


        # --- 工作流2: 分析领域的热点问题 ---
        print("\n➡️ [Workflow 2/3] 分析领域的热点问题...")
        field_problems_results = self.field_problems_workflow.run(main_papers, ref1_papers)
        # print(json.dumps(field_problems_results, indent=2, ensure_ascii=False))
        all_results['field_problems_analysis'] = field_problems_results


        # --- 工作流3: 分析本科生可参与的项目 ---
        print("\n➡️ [Workflow 3/3] 分析本科生可参与的项目...")
        undergrad_projects_results = self.undergrad_projects_workflow.run(ref1_papers, ref2_papers)
        # print(json.dumps(undergrad_projects_results, indent=2, ensure_ascii=False))
        all_results['undergrad_projects_analysis'] = undergrad_projects_results


        print("\n--- 所有工作流执行完毕 ---\n")
        
        return all_results
