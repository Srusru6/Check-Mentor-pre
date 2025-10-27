"""
论文元数据管理模块

该模块负责处理论文的元数据，包括：
- DOI (论文唯一标识符)
- 作者列表
- 发布时间
- 青年学者索引 (第一位青年学者在作者列表中的位置)

元数据的应用包括：
- 按发布时间对论文进行排序和加权
- 识别青年学者的贡献
- 提供更准确的论文信息
"""
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path


class PaperMetadata:
    """论文元数据类"""
    
    def __init__(
        self,
        doi: str = "",
        authors: List[str] = None,
        publish_date: str = "",
        young_scholar_index: int = -1
    ):
        """
        初始化论文元数据
        
        Args:
            doi: 论文的DOI标识符
            authors: 作者列表
            publish_date: 发布时间 (ISO格式字符串, 如 "2024-01-15")
            young_scholar_index: 第一位青年学者在作者列表中的索引，-1表示无青年学者
        """
        self.doi = doi
        self.authors = authors if authors is not None else []
        self.publish_date = publish_date
        self.young_scholar_index = young_scholar_index
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "doi": self.doi,
            "authors": self.authors,
            "publish_date": self.publish_date,
            "young_scholar_index": self.young_scholar_index
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaperMetadata':
        """从字典创建元数据对象"""
        return cls(
            doi=data.get("doi", ""),
            authors=data.get("authors", []),
            publish_date=data.get("publish_date", ""),
            young_scholar_index=data.get("young_scholar_index", -1)
        )
    
    def get_publish_year(self) -> Optional[int]:
        """
        获取发布年份
        
        Returns:
            发布年份，如果日期无效则返回 None
        """
        if not self.publish_date:
            return None
        try:
            return datetime.fromisoformat(self.publish_date).year
        except (ValueError, AttributeError):
            return None
    
    def has_young_scholar(self) -> bool:
        """检查是否有青年学者参与"""
        return self.young_scholar_index >= 0
    
    def get_young_scholar_name(self) -> Optional[str]:
        """
        获取青年学者姓名
        
        Returns:
            青年学者姓名，如果没有则返回 None
        """
        if self.has_young_scholar() and self.young_scholar_index < len(self.authors):
            return self.authors[self.young_scholar_index]
        return None
    
    def get_recency_score(self, reference_year: Optional[int] = None) -> float:
        """
        计算论文的时效性得分 (0.0 - 1.0)
        
        更新的论文得分更高。使用指数衰减函数。
        
        Args:
            reference_year: 参考年份，默认为当前年份
            
        Returns:
            时效性得分，范围 [0.0, 1.0]
        """
        publish_year = self.get_publish_year()
        if publish_year is None:
            return 0.5  # 如果没有日期信息，返回中性得分
        
        if reference_year is None:
            reference_year = datetime.now().year
        
        # 计算论文年龄
        age = reference_year - publish_year
        
        # 使用指数衰减：半衰期为5年
        # score = 0.5^(age/5)
        # 这样：当前年份=1.0, 5年前≈0.5, 10年前≈0.25
        if age < 0:
            return 1.0  # 未来的日期（数据错误）
        
        half_life = 5.0
        score = 0.5 ** (age / half_life)
        
        return min(max(score, 0.0), 1.0)  # 限制在 [0, 1] 范围内


