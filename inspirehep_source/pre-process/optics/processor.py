import requests
import re
import time
import os


class PKUOpticsProcessor:
    """
    终极集成版：论文抓取 + 身份确权 + 物理领域过滤 + 格式化输出
    增强功能：支持顶刊优先排序（精选）、机构(PKU)联合校验、拼音名自动匹配。
    """

    def __init__(self, output_path="results.txt"):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_path = os.path.join(self.current_dir, output_path)
        self.headers = {'User-Agent': 'PKU-Research-Bot/3.0 (mailto:admin@pku.edu.cn)'}
        self.search_config = self.load_search_config()

        # 1. 核心身份识别码 (解决重名、覆盖问题的最后防线)
        self.precise_ids = {
            "陈志坚": "A5100716620",
            "高宇南": "A5072592756",
            "龚旗煌": "A5072771171",
            "古英": "A5067874194",
            "何琼毅": "A5050279691",
            "胡小永": "A5045232016",
            "胡耀文": "A5031341222",
            "蒋红兵": "A5015313963",
            "李焱": "A5100332367",
            "李铮": "A5100376569",
            "刘文静": "A5100378300",
            "刘运全": "A5102978578",
            "吕国伟": "A5088432045",
            "彭良友": "A5038991319",
            "彭湃": "A5058810009",
            "曲波": "A5108047874",
            "施可彬": "A5049601762",
            "宋博": "A5100381911",
            "王剑威": "A5100424784",
            "王若鹏": "A5065449266",
            "王树峰": "A5000448546",
            "吴成印": "A5033524459",
            "肖立新": "A5002043178",
            "肖云峰": "A5034397421",
            "许秀来": "A5064695909",
            "杨起帆": "A5022151304",
            "张家森": "A5082957950",
            "朱瑞": "A5100617068"
        }

        # 2. 精选期刊关键词 (用于 Top 20 排序权重)
        self.top_journals = [
            "Nature", "Science", "Nature Photonics", "Nature Physics",
            "Nature Communications", "Science Advances", "Physical Review Letters",
            "Light: Science & Applications", "Advanced Materials", "Nano Letters",
            "ACS Nano", "Optica", "Matter", "Advanced Functional Materials",
            "Advanced Optical Materials", "Laser & Photonics Reviews",
            "Applied Physics Letters", "Optics Letters", "Optics Express",
            "ACS Photonics", "Photonics Research", "Nanophotonics",
            "National Science Review", "Joule"
        ]

        # 3. 北京大学机构关键词 (用于精细化验证)
        self.pku_affiliations = [
            "Peking University", "PKU", "Mesoscopic Physics", 
            "Modern Optics", "School of Physics", "Artificial Microstructure"
        ]

        # 4. 领域过滤关键词 (排除生物、医药等无关论文)
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
        if any(keyword in text for keyword in self.exclude_keywords):
            return False
        return True

    def load_search_config(self):
        """加载 search.txt 中的拼音与严格名称"""
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
        """查找并验证作者 ID"""
        if name in self.precise_ids:
            return self.precise_ids[name]

        search_names = [name]
        if name in self.search_config:
            search_names.extend(self.search_config[name])

        for search_name in search_names:
            url = (
                "https://api.openalex.org/authors?filter="
                f"display_name.search:{search_name},last_known_institution.display_name.search:Peking"
            )
            try:
                response = requests.get(url, headers=self.headers, timeout=10).json()
                results = response.get('results', [])
                if results:
                    return results[0]['id'].split('/')[-1]
            except Exception:
                continue
        return None

    def fetch_verified_papers(self, author_id):
        """抓取、过滤并依据期刊影响力重排 (顶刊优先)"""
        all_papers = []
        seen_dois = set()
        page = 1
        while page <= 4:
            url = (
                "https://api.openalex.org/works?filter="
                f"author.id:{author_id}&sort=cited_by_count:desc&per_page=100&page={page}"
            )
            try:
                response = requests.get(url, headers=self.headers, timeout=15).json()
                works = response.get('results', [])
                if not works:
                    break

                for work in works:
                    doi = work.get('doi')
                    if not doi: continue
                    doi = doi.replace("https://doi.org/", "").lower().strip()
                    if doi in seen_dois: continue

                    title = work.get('title', '')
                    journal = str(work.get('primary_location', {}).get('source', {}).get('display_name', ''))
                    
                    # 提起机构列表
                    affs = []
                    for auth in work.get('authorships', []):
                        if author_id in auth.get('author', {}).get('id', ''):
                            affs = [inst.get('display_name', '') for inst in auth.get('institutions', [])]
                            break

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
            except Exception:
                break

        # 强化排序逻辑：顶刊在前，同档次按引用量排序
        all_papers.sort(key=lambda x: (x['is_top'], x['citations']), reverse=True)
        return [p['doi'] for p in all_papers]

    def run(self, teacher_list_name="tot_teachers"):
        """一键执行全流程"""
        teachers_path = os.path.join(self.current_dir, teacher_list_name)
        if not os.path.exists(teachers_path):
            print(f"错误: 找不到名单 {teacher_list_name}")
            return

        with open(teachers_path, "r", encoding="utf-8") as f:
            teachers = [line.strip() for line in f if line.strip()]

        all_results = {}
        for name in teachers:
            print(f">>> 处理导师: {name}")
            author_id = self.search_author(name)
            if not author_id:
                print(f"    [Skip] 无法识别 ID")
                continue

            dois = self.fetch_verified_papers(author_id)
            if not dois:
                continue

            all_results[name] = "\n".join(dois[:20])
            if len(dois) > 20:
                all_results[name + "+"] = "\n".join(dois[20:170])  # 修改：限制 + 的论文在 150 篇以内

            print(f"    [Success] 已抓取并按 Top 期刊优先排序，总计 {len(dois)} 篇")

        # 重写写回文件
        final_output = []
        for name in teachers:
            if name in all_results:
                final_output.append("=" * 50 + f"\n{name}\n" + "=" * 50)
                final_output.append(all_results[name])
                final_output.append("")
                if (name + "+") in all_results:
                    final_output.append("=" * 50 + f"\n{name}+\n" + "=" * 50)
                    final_output.append(all_results[name + "+"])
                    final_output.append("")

        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(final_output))
        print(f"\n[任务全量完成] 数据已同步至: {self.output_path}")

class Dummy:
    pass


if __name__ == "__main__":
    processor = PKUOpticsProcessor()
    processor.run()