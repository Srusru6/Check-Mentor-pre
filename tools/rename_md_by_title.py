#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据 _metadata.json 中的 title 字段重命名同名的 .md 文件。

用法：
    python tools/rename_md_by_title.py [--data-root ./data] [--dry-run]
"""
import argparse
import json
import re
import sys
from pathlib import Path

def sanitize_filename(name: str, max_length: int = 200) -> str:
    # Replace invalid characters with underscore
    # Windows invalid: < > : " / \ | ? *
    name = re.sub(r'[<>:"/\\|?*\n\t]', '_', name)
    name = name.strip()
    if len(name) > max_length:
        name = name[:max_length].strip()
    return name

def rename_md_files(data_root: Path, dry_run: bool):
    json_files = list(data_root.rglob("*_metadata.json"))
    print(f"Found {len(json_files)} metadata files in {data_root}.")
    
    count = 0
    for json_path in json_files:
        # json_path: .../foo_metadata.json
        # md_path: .../foo.md
        
        stem = json_path.stem
        if stem.endswith("_metadata"):
            base_name = stem[:-9] # remove _metadata
        else:
            continue
            
        md_path = json_path.with_name(base_name + ".md")
        
        if not md_path.exists():
            # MD file might be missing or already renamed
            continue
            
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                title = data.get('title', '').strip()
        except Exception as e:
            print(f"Error reading {json_path}: {e}")
            continue
            
        if not title:
            print(f"No title in {json_path}")
            continue
            
        safe_title = sanitize_filename(title)
        if not safe_title:
            print(f"Empty title after sanitization for {json_path}")
            continue
            
        new_md_path = json_path.with_name(safe_title + ".md")
        
        if new_md_path == md_path:
            continue
            
        if new_md_path.exists():
            print(f"Target file already exists: {new_md_path.name}. Skipping {md_path.name}")
            continue
            
        print(f"Renaming '{md_path.name}' -> '{new_md_path.name}'")
        if not dry_run:
            try:
                md_path.rename(new_md_path)
                count += 1
            except OSError as e:
                print(f"Error renaming {md_path}: {e}")
                
    print(f"Renamed {count} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename .md files based on title in _metadata.json")
    parser.add_argument("--data-root", default="./data", help="Root directory to scan")
    parser.add_argument("--dry-run", action="store_true", help="Dry run")
    args = parser.parse_args()
    
    root = Path(args.data_root).resolve()
    if not root.exists():
        print(f"Path not found: {root}")
        sys.exit(1)
        
    rename_md_files(root, args.dry_run)
