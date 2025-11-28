#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
解压 data 目录中的 ZIP，仅保留指定后缀的文件（默认 PDF）。

功能特性：
- 递归遍历 data/<教师>/... 目录，查找 *.zip
- 仅解压 ZIP 内指定后缀（大小写不敏感），其它类型不解压
- 默认将文件解压到 ZIP 同级目录（扁平化），自动处理重名冲突
- 可选在成功后删除 ZIP 文件
- 支持 dry-run 查看将要进行的操作

用法：
    python tools/unzip_keep_pdf.py \
        --data-root ./data \
        [--only-ext pdf] [--only-ext md] \
        [--remove-zip] [--prefix-with-zip-stem] [--dry-run]

参数说明：
- --data-root：扫描的根目录（默认 ./data）
- --only-ext：要保留的文件后缀（不含点），可多次指定；默认 pdf。例如：--only-ext md
- --remove-zip：完成解压并提取后，删除原 ZIP 文件
- --prefix-with-zip-stem：发生重名冲突时，优先用 ZIP 文件名作为前缀，降低冲突概率
- --dry-run：只打印计划操作，不实际写文件
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
import zipfile
import shutil
import os


def is_allowed_member(name: str, exts: list[str]) -> bool:
    nl = name.lower()
    for e in exts:
        e = e.lower().lstrip(".")
        if nl.endswith("." + e):
            return True
    return False


def safe_write_bytes(dest: Path, data: bytes) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)
    return dest


def unique_path(base: Path) -> Path:
    if not base.exists():
        return base
    stem, suffix = base.stem, base.suffix
    idx = 1
    while True:
        cand = base.with_name(f"{stem} ({idx}){suffix}")
        if not cand.exists():
            return cand
        idx += 1


def extract_selected_from_zip(zip_path: Path, *, exts: list[str], prefix_with_zip: bool, dry_run: bool) -> tuple[int, list[Path]]:
    """从 zip 中提取指定后缀到 zip 同级目录，返回 (提取数量, 文件列表)。"""
    extracted: list[Path] = []
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                if not is_allowed_member(info.filename, exts):
                    continue
                # 输出文件名：默认采用成员的 basename；可选用 zip stem 前缀
                member_name = Path(info.filename).name
                
                if member_name == 'full.md':
                    out_name = f"{zip_path.stem}.md"
                else:
                    out_name = member_name
                    if prefix_with_zip:
                        out_name = f"{zip_path.stem}_{member_name}"

                out_path = zip_path.parent / out_name
                if out_path.exists():
                    out_path = unique_path(out_path)
                if dry_run:
                    extracted.append(out_path)
                    continue
                data = zf.read(info)  # 读取条目（以字节写出，适配二进制/文本）
                safe_write_bytes(out_path, data)
                extracted.append(out_path)
        return len(extracted), extracted
    except zipfile.BadZipFile:
        print(f"✗ 无效 ZIP：{zip_path}")
        return 0, []
    except Exception as e:
        print(f"✗ 解压失败：{zip_path} => {e}")
        return 0, []


def scan_and_extract(data_root: Path, *, exts: list[str], remove_zip: bool, prefix_with_zip: bool, dry_run: bool) -> int:
    zips = list(data_root.rglob("*.zip"))
    if not zips:
        print(f"未在 {data_root} 下找到任何 ZIP 文件。")
        return 0
    total_pdf = 0
    label = "/".join([f".{e.lstrip('.')}" for e in exts])
    print(f"发现 ZIP 文件 {len(zips)} 个，开始处理...\n")
    for zp in zips:
        print(f"→ 处理: {zp}")
        cnt, files = extract_selected_from_zip(zp, exts=exts, prefix_with_zip=prefix_with_zip, dry_run=dry_run)
        print(f"   提取 {label} 数量: {cnt}")
        for f in files[:5]:
            print(f"     - {f}")
        if len(files) > 5:
            print(f"     ... 共 {len(files)} 个")
        total_pdf += cnt
        if remove_zip and cnt > 0 and not dry_run:
            try:
                zp.unlink(missing_ok=True)
                print("   已删除 ZIP")
            except Exception as e:
                print(f"   ✗ 删除 ZIP 失败: {e}")
    print(f"\n完成：共提取 {label} {total_pdf} 个。")
    return total_pdf


def clean_non_md_json(data_root: Path, dry_run: bool) -> None:
    """清理 data_root 下除 .md 和 .json 以外的所有文件"""
    print(f"\n开始清理非 .md/.json 文件 (Dry run: {dry_run})...")
    allowed = {'.md', '.json'}
    count = 0
    # 遍历所有文件
    for p in data_root.rglob('*'):
        if p.is_file():
            if p.suffix.lower() not in allowed:
                if dry_run:
                    print(f"  [Plan Delete] {p}")
                else:
                    try:
                        p.unlink()
                    except Exception as e:
                        print(f"  [Error] 删除失败 {p}: {e}")
                count += 1
    
    action = "预计删除" if dry_run else "已删除"
    print(f"{action} {count} 个非 .md/.json 文件。")


def main() -> int:
    ap = argparse.ArgumentParser(description="解压 data 目录的 ZIP，仅保留指定后缀（默认 md）")
    ap.add_argument("--data-root", default=str(Path(__file__).resolve().parents[1] / "data"), help="待扫描的根目录（默认 ./data）")
    ap.add_argument("--only-ext", action="append", help="要保留的后缀（不含点），可多次指定；默认 md")
    ap.add_argument("--remove-zip", action="store_true", help="成功后删除 ZIP 文件")
    ap.add_argument("--prefix-with-zip-stem", action="store_true", help="重名时使用 ZIP 文件名作为前缀，降低冲突")
    ap.add_argument("--clean-others", action="store_true", help="完成后删除除 .md 和 .json 以外的所有文件")
    ap.add_argument("--dry-run", action="store_true", help="仅打印操作计划，不写文件")
    args = ap.parse_args()

    data_root = Path(args.data_root).resolve()
    if not data_root.exists():
        print(f"目录不存在：{data_root}")
        return 2
    exts = args.only_ext if args.only_ext else ["md"]
    
    ret = scan_and_extract(data_root, exts=exts, remove_zip=args.remove_zip, prefix_with_zip=args.prefix_with_zip_stem, dry_run=args.dry_run)
    
    if args.clean_others:
        clean_non_md_json(data_root, args.dry_run)
        
    return 0 if ret >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
