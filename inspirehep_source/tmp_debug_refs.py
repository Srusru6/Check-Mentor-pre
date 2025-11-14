from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
PKG_ROOT = ROOT / 'inspirehep_downloader'
INNER_PKG = PKG_ROOT / 'inspirehep_downloader'
META_DIR = PKG_ROOT / 'meta-data'

for p in (str(PKG_ROOT), str(INNER_PKG), str(META_DIR)):
    if p not in sys.path:
        sys.path.insert(0, p)

from inspirehep_downloader.inspirehep_downloader.client import InspireHEPClient  # type: ignore
import importlib.util as iu
doi_mod_path = META_DIR / 'doi_downloader.py'
spec = iu.spec_from_file_location('doi_mod', str(doi_mod_path))
doi_mod = iu.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(doi_mod)  # type: ignore
fetch_related_ids = getattr(doi_mod, 'fetch_related_ids')


def main():
    rid = '3063719'
    c = InspireHEPClient()
    log_dir = Path(__file__).resolve().parents[1] / 'log'
    log_dir.mkdir(parents=True, exist_ok=True)
    out = log_dir / 'related_debug2.txt'
    try:
        refs_raw = c.get_references(rid, size=5)
        cits_raw = c.get_citations(rid, size=5)
        with open(out, 'a', encoding='utf-8') as f:
            f.write(f"rid={rid} refs_keys={list(refs_raw.keys())}\n")
            f.write(f"rid={rid} cits_keys={list(cits_raw.keys())}\n")
            f.write(f"parsed refs={fetch_related_ids(c, rid, 'references', 5)}\n")
            f.write(f"parsed cits={fetch_related_ids(c, rid, 'citations', 5)}\n")
    except Exception as e:
        with open(out, 'a', encoding='utf-8') as f:
            f.write(f"error: {e}\n")


if __name__ == '__main__':
    main()