class MetadataManager:
    """元数据管理器"""
    
    def __init__(self):
        """初始化元数据管理器"""
        self.metadata_cache: Dict[str, PaperMetadata] = {}
    
    def load_metadata_file(self, metadata_file: Path) -> bool:
        """
        从JSON文件加载元数据
        
        Args:
            metadata_file: 元数据JSON文件路径
            
        Returns:
            加载是否成功
        """
        if not metadata_file.exists():
            print(f"    ℹ️  元数据文件不存在: {metadata_file}")
            return False
        
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 假设元数据文件格式为:
            # {
            #   "paper_filename_1.md": {
            #     "doi": "...",
            #     "authors": [...],
            #     "publish_date": "...",
            #     "young_scholar_index": ...
            #   },
            #   ...
            # }
            
            for filename, metadata_dict in data.items():
                metadata = PaperMetadata.from_dict(metadata_dict)
                self.metadata_cache[filename] = metadata
            
            print(f"    ✓ 已加载 {len(self.metadata_cache)} 条元数据记录")
            return True
            
        except Exception as e:
            print(f"    ⚠️  加载元数据文件失败: {e}")
            return False
    
    def get_metadata(self, paper_filename: str) -> Optional[PaperMetadata]:
        """
        获取指定论文的元数据
        
        Args:
            paper_filename: 论文文件名（含扩展名）
            
        Returns:
            元数据对象，如果不存在则返回 None
        """
        # 尝试完整文件名
        if paper_filename in self.metadata_cache:
            return self.metadata_cache[paper_filename]
        
        # 尝试只用文件名（不含路径）
        filename_only = Path(paper_filename).name
        if filename_only in self.metadata_cache:
            return self.metadata_cache[filename_only]
        
        return None
    
    def add_metadata(self, paper_filename: str, metadata: PaperMetadata):
        """
        添加或更新论文元数据
        
        Args:
            paper_filename: 论文文件名
            metadata: 元数据对象
        """
        self.metadata_cache[paper_filename] = metadata
    
    def sort_papers_by_recency(
        self,
        papers: List[Dict[str, Any]],
        descending: bool = True
    ) -> List[Dict[str, Any]]:
        """
        按发布时间对论文列表进行排序
        
        Args:
            papers: 论文列表
            descending: True表示从新到旧，False表示从旧到新
            
        Returns:
            排序后的论文列表
        """
        def get_sort_key(paper: Dict[str, Any]) -> tuple:
            """
            生成排序键
            
            Returns:
                (年份, 原始索引) - 没有元数据的论文会被放在最后
            """
            filename = Path(paper.get('md_filename', '')).name
            metadata = self.get_metadata(filename)
            
            if metadata:
                year = metadata.get_publish_year()
                if year is not None:
                    return (year, 0)
            
            # 没有元数据的论文使用一个很小/很大的年份
            return (-9999 if descending else 9999, 1)
        
        sorted_papers = sorted(
            papers,
            key=get_sort_key,
            reverse=descending
        )
        
        return sorted_papers
    
    def get_papers_with_metadata(
        self,
        papers: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        为论文列表添加元数据信息
        
        Args:
            papers: 原始论文列表
            
        Returns:
            添加了元数据字段的论文列表
        """
        enriched_papers = []
        
        for paper in papers:
            # 创建副本以避免修改原始数据
            enriched_paper = paper.copy()
            
            filename = Path(paper.get('md_filename', '')).name
            metadata = self.get_metadata(filename)
            
            if metadata:
                enriched_paper['metadata'] = metadata.to_dict()
                enriched_paper['recency_score'] = metadata.get_recency_score()
            else:
                enriched_paper['metadata'] = None
                enriched_paper['recency_score'] = 0.5  # 默认中性得分
            
            enriched_papers.append(enriched_paper)
        
        return enriched_papers
    
    def export_metadata(self, output_file: Path):
        """
        导出元数据到JSON文件
        
        Args:
            output_file: 输出文件路径
        """
        data = {
            filename: metadata.to_dict()
            for filename, metadata in self.metadata_cache.items()
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"    ✓ 元数据已导出到: {output_file}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        获取元数据统计信息
        
        Returns:
            统计信息字典
        """
        total = len(self.metadata_cache)
        with_dates = sum(1 for m in self.metadata_cache.values() if m.publish_date)
        with_young_scholars = sum(1 for m in self.metadata_cache.values() if m.has_young_scholar())
        
        years = [m.get_publish_year() for m in self.metadata_cache.values()]
        valid_years = [y for y in years if y is not None]
        
        stats = {
            "total_papers": total,
            "papers_with_dates": with_dates,
            "papers_with_young_scholars": with_young_scholars,
            "year_range": (min(valid_years), max(valid_years)) if valid_years else None,
            "avg_recency_score": sum(m.get_recency_score() for m in self.metadata_cache.values()) / total if total > 0 else 0
        }
        
        return stats
    
    def print_statistics(self):
        """打印元数据统计信息"""
        stats = self.get_statistics()
        
        print("\n📊 元数据统计:")
        print(f"  - 总论文数: {stats['total_papers']}")
        print(f"  - 有日期信息: {stats['papers_with_dates']}/{stats['total_papers']}")
        print(f"  - 有青年学者: {stats['papers_with_young_scholars']}/{stats['total_papers']}")
        
        if stats['year_range']:
            print(f"  - 年份范围: {stats['year_range'][0]} - {stats['year_range'][1]}")
        
        print(f"  - 平均时效性得分: {stats['avg_recency_score']:.3f}")
