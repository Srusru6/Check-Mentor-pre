"""
数据管理模块
处理论文数据的存储和检索
"""
import json
from typing import Dict, Any, List, Optional
from datetime import datetime

from . import config


class DataManager:
    """数据管理器，负责读写 JSON 文件"""
    
    def __init__(self, data_file: str = "research_data.json"):
        """
        初始化数据管理器
        
        Args:
            data_file: 数据文件名
        """
        self.data_file = config.OUTPUT_DIR / data_file
        self.data = self._load_or_create()
    
    def _load_or_create(self) -> Dict[str, Any]:
        """加载现有数据或创建新数据结构"""
        if self.data_file.exists():
            print(f"📖 Loading existing data from: {self.data_file}")
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"📝 Creating new data structure")
            return self._create_empty_structure()
    
    def _create_empty_structure(self) -> Dict[str, Any]:
        """创建空的数据结构"""
        return {
            "metadata": {
                "project_version": config.PROJECT_VERSION,
                "created_date": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "total_papers": 0,
                "analysis_model": config.LLM_MODEL,
                "embedding_model": config.EMBEDDING_MODEL,
                "data_sources": []
            },
            "professor_info": {},
            "papers": [],
            "analysis_results": {},
            "correlation_data": {},
            "report_cache": {}
        }
    
    def save(self):
        """保存数据到文件"""
        # 更新时间戳
        self.data["metadata"]["last_updated"] = datetime.now().isoformat()
        self.data["metadata"]["total_papers"] = len(self.data["papers"])
        
        print(f"💾 Saving data to: {self.data_file}")
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print(f"✓ Data saved successfully")
    
    def set_professor_info(self, name: str, **kwargs):
        """
        设置教授信息
        
        Args:
            name: 教授姓名
            **kwargs: 其他信息（如 department, university等）
        """
        self.data["professor_info"] = {
            "name": name,
            **kwargs
        }
    
    def add_paper(self, paper_info: Dict[str, Any]):
        """
        添加论文信息
        
        Args:
            paper_info: 论文信息字典
        """
        # 检查是否已存在
        paper_id = paper_info['id']
        existing_ids = [p['id'] for p in self.data["papers"]]
        
        if paper_id in existing_ids:
            # 更新现有论文
            for i, p in enumerate(self.data["papers"]):
                if p['id'] == paper_id:
                    self.data["papers"][i] = paper_info
                    break
        else:
            # 添加新论文
            self.data["papers"].append(paper_info)
    
    def add_paper_summary(self, paper_id: str, summary: Dict[str, Any]):
        """
        添加论文总结
        
        Args:
            paper_id: 论文 ID
            summary: 总结内容
        """
        for paper in self.data["papers"]:
            if paper['id'] == paper_id:
                paper['summary'] = summary
                break
    
    def add_analysis_result(self, paper_id: str, analysis: Dict[str, Any]):
        """
        添加论文分析结果
        
        Args:
            paper_id: 论文 ID
            analysis: 分析结果（relevance_analysis格式）
        """
        self.data["analysis_results"][paper_id] = analysis
    
    def get_paper(self, paper_id: str) -> Optional[Dict[str, Any]]:
        """
        获取论文信息
        
        Args:
            paper_id: 论文 ID
            
        Returns:
            论文信息字典，如果不存在则返回 None
        """
        for paper in self.data["papers"]:
            if paper['id'] == paper_id:
                return paper
        return None
    
    def get_analysis_result(self, paper_id: str) -> Optional[Dict[str, Any]]:
        """
        获取论文分析结果
        
        Args:
            paper_id: 论文 ID
            
        Returns:
            分析结果，如果不存在则返回 None
        """
        return self.data["analysis_results"].get(paper_id)
    
    def get_all_papers(self) -> List[Dict[str, Any]]:
        """获取所有论文"""
        return self.data["papers"]
    
    def get_all_analysis_results(self) -> Dict[str, Dict[str, Any]]:
        """获取所有分析结果"""
        return self.data["analysis_results"]
    
    def update_metadata(self, **kwargs):
        """
        更新元数据
        
        Args:
            **kwargs: 要更新的元数据字段
        """
        self.data["metadata"].update(kwargs)
    
    def add_data_source(self, source: str):
        """
        添加数据来源
        
        Args:
            source: 数据来源名称
        """
        if source not in self.data["metadata"]["data_sources"]:
            self.data["metadata"]["data_sources"].append(source)
    
    def export_analysis_summary(self, output_file: str = None) -> str:
        """
        导出分析摘要
        
        Args:
            output_file: 输出文件路径（可选）
            
        Returns:
            摘要文本
        """
        summary_lines = []
        summary_lines.append(f"# {config.PROJECT_NAME} - Analysis Summary")
        summary_lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        summary_lines.append(f"Total Papers: {len(self.data['papers'])}")
        summary_lines.append(f"\n## Papers:\n")
        
        for paper in self.data["papers"]:
            summary_lines.append(f"- [{paper['id']}] {paper.get('title', 'Unknown')}")
            
            # 添加分析结果摘要
            if paper['id'] in self.data["analysis_results"]:
                analysis = self.data["analysis_results"][paper['id']]
                summary_lines.append(f"  Analysis:")
                for key, result in analysis.items():
                    score = result.get('score', 0)
                    summary_lines.append(f"    - {key}: {score:.3f}")
            summary_lines.append("")
        
        summary_text = "\n".join(summary_lines)
        
        if output_file:
            output_path = config.OUTPUT_DIR / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(summary_text)
            print(f"✓ Summary exported to: {output_path}")
        
        return summary_text


# 模块提供 DataManager 类；测试代码已移除以避免导入时副作用
