import argparse
import sys
import json
import concurrent.futures
from pathlib import Path

# Ensure we can import ex.py from the same directory
sys.path.append(str(Path(__file__).parent))
import ex

def main():
    parser = argparse.ArgumentParser(description="Run Meta Pack (InspireHEP Downloader)")
    parser.add_argument('--mid-file', default=None, help='Path to mid file (not used directly in this wrapper, but kept for compatibility)')
    parser.add_argument('--teacher', default=None, help='Teacher name')
    parser.add_argument('--dois', default=None, help='Comma separated DOIs')
    parser.add_argument('-o', '--data-root', default=None, help='Data root directory')
    parser.add_argument('--pdf-root', default=None, help='PDF root directory')
    parser.add_argument('--k', type=int, default=None, help='Top K items (not fully implemented in wrapper yet)')
    parser.add_argument('--no-related-downloads', action='store_true', help='Skip related downloads')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--token', default=None, help='MinerU Token')

    args = parser.parse_args()

    # Construct papers data dict
    papers_data = {}
    if args.teacher and args.dois:
        dois_list = [d.strip() for d in args.dois.split(',') if d.strip()]
        papers_data[args.teacher] = dois_list
    elif args.mid_file:
        # Fallback to parsing mid file if provided (assuming it's papers_data.txt format)
        papers_data = ex.parse_papers_data(Path(args.mid_file))
    else:
        # Default fallback
        papers_data = ex.parse_papers_data(ex.PROJ_ROOT / 'inspirehep_source/pre-process/papers_data.txt')

    config = ex.load_config()
    sample_threshold, sample_size = ex.get_sampling_cfg(config)
    years_window = ex.get_young_author_years(config)
    workers_main, workers_related = ex.get_worker_cfg(config)
    limit_ref, limit_cited = ex.get_limit_cfg(config)
    
    # Override data_root if provided
    data_root = Path(args.data_root) if args.data_root else ex.PROJ_ROOT / 'data'
    
    processed_records = ex.load_progress()
    
    for teacher, dois in papers_data.items():
        print(f"\nProcessing Teacher: {teacher}")
        teacher_dir = data_root / teacher
        main_dir = teacher_dir / 'main'
        ref_dir = teacher_dir / 'ref1'
        cited_dir = teacher_dir / 'cited'
        
        client = ex.InspireHEPClient()

        tasks = []
        for doi in dois:
            if f"{teacher}|{doi}" in processed_records:
                print(f"  [Skipped] {doi} (Already processed)")
                continue
            tasks.append((client, doi, main_dir, ref_dir, cited_dir, sample_size, years_window, workers_related, limit_ref, limit_cited, teacher))
        
        if tasks:
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers_main) as executor:
                list(executor.map(ex.process_doi_task, tasks))
        else:
            print(f"  All DOIs for {teacher} are already processed.")

        # Convert to MD
        token = args.token or ex.os.getenv('MINERU_TOKEN')
        if token:
            print(f"  Converting PDFs to MD for {teacher}...")
            ex.convert_pdfs_to_md(teacher, data_root, data_root, token)
        else:
            print(f"  Skipping PDF to MD conversion for {teacher} (no token).")
            
        # Generate Metadata JSON
        all_items = []
        for subdir in [main_dir, ref_dir, cited_dir]:
            if not subdir.exists(): continue
            for meta_file in subdir.glob('*_metadata.json'):
                try:
                    with open(meta_file, 'r', encoding='utf-8') as f:
                        meta = json.load(f)
                        if subdir.name == 'main': meta['role'] = 'main'
                        elif subdir.name == 'ref1': meta['role'] = 'reference'
                        elif subdir.name == 'cited': meta['role'] = 'citation'
                        
                        item = {
                            "title": meta.get("title"),
                            "doi": meta.get("doi"),
                            "authors": meta.get("authors"),
                            "published": ex.parse_year_month(meta.get("publication_date")),
                            "role": meta.get("role"),
                            "record_id": meta.get("record_id"),
                            "inspire_url": meta.get("inspire_url"),
                            "citations_count": meta.get("citations", 0)
                        }
                        pub_year = item.get("published", {}).get("year")
                        ya = ex.compute_young_author_fields(client, item.get("authors", []), pub_year, years_window)
                        item.update(ya)
                        all_items.append(item)
                except Exception: pass
        
        with open(teacher_dir / 'metadata_items.json', 'w', encoding='utf-8') as f:
            json.dump({"items": all_items}, f, ensure_ascii=False, indent=2)
        print(f"  Metadata saved to {teacher_dir / 'metadata_items.json'}")

if __name__ == "__main__":
    main()
