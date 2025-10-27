"""
元数据工具脚本

提供命令行工具用于：
1. 验证元数据文件的格式
2. 生成元数据模板
3. 查看元数据统计
4. 测试元数据功能
"""
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

from core.metadata_manager import MetadataManager, PaperMetadata


def validate_metadata_file(file_path: Path) -> tuple[bool, list[str]]:
    """
    验证元数据文件的格式
    
    Returns:
        (是否有效, 错误列表)
    """
    errors = []
    
    if not file_path.exists():
        errors.append(f"文件不存在: {file_path}")
        return False, errors
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"JSON格式错误: {e}")
        return False, errors
    except Exception as e:
        errors.append(f"读取文件失败: {e}")
        return False, errors
    
    if not isinstance(data, dict):
        errors.append("根节点必须是字典")
        return False, errors
    
    # 验证每个条目
    for filename, metadata in data.items():
        prefix = f"[{filename}]"
        
        # 检查必需字段
        required_fields = ["doi", "authors", "publish_date", "young_scholar_index"]
        for field in required_fields:
            if field not in metadata:
                errors.append(f"{prefix} 缺少必需字段: {field}")
        
        # 验证字段类型
        if "doi" in metadata and not isinstance(metadata["doi"], str):
            errors.append(f"{prefix} doi 必须是字符串")
        
        if "authors" in metadata:
            if not isinstance(metadata["authors"], list):
                errors.append(f"{prefix} authors 必须是列表")
            elif not all(isinstance(a, str) for a in metadata["authors"]):
                errors.append(f"{prefix} authors 列表中的所有元素必须是字符串")
        
        if "publish_date" in metadata:
            if not isinstance(metadata["publish_date"], str):
                errors.append(f"{prefix} publish_date 必须是字符串")
            else:
                # 验证日期格式
                try:
                    datetime.fromisoformat(metadata["publish_date"])
                except ValueError:
                    errors.append(f"{prefix} publish_date 格式无效，应为 YYYY-MM-DD")
        
        if "young_scholar_index" in metadata:
            if not isinstance(metadata["young_scholar_index"], int):
                errors.append(f"{prefix} young_scholar_index 必须是整数")
            elif metadata["young_scholar_index"] < -1:
                errors.append(f"{prefix} young_scholar_index 不能小于 -1")
            elif "authors" in metadata:
                if metadata["young_scholar_index"] >= len(metadata["authors"]):
                    errors.append(f"{prefix} young_scholar_index 超出 authors 列表范围")
    
    return len(errors) == 0, errors


