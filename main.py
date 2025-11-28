import argparse
import sys
import subprocess
from pathlib import Path



def _run_py(script: Path, argv: list[str]) -> int:
    cmd = [sys.executable, str(script), *argv]
    print(f"Running: {cmd}")
    return subprocess.call(cmd)


def cmd_analyze(ns: argparse.Namespace) -> int:
    # 延迟导入，避免未安装依赖时 -h 失败
    from core.workflow_orchestrator import WorkflowOrchestrator
    target = ns.target
    data_root = ns.data_root
    # 若未指定 data_root，默认使用 data/<target>
    if not data_root:
        repo = Path(__file__).resolve().parent
        data_root = str(repo / 'data' / target)

    orchestrator = WorkflowOrchestrator(
        professor_name=target,
        test_mode=ns.test_mode,
        data_root=data_root,
    )
    orchestrator.run()
    return 0


def cmd_download(ns: argparse.Namespace) -> int:
    repo = Path(__file__).resolve().parent
    script = repo / 'DOI_source' / 'download.py'
    # 透传参数（保持与 download.py 对齐的常见选项子集）
    argv = []
    if ns.prod:
        argv.append('--prod')
    if ns.doi:
        argv += ['--doi', ns.doi]
    if ns.teacher:
        argv += ['--teacher', ns.teacher]
    if ns.depth is not None:
        argv += ['--depth', str(ns.depth)]
    if ns.workers is not None:
        argv += ['--workers', str(ns.workers)]
    if ns.from_results:
        # 如果未提供路径，则传 AUTO 由脚本自行决定
        if ns.from_results == 'AUTO':
            argv += ['--from-results']
        else:
            argv += ['--from-results', ns.from_results]
    if ns.pdf_root:
        argv += ['--pdf-root', ns.pdf_root]
    if ns.max_pages is not None:
        argv += ['--max-pages', str(ns.max_pages)]
    if ns.no_cited:
        argv.append('--no-cited')
    return _run_py(script, argv)


def cmd_pdf2md(ns: argparse.Namespace) -> int:
    repo = Path(__file__).resolve().parent
    # 新位置：tools/pdf2md/pdf2md.py（若不存在则回退到旧位置 DOI_source/pdf2md.py）
    candidate_new = repo / 'tools' / 'pdf2md' / 'pdf2md.py'
    script = candidate_new if candidate_new.exists() else (repo / 'DOI_source' / 'pdf2md.py')
    argv = ['--teacher', ns.teacher]
    if ns.pdf_root:
        argv += ['--pdf-root', ns.pdf_root]
    if ns.md_root:
        argv += ['--md-root', ns.md_root]
    if ns.token:
        argv += ['--token', ns.token]
    if ns.subdirs:
        argv += ['--subdirs', ns.subdirs]
    if ns.limit is not None:
        argv += ['--limit', str(ns.limit)]
    return _run_py(script, argv)


def cmd_merge_history(ns: argparse.Namespace) -> int:
    repo = Path(__file__).resolve().parent
    # 修正路径：文件实际位于 DOI_source/merge_history_to_md.py
    script = repo / 'DOI_source' / 'merge_history_to_md.py'
    argv = ['--teacher', ns.teacher]
    if ns.subdir:
        argv += ['--subdir', ns.subdir]
    return _run_py(script, argv)


def cmd_run_all(ns: argparse.Namespace) -> int:
    # 仅整合：pdf2md -> merge_history(main/ref1/cited) -> analyze
    repo = Path(__file__).resolve().parent
    teacher = ns.target
    pdf_root = ns.pdf_root or str(repo / 'Downloads_pdf')
    md_root = ns.md_root or str(repo / 'data')

    # 1) 转换 PDF -> MD（限定 main/ref1/cited）
    print("[1/3] Converting PDFs to Markdown...")
    ret = cmd_pdf2md(argparse.Namespace(
        teacher=teacher,
        pdf_root=pdf_root,
        md_root=md_root,
        token=ns.token,
    subdirs='main,ref1,cited',
        limit=ns.limit,
    ))
    if ret != 0:
        return ret

    # 2) 合并 history.json（供前端/后续查看）
    print("[2/3] Merging histories into data...")
    for sd in ['main', 'ref1', 'cited']:
        r = cmd_merge_history(argparse.Namespace(teacher=teacher, subdir=sd))
        if r != 0:
            return r

    # 3) 分析（直接使用 data/<teacher> 作为数据根）
    print("[3/3] Running analysis...")
    return cmd_analyze(argparse.Namespace(target=teacher, test_mode=ns.test_mode, data_root=str(Path(md_root) / teacher)))


