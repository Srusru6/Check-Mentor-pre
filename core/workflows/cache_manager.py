"""
缓存管理模块
"""
import json
import os
from typing import Dict, Any, Optional

from .. import config

class CacheManager:
    """
    一个简单的基于 JSON 文件的缓存管理器。
    """
    def __init__(self, professor_name: str, workflow_name: str):
        """
        初始化缓存管理器。

        Args:
            professor_name (str): 教授姓名，用于构建缓存文件名。
            workflow_name (str): 工作流名称，用于构建缓存文件名。
        """
        cache_filename = f"{professor_name}_{workflow_name}_cache.json"
        self.cache_path = config.CACHE_DIR / cache_filename
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict[str, Any]:
        """加载缓存文件，如果不存在则创建一个空的缓存。"""
        if self.cache_path.exists():
            try:
                with open(self.cache_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                # 如果文件损坏或为空，则返回空字典
                return {}
        return {}

    def _save_cache(self):
        """将当前缓存数据写入文件。"""
        with open(self.cache_path, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)

    def get(self, key: str) -> Optional[Any]:
        """
        从缓存中获取一个值。

        Args:
            key (str): 要获取的数据的键（通常是 paper_id）。

        Returns:
            Optional[Any]: 缓存的数据，如果不存在则返回 None。
        """
        return self.cache.get(key)

    def set(self, key: str, value: Any):
        """
        向缓存中设置一个值，并立即保存到文件。

        Args:
            key (str): 要设置的数据的键。
            value (Any): 要设置的数据的值。
        """
        self.cache[key] = value
        self._save_cache()
