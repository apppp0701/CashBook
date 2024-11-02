import json
import os

# 定义数据文件的名称
DATA_FILE = 'data/records.json'

def load_records():
    """加载已有记录."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_records(records):
    """保存记录到 JSON 文件."""
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(records, file, ensure_ascii=False, indent=4)

def add_record(date, amount, category, note):
    """添加一条新的记账记录."""
    records = load_records()
    
    # 创建新的记录
    new_record = {
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    }
    
    # 将新记录添加到列表
    records.append(new_record)
    
    # 保存所有记录
    save_records(records)
