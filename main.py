import os
import sys
import json
import importlib.util
from datetime import datetime
from pathlib import Path

# --- 动态导入任务一模块 ---
# 这种方法可以避免因中文路径导致的 'from 任务一：总结...' 语法错误
def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None:
        raise ImportError(f"Could not load spec for module '{module_name}' from path '{file_path}'")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# 获取 task1_summarize/main.py 的绝对路径
task1_main_py_path = Path(__file__).parent / '任务一：总结' / 'main.py'
# 动态导入
task1_main = import_from_path('task1_main', str(task1_main_py_path))
# 从导入的模块中获取函数
summarize_paper = task1_main.summarize_paper
load_summary_config = task1_main.load_config

# --- 导入核心模块 ---
from core.rag_processor import PaperRAGProcessor
from core.data_manager import DataManager
from core.final_analysis import FinalAnalyzer
import core.config as core_config


def run_task_1_summarize(input_dir, output_dir, config):
    """
    执行任务一：总结指定目录下的所有论文。
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    summary_length = config.get('summary_length', 200)
    api_key = config.get('api_key')

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("错误：请在 任务一：总结/config.json 文件中设置您的 Gemini API 密钥。")
        return None

    summaries = {}
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_path = os.path.join(input_dir, filename)
            print(f"正在处理: {filename}...")
            try:
                with open(input_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                summary = summarize_paper(api_key, content, summary_length)
                
                # 将摘要存入字典，而不是写入文件
                summaries[filename] = summary
                print(f"已生成摘要: {filename}")

            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")
    return summaries

def main():
    """
    主函数，整合并执行所有任务
    """
    print(f"\n{'='*70}")
    print(f"🎓 学术开盒demo - 整体流程")
    print(f"{'='*70}\n")

    # --- 基本设置 ---
    # 使用绝对路径
    base_dir = Path(__file__).parent.resolve()
    professor_name = "测试教授"
    output_data_file = base_dir / "output" / f"{professor_name}_research_data.json"
    
    # --- 任务一：总结论文 ---
    print("\n--- 任务一：开始总结论文 ---")
    summary_config_path = base_dir / '任务一：总结' / 'config.json'
    summary_config = load_summary_config(str(summary_config_path))
    
    if not summary_config:
        print("无法加载任务一的配置，流程终止。")
        return

    # 使用 data/sample/main 中的论文作为测试数据
    paper_input_dir = base_dir / 'data' / 'sample' / 'main'
    
    # 运行总结任务
    paper_summaries = run_task_1_summarize(
        input_dir=str(paper_input_dir),
        output_dir=str(base_dir / "output" / "summaries"), # 临时输出，主要使用内存中的summaries
        config=summary_config
    )

    if not paper_summaries:
        print("没有生成任何论文摘要，流程终止。")
        return
    print("--- 任务一：论文总结完成 ---\n")


    # --- 任务二：问题评分 ---
    print("\n--- 任务二：开始进行问题评分 ---")
    
    # 1. 初始化数据管理器
    data_manager = DataManager(str(output_data_file))
    
    # 2. 设置教授信息
    data_manager.set_professor_info(
        name=professor_name,
        department="未知",
        university="未知",
        research_areas=[] # 将由报告生成阶段填充
    )

    # 3. 准备论文信息
    papers_info = []
    paper_id_counter = 1
    for md_filename, summary in paper_summaries.items():
        paper_id = f"{paper_id_counter:03d}"
        paper_info = {
            "id": paper_id,
            "title": Path(md_filename).stem,
            "authors": [professor_name],
            "year": datetime.now().year,
            "md_filename": str(Path('data') / 'sample' / 'main' / md_filename),
            "summary": summary # 直接使用任务一的总结
        }
        papers_info.append(paper_info)
        data_manager.add_paper(paper_info)
        paper_id_counter += 1

    # 4. 初始化 RAG 处理器并处理论文
    try:
        core_config.validate_config() # 验证任务二所需的环境变量
        processor = PaperRAGProcessor()
        
        # 注意：process_papers_batch 需要论文的绝对路径
        # 我们需要调整 rag_processor 来接受内容而不是路径，或者确保路径正确
        # 当前，我们将使用相对路径，并假设 rag_processor 在项目根目录运行
        
        results = processor.process_papers_batch(papers_info, str(base_dir), file_type="md")

        # 5. 保存分析结果
        for paper_id, analysis in results["analysis_results"].items():
            data_manager.add_analysis_result(paper_id, analysis)
        
        # 任务一的总结也需要保存到数据管理器中
        for paper in papers_info:
             data_manager.add_paper_summary(paper['id'], paper['summary'])

        data_manager.save()
        print("--- 任务二：问题评分完成 ---\n")

    except ValueError as e:
        print(f"\n❌ 任务二配置错误: {e}")
        print(f"请检查 .env 文件并确保所有必需的 API 密钥都已设置。")
        return
    except Exception as e:
        print(f"\n❌ 任务二执行出错: {e}")
        import traceback
        traceback.print_exc()
        return

    # --- 任务三：生成最终报告 ---
    print("\n--- 任务三：开始生成最终报告 ---")
    try:
        analyzer = FinalAnalyzer(str(output_data_file))
        final_report = analyzer.generate_final_report()
        
        # 打印最终报告
        print("\n" + "="*30 + " 最终研究报告 " + "="*30)
        print(final_report)
        print("="*75)

        # 保存包含报告缓存的最终数据
        analyzer.save_results(str(output_data_file))
        print(f"\n最终报告及所有数据已保存至: {output_data_file}")
        print("--- 任务三：报告生成完成 ---\n")

    except Exception as e:
        print(f"\n❌ 任务三执行出错: {e}")
        import traceback
        traceback.print_exc()
        return

    print(f"\n{'='*70}")
    print(f"✅ 整体流程执行完毕！")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
