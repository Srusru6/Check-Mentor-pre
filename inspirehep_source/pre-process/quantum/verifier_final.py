import requests
import re
import os
import argparse
from tqdm import tqdm

class PKUPaperVerifier:
    """
    PKU 论文验证审计程序最终版
    功能：对已生成的 results.txt 进行二次审计，识别跨学科撞名干扰
    """
    def __init__(self):
        self.headers = {'User-Agent': 'PKU-Audit-Bot/2.0'}
        # 排除关键词 (核心生物/化学/医学红旗)
        self.red_flags = [
            "cancer", "tumor", "clinical", "surgery", "patient", "brain", "drug",
            "medicine", "insect", "plant", "soil", "microbiology", "epidemiology",
            "psychology", "social", "marketing", "business", "economy", "finance",
            "nursing", "food", "ecology", "veterinary", "concrete", "cement"
        ]
        # 物理/量子核心期刊 (白名单，有这些词通常是安全的)
        self.physics_white_list = [
            "physical review", "physics", "nature physics", "nature materials",
            "nanotechnology", "optics", "quantum", "applied physics", "nano letters",
            "advanced materials", "science", "nature communications", "pnas"
        ]

    def audit_doi(self, doi):
        """调用 Crossref/OpenAlex 检查单篇论文的领域属性"""
        url = f"https://api.crossref.org/works/{doi}"
        try:
            r = requests.get(url, timeout=10).json()
            message = r.get('message', {})
            title = str(message.get('title', [''])[0]).lower()
            journal = str(message.get('container-title', [''])[0]).lower()
            
            # 策略：如果命中红旗且不在白名单内，则判为 Bad
            has_red_flag = any(flag in title or flag in journal for flag in self.red_flags)
            is_physics = any(white in journal for white in self.physics_white_list)
            
            if has_red_flag and not is_physics:
                return False, f"[Bad] {journal} | {title[:60]}..."
            return True, f"[OK] {journal}"
        except:
            return True, "Check Failed (API)"

    def audit_results_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"文件不存在: {file_path}")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 解析 blocks
        blocks = re.split(r'={10,}', content)
        report = []
        
        print(f"--- 启动论文审计: {file_path} ---")
        
        for i in range(1, len(blocks)-1, 2):
            name = blocks[i].strip()
            data = blocks[i+1].strip()
            dois = [l.strip() for l in data.split('\n') if '.' in l and '/' in l]
            
            if not dois: continue
            
            print(f"审计 {name} ({len(dois)} 篇)...")
            bad_papers = []
            for doi in tqdm(dois, leave=False):
                ok, msg = self.audit_doi(doi)
                if not ok:
                    bad_papers.append((doi, msg))
            
            if bad_papers:
                summary = f"导师: {name} | 疑似干扰项: {len(bad_papers)}\n"
                for doi, msg in bad_papers:
                    summary += f"  - {doi}: {msg}\n"
                report.append(summary)

        # 保存审计报告
        report_path = file_path.replace("results.txt", "audit_report.txt")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(report))
        
        print(f"\n[OK] 审计完成。发现干扰项的导师报告已保存至: {report_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PKU Paper Verifier Final")
    parser.add_argument("file", help="results.txt 的完整路径")
    args = parser.parse_args()
    
    verifier = PKUPaperVerifier()
    verifier.audit_results_file(args.file)
