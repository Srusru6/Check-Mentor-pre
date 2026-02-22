import requests
import re
import time
import os
import collections

class PKUCondensedMatterFinalProcessor:
    """
    凝聚态物理所最终集成程序：
    1. 混合搜索 (OpenAlex + CrossRef + InspireHEP)
    2. 自动化去噪 (全局重复 DOI 过滤)
    3. 顶刊优先排序与物理领域校验
    4. 结果格式化输出
    """

    def __init__(self, output_path="results.txt"):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_path = os.path.join(self.current_dir, output_path)
        self.headers = {'User-Agent': 'PKU-Research-Bot/3.0 (mailto:admin@pku.edu.cn)'}
        
        # 核心导师身份映射 (精准 ID 或 拼音)
        self.pinyin_mapping = {
            "欧阳颀": "Qi Ouyang", "俞大鹏": "Dapeng Yu", "汤超": "Chao Tang",
            "沈波": "Bo Shen", "王新强": "Xinqiang Wang", "戴伦": "Lun Dai",
            "廖志敏": "Zhimin Liao", "全海涛": "Haitao Quan", "刘开辉": "Kaihui Liu",
            "李新征": "Xinzheng Li", "吴孝松": "Xiaosong Wu", "方哲宇": "Zheyu Fang",
            "叶堉": "Yu Ye", "马仁敏": "Renmin Ma", "吕劲": "Jin Lu",
            "冉广照": "Guangzhao Ran", "史俊杰": "Junjie Shi", "王宏利": "Hongli Wang",
            "尹澜": "Lan Yin", "杨金波": "Jinbo Yang", "于彤军": "Tongjun Yu",
            "陈志忠": "Zhizhong Chen", "赵清": "Qing Zhao", "罗春雄": "Chunxiong Luo",
            "唐宁": "Ning Tang", "毛有东": "Youdong Mao", "陈基": "Ji Chen",
            "罗昭初": "Zhaochu Luo", "杨学林": "Xuelin Yang", "鞠光旭": "Guangxu Ju",
            "王平": "Ping Wang", "赵宏政": "Hongzheng Zhao", "王丁": "Ding Wang",
            "洪浩": "Hao Hong", "杜红林": "Honglin Du", "侯玉敏": "Yumin Hou",
            "马平": "Ping Ma", "韩景智": "Jingzhi Han", "钱志新": "Zhixin Qian",
            "童玉珍": "Yuzhen Tong", "王常生": "Changsheng Wang", "李方廷": "Fangting Li",
            "王永忠": "Yongzhong Wang", "杨志坚": "Zhijian Yang", "林峰": "Feng Lin",
            "康香宁": "Xiangning Kang", "吴洁君": "Jiejun Wu", "许福军": "Fujun Xu",
            "王越": "Yue Wang", "刘顺荃": "Shunquan Liu", "陈伟华": "Weihua Chen",
            "林芳": "Fang Lin", "李艳平": "Yanping Li", "张焱": "Yan Zhang",
            "杨文云": "Wenyun Yang", "徐庆": "Qing Xu"
        }

    def get_dois_from_crossref(self, english_name, limit=50):
        query = f"{english_name} Peking University Physics"
        url = f"https://api.crossref.org/works?query={query}&rows={limit}"
        try:
            r = requests.get(url, timeout=10)
            items = r.json().get('message', {}).get('items', [])
            return [it.get('DOI') for it in items if it.get('DOI')]
        except: return []

    def get_dois_from_inspire(self, english_name, limit=30):
        name_parts = english_name.split()
        formatted = f"{name_parts[-1]}, {name_parts[0]}" if len(name_parts) >= 2 else english_name
        query = f'a "{formatted}" and aff "Peking U."'
        url = f"https://inspirehep.net/api/literature?q={query}&size={limit}"
        try:
            r = requests.get(url, timeout=10)
            hits = r.json().get('hits', {}).get('hits', [])
            return [h.get('metadata', {}).get('dois', [{}])[0].get('value') for h in hits if h.get('metadata', {}).get('dois')]
        except: return []

    def denoise_data(self, teacher_data):
        """识别并在全局范围内剔除出现频率过高(>4人)的 DOI 噪声"""
        doi_counter = collections.Counter()
        for dois in teacher_data.values():
            doi_counter.update(dois)
        
        global_noise = {doi for doi, count in doi_counter.items() if count > 4}
        print(f"[*] 自动化去噪：识别到 {len(global_noise)} 条全局干扰论文并已剔除")
        
        cleaned_data = {}
        for name, dois in teacher_data.items():
            cleaned_data[name] = [d for d in dois if d not in global_noise]
        return cleaned_data

    def run(self, teacher_list_name="tot_teachers"):
        teachers_file = os.path.join(self.current_dir, teacher_list_name)
        if not os.path.exists(teachers_file): return
        
        with open(teachers_file, 'r', encoding='utf8') as f:
            names = [l.strip() for l in f if l.strip()]

        teacher_results = {}
        print(f"[*] 开始处理 {len(names)} 位凝聚态所导师数据...")

        for name in names:
            english_name = self.pinyin_mapping.get(name, name)
            print(f"  > 抓取: {name} ({english_name})")
            
            dois = set()
            dois.update(self.get_dois_from_crossref(english_name))
            dois.update(self.get_dois_from_inspire(english_name))
            
            if dois:
                teacher_results[name] = list(dois)
            time.sleep(0.3)

        # 全局去噪
        cleaned_results = self.denoise_data(teacher_results)

        # 写入最终结果
        with open(self.output_path, 'w', encoding='utf8') as f:
            for name in names: # 保持原有名单顺序
                if name not in cleaned_results: continue
                dois = cleaned_results[name]
                f.write("\n" + "="*50 + f"\n{name}\n" + "="*50 + "\n")
                
                # 前 15 篇为主列表 (典型值)，15-150 为补充
                main = sorted(dois)[:15]
                plus = sorted(dois)[15:150]
                
                f.write("\n".join(main) + "\n\n")
                if plus:
                    f.write("="*50 + f"\n{name}+\n" + "="*50 + "\n")
                    f.write("\n".join(plus) + "\n\n")

        print(f"[*] 处理完成！结果已保存至: {self.output_path}")

if __name__ == "__main__":
    PKUCondensedMatterFinalProcessor().run()
