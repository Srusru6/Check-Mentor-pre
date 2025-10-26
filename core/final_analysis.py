import json
from typing import Dict, Any, List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from . import config
from . import templates

class FinalAnalyzer:
    """
    负责将所有工作流的分析结果整合成一份最终的、连贯的报告。
    """
    def __init__(self, professor_name: str, results: Dict[str, Any]):
        """
        初始化最终分析器。

        Args:
            professor_name (str): 教授姓名。
            results (Dict[str, Any]): 来自 WorkflowOrchestrator 的完整结果。
        """
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=config.LLM_TEMPERATURE,
            openai_api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE
        )
        self.professor_name = professor_name
        self.results = results

    def _format_contribution_details(self, contributions: List[Dict[str, Any]]) -> str:
        """格式化贡献详情为 Markdown 列表。"""
        if not contributions:
            return "无详细贡献信息。"
        
        lines = []
        for item in contributions:
            lines.append(f"- **论文《{item.get('title', '未知标题')}》**: {item.get('contribution', '无具体贡献说明')}")
        return "\n".join(lines)

    def _format_hot_topics_details(self, topics: List[str]) -> str:
        """格式化热点问题为 Markdown 列表。"""
        if not topics:
            return "无详细热点问题信息。"
        
        lines = [f"- {topic}" for topic in topics]
        return "\n".join(lines)

    def _format_project_ideas_details(self, ideas: List[Dict[str, Any]]) -> str:
        """格式化项目点子为 Markdown 列表。"""
        if not ideas:
            return "无详细项目建议。"
        
        lines = []
        for item in ideas:
            lines.append(f"- **基于论文《{item.get('title', '未知标题')}》**: {item.get('idea', '无具体点子')}")
        return "\n".join(lines)

    def generate_final_report(self) -> str:
        """
        使用 LLM 将三个独立工作流的总结报告融合成一份最终报告。
        """
        print("  -> Generating final report with rich details...")

        # 提取每个工作流的总结和详情
        contrib_analysis = self.results.get("contribution_analysis", {})
        field_analysis = self.results.get("field_problems_analysis", {})
        undergrad_analysis = self.results.get("undergrad_projects_analysis", {})

        contribution_summary = contrib_analysis.get("summary", "无相关分析。")
        contribution_details = self._format_contribution_details(contrib_analysis.get("key_contributions", []))

        field_problems_summary = field_analysis.get("summary", "无相关分析。")
        field_problems_details = self._format_hot_topics_details(field_analysis.get("hot_topics", []))

        undergrad_projects_summary = undergrad_analysis.get("summary", "无相关分析。")
        undergrad_projects_details = self._format_project_ideas_details(undergrad_analysis.get("project_ideas", []))

        # 使用模板格式化输入
        prompt = ChatPromptTemplate.from_template(templates.FINAL_SYNTHESIS_TEMPLATE)
        
        messages = prompt.format_messages(
            professor_name=self.professor_name,
            contribution_summary=contribution_summary,
            contribution_details=contribution_details,
            field_problems_summary=field_problems_summary,
            field_problems_details=field_problems_details,
            undergrad_projects_summary=undergrad_projects_summary,
            undergrad_projects_details=undergrad_projects_details
        )
        response = self.llm.invoke(messages)
        final_report_content = response.content
        
        print("  -> Final report generated.")
        return final_report_content
