"""轻量包装：将 meta-data 下载器打包为一个小 CLI，输出与 DOI_source 相同的数据布局到 `data/`。

用法示例：
  python run_meta_pack.py --mid-file ..\pre-process\mid_batch.json --teacher "曹庆宏" --no-related-downloads

支持：
- --mid-file : JSON 或文本格式（与 batch_from_mid.py 兼容）
- --teacher 和 --dois: 直接传入教师名和逗号分隔 DOI 列表
- --data-root, --k, --no-related-downloads, --verbose 与 batch_from_mid.py 保持一致
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

CUR_DIR = Path(__file__).resolve().parent
PROJ_ROOT = CUR_DIR.parents[2]
SRC_ROOT = PROJ_ROOT / 'inspirehep_source'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

# 导入已有实现
from batch_from_mid import parse_mid_file, download_for_teacher, get_default_k
from doi_downloader import InspireHEPClient


def parse_simple_dois(s: str):
    return [p.strip() for p in s.split(',') if p.strip()]


def main():
    ap = argparse.ArgumentParser(description='Package meta-data downloader -> produce DOI_source-style data layout')
    ap.add_argument('--mid-file', default=None, help='mid 文件路径（JSON 或文本块）')
    ap.add_argument('--teacher', default=None, help='仅处理该老师（可选）')
    ap.add_argument('--dois', default=None, help='逗号分隔的 DOI 列表（与 --teacher 一起使用）')
    ap.add_argument('-o', '--data-root', default=str(PROJ_ROOT / 'data'), help='data 根目录，默认项目根下的 data')
    ap.add_argument('--pdf-root', default=str(PROJ_ROOT / 'Downloads_pdf'), help='PDF 根目录（用于镜像到 DOI_source 风格），默认项目根下的 Downloads_pdf')
    ap.add_argument('--k', type=int, default=None, help='每个列表最多处理前 K 篇（可选，默认读取 config.ini [batch] k_per_list）')
    ap.add_argument('--no-related-downloads', action='store_true', help='仅索引相关文献，不下载其 PDF/元数据')
    ap.add_argument('--verbose', action='store_true', help='详细输出')
    args = ap.parse_args()

    # 读取 plan
    plan = {}
    if args.mid_file:
        mid_path = Path(args.mid_file)
        if not mid_path.exists():
            print(f"mid 文件不存在: {mid_path}")
            return 1
        plan = parse_mid_file(mid_path)
    elif args.teacher and args.dois:
        plan[args.teacher] = {
            'recent': parse_simple_dois(args.dois),
            'cited': []
        }
    else:
        print('需要提供 --mid-file 或 (--teacher 且 --dois)')
        return 2

    data_root = Path(args.data_root)
    pdf_root = Path(args.pdf_root)
    client = InspireHEPClient()
    # 若未提供 --k，读取 config.ini 的默认值
    if args.k is None:
        args.k = get_default_k()

    for teacher, items in plan.items():
        if args.teacher and teacher != args.teacher:
            continue
        recents = items.get('recent', [])
        citeds = items.get('cited', [])
        print(f"\n=== 处理老师: {teacher} | recent={len(recents)} | cited={len(citeds)} ===")
        download_for_teacher(client, teacher, recents, citeds, args.k, data_root, args.no_related_downloads, verbose=args.verbose, pdf_root=pdf_root)

    print('\n✓ 全部处理完成')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
