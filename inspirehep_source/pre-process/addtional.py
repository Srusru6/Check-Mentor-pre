import os
import re
import time
import random
import urllib.parse
import configparser
from dataclasses import dataclass
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup

# Settings
MAX_AUTHORS = 10
PHYSREV_TAGS = (
    "physreva",
    "physrevb",
    "physrevc",
    "physrevd",
    "physreve",
    "physrevx",
    "prxquantum",
    "physrevresearch",
    "revmodphys",
)
PHYSICS_ALLOW_HINTS = (
    "physrev",
    "physlett",
    "jhep",
    "epjc",
    "jcap",
    "prxquantum",
    "revmodphys",
    "jphys",
    "apj",
    "mnras",
    "ajp",
    "cqg",
    "nphys",
    "natphys",
    "astro",
    "astron",
    "cosmo",
)
EXCLUDED_KEYWORDS = (
    "medicine",
    "medical",
    "medic",
    "oncology",
    "cancer",
    "bio",
    "biology",
    "biomed",
    "chem",
    "chemical",
    "chemistry",
    "pharm",
    "drug",
    "cell",
    "clinic",
    "clinical",
    "neuro",
    "immun",
    "virol",
    "virus",
    "bacteria",
)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "config.ini"))
UNFINISHED_PATH = os.path.join(CURRENT_DIR, "unfinished_teachers.txt")
RESULTS_PATH = os.path.join(CURRENT_DIR, "results.txt")
FINISHED_PATH = os.path.join(CURRENT_DIR, "finished_teachers.txt")
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.x-mol.com/paper/search",
}
BASE_DELAY = 0.6
JITTER = 0.4


@dataclass
class Target:
    cn_name: str
    url: str
    strict_names: List[str]


def parse_targets(file_path: str) -> List[Target]:
    targets: List[Target] = []
    current_name = None
    current_url = None
    strict_names: List[str] = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f]

    def flush():
        nonlocal current_name, current_url, strict_names
        if current_name and current_url:
            targets.append(Target(current_name, current_url, strict_names or [extract_option_from_url(current_url)]))
        current_name, current_url, strict_names = None, None, []

    for line in lines:
        if not line:
            continue
        if line.startswith("*"):
            strict_names.append(line.lstrip("*").strip())
            continue
        if line.startswith("http"):
            current_url = line.strip()
            continue
        # Chinese name line
        if current_name and current_url:
            flush()
        current_name = line.rstrip("：:").strip()

    flush()

    # Construct missing URLs from strict names
    for t in targets:
        if not t.url and t.strict_names:
            option = urllib.parse.quote_plus(t.strict_names[0])
            t.url = f"https://www.x-mol.com/paper/search/q?selectSearchType=0&option={option}"
        if t.cn_name == "黄华卿" and all("huang" not in name.lower() for name in t.strict_names):
            t.strict_names.append("Huaqing Huang")
        if t.cn_name == "张大新" and all("zhang" not in name.lower() for name in t.strict_names):
            t.strict_names.append("Da-Xin Zhang")
    return targets


def extract_option_from_url(url: str) -> str:
    query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    option = query.get("option", [""])[0]
    return option.replace("+", " ").strip()


def build_page_url(base_url: str, page_index: int) -> str:
    parsed = urllib.parse.urlparse(base_url)
    query = dict(urllib.parse.parse_qsl(parsed.query))
    query["pageIndex"] = str(page_index)
    new_query = urllib.parse.urlencode(query)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment))


def sleep_with_jitter():
    time.sleep(BASE_DELAY + random.random() * JITTER)


def load_xmol_cookie() -> str | None:
    # 优先环境变量，其次 config.ini 的 [preprocess] xmol_cookie
    env_val = os.environ.get("XMOL_COOKIE")
    if env_val:
        return env_val.strip()

    if os.path.exists(CONFIG_PATH):
        parser = configparser.RawConfigParser()
        parser.read(CONFIG_PATH, encoding="utf-8")
        if parser.has_option("preprocess", "xmol_cookie"):
            cfg_val = parser.get("preprocess", "xmol_cookie").strip()
            return cfg_val or None
    return None


