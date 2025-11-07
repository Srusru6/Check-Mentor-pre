import os
import json
import argparse
from typing import Dict, Any

PDF_ROOT = os.path.join(os.getcwd(), 'Downloads_pdf')
MD_ROOT = os.path.join(os.getcwd(), 'data')


def load_history(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {"items": []}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and isinstance(data.get('items'), list):
                return data
    except Exception:
        pass
    return {"items": []}


essential_keys = {"title", "doi", "authors", "published", "young_authors"}

def normalize_item(it: Dict[str, Any]) -> Dict[str, Any]:
    # Ensure required keys exist
    out = {
        "title": it.get("title") or "",
        "doi": it.get("doi") or "",
        "authors": it.get("authors") or [],
        "published": it.get("published") or {},
        "young_authors": it.get("young_authors") or [],
    }
    # Keep any extra fields
    for k, v in it.items():
        if k not in essential_keys:
            out[k] = v
    return out


def merge_histories(pdf_hist: Dict[str, Any], md_hist: Dict[str, Any]) -> Dict[str, Any]:
    merged: Dict[str, Dict[str, Any]] = {}
    for src in (md_hist, pdf_hist):
        for it in src.get('items', []) or []:
            it = normalize_item(it)
            doi = (it.get('doi') or '').strip()
            if not doi:
                continue
            # Prefer PDF side (comes later) on conflict; md is loaded first
            merged[doi] = it
    # Sort: by published year (desc), month (desc), title
    def sort_key(it: Dict[str, Any]):
        pub = it.get('published') or {}
        y = pub.get('year') or 0
        m = pub.get('month') or 0
        try:
            y = int(y)
        except Exception:
            y = 0
        try:
            m = int(m)
        except Exception:
            m = 0
        return (-y, -m, it.get('title') or '')
    items = sorted(merged.values(), key=sort_key)
    return {"items": items}


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def main():
    ap = argparse.ArgumentParser(description='Merge Downloads_pdf history.json into data history.json')
    ap.add_argument('--teacher', required=True, help='Teacher name (folder)')
    ap.add_argument('--subdir', default='main', help='Subdirectory: main|ref1|cited|...')
    args = ap.parse_args()

    teacher = args.teacher
    subdir = args.subdir

    pdf_hist_path = os.path.join(PDF_ROOT, teacher, subdir, 'history.json')
    md_dir = os.path.join(MD_ROOT, teacher, subdir)
    md_hist_path = os.path.join(md_dir, 'history.json')

    pdf_hist = load_history(pdf_hist_path)
    md_hist = load_history(md_hist_path)

    if not pdf_hist.get('items') and not md_hist.get('items'):
        print(f'No history found for {teacher}/{subdir}. Nothing to merge.')
        return

    merged = merge_histories(pdf_hist, md_hist)
    ensure_dir(md_dir)
    tmp = md_hist_path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    os.replace(tmp, md_hist_path)
    print(f'Merged {len(pdf_hist.get("items", []))} (pdf) + {len(md_hist.get("items", []))} (md) -> {len(merged.get("items", []))} items at {md_hist_path}')


if __name__ == '__main__':
    main()
