
import os
import json
import random
from datetime import datetime


def ensure_dir(path: str):
    """确保目录存在，不存在则创建"""
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def load_json(file_path: str):
    """加载 JSON 文件"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load {file_path}: {e}")
        return None


def save_json(data, file_path: str, indent: int = 2):
    """保存 JSON 文件"""
    ensure_dir(os.path.dirname(file_path))
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
    print(f"[INFO] Saved: {file_path}")


def get_timestamp():
    """获取当前时间戳字符串"""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def random_filename(prefix="file", ext=".txt"):
    """生成随机文件名"""
    return f"{prefix}_{get_timestamp()}_{random.randint(1000,9999)}{ext}"

if __name__ == "__main__":
    print("当前时间:", get_timestamp())
    print("随机文件名:", random_filename("demo", ".json"))
