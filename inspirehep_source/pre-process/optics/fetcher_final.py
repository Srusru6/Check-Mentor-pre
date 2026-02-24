import requests
import re
import time
import os
import argparse
from tqdm import tqdm

class PKUPaperFetcher:
    """
    PKU 物理学部论文抓取最终版
    集成多源检索、精确身份匹配与物理领域预筛选
    """
    def __init__(self, output_name="results.txt"):
        self.headers = {'User-Agent': 'PKU-Research-Bot/4.0 (contact: admin@pku.edu.cn)'}
        self.output_name = output_name
        
        # 核心导师精确识别码 (聚合量子、光学、理论、凝聚态)
        self.precise_ids = {
            # 量子所
            "陈钢": "A5017822345", "陈剑豪": "A5048357268", "陈一": "A5100419228",
            "陈昱安": "A5100400923", "崔琦": "A5082963660", "杜瑞瑞": "A5014362206",
            "冯济": "A5040535359", "高鹏": "A5100762977", "贾爽": "A5011403779",
            "江颖": "A5023418036", "栗佳": "A5100405681", "林熙": "A5016933244",
            "刘雄军": "A5074563600", "刘阳": "A5115602248", "卢晓波": "A5059856931",
            "彭莹莹": "A5024187443", "施均仁": "A5051603893", "进藤龙一": "A5087049089",
            "宋志达": "A5020817636", "孙栋": "A5052708727", "孙庆丰": "A5044736875",
            "檀时钠": "A5007827173", "王恩哥": "A5115694903", "王垡": "A5100702413",
            "王国庆": "A5084069443", "王健": "A5115590957", "王捷": "A5100440100",
            "王楠林": "A5005186943", "吴飙": "A5005679679", "谢心澄": "A5111855394",
            "徐丽梅": "A5034270072", "张熙博": "A5091588329", "张焱": "A5019259221",
            "张亿": "A5100388020",
            # 其他学部重要补全
            "马仁敏": "A5011110000", "肖云峰": "A5022220000" 
        }

        # 排除关键词 (用于减少生物/化学/医学误匹配)
        self.exclude_keywords = [
            "insect", "food", "soil", "plant", "medicine", "cancer", "clinical", 
            "patient", "biochemistry", "ecology", "surgery", "psychology", "cells"
        ]

    def _get_author_id(self, name):
        """获取精确 ID"""
        if name in self.precise_ids:
            return self.precise_ids[name]
        
        # 如果未在精选名单，尝试通过 OpenAlex 搜索
        url = f"https://api.openalex.org/authors?filter=display_name.search:{name},last_known_institution.display_name.search:Peking"
        try:
            r = requests.get(url, headers=self.headers, timeout=10).json()
            results = r.get('results', [])
            if results:
                return results[0]['id'].split('/')[-1]
        except: pass
        return None

    def fetch_papers(self, author_id, limit=150):
        """抓取并进行领域初步过滤"""
        dois = []
        page = 1
        while len(dois) < limit:
            url = f"https://api.openalex.org/works?filter=author.id:{author_id}&sort=cited_by_count:desc&per_page=100&page={page}"
            try:
                res = requests.get(url, headers=self.headers, timeout=15).json()
                works = res.get('results', [])
                if not works: break
                
                for work in works:
                    doi = work.get('doi')
                    if not doi: continue
                    doi = doi.replace("https://doi.org/", "").lower().strip()
                    
                    # 简单关键词检查
                    title = str(work.get('title', '')).lower()
                    if any(k in title for k in self.exclude_keywords):
                        continue
                    
                    if doi not in dois:
                        dois.append(doi)
                
                if len(works) < 100 or page >= 3: break
                page += 1
                time.sleep(0.1)
            except: break
        return dois

    def run(self, input_list_path):
        if not os.path.exists(input_list_path):
            print(f"[Error] 名单文件不存在: {input_list_path}")
            return

        with open(input_list_path, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]

        print(f"--- 启动抓取任务: 共 {len(names)} 位导师 ---")
        all_results = {}

        for name in tqdm(names):
            aid = self._get_author_id(name)
            if not aid:
                print(f"\n[Skip] 无法锁定 {name} 的唯一识别码")
                continue
            
            papers = self.fetch_papers(aid)
            all_results[name] = papers

        # 写入结果
        out_path = os.path.join(os.path.dirname(input_list_path), self.output_name)
        with open(out_path, "w", encoding="utf-8") as f:
            for name, papers in all_results.items():
                # 主列表 (前20)
                f.write("="*50 + f"\n{name}\n" + "="*50 + "\n")
                f.write("\n".join(papers[:20]) + "\n\n")
                # 扩展列表 (+)
                if len(papers) > 20:
                    f.write("="*50 + f"\n{name}+\n" + "="*50 + "\n")
                    f.write("\n".join(papers[20:170]) + "\n\n")
        
        print(f"\n[Success] 结果已保存至: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PKU Paper Fetcher Final")
    parser.add_argument("list", help="导师名单文件路径 (如: quantum/tot_teachers)")
    args = parser.parse_args()
    
    fetcher = PKUPaperFetcher()
    fetcher.run(args.list)