def cmd_meta_pack(ns: argparse.Namespace) -> int:
    repo = Path(__file__).resolve().parent
    script = repo / 'inspirehep_source' / 'meta-process' / 'run_meta_pack.py'
    argv = []
    if ns.mid_file:
        argv += ['--mid-file', ns.mid_file]
    if ns.teacher:
        argv += ['--teacher', ns.teacher]
    if ns.dois:
        argv += ['--dois', ns.dois]
    if ns.data_root:
        argv += ['-o', ns.data_root]
    if ns.pdf_root:
        argv += ['--pdf-root', ns.pdf_root]
    if ns.k is not None:
        argv += ['--k', str(ns.k)]
    if ns.no_related_downloads:
        argv.append('--no-related-downloads')
    if ns.verbose:
        argv.append('--verbose')
    if ns.token:
        argv += ['--token', ns.token]
    return _run_py(script, argv)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Check-Mentor 统一入口')
    sub = p.add_subparsers(dest='cmd', required=True)

    # analyze
    pa = sub.add_parser('analyze', help='运行分析工作流，生成最终报告')
    pa.add_argument('--target', required=True, help='要分析的目标教授姓名')
    pa.add_argument('--test-mode', action='store_true', help='测试模式，仅处理少量数据')
    pa.add_argument('--data-root', default=None, help='数据根目录（包含 main/ref1/cited 的目录）；默认 data/<target>')
    pa.set_defaults(func=cmd_analyze)

    # download
    pd = sub.add_parser('download', help='从DOI下载PDF（封装 DOI_source/download.py）')
    pd.add_argument('--prod', action='store_true', help='生产模式输出')
    pd.add_argument('--doi', default=None, help='DOI 列表，逗号或空白分隔')
    pd.add_argument('--teacher', default=None, help='教师名称（输出目录名）')
    pd.add_argument('--depth', type=int, default=1, help='递归深度')
    pd.add_argument('--workers', type=int, default=4, help='并发线程数')
    pd.add_argument('--from-results', default='AUTO', help='从 results.txt 读取DOI（可指定路径，默认 AUTO）')
    pd.add_argument('--pdf-root', default=None, help='PDF 输出根目录（默认 ./Downloads_pdf）')
    pd.add_argument('--max-pages', type=int, default=None, help='最大页数阈值，超过则跳过下载')
    pd.add_argument('--no-cited', action='store_true', help='禁用被引文章下载')
    pd.set_defaults(func=cmd_download)

    # pdf2md
    pp = sub.add_parser('pdf2md', help='批量将 PDF 转换为 MD（封装 tools/pdf2md/pdf2md.py）')
    pp.add_argument('--teacher', required=True, help='教师名称（输入/输出目录名）')
    pp.add_argument('--pdf-root', default=None, help='PDF 根目录（默认 ./Downloads_pdf）')
    pp.add_argument('--md-root', default=None, help='MD 根目录（默认 ./data）')
    pp.add_argument('--token', default=None, help='MinerU API Token（默认读环境变量 MINERU_TOKEN）')
    pp.add_argument('--subdirs', default=None, help='限定处理子目录，逗号分隔，如 main,ref1,cited')
    pp.add_argument('--limit', type=int, default=None, help='最多处理的文件数')
    pp.set_defaults(func=cmd_pdf2md)

    # merge-history
    pm = sub.add_parser('merge-history', help='合并 Downloads_pdf 与 data 下的 history.json')
    pm.add_argument('--teacher', required=True, help='教师名称（文件夹）')
    pm.add_argument('--subdir', default='main', help='子目录（main|ref1|cited|...）')
    pm.set_defaults(func=cmd_merge_history)

    # run-all
    pr = sub.add_parser('run-all', help='一条龙：pdf2md -> merge-history -> analyze')
    pr.add_argument('--target', required=True, help='教师名称（目标教授）')
    pr.add_argument('--test-mode', action='store_true', help='测试模式，仅处理少量数据')
    pr.add_argument('--pdf-root', default=None, help='PDF 根目录（默认 ./Downloads_pdf）')
    pr.add_argument('--md-root', default=None, help='MD 根目录（默认 ./data）')
    pr.add_argument('--token', default=None, help='MinerU API Token（默认读环境变量 MINERU_TOKEN）')
    pr.add_argument('--limit', type=int, default=None, help='最多处理的文件数')
    pr.set_defaults(func=cmd_run_all)

    # meta-pack
    pm = sub.add_parser('meta-pack', help='基于 InspireHEP 生成数据布局（data/<teacher>/main|ref1|cited）')
    pm.add_argument('--mid-file', default=None, help='mid 文件路径（JSON 或文本块）')
    pm.add_argument('--teacher', default=None, help='仅处理该老师（可选）')
    pm.add_argument('--dois', default=None, help='逗号分隔的 DOI 列表（与 --teacher 一起使用）')
    pm.add_argument('-o', '--data-root', default=None, help='data 根目录（默认 ./data）')
    pm.add_argument('--pdf-root', default=None, help='PDF 根目录（默认 ./Downloads_pdf）')
    pm.add_argument('--k', type=int, default=None, help='每个列表最多处理前 K 篇（可选）')
    pm.add_argument('--no-related-downloads', action='store_true', help='仅索引相关文献，不下载其 PDF/元数据')
    pm.add_argument('--verbose', action='store_true', help='详细输出')
    pm.add_argument('--token', default=None, help='MinerU API Token')
    pm.set_defaults(func=cmd_meta_pack)

    # download-inspire
    pdi = sub.add_parser('download-inspire', help='从 InspireHEP 下载论文（meta-pack 的别名）')
    pdi.add_argument('--mid-file', default=None, help='mid 文件路径（JSON 或文本块）')
    pdi.add_argument('--teacher', default=None, help='仅处理该老师（可选）')
    pdi.add_argument('--dois', default=None, help='逗号分隔的 DOI 列表（与 --teacher 一起使用）')
    pdi.add_argument('-o', '--data-root', default=None, help='data 根目录（默认 ./data）')
    pdi.add_argument('--pdf-root', default=None, help='PDF 根目录（默认 ./Downloads_pdf）')
    pdi.add_argument('--k', type=int, default=None, help='每个列表最多处理前 K 篇（可选）')
    pdi.add_argument('--no-related-downloads', action='store_true', help='仅索引相关文献，不下载其 PDF/元数据')
    pdi.add_argument('--verbose', action='store_true', help='详细输出')
    pdi.add_argument('--token', default=None, help='MinerU API Token')
    pdi.set_defaults(func=cmd_meta_pack)

    return p


def main():
    parser = build_parser()
    ns = parser.parse_args()
    return ns.func(ns)

if __name__ == "__main__":
    main()

