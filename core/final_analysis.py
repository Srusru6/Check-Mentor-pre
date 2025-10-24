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
            model_name=MODEL_NAME,
            temperature=TEMPERATURE
        )
        self.data = self._load_json(json_path)
        
    def _load_json(self, path: str) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
            
    def sort_papers_by_aspect(self, aspect: str) -> List[Dict]:
        papers = []
        for paper_id, analysis in self.data['analysis_results'].items():
            if aspect in analysis:
                papers.append({
                    'paper_id': paper_id,
                    'score': analysis[aspect]['score'],
                    'analysis': analysis[aspect]
                })
        return sorted(papers, key=lambda x: x['score'], reverse=True)
        
    def generate_aspect_report(self, aspect: str) -> str:
        sorted_papers = self.sort_papers_by_aspect(aspect)
        top_papers = sorted_papers[:TOP_K_PAPERS]
        
        paper_analysis = ""
        for paper in top_papers:
            paper_info = next(p for p in self.data['papers'] if p['id'] == paper['paper_id'])
            paper_analysis += f"论文《{paper_info['title']}》:\n"
            paper_analysis += f"评分：{paper['score']}\n"
            paper_analysis += f"证据：{paper['analysis']['evidence']}\n"
            paper_analysis += f"推理：{paper['analysis']['reasoning']}\n\n"
            
        prompt = ChatPromptTemplate.from_template(REPORT_TEMPLATE)
        messages = prompt.format_messages(
            num_papers=len(top_papers),
            aspect=QUESTIONS[aspect],
            paper_analysis=paper_analysis
        )
        
        response = self.llm.invoke(messages)
        self.data['report_cache'][aspect] = response.content
        return response.content
        
    def generate_final_report(self) -> str:
        aspect_reports = ""
        for aspect, question in QUESTIONS.items():
            if aspect not in self.data['report_cache']:
                self.generate_aspect_report(aspect)
            aspect_reports += f"【{question}】\n"
            aspect_reports += self.data['report_cache'][aspect] + "\n\n"
            
        prompt = ChatPromptTemplate.from_template(FINAL_SYNTHESIS_TEMPLATE)
        messages = prompt.format_messages(aspect_reports=aspect_reports)
        response = self.llm.invoke(messages)
        return response.content
        
    def save_results(self, output_path: str):
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

def main():
    analyzer = FinalAnalyzer("path/to/input.json")
    final_report = analyzer.generate_final_report()
    print(final_report)
    analyzer.save_results("path/to/output.json")

if __name__ == "__main__":
    main()
