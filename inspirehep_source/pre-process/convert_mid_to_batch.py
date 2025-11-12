import json
import re
from pathlib import Path


def extract_dois_from_bib_block(block: str) -> list[str]:
    """从一个 BibTeX-ish 文本块中提取 DOI，返回 DOI 列表（通常 0 或 1 个）。"""
    dois: list[str] = []
    # 匹配形如 doi = "10.xxx" 或 doi = 10.xxx 或 DOI = ...
    for m in re.finditer(r"\bdoi\s*=\s*([\"']?)(10\.[^\s\",}]+)\1", block, flags=re.IGNORECASE):
        # 去掉末尾的逗号或花括号前的多余字符
        doi = m.group(2).strip().rstrip(',')
        # 清理可能包含的结尾引号或括号
        doi = doi.strip('"\'{} ')
        if doi and doi not in dois:
            dois.append(doi)
    return dois


def parse_mid_txt(path: Path) -> tuple[str | None, list[str], list[str]]:
    """解析 mid.txt，返回 (teacher, recent_dois, cited_dois)。

    假设结构：
    - 第一行可能为注释；读取首个非空且不以 '##' 开头的行作为老师姓名。
    - 存在两个分段标题：`时间排序：` 与 `引用排序：`，其后各跟若干 BibTeX 条目。
    - 仅提取包含 DOI 的条目；无 DOI 的条目将被忽略。
    """
    text = path.read_text(encoding='utf-8')
    lines = [ln.rstrip('\n') for ln in text.splitlines()]

    # 老师名：首个非空且不以 '##' 开头的行
    teacher: str | None = None
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith('##'):
            continue
        teacher = s
        break

    # 按分段切
    content = '\n'.join(lines)
    # 使用标题定位两个区域
    recent_start = content.find('时间排序')
    cited_start = content.find('引用排序')

    recent_block = ''
    cited_block = ''
    if recent_start != -1 and cited_start != -1:
        if recent_start < cited_start:
            recent_block = content[recent_start:cited_start]
            cited_block = content[cited_start:]
        else:
            cited_block = content[cited_start:recent_start]
            recent_block = content[recent_start:]
    elif recent_start != -1:
        recent_block = content[recent_start:]
    elif cited_start != -1:
        cited_block = content[cited_start:]

    # 以 @article{...} 块切分提取
    def split_bib_blocks(txt: str) -> list[str]:
        parts: list[str] = []
        cur: list[str] = []
        inside = False
        for ln in txt.splitlines():
            if ln.strip().startswith('@'):
                if cur:
                    parts.append('\n'.join(cur))
                    cur = []
                inside = True
            if inside:
                cur.append(ln)
            # 宽松判断：以单独的 '}' 结束一个条目
            if inside and ln.strip() == '}':
                parts.append('\n'.join(cur))
                cur = []
                inside = False
        if cur:
            parts.append('\n'.join(cur))
        return parts

    recent_blocks = split_bib_blocks(recent_block)
    cited_blocks = split_bib_blocks(cited_block)

    recent_dois: list[str] = []
    cited_dois: list[str] = []
    for b in recent_blocks:
        recent_dois.extend(extract_dois_from_bib_block(b))
    for b in cited_blocks:
        cited_dois.extend(extract_dois_from_bib_block(b))

    # 去重，保持原顺序
    def dedup(seq: list[str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for x in seq:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    return teacher, dedup(recent_dois), dedup(cited_dois)


def main():
    root = Path(__file__).resolve().parent
    mid_txt = root / 'mid.txt'
    if not mid_txt.exists():
        raise SystemExit(f'未找到 {mid_txt}')
    teacher, recents, citeds = parse_mid_txt(mid_txt)
    if not teacher:
        raise SystemExit('未识别老师姓名（首个非空非注释行）。')
    if not recents and not citeds:
        raise SystemExit('未提取到任何 DOI（请确认条目包含 doi 字段）。')

    out = {
        teacher: {
            'recent': recents,
            'cited': citeds,
        }
    }
    out_path = root / 'mid_batch.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'✓ 已生成 {out_path} ({len(recents)} recent, {len(citeds)} cited)')


if __name__ == '__main__':
    main()
