import json
from typing import Dict, Any, List
from . import config

class FinalAnalyzer:
    """
    负责将所有工作流的分析结果整合成一份最终的、连贯的报告。
    """
    def __init__(self, professor_name: str):
        """
        初始化最终分析器。

        Args:
            professor_name (str): 教授姓名。
        """
        self.professor_name = professor_name

    def generate_final_report(self, results: Dict[str, Any]) -> str:
        """
        生成最终的 Markdown 格式报告。

        Args:
            results (Dict[str, Any]): 来自 WorkflowOrchestrator 的完整结果。
        
        Returns:
            str: 格式化后的完整报告。
        """
        print("  -> Generating final report...")
        
        # 从传入的 results 中提取各个部分
        contribution_analysis = results.get('contribution_analysis', {})
        field_problems_analysis = results.get('field_problems_analysis', {})
        undergrad_projects_analysis = results.get('undergrad_projects_analysis', {})

        # 准备报告的各个部分
        report_title = f"# 对「{self.professor_name}」教授的学术研究分析报告\n\n"
        
        # 1. 核心贡献总结
        contribution_summary = "## 一、核心研究贡献\n\n"
        contribution_summary += contribution_analysis.get('summary', '未能生成核心贡献总结。')
        contribution_summary += "\n\n"

        # 2. 领域热点问题
        hot_topics_summary = "## 二、领域前沿与热点问题\n\n"
        hot_topics_summary += field_problems_analysis.get('summary', '未能生成领域热点问题总结。')
        hot_topics_summary += "\n\n"
        hot_topics = field_problems_analysis.get('hot_topics', [])
        if hot_topics:
            hot_topics_summary += "### 主要热点问题:\n"
            for i, topic in enumerate(hot_topics, 1):
                hot_topics_summary += f"**{i}. {topic.get('topic_name', 'N/A')}**\n"
                hot_topics_summary += f"   - **核心挑战**: {topic.get('challenge', 'N/A')}\n"
                hot_topics_summary += f"   - **相关论文**: {', '.join(topic.get('related_papers', []))}\n\n"

        # 3. 本科生可参与项目
        undergrad_projects_summary = "## 三、本科生可参与的研究项目建议\n\n"
        undergrad_projects_summary += undergrad_projects_analysis.get('summary', '未能生成本科生项目建议。')
        undergrad_projects_summary += "\n\n"
        project_ideas = undergrad_projects_analysis.get('project_ideas', [])
        if project_ideas:
            undergrad_projects_summary += "### 具体项目构想:\n"
            for i, idea in enumerate(project_ideas, 1):
                undergrad_projects_summary += f"**{i}. 项目名称: {idea.get('project_title', 'N/A')}**\n"
                undergrad_projects_summary += f"   - **研究目标**: {idea.get('research_goal', 'N/A')}\n"
                undergrad_projects_summary += f"   - **核心任务**: {idea.get('core_tasks', 'N/A')}\n"
                undergrad_projects_summary += f"   - **预期成果**: {idea.get('expected_outcomes', 'N/A')}\n"
                undergrad_projects_summary += f"   - **参考论文**: {idea.get('reference_paper_title', 'N/A')}\n\n"

        # 4. 数据来源附录
        appendix = "## 四、分析数据来源\n\n"
        appendix += "### 1. 教授核心贡献分析来源 (代表作)\n"
        analyzed_contrib_papers = contribution_analysis.get('analyzed_papers', [])
        if analyzed_contrib_papers:
            for paper in analyzed_contrib_papers:
                appendix += f"- {paper.get('title', 'N/A')}\n"
        else:
            appendix += "- 无\n"
        appendix += "\n"
        
        appendix += "### 2. 领域热点问题分析来源 (高分论文)\n"
        rated_field_papers = [p for p in field_problems_analysis.get('rated_papers', []) if p.get("problem_representativeness_score", 0) >= 7]
        if rated_field_papers:
            for paper in rated_field_papers:
                appendix += f"- {paper.get('title', 'N/A')} (评分: {paper.get('problem_representativeness_score')})\n"
        else:
            appendix += "- 无\n"
        appendix += "\n"

        appendix += "### 3. 本科生项目建议来源 (复杂度与友好度筛选)\n"
        rated_undergrad_papers = [p for p in undergrad_projects_analysis.get('rated_papers', []) if 4 <= p.get("complexity_score", 0) <= 8 and p.get("friendliness_score", 0) >= 6]
        if rated_undergrad_papers:
            for paper in rated_undergrad_papers:
                appendix += f"- {paper.get('title', 'N/A')} (复杂度: {paper.get('complexity_score')}, 友好度: {paper.get('friendliness_score')})\n"
        else:
            appendix += "- 无\n"
        appendix += "\n"

        final_report = (
            report_title
            + contribution_summary
            + hot_topics_summary
            + undergrad_projects_summary
            + appendix
        )
        
        print("  -> Final report generated successfully.")
        return final_report
