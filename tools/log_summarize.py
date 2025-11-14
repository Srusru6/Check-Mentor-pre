import sys
import re
from pathlib import Path
from datetime import datetime, timedelta

TS_RE = re.compile(r"^(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+([+-]\d{2}:\d{2}|Z)?)\s+\t\s*(?P<msg>.*)$")


def parse_ts(s: str) -> datetime | None:
    try:
        # Accept ISO with timezone or Z
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def summarize(log_path: Path):
    if not log_path.exists():
        print(f"Log not found: {log_path}")
        return 2
    records = []
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = TS_RE.match(line.rstrip("\n"))
            if not m:
                continue
            ts = parse_ts(m.group("ts"))
            if not ts:
                continue
            msg = m.group("msg")
            records.append((ts, msg))
    if not records:
        print("No timestamped lines to summarize.")
        return 0
    records.sort(key=lambda x: x[0])
    start = records[0][0]
    cut1 = start + timedelta(minutes=5)
    cut2 = start + timedelta(minutes=10)

    def in_win(ts: datetime, a: datetime, b: datetime) -> bool:
        return a <= ts < b

    def count_win(a: datetime, b: datetime):
        c_main = c_refs = c_cited = c_429 = 0
        for ts, msg in records:
            if not in_win(ts, a, b):
                continue
            m = msg
            if "429" in m or "Too Many Requests" in m:
                c_429 += 1
            if "main saved at" in m:
                c_main += 1
            # refs/cited processed lines
            if (" refs " in m or m.strip().startswith("refs ")) and "->" in m:
                c_refs += 1
            if (" cited " in m or m.strip().startswith("cited ")) and "->" in m:
                c_cited += 1
        mins = max(1.0, (b - a).total_seconds() / 60.0)
        return {
            "main": c_main,
            "refs": c_refs,
            "cited": c_cited,
            "429": c_429,
            "rate_main_per_min": round(c_main / mins, 3),
            "rate_related_per_min": round((c_refs + c_cited) / mins, 3),
        }

    w1 = count_win(start, cut1)
    w2 = count_win(cut1, cut2)
    print("Summary (first 5 min):", w1)
    print("Summary (last 5 min):", w2)
    # Simple diagnose
    diag = []
    if w2["rate_main_per_min"] + w2["rate_related_per_min"] < (w1["rate_main_per_min"] + w1["rate_related_per_min"]) * 0.6:
        if w2["429"] > w1["429"]:
            diag.append("Likely throttling (429 increased, throughput dropped)")
        else:
            diag.append("Likely local I/O or long-tail related items")
    else:
        diag.append("Throughput relatively stable")
    print("Diagnosis:", "; ".join(diag))
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        path = Path(argv[1])
    else:
        log_dir = Path("log")
        cands = sorted(log_dir.glob("run_*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not cands:
            print("No log files under ./log")
            return 1
        path = cands[0]
    print(f"Analyzing: {path}")
    return summarize(path)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
