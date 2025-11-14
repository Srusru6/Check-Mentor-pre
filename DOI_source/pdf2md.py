"""
兼容层：原位置的 pdf2md.py。
实际实现已迁移至 tools/pdf2md/pdf2md.py。
此文件保留为薄包装以避免破坏旧入口。
"""
from pathlib import Path
import sys

_NEW_PATH = Path(__file__).resolve().parents[1] / 'tools' / 'pdf2md'
if str(_NEW_PATH) not in sys.path:
    sys.path.insert(0, str(_NEW_PATH))

from pdf2md import main as _main  # type: ignore


if __name__ == '__main__':
    _main()
