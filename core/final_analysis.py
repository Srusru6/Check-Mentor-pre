import json
import os
from typing import Dict, List
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from . import config
from . import templates
from .core_questions import CORE_QUESTIONS

class FinalAnalyzer:
    def __init__(self, json_path: str):
        load_dotenv()
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=config.LLM_TEMPERATURE,
            openai_api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE
        )
        self.data = self._load_json(json_path)
        self.json_path = json_path

    def _load_json(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def sort_papers_by_aspect(self, aspect: str) -> List[Dict]:
        papers = []
        for paper_id, analysis in self.data['analysis_results'].items():
            if aspect in analysis and isinstance(analysis[aspect], dict):
                papers.append({
                    'paper_id': paper_id,
                    'score': analysis[aspect].get('score', 0),
                    'analysis': analysis[aspect]
                })
        return sorted(papers, key=lambda x: x['score'], reverse=True)

    def generate_aspect_report(self, aspect: str, top_k: int = 3) -> str:
        sorted_papers = self.sort_papers_by_aspect(aspect)
        top_papers = sorted_papers[:top_k]

        if not top_papers:
            return "没有找到与此问题相关的足够信息。"

        paper_analysis = ""
        for paper in top_papers:
            paper_info = next((p for p in self.data['papers'] if p['id'] == paper['paper_id']), None)
            if paper_info:
                paper_analysis += f"论文《{paper_info.get('title', '未知标题')}》:\n"
                paper_analysis += f"相关性评分：{paper.get('score', 0):.2f}\n"
                paper_analysis += f"核心证据：{paper['analysis'].get('evidence', '无')}\n"
                paper_analysis += f"推理过程：{paper['analysis'].get('reasoning', '无')}\n\n"

        prompt = ChatPromptTemplate.from_template(templates.REPORT_TEMPLATE)
        
        question_text = CORE_QUESTIONS.get(aspect, {}).get("question_zh", aspect)

        messages = prompt.format_messages(
            num_papers=len(top_papers),
            aspect=question_text,
            paper_analysis=paper_analysis
        )

        response = self.llm.invoke(messages)
        report_content = response.content
        
        # 将生成的报告存入缓存
        if 'report_cache' not in self.data:
            self.data['report_cache'] = {}
        self.data['report_cache'][aspect] = report_content
        
        return report_content

    def generate_final_report(self) -> str:
        aspect_reports = ""
        # 确保 'report_cache' 存在
        if 'report_cache' not in self.data:
            self.data['report_cache'] = {}

        for aspect, question_info in CORE_QUESTIONS.items():
            question_zh = question_info["question_zh"]
            # 如果缓存中没有，则生成报告
            if aspect not in self.data['report_cache']:
                print(f"缓存未命中，正在为 '{question_zh}' 生成报告...")
                self.generate_aspect_report(aspect)
            
            aspect_reports += f"【{question_zh}】\n"
            aspect_reports += self.data['report_cache'][aspect] + "\n\n"

        # 准备最终报告的 prompt
        professor_name = self.data.get("professor_info", {}).get("name", "这位学者")
        num_papers = self.data.get("metadata", {}).get("total_papers", "多篇")

        prompt = ChatPromptTemplate.from_template(templates.FINAL_SYNTHESIS_TEMPLATE)
        messages = prompt.format_messages(
            professor_name=professor_name,
            num_papers=num_papers,
            aspect_reports=aspect_reports
        )
        
        print("正在生成最终综合报告...")
        response = self.llm.invoke(messages)
        final_report_content = response.content

        # 将最终报告也存入缓存
        self.data['report_cache']['final_summary'] = final_report_content
        return final_report_content

    def save_results(self, output_path: str = None):
        # 如果未提供 output_path，则使用初始化时的路径
        path_to_save = output_path or self.json_path
        with open(path_to_save, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print(f"结果已保存至: {path_to_save}")

def main():
    # 这是一个示例用法，实际执行在主 main.py 中
    # 请确保 'output/测试教授_research_data.json' 文件存在
    json_file_path = os.path.join(config.OUTPUT_DIR, '测试教授_research_data.json')
    if not os.path.exists(json_file_path):
        print(f"错误: 输入文件不存在 -> {json_file_path}")
        print("请先运行 main.py 的任务一和任务二部分来生成此文件。")
        return

    analyzer = FinalAnalyzer(json_file_path)
    final_report = analyzer.generate_final_report()
    print("\n" + "="*30 + " 最终研究报告 " + "="*30)
    print(final_report)
    print("="*75)
    analyzer.save_results()

if __name__ == "__main__":
    main()
