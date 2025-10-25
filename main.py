import os
import uuid
from pathlib import Path
from typing import List, Dict, Any
import datetime

from core import config as core_config
from core.final_analysis import FinalAnalyzer
from core.workflow_orchestrator import WorkflowOrchestrator


def print_section_header(title: str, level: int = 1):
    """打印带样式的章节标题"""
    if level == 1:
        print(f"\n{'='*70}\n🎓 {title}\n{'='*70}")
    elif level == 2:
        print(f"\n--- {title} ---")


def load_papers_from_dir(dir_path: str, author: str) -> List[Dict[str, Any]]:
    """从指定目录加载所有论文的元数据。"""
    papers = []
    if not os.path.isdir(dir_path):
        print(f"警告：目录不存在，跳过: {dir_path}")
        return papers

    for md_file in Path(dir_path).glob("*.md"):
        paper_id = str(uuid.uuid4())
        papers.append({
            "id": paper_id,
            "title": md_file.stem,
            "authors": [author],
            "publication_date": datetime.date.today().isoformat(),
            "abstract": "...",
            "md_filename": str(md_file),
            "text_chunks": [],
            "analysis_results": {}
        })
    return papers


def main(professor_name: str, test_mode: bool):
    """
    主函数，执行整个分析流程。
    """
    print_section_header("学术开盒demo - 整体流程", level=1)

    # 步骤 1: 准备和分离数据源
    print_section_header("任务一：开始准备和分离论文数据源", level=2)
    
    base_data_path = Path("data/sample") if test_mode else Path(f"data/{professor_name}")
    
    main_papers = load_papers_from_dir(str(base_data_path / "main"), professor_name)
    ref1_papers = load_papers_from_dir(str(base_data_path / "ref1"), "Various Authors")
    ref2_papers = load_papers_from_dir(str(base_data_path / "ref2"), "Various Authors")

    print("✓ 数据源分离完成:")
    print(f"  - 教授代表作 (main): {len(main_papers)} 篇")
    print(f"  - 引用文献 (ref1): {len(ref1_papers)} 篇")
    print(f"  - 潜在项目文献 (ref2): {len(ref2_papers)} 篇")

    # 步骤 2: 初始化工作流编排器
    core_config.validate_config()
    orchestrator = WorkflowOrchestrator()
    
    # 步骤 3: 调用新的工作流编排器
    all_results = orchestrator.run(main_papers, ref1_papers, ref2_papers)
    
    # 步骤 4: 初始化最终分析器并生成报告
    print("\n--- 步骤四：整合结果并生成最终报告 ---\n")
    final_analyzer = FinalAnalyzer(professor_name, all_results)
    final_report = final_analyzer.generate_final_report()

    # 步骤 5: 保存最终报告
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    report_filename = os.path.join(output_dir, f"{professor_name}_final_report.md")
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(final_report)
    print(f"\n✅ 最终报告已保存至: {report_filename}")


    print_section_header("学术开盒完成", level=1)


if __name__ == "__main__":
    # 在实际使用中，可以更改为目标教授的姓名
    # The professor's name can be changed for actual use.
    main(professor_name="测试教授", test_mode=True)