def split_authors(raw: str) -> List[str]:
    cleaned = raw.replace(" and ", ",").replace(";", ",")
    parts = [p.strip() for p in cleaned.split(",") if p.strip()]
    # 处理没有逗号/分号时相邻作者（用 2 个以上空格分隔）
    if len(parts) == 1 and "  " in cleaned:
        import re
        parts = [p.strip() for p in re.split(r"\s{2,}", cleaned) if p.strip()]
    return parts


def check_exact_match(authors: List[str], strict_names: List[str]) -> bool:
    """Strict name matching borrowed from main.py logic (supports order/space variants)."""
    for author in authors:
        full_lower = author.lower().strip()
        full_no_space = full_lower.replace(" ", "")
        full_tokens = __import__("re").findall(r"[a-z]+(?:-[a-z]+)?", full_lower)

        for strict in strict_names:
            strict_lower = strict.lower().strip()
            strict_no_space = strict_lower.replace(" ", "")

            # 1) exact match
            if full_lower == strict_lower:
                return True

            # 2) space-insensitive match
            if full_no_space == strict_no_space:
                return True

            # 3) comma order swap (e.g., "Feng, Xu" vs "Xu, Feng")
            if "," in full_lower and "," in strict_lower:
                f_parts = [p.strip() for p in full_lower.split(",")]
                s_parts = [p.strip() for p in strict_lower.split(",")]
                if len(f_parts) == 2 and len(s_parts) == 2:
                    if f_parts[0] == s_parts[1] and f_parts[1] == s_parts[0]:
                        return True
                    f_no_space = [p.replace(" ", "") for p in f_parts]
                    s_no_space = [p.replace(" ", "") for p in s_parts]
                    if f_no_space[0] == s_no_space[1] and f_no_space[1] == s_no_space[0]:
                        return True

            # 4) strict without comma vs full with comma
            # 要求严格按词匹配，且作者名仅由两词（或至多包含一个中间缩写）构成
            if "," not in strict_lower and "," in full_lower:
                s_parts_ws = [p.strip() for p in strict_lower.split() if p.strip()]
                if len(s_parts_ws) == 2 and len(full_tokens) == 2 and set(s_parts_ws) == set(full_tokens):
                    return True

            # 5) strict has comma but full has no comma (e.g., strict "Li, Dingping" vs full "Dingping Li")
            if "," in strict_lower and "," not in full_lower:
                s_parts = [p.strip() for p in strict_lower.split(",") if p.strip()]
                if len(s_parts) == 2 and len(full_tokens) == 2 and set(s_parts) == set(full_tokens):
                    return True

    return False


def is_physical_review(doi: str) -> bool:
    lower = doi.lower()
    return any(tag in lower for tag in PHYSREV_TAGS)


def is_high_priority_main(doi: str) -> bool:
    lower = doi.lower()
    return (
        "physrevd" in lower or
        "physrevlett" in lower or
        "nature" in lower or
        "science" in lower
    )


def is_secondary_main(doi: str) -> bool:
    lower = doi.lower()
    return ("physreva" in lower or "physrevb" in lower)


def looks_physics_doi(doi: str) -> bool:
    lower = doi.lower()
    if any(bad in lower for bad in EXCLUDED_KEYWORDS):
        return False
    if is_physical_review(doi):
        return True
    return any(hint in lower for hint in PHYSICS_ALLOW_HINTS)


def fetch_doi(session: requests.Session, paper_id: str, referer: str) -> str | None:
    url = f"https://www.x-mol.com/paperRedirect/{paper_id}"
    headers = {**DEFAULT_HEADERS, "Referer": referer}
    sleep_with_jitter()
    resp = session.get(url, headers=headers, allow_redirects=False, timeout=12)
    location = resp.headers.get("Location", "")
    if resp.status_code in (301, 302) and location:
        # 提取 DOI 并去掉查询参数（utm_* 等）
        m = re.search(r"10\.[^\s?#]+", location)
        if not m:
            return None
        doi = m.group(0)
        # 部分情况 DOI 可能后随 '?' 或 '#'
        doi = doi.split('?')[0].split('#')[0]
        return doi
    return None


def parse_page(html: str) -> List[Tuple[str, List[str]]]:
    soup = BeautifulSoup(html, "html.parser")
    items = []
    for li in soup.select("li[id^=searchPaperLi]"):
        paper_id = li.get("id", "").replace("searchPaperLi", "")
        author_span = li.select_one("span.magazine-text-atten-new")
        if not paper_id or not author_span:
            continue
        authors = split_authors(author_span.get_text(" ", strip=True))
        items.append((paper_id, authors))
    return items