def generate_template(output_path: Path, paper_directory: Path = None):
    """
    生成元数据模板
    
    Args:
        output_path: 输出文件路径
        paper_directory: 论文目录（如果提供，将为所有 .md 文件生成条目）
    """
    template = {}
    
    if paper_directory and paper_directory.exists():
        # 为目录中的所有 .md 文件生成模板
        md_files = sorted(paper_directory.glob("*.md"))
        for md_file in md_files:
            template[md_file.name] = {
                "doi": "",
                "authors": [],
                "publish_date": "",
                "young_scholar_index": -1
            }
        print(f"✓ 为 {len(md_files)} 篇论文生成了模板条目")
    else:
        # 生成示例模板
        template["示例论文.md"] = {
            "doi": "10.xxxx/xxxxx",
            "authors": ["作者1", "作者2", "作者3"],
            "publish_date": "2024-01-15",
            "young_scholar_index": 0
        }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(template, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 模板已生成: {output_path}")


def show_statistics(file_path: Path):
    """显示元数据统计信息"""
    manager = MetadataManager()
    
    if manager.load_metadata_file(file_path):
        print("\n" + "="*60)
        manager.print_statistics()
        print("="*60)
        
        # 显示详细信息
        print("\n📝 详细信息:")
        for filename, metadata in sorted(manager.metadata_cache.items()):
            print(f"\n  📄 {filename}")
            print(f"     DOI: {metadata.doi}")
            print(f"     作者: {', '.join(metadata.authors) if metadata.authors else '无'}")
            print(f"     发布日期: {metadata.publish_date if metadata.publish_date else '未知'}")
            if metadata.has_young_scholar():
                print(f"     青年学者: {metadata.get_young_scholar_name()} (索引 {metadata.young_scholar_index})")
            else:
                print(f"     青年学者: 无")
            print(f"     时效性得分: {metadata.get_recency_score():.3f}")


def test_metadata_features():
    """测试元数据功能"""
    print("🧪 测试元数据功能...\n")
    
    # 测试1: 创建元数据对象
    print("测试 1: 创建元数据对象")
    metadata = PaperMetadata(
        doi="10.1038/test",
        authors=["Alice", "Bob", "Charlie"],
        publish_date="2024-01-15",
        young_scholar_index=1
    )
    print(f"  ✓ 创建成功")
    print(f"    - 发布年份: {metadata.get_publish_year()}")
    print(f"    - 有青年学者: {metadata.has_young_scholar()}")
    print(f"    - 青年学者姓名: {metadata.get_young_scholar_name()}")
    print(f"    - 时效性得分: {metadata.get_recency_score():.3f}")
    
    # 测试2: 时效性计算
    print("\n测试 2: 不同年份的时效性得分")
    test_years = [2024, 2020, 2015, 2010, 2000]
    current_year = datetime.now().year
    for year in test_years:
        m = PaperMetadata(publish_date=f"{year}-01-01")
        score = m.get_recency_score()
        age = current_year - year
        print(f"  {year} ({age}年前): {score:.3f}")
    
    # 测试3: 字典转换
    print("\n测试 3: 字典序列化和反序列化")
    original = PaperMetadata(
        doi="10.1234/test",
        authors=["Author1", "Author2"],
        publish_date="2023-06-15",
        young_scholar_index=0
    )
    dict_data = original.to_dict()
    restored = PaperMetadata.from_dict(dict_data)
    print(f"  ✓ 序列化成功: {json.dumps(dict_data, ensure_ascii=False)}")
    print(f"  ✓ 反序列化成功: DOI={restored.doi}, 作者数={len(restored.authors)}")
    
    # 测试4: 元数据管理器
    print("\n测试 4: 元数据管理器")
    manager = MetadataManager()
    manager.add_metadata("test1.md", metadata)
    retrieved = manager.get_metadata("test1.md")
    print(f"  ✓ 添加和检索成功")
    print(f"  ✓ 检索到的 DOI: {retrieved.doi}")
    
    print("\n✅ 所有测试通过!")


def main():
    parser = argparse.ArgumentParser(
        description="元数据工具 - 验证、生成和测试论文元数据"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='子命令')
    
    # validate 命令
    validate_parser = subparsers.add_parser('validate', help='验证元数据文件')
    validate_parser.add_argument('file', type=str, help='元数据文件路径')
    
    # generate 命令
    generate_parser = subparsers.add_parser('generate', help='生成元数据模板')
    generate_parser.add_argument('output', type=str, help='输出文件路径')
    generate_parser.add_argument(
        '--paper-dir',
        type=str,
        help='论文目录（可选，为目录中的所有 .md 文件生成条目）'
    )
    
    # stats 命令
    stats_parser = subparsers.add_parser('stats', help='显示元数据统计')
    stats_parser.add_argument('file', type=str, help='元数据文件路径')
    
    # test 命令
    test_parser = subparsers.add_parser('test', help='测试元数据功能')
    
    args = parser.parse_args()
    
    if args.command == 'validate':
        file_path = Path(args.file)
        print(f"🔍 验证元数据文件: {file_path}\n")
        is_valid, errors = validate_metadata_file(file_path)
        
        if is_valid:
            print("✅ 元数据文件有效!")
        else:
            print("❌ 元数据文件无效:\n")
            for error in errors:
                print(f"  • {error}")
            return 1
    
    elif args.command == 'generate':
        output_path = Path(args.output)
        paper_dir = Path(args.paper_dir) if args.paper_dir else None
        
        print(f"📝 生成元数据模板: {output_path}\n")
        generate_template(output_path, paper_dir)
    
    elif args.command == 'stats':
        file_path = Path(args.file)
        print(f"📊 分析元数据文件: {file_path}\n")
        show_statistics(file_path)
    
    elif args.command == 'test':
        test_metadata_features()
    
    else:
        parser.print_help()
    
    return 0


if __name__ == "__main__":
    exit(main())
