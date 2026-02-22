import requests
import re
import time
import os


class PKUCondensedMatterProcessor:
    """
    凝聚态物理所专用：论文抓取 + 身份确权 + 物理领域过滤 + 格式化输出
    支持顶刊优先排序（精选）、机构(PKU)联合校验、结果数量限制。
    """

    def __init__(self, output_path="results.txt"):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_path = os.path.join(self.current_dir, output_path)
        self.headers = {'User-Agent': 'PKU-Research-Bot/3.0 (mailto:admin@pku.edu.cn)'}
        self.search_config = self.load_search_config()

        # 1. 凝聚态所核心身份 ID (精准锁定以解决重名和 ID 漂移问题)
        self.precise_ids = {
            "欧阳颀": "A5056459691",
            "俞大鹏": "A5108252277", # 院士专用 ID
            "汤超": "A5021238965",
            "沈波": "A5034873347",
            "王新强": "A5063851586",
            "戴伦": "A5000097979",
            "廖志敏": "A5032228398",
            "全海涛": "A5009360097",
            "刘开辉": "A5057034444",
            "李新征": "A5009852230",
            "马仁敏": "A5076287552",
            "方哲宇": "A5042698716",
            "吴孝松": "A5045474324",
            "马平": "A5112102874",
            "韩景智": "A5058778438",
            "杨金波": "A5064619965"
        }

        # 2. 精选期刊关键词 (针对凝聚态物理进行了调整)
        self.top_journals = [
            "Nature", "Science", "Nature Physics", "Nature Materials", "Nature Nanotechnology",
            "Nature Photonics", "Nature Electronics", "Nature Communications", "Science Advances", 
            "Physical Review Letters", "Physical Review X", "Advanced Materials", "Nano Letters", 
            "ACS Nano", "Advanced Functional Materials", "Physical Review B", "Applied Physics Letters", 
            "NPJ Quantum Materials", "National Science Review", "Joule", "Matter", "Nano Energy",
            "Optica", "Laser & Photonics Reviews", "Light: Science & Applications"
        ]

        # 3. 北京大学机构关键词
        self.pku_affiliations = [
            "Peking University", "PKU", "Condensed Matter", "Physics", 
            "State Key Laboratory", "Quantum Matter"
        ]

        # 4. 领域过滤关键词 (排除非物理类干扰)
        self.exclude_keywords = [
            "insect", "food", "forensic", "soil", "plant", "biol", "bio", "med", "drug",
            "cancer", "psych", "econ", "social", "envir", "earth", "geol", "agro",
            "forest", "veter", "animal", "climat", "virus", "cells", "brain", "neuro",
            "clinical", "orthop", "surgery", "patient", "nursing", "public health",
            "epidemiol", "genet", "molecular biology"
        ]

    def is_physical_paper(self, title, journal=""):
        text = (str(title) + " " + str(journal)).lower()
        if any(keyword in text for keyword in self.exclude_keywords):
            return False
        if any(k in text for k in ["insect", "plant physiology", "clinical trial"]):
            return False
        return True

    def load_search_config(self):
        config = {}
        path = os.path.join(self.current_dir, "search.txt")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            entries = re.findall(r'(.*?)：\n"strict_names": \[(.*?)\]', content)
            for name, names_str in entries:
                names = [item.strip().strip('"').replace(',', ' ') for item in names_str.split(',')]
                config[name.strip()] = names
        return config

    def search_author(self, name):
        if name in self.precise_ids:
            return self.precise_ids[name]

        search_names = [name]
        if name in self.search_config:
            search_names.extend(self.search_config[name])

        for search_name in search_names:
            encoded_name = search_name.replace(" ", "%20")
            url = (
                "https://api.openalex.org/authors?filter="
                f"display_name.search:{encoded_name},last_known_institutions.id:I20231570"
            )
            try:
                url_no_filter = f"https://api.openalex.org/authors?filter=display_name.search:{encoded_name}"
                resp = requests.get(url_no_filter, headers=self.headers, timeout=10).json()
                results = resp.get('results', [])
                for r in results:
                    insts = str(r.get('last_known_institutions', []))
                    if "Peking" in insts or "I20231570" in insts:
                        return r['id'].split('/')[-1]

                response = requests.get(url, headers=self.headers, timeout=10).json()
                results = response.get('results', [])
                if results:
                    return results[0]['id'].split('/')[-1]
            except Exception:
                continue
        return None

    def fetch_verified_papers(self, author_id):
        all_papers = []
        seen_dois = set()
        page = 1
        while page <= 5: 
            url = (
                "https://api.openalex.org/works?filter="
                f"author.id:{author_id}&sort=cited_by_count:desc&per_page=100&page={page}"
            )
            try:
                response = requests.get(url, headers=self.headers, timeout=15).json()
                works = response.get('results', [])
                if not works: break

                for work in works:
                    doi = work.get('doi')
                    if not doi: continue
                    doi = doi.replace("https://doi.org/", "").lower().strip()
                    if doi in seen_dois: continue

                    title = work.get('title', '')
                    journal = str(work.get('primary_location', {}).get('source', {}).get('display_name', ''))
                    
                    if self.is_physical_paper(title, journal):
                        is_top = any(tj.lower() in journal.lower() for tj in self.top_journals)
                        all_papers.append({
                            'doi': doi,
                            'is_top': is_top,
                            'citations': work.get('cited_by_count', 0)
                        })
                        seen_dois.add(doi)

                if len(works) < 100: break
                page += 1
                time.sleep(0.05)
            except Exception: break

        all_papers.sort(key=lambda x: (x['is_top'], x['citations']), reverse=True)
        return [p['doi'] for p in all_papers]

    def run(self, teacher_list_name="tot_teachers"):
        teachers_path = os.path.join(self.current_dir, teacher_list_name)
        if not os.path.exists(teachers_path):
            print(f"教师名单不存在: {teachers_path}")
            return

        with open(teachers_path, "r", encoding="utf-8") as f:
            teachers = [line.strip() for line in f if line.strip()]

        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write("") 

        for name in teachers:
            print(f">>> 处理凝聚态所导师: {name}")
            author_id = self.search_author(name)
            if not author_id:
                print(f"    [Skip] 无法识别 ID")
                continue

            dois = self.fetch_verified_papers(author_id)
            if not dois:
                print(f"    [Skip] 无法检索到有效论文")
                continue

            main_list = dois[:20]
            plus_list = []
            if len(dois) > 20:
                plus_list = dois[20:170] # 限制在 150 篇以内

            with open(self.output_path, "a", encoding="utf-8") as f:
                f.write("=" * 50 + f"\n{name}\n" + "=" * 50 + "\n")
                f.write("\n".join(main_list) + "\n\n")
                if plus_list:
                    f.write("=" * 50 + f"\n{name}+\n" + "=" * 50 + "\n")
                    f.write("\n".join(plus_list) + "\n\n")

            print(f"    [Success] 已抓取 {len(main_list)} 主论文 + {len(plus_list)} 补充论文")
            time.sleep(0.05)


if __name__ == "__main__":
    processor = PKUCondensedMatterProcessor()
    processor.run()
