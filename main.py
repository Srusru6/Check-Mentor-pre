import argparse
from core.workflow_orchestrator import WorkflowOrchestrator

def main():
    """
    主函数，解析命令行参数并启动工作流。
    """
    parser = argparse.ArgumentParser(
        description="分析一位教授的学术产出，生成综合报告。"
    )
    parser.add_argument(
        "--target",
        type=str,
        required=True,
        help="要分析的目标教授姓名。"
    )
    parser.add_argument(
        "--test-mode",
        action="store_true",
        help="如果设置此标志，程序将以测试模式运行，只处理少量数据。"
    )
    
    args = parser.parse_args()

    # 初始化并运行工作流编排器
    orchestrator = WorkflowOrchestrator(
        professor_name=args.target,
        test_mode=args.test_mode
    )
    orchestrator.run()

if __name__ == "__main__":
    main()

