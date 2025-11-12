"""
该模块为 CheckMentor 项目提供了一个简单的集成点。
"""
from .client import InspireHEPClient
from .downloader import download_record

def search_and_download_author_papers(author_name: str, output_dir: str = ".", num_papers: int = 1):
    """
    搜索给定作者的论文并下载指定数量的论文。

    :param author_name: 作者姓名，格式为 "姓, 名" 或 "名 姓"。
    :param output_dir: 保存下载文件的目录。
    :param num_papers: 要下载的论文数量。
    :return: 一个包含已下载文件路径的字典列表。
    """
    client = InspireHEPClient()
    
    # 尝试不同的作者姓名格式
    queries = [
        f"find a {author_name}",
        f"author:{author_name}"
    ]
    
    search_results = None
    for query in queries:
        try:
            print(f"正在尝试搜索: {query}")
            results = client.search_literature(query, size=num_papers)
            if results.get("hits", {}).get("hits"):
                search_results = results
                print("搜索成功。")
                break
        except Exception as e:
            print(f"使用查询 '{query}' 搜索时出错: {e}")
            continue
            
    if not search_results:
        print(f"找不到作者 '{author_name}' 的任何论文。")
        return []

    downloaded_files = []
    for hit in search_results["hits"]["hits"]:
        record_id = hit["id"]
        print(f"正在下载记录 {record_id}...")
        try:
            download_info = download_record(record_id, output_dir=output_dir)
            downloaded_files.append(download_info)
            print(f"成功下载记录 {record_id}。")
        except Exception as e:
            print(f"下载记录 {record_id} 时出错: {e}")
    
    return downloaded_files

