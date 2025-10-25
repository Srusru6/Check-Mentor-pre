import os
import sys
import json
from datetime import datetime
from pathlib import Path

# --- 核心模块导入 ---
# 移除了对 "任务一：总结" 的动态导入，功能将由 RAG 处理器统一处理
from core.rag_processor import PaperRAGProcessor
from core.data_manager import DataManager
from core.final_analysis import FinalAnalyzer
import core.config as core_config

def main():
    """
    主函数，整合并执行所有任务
    """
    print(f"\n{'='*70}")
    print(f"🎓 学术开盒demo - 整体流程")
    print(f"{'='*70}\n")

    # --- 基本设置 ---
    # True:  使用 data/sample/main 中的一篇论文进行测试
    # False: 使用 data/王剑威 中所有论文进行完整分析
    test_mode = True 
    
    base_dir = Path(__file__).parent.resolve()
    professor_name = "测试教授" if test_mode else "王剑威"
    output_data_file = base_dir / "output" / f"{professor_name}_research_data.json"
    
    # --- 准备论文数据 ---
    paper_input_dirs = []
    if test_mode:
        # 测试模式：使用 data/sample/main 中的论文
        paper_input_dirs.append(base_dir / 'data' / 'sample' / 'main')
    else:
        # 完整模式：使用 data/王剑威 中的论文
        wang_jianwei_dir = base_dir / 'data' / '王剑威'
        paper_input_dirs.extend([
            wang_jianwei_dir / 'main',
            wang_jianwei_dir / 'ref1',
            wang_jianwei_dir / 'ref2'
        ])

    # --- 任务一和任务二：处理论文并进行分析 ---
    # 这两个任务紧密相连，统一由 RAG 处理器完成
    print("\n--- 任务一 & 二：开始处理论文并进行问题评分 ---")
    
    try:
        # 1. 验证核心配置 (API keys等)
        core_config.validate_config()

        # 2. 初始化数据管理器
        data_manager = DataManager(output_data_file.name) # 传递文件名而非完整路径
        
        # 3. 设置教授信息
        data_manager.set_professor_info(
            name=professor_name,
            department="未知",
            university="未知",
            research_areas=[] # 将由报告生成阶段填充
        )

        # 4. 准备论文信息列表
        papers_info = []
        paper_id_counter = 1
        
        for paper_dir in paper_input_dirs:
            if not paper_dir.exists():
                print(f"警告：目录不存在，跳过: {paper_dir}")
                continue
            
            file_list = list(os.listdir(paper_dir))
            
            # 在测试模式下，只取一篇论文
            if test_mode and len(file_list) > 0:
                file_list = file_list[:1]

            for md_filename in file_list:
                if md_filename.endswith(".md"):
                    paper_path = paper_dir / md_filename
                    paper_id = f"{paper_id_counter:03d}"
                    paper_info = {
                        "id": paper_id,
                        "title": paper_path.stem,
                        "authors": [professor_name],
                        "year": datetime.now().year,
                        "md_filename": str(paper_path.resolve()), # 使用绝对路径
                        "summary": "" # 总结将由 RAG 处理器生成
                    }
                    papers_info.append(paper_info)
                    paper_id_counter += 1

        if not papers_info:
            print("错误：在指定目录中未找到 .md 格式的论文文件。")
            return

        # 5. 初始化 RAG 处理器并处理论文
        # PaperRAGProcessor 现在会处理加载、分割、向量化、总结和分析的完整流程
        processor = PaperRAGProcessor()
        
        # process_papers_batch 接收论文信息列表，并返回所有结果
        results = processor.process_papers_batch(papers_info, file_type="md")

        # 6. 保存所有结果到数据管理器
        for paper_info in papers_info:
            paper_id = paper_info['id']
            
            # 添加论文元数据
            data_manager.add_paper(paper_info)

            # 添加总结
            if paper_id in results["summaries"]:
                summary_data = results["summaries"][paper_id]
                # 确保 summary_data 是字典并且包含 'summary' 键
                if isinstance(summary_data, dict) and 'summary' in summary_data:
                    data_manager.add_paper_summary(paper_id, summary_data['summary'])
                else:
                    # 如果不是预期的格式，记录错误或默认值
                    data_manager.add_paper_summary(paper_id, "总结生成失败。")


            # 添加分析结果
            if paper_id in results["analysis_results"]:
                data_manager.add_analysis_result(paper_id, results["analysis_results"][paper_id])
        
        data_manager.save()
        print("--- 任务一 & 二：论文处理和评分完成 ---\n")

    except ValueError as e:
        print(f"\n❌ 任务配置错误: {e}")
        print(f"请检查 .env 文件并确保所有必需的 API 密钥都已设置。")
        return
    except Exception as e:
        print(f"\n❌ 任务执行出错: {e}")
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

        # 将最终报告保存为 Markdown 文件
        report_md_file = base_dir / "output" / f"{professor_name}_final_report.md"
        with open(report_md_file, 'w', encoding='utf-8') as f:
            f.write(final_report)
        print(f"\n最终报告已保存为 Markdown 文件: {report_md_file}")

        # 保存包含报告缓存的最终数据
        analyzer.save_results()
        print(f"\n最终 JSON 数据及缓存已保存至: {output_data_file}")
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
