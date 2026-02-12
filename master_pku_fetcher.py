
import requests
import re
import time
import os

class PKUMasterFetcher:
    """
    高度集成的论文抓取与身份验证程序
    功能：多源检索（OpenAlex API）、身份验证、领域筛选、结果聚合
    """
    def __init__(self, output_path="master_results.txt", affiliation="Peking University"):
        self.output_path = output_path
        self.affiliation = affiliation
        self.headers = {'User-Agent': 'PKU-Research-Bot/2.0 (mailto:admin@pku.edu.cn)'}
        # 预存的精确 ID (针对重名率高的导师)
        self.precise_ids = {
            "谢心澄": "A5055967310",
            "江颖": "A5023418036",
            "王恩哥": "A5111166668",
            "崔琦": "A5110862535",
            "张亿": "A5100393074",
            "宋志达": "A5020817636",
            "徐丽梅": "A5034270072"
        }

    def search_author(self, name):
        """查找并验证作者 ID"""
        if name in self.precise_ids:
            return self.precise_ids[name]
        
        url = f"https://api.openalex.org/authors?filter=display_name.search:{name},last_known_institution.display_name.search:Peking"
        try:
            r = requests.get(url, headers=self.headers, timeout=10).json()
            results = r.get('results', [])
            if results:
                # 返回引用最高的匹配项
                return results[0]['id'].split('/')[-1]
        except Exception as e:
            print(f"  [Error] 查找作者 {name} 失败: {e}")
        return None

    def fetch_papers(self, author_id, keywords=None):
        """抓取并筛选论文"""
        dois = []
        page = 1
        while page <= 3: # 抓取前300篇
            url = f"https://api.openalex.org/works?filter=author.id:{author_id}&sort=cited_by_count:desc&per_page=100&page={page}"
            try:
                r = requests.get(url, headers=self.headers, timeout=15).json()
                works = r.get('results', [])
                if not works: break
                
                for work in works:
                    doi = work.get('doi')
                    if not doi: continue
                    doi = doi.replace("https://doi.org/", "").lower()
                    
                    # 领域筛选 (如果提供关键词)
                    if keywords:
                        text = (str(work.get('title')) + str(work.get('abstract'))).lower()
                        if not any(k.lower() in text for k in keywords):
                            continue
                            
                    if doi not in dois:
                        dois.append(doi)
                
                if len(works) < 100: break
                page += 1
                time.sleep(0.2)
            except: break
        return dois

    def generate_results(self, teacher_list_path, keywords=None):
        """核心流程：读取名单 -> 抓取 -> 格式化输出"""
        if not os.path.exists(teacher_list_path):
            print(f"教师名单文件 {teacher_list_path} 不存在")
            return

        with open(teacher_list_path, "r", encoding="utf-8") as f:
            teachers = [line.strip() for line in f if line.strip()]

        final_output = []
        for name in teachers:
            print(f"正在处理: {name}...")
            aid = self.search_author(name)
            if not aid:
                print(f"  [Warning] 未能锁定 {name} 的唯一识别码")
                continue
            
            dois = self.fetch_papers(aid, keywords)
            if not dois:
                print(f"  [Info] {name} 未找到符合条件的论文")
                continue

            # 格式化输出
            main = dois[:20]
            plus = dois[20:]
            
            final_output.append("="*50 + f"\n{name}\n" + "="*50)
            final_output.extend(main)
            final_output.append("")
            
            if plus:
                final_output.append("="*50 + f"\n{name}+\n" + "="*50)
                final_output.extend(plus)
                final_output.append("")
            
            print(f"  [Success] 已获取 {len(dois)} 篇论文")

        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(final_output))
        print(f"\n任务完成！结果已保存至 {self.output_path}")

if __name__ == "__main__":
    # 配置：教师名单路径，以及感兴趣的关键词（可选）
    TEACHER_LIST = r"inspirehep_source/pre-process/quantum/tot_teachers"
    KEYWORDS = ["physics", "quantum", "nano", "material", "condensed"] 
    
    fetcher = PKUMasterFetcher(output_path="final_results_summary.txt")
    fetcher.generate_results(TEACHER_LIST, keywords=None) # 这里 keywords=None 表示获取全量
