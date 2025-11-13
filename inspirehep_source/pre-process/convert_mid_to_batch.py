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


def parse_mid_multi(path: Path) -> dict[str, dict[str, list[str]]]:
    """解析包含一位或多位老师的 mid.txt，返回 {teacher: {recent: [...], cited: [...]}}。

    兼容格式：
    - 老师名单独成行（非空、非注释、非条目/字段行），其后出现“时间排序”与“引用排序”两个分段，各包含若干 BibTeX-ish 条目；
    - 分段标题可写作“时间排序”/“时间排序：”“引用排序”/“引用排序：”，均可；
    - 条目中以 @article{...} ... } 组织，提取包含 doi= 的条目；
    - 文件内可包含多位老师，按“老师名”开始到下一个“老师名”开始之间作为一个分块解析。
    """
    text = path.read_text(encoding='utf-8')
    lines = [ln.rstrip('\n') for ln in text.splitlines()]

    def is_teacher_header(idx: int) -> bool:
        s = lines[idx].strip()
        if not s or s.startswith('##'):
            return False
        low = s.lower()
        if low.startswith('@'):
            return False
        if any(k in s for k in ['=', '{', '}', ': ']):
            # 避免匹配到字段或条目标题行
            return False
        if '时间排序' in s or '引用排序' in s:
            return False
        # 进一步校验：后续若干行中出现“时间排序/引用排序”，更像老师段落
        for j in range(1, 15):
            k = idx + j
            if k >= len(lines):
                break
            sj = lines[k].strip()
            if not sj:
                continue
            if ('时间排序' in sj) or ('引用排序' in sj):
                return True
            # 若遇到另一个明显的 header 或 bib 开始，认为不是老师名
            if sj.startswith('@'):
                return False
        # 若未观察到分段标题，也允许作为老师名（宽松处理）
        return True

    # 定位所有老师名的起始行
    headers: list[tuple[int, str]] = []
    for i, raw in enumerate(lines):
        if is_teacher_header(i):
            headers.append((i, lines[i].strip()))

    # 若未识别 header，则尝试兼容旧逻辑：首个非注释非空行作为老师
    if not headers:
        for ln in lines:
            s = ln.strip()
            if not s or s.startswith('##'):
                continue
            headers = [(0, s)]
            break

    # 为了避免误判，将 header 按位置去重（遇到连续相同行去重）
    uniq_headers: list[tuple[int, str]] = []
    last_pos = -999
    for pos, name in headers:
        if pos != last_pos:
            uniq_headers.append((pos, name))
            last_pos = pos

    # 辅助：拆分 bib 条目
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
            if inside and ln.strip() == '}':
                parts.append('\n'.join(cur))
                cur = []
                inside = False
        if cur:
            parts.append('\n'.join(cur))
        return parts

    # 辅助：去重但保序
    def dedup(seq: list[str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for x in seq:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    # 结果
    result: dict[str, dict[str, list[str]]] = {}

    # 遍历每位老师分块
    for idx, (start, teacher_name) in enumerate(uniq_headers):
        end = uniq_headers[idx + 1][0] if idx + 1 < len(uniq_headers) else len(lines)
        block_text = '\n'.join(lines[start:end])

        # 在该分块内查找“时间排序/引用排序”分段（允许有中文冒号或无冒号）
        rec_pat = re.compile(r"时间排序\s*[:：]?", re.S)
        cit_pat = re.compile(r"引用排序\s*[:：]?", re.S)

        rec_m = rec_pat.search(block_text)
        cit_m = cit_pat.search(block_text)

        recent_block = ''
        cited_block = ''
        if rec_m and cit_m:
            if rec_m.start() < cit_m.start():
                recent_block = block_text[rec_m.end():cit_m.start()]
                cited_block = block_text[cit_m.end():]
            else:
                cited_block = block_text[cit_m.end():rec_m.start()]
                recent_block = block_text[rec_m.end():]
        elif rec_m:
            recent_block = block_text[rec_m.end():]
        elif cit_m:
            cited_block = block_text[cit_m.end():]

        recent_dois: list[str] = []
        cited_dois: list[str] = []
        for b in split_bib_blocks(recent_block):
            recent_dois.extend(extract_dois_from_bib_block(b))
        for b in split_bib_blocks(cited_block):
            cited_dois.extend(extract_dois_from_bib_block(b))

        tname = teacher_name.strip()
        if not tname or tname.startswith('##'):
            continue
        if (not recent_dois) and (not cited_dois):
            # 本分块未解析到任何 DOI，跳过
            continue
        result[tname] = {
            'recent': dedup(recent_dois),
            'cited': dedup(cited_dois),
        }

    return result


def main():
    root = Path(__file__).resolve().parent
    mid_txt = root / 'mid.txt'
    if not mid_txt.exists():
        raise SystemExit(f'未找到 {mid_txt}')
    plan = parse_mid_multi(mid_txt)
    if not plan:
        raise SystemExit('未在 mid.txt 中解析到任何老师或 DOI。')

    out = plan
    out_path = root / 'mid_batch.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    # 汇总统计
    total_recent = sum(len(v.get('recent', [])) for v in out.values())
    total_cited = sum(len(v.get('cited', [])) for v in out.values())
    print(f'✓ 已生成 {out_path} （老师数={len(out)} | recent 总数={total_recent} | cited 总数={total_cited}）')


if __name__ == '__main__':
    main()
