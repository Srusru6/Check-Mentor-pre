
import requests
import re
import time
import os

class PKUQuantumProcessor:
    """
    终极集成版：论文抓取 + 身份确权 + 物理领域过滤 + 格式化输出
    由 master_pku_fetcher 与 master_process 合并而成。
    """
    def __init__(self, output_path="results.txt"):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_path = os.path.join(self.current_dir, output_path)
        self.headers = {'User-Agent': 'PKU-Research-Bot/3.0 (mailto:admin@pku.edu.cn)'}
        
        # 1. 核心身份识别码 (解决重名、覆盖问题的最后防线)
        self.precise_ids = {
            "谢心澄": "A5055967310", "江颖": "A5023418036", "王恩哥": "A5111166668",
            "崔琦": "A5110862535", "张亿": "A5100393074", "宋志达": "A5020817636",
            "徐丽梅": "A5034270072", "卢晓波": "A5059856931", "施均仁": "A5051603893"
        }

        # 2. 领域过滤关键词 (排除生物、医药等无关论文)
        self.exclude_keywords = [
            "insect", "food", "forensic", "soil", "plant", "biol", "bio", "med", "drug", 
            "cancer", "psych", "econ", "social", "envir", "earth", "geol", "agro", 
            "forest", "veter", "animal", "climat", "virus", "cells", "brain", "neuro", 
            "clinical", "orthop", "surgery", "patient", "nursing", "public health", 
            "epidemiol", "genet", "molecular biology", "mechanical engineering", 
            "civil engineering", "mechanical", "ijoes", "scitotenv", "total environment", 
            "mechanical science", "polymer science", "petrol", "geophysical", "ocean"
        ]

    def is_physical_paper(self, title, journal=""):
        """检查论文是否属于物理/材料方向"""
        text = (str(title) + " " + str(journal)).lower()
        # 如果包含排除词，则过滤
        if any(k in text for k in self.exclude_keywords):
            return False
        return True

    def search_author(self, name):
        """查找并验证作者 ID"""
        if name in self.precise_ids:
            return self.precise_ids[name]
        
        url = f"https://api.openalex.org/authors?filter=display_name.search:{name},last_known_institution.display_name.search:Peking"
        try:
            r = requests.get(url, headers=self.headers, timeout=10).json()
            results = r.get('results', [])
            if results:
                return results[0]['id'].split('/')[-1]
        except Exception as e:
            print(f"  [Error] 查找作者 {name} 失败: {e}")
        return None

    def fetch_verified_papers(self, author_id):
        """抓取、过滤并去重"""
        dois = []
        page = 1
        while page <= 3:
            url = f"https://api.openalex.org/works?filter=author.id:{author_id}&sort=cited_by_count:desc&per_page=100&page={page}"
            try:
                r = requests.get(url, headers=self.headers, timeout=15).json()
                works = r.get('results', [])
                if not works: break
                
                for work in works:
                    doi = work.get('doi')
                    if not doi: continue
                    doi = doi.replace("https://doi.org/", "").lower().strip()
                    
                    title = work.get('title', '')
                    journal = work.get('primary_location', {}).get('source', {}).get('display_name', '')
                    
                    # 运行领域过滤逻辑
                    if self.is_physical_paper(title, journal):
                        if doi not in dois:
                            dois.append(doi)
                
                if len(works) < 100: break
                page += 1
                time.sleep(0.1)
            except: break
        return dois

    def run(self, teacher_list_name="tot_teachers"):
        """一键执行全流程"""
        teachers_path = os.path.join(self.current_dir, teacher_list_name)
        if not os.path.exists(teachers_path):
            print(f"错误: 找不到名单 {teacher_list_name}")
            return

        with open(teachers_path, "r", encoding="utf-8") as f:
            teachers = [line.strip() for line in f if line.strip()]

        final_content = []
        for name in teachers:
            print(f">>> 处理导师: {name}")
            aid = self.search_author(name)
            if not aid:
                print(f"    [Skip] 无法识别 ID")
                continue
            
            dois = self.fetch_verified_papers(aid)
            if not dois:
                print(f"    [Info] 未找到符合物理领域的论文")
                continue
            
            # 分割 20 + Plus
            main = dois[:20]
            plus = dois[20:]
            
            # 写入精选部分
            final_content.append("="*50 + f"\n{name}\n" + "="*50)
            final_content.extend(main)
            final_content.append("")
            
            # 写入附加部分
            if plus:
                final_content.append("="*50 + f"\n{name}+\n" + "="*50)
                final_content.extend(plus)
                final_content.append("")
            
            print(f"    [Success] 已抓取并过滤出 {len(dois)} 篇论文")

        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(final_content))
        print(f"\n[任务全量完成] 数据已同步至: {self.output_path}")

if __name__ == "__main__":
    processor = PKUQuantumProcessor()
    processor.run()