def collect_for_target(session: requests.Session, target: Target) -> Tuple[List[str], List[str]]:
    main_high, main_secondary, other_physics = [], [], []
    seen = set()
    base_url = target.url
    strict_names = target.strict_names or [extract_option_from_url(base_url)]

    for page in range(1, 11):
        page_url = build_page_url(base_url, page)
        sleep_with_jitter()
        resp = session.get(page_url, headers=DEFAULT_HEADERS, timeout=15)
        if resp.status_code == 302 and "login" in resp.headers.get("Location", ""):
            print(f"[WARN] Login required for {target.cn_name} page {page}")
            break
        if resp.status_code != 200:
            print(f"[WARN] Failed page {page} for {target.cn_name}: {resp.status_code}")
            continue
        items = parse_page(resp.text)
        if not items:
            break
        for paper_id, authors in items:
            if len(authors) > MAX_AUTHORS:
                continue
            if not check_exact_match(authors, strict_names):
                continue
            doi = fetch_doi(session, paper_id, referer=page_url)
            if not doi or doi in seen:
                continue
            if not looks_physics_doi(doi):
                continue
            seen.add(doi)
            if is_high_priority_main(doi):
                main_high.append(doi)
            elif is_secondary_main(doi):
                main_secondary.append(doi)
            else:
                other_physics.append(doi)
    # 主栏：优先 PRD/PRL/Nature/Science，然后用 PRA/PRB 填满至 20
    main_bucket = []
    for doi in main_high:
        if len(main_bucket) >= 20:
            break
        main_bucket.append(doi)
    if len(main_bucket) < 20:
        for doi in main_secondary:
            if len(main_bucket) >= 20:
                break
            main_bucket.append(doi)
    # 加号栏：其余 PRA/PRB 的溢出 + 所有其他物理期刊
    used = set(main_bucket)
    overflow_secondary = [d for d in main_secondary if d not in used]
    plus_bucket = overflow_secondary + other_physics
    return main_bucket, plus_bucket


def write_results(results_path: str, target: Target, main_bucket: List[str], plus_bucket: List[str]) -> None:
    with open(results_path, "a", encoding="utf-8") as f:
        if main_bucket:
            f.write("=" * 50 + "\n")
            f.write(f"{target.cn_name}\n")
            f.write("=" * 50 + "\n")
            for doi in main_bucket:
                f.write(doi + "\n")
            f.write("\n")
        if plus_bucket:
            f.write("=" * 50 + "\n")
            f.write(f"{target.cn_name}+\n")
            f.write("=" * 50 + "\n")
            for doi in plus_bucket:
                f.write(doi + "\n")
            f.write("\n")


def mark_finished(name: str) -> None:
    existing: set[str] = set()
    if os.path.exists(FINISHED_PATH):
        with open(FINISHED_PATH, "r", encoding="utf-8") as f:
            existing = {line.strip() for line in f if line.strip()}
    if name not in existing:
        current_size = os.path.getsize(FINISHED_PATH) if os.path.exists(FINISHED_PATH) else 0
        with open(FINISHED_PATH, "a", encoding="utf-8") as f:
            if current_size > 0:
                f.write("\n")
            f.write(name)


def main():
    if not os.path.exists(UNFINISHED_PATH):
        raise FileNotFoundError(f"Missing {UNFINISHED_PATH}")

    targets = parse_targets(UNFINISHED_PATH)
    if not targets:
        print("No targets found in unfinished_teachers.txt")
        return

    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)

    cookie = load_xmol_cookie()
    if cookie:
        session.headers.update({"Cookie": cookie})
        print("Loaded XMOL cookie from env/config")
    else:
        print("[WARN] XMOL cookie missing; login pages may block results")

    print(f"Total targets: {len(targets)}")

    for target in targets:
        print(f"\n>>> {target.cn_name} | {target.url}")
        main_bucket, plus_bucket = collect_for_target(session, target)
        print(f"   main={len(main_bucket)}, plus={len(plus_bucket)}")
        write_results(RESULTS_PATH, target, main_bucket, plus_bucket)
        mark_finished(target.cn_name)


if __name__ == "__main__":
    main()
