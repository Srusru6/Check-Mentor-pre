"""
工作流编排器 (Workflow Orchestrator)

该模块是新架构的核心，负责：
1. 接收分离后的数据源（main_papers, ref1_papers, ref2_papers）。
2. 初始化并调用三个独立的工作流，分别处理三个核心问题。
3. 收集每个工作流的分析结果。
4. 将整合后的结果返回给主流程，用于最终报告的生成。
"""
import os
import uuid
import json
from pathlib import Path
from typing import List, Dict, Any

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi

from . import config
from .final_analysis import FinalAnalyzer
from .metadata_manager import MetadataManager
from .workflows.workflow_contribution import ContributionWorkflow
from .workflows.workflow_field_problems import FieldProblemsWorkflow
from .workflows.workflow_undergrad_projects import UndergradProjectsWorkflow

class WorkflowOrchestrator:
    """
    负责调度和执行所有分析工作流的中心控制器。
    """
    def __init__(self, professor_name: str, test_mode: bool):
        """
        初始化所有LLM实例、工作流以及配置。
        """
        self._print_section_header("学术开盒demo - 整体流程", level=1)
        print("⚙️  Initializing Workflow Orchestrator...")

        self.professor_name = professor_name
        self.test_mode = test_mode
        
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
            print("  -> INFO: Fallback LLM not configured. The program will run with the main LLM only.")

        # 2. 将LLM实例注入到各个工作流中
        self.contribution_workflow = ContributionWorkflow(main_llm, fallback_llm)
        self.field_problems_workflow = FieldProblemsWorkflow(main_llm, fallback_llm)
        self.undergrad_projects_workflow = UndergradProjectsWorkflow(main_llm, fallback_llm)
        
        # 3. 初始化最终分析器，并注入LLM用于翻译
        self.final_analyzer = FinalAnalyzer(self.professor_name, main_llm)
        
        # 4. 初始化元数据管理器
        self.metadata_manager = MetadataManager()
        
        config.validate_config()
        print("✅ Orchestrator initialized successfully.")

    def _print_section_header(self, title: str, level: int = 1):
        """打印带样式的章节标题"""
        if level == 1:
            print(f"\n{'='*70}\n🎓 {title}\n{'='*70}")
        elif level == 2:
            print(f"\n--- {title} ---")

    def _load_papers_from_dir(self, dir_path: str, author: str, limit: int = 0) -> List[Dict[str, Any]]:
        """从指定目录加载所有论文的元数据。"""
        papers = []
        full_path = Path(dir_path)
        if not full_path.is_dir():
            print(f"    ⚠️ Directory does not exist, skipping: {full_path}")
            return papers

        md_files = sorted(list(full_path.glob("*.md")))
        if limit > 0:
            md_files = md_files[:limit]

        for md_file in md_files:
            paper_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, md_file.stem))
            papers.append({
                "id": paper_id,
                "title": md_file.stem,
                "authors": [author],
                "md_filename": str(md_file),
            })
        return papers
    
    def _load_metadata_for_directory(self, dir_path: Path) -> bool:
        """
        为指定目录加载元数据文件（如果存在）
        
        元数据文件应命名为 'metadata.json' 并位于论文目录中
        
        Args:
            dir_path: 论文目录路径
            
        Returns:
            是否成功加载元数据
        """
        metadata_file = dir_path / "metadata.json"
        if metadata_file.exists():
            print(f"    📋 发现元数据文件: {metadata_file.name}")
            return self.metadata_manager.load_metadata_file(metadata_file)
        else:
            print(f"    ℹ️  未找到元数据文件 (metadata.json)")
            return False

    def run(self):
        """
        执行完整的分析流程，从数据加载到报告生成。
        """
        # 步骤 1: 准备和分离数据源
        self._print_section_header("任务一：准备和分离论文数据源", level=2)
        
        limit = config.TEST_MODE_PAPER_LIMIT if self.test_mode else 0
        base_data_path = Path(f"data/{self.professor_name}")
        
        # 尝试加载各个目录的元数据
        print("\n🔍 检查并加载元数据文件...")
        main_path = base_data_path / "main"
        ref1_path = base_data_path / "ref1"
        ref2_path = base_data_path / "ref2"
        
        print(f"  [Main] {main_path}")
        self._load_metadata_for_directory(main_path)
        
        print(f"  [Ref1] {ref1_path}")
        self._load_metadata_for_directory(ref1_path)
        
        print(f"  [Ref2] {ref2_path}")
        self._load_metadata_for_directory(ref2_path)
        
        # 打印元数据统计
        if len(self.metadata_manager.metadata_cache) > 0:
            self.metadata_manager.print_statistics()
        else:
            print("    ℹ️  未加载任何元数据，将使用默认配置")
        
        # 加载教授代表作 (main) - 始终完整加载
        main_papers = self._load_papers_from_dir(str(main_path), self.professor_name)

        if self.test_mode:
            print(f"  -> 运行在测试模式: 教授代表作将完整加载 ({len(main_papers)}篇) 以保证分析准确性。")
            print(f"  -> 其余数据源 (ref1, ref2) 最多处理 {limit} 篇论文。")
            ref1_papers = self._load_papers_from_dir(str(ref1_path), "Various Authors", limit)
            ref2_papers = self._load_papers_from_dir(str(ref2_path), "Various Authors", limit)
        else:
            ref1_papers = self._load_papers_from_dir(str(ref1_path), "Various Authors")
            ref2_papers = self._load_papers_from_dir(str(ref2_path), "Various Authors")
        
        # 为论文添加元数据信息
        print("\n📝 为论文添加元数据...")
        main_papers = self.metadata_manager.get_papers_with_metadata(main_papers)
        ref1_papers = self.metadata_manager.get_papers_with_metadata(ref1_papers)
        ref2_papers = self.metadata_manager.get_papers_with_metadata(ref2_papers)
        
        # 按发布时间对论文进行排序（更新的论文在前）
        if len(self.metadata_manager.metadata_cache) > 0:
            print("  ✓ 按发布时间对论文进行排序（新→旧）...")
            main_papers = self.metadata_manager.sort_papers_by_recency(main_papers, descending=True)
            ref1_papers = self.metadata_manager.sort_papers_by_recency(ref1_papers, descending=True)
            ref2_papers = self.metadata_manager.sort_papers_by_recency(ref2_papers, descending=True)

        print("  -> 数据源分离完成:")
        print(f"    - 教授代表作 (main): {len(main_papers)} 篇")
        print(f"    - 引用文献 (ref1): {len(ref1_papers)} 篇")
        print(f"    - 潜在项目文献 (ref2): {len(ref2_papers)} 篇")

        # 创建日志目录
        log_dir = "log"
        os.makedirs(log_dir, exist_ok=True)

        def log_workflow_output(workflow_name: str, data: Any):
            """将工作流的输出结果以JSON格式记录到日志文件。"""
            log_path = os.path.join(log_dir, f"{self.professor_name}_{workflow_name}_output.json")
            try:
                with open(log_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                # print(f"    -> Logged {workflow_name} output to {log_path}")
            except Exception as e:
                print(f"    ⚠️ Failed to log {workflow_name} output. Reason: {e}")

        # 步骤 2: 执行各个工作流
        self._print_section_header("任务二：执行分析工作流", level=2)
        all_results = {}

        # --- 工作流1: 分析教授的核心贡献 ---
        print("\n➡️ [Workflow 1/3] 分析教授的核心贡献...")
        contribution_results = self.contribution_workflow.run(self.professor_name, main_papers)
        log_workflow_output("contribution", contribution_results)
        all_results['contribution_analysis'] = contribution_results

        # --- 工作流2: 分析领域的热点问题 ---
        print("\n➡️ [Workflow 2/3] 分析领域的热点问题...")
        field_problems_results = self.field_problems_workflow.run(
            professor_name=self.professor_name,
            main_papers=main_papers,
            ref1_papers=ref1_papers
        )
        log_workflow_output("field_problems", field_problems_results)
        all_results['field_problems_analysis'] = field_problems_results

        # --- 工作流3: 分析本科生可参与的项目 ---
        print("\n➡️ [Workflow 3/3] 分析本科生可参与的项目...")
        # 将工作流1的总结作为输入，传递给工作流3
        contribution_summary = contribution_results.get("contribution_summary", "")
        undergrad_projects_results = self.undergrad_projects_workflow.run(
            self.professor_name, 
            ref2_papers,
            contribution_summary
        )
        log_workflow_output("undergrad_projects", undergrad_projects_results)
        all_results['undergrad_projects_analysis'] = undergrad_projects_results

        print("\n--- 所有工作流执行完毕 ---\n")

        # 步骤 3: 整合结果并生成最终报告
        self._print_section_header("任务三：整合结果并生成最终报告", level=2)
        english_report = self.final_analyzer.generate_final_report(all_results)

        # 步骤 4: 将报告翻译为中文
        self._print_section_header("任务四：翻译报告为中文", level=2)
        chinese_report = self.final_analyzer.translate_report(english_report, "Chinese")

        # 步骤 5: 保存最终报告
        report_filename = config.OUTPUT_DIR / f"{self.professor_name}_final_report.md"
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(chinese_report)
        print(f"\n✅ 最终报告已保存至: {report_filename}")

        self._print_section_header("学术开盒完成", level=1)
