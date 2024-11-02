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

def calculate_statistics():
    """计算总支出和总收入."""
    records = load_records()
    
    total_income = 0
    total_expense = 0
    income_categories = {}
    expense_categories = {}

    for record in records:
        amount = record['amount']
        category = record['category']

        # 假设正数为收入，负数为支出
        if amount > 0:
            total_income += amount
            if category in income_categories:
                income_categories[category] += amount
            else:
                income_categories[category] = amount
        else:
            total_expense += abs(amount)
            if category in expense_categories:
                expense_categories[category] += abs(amount)
            else:
                expense_categories[category] = abs(amount)

    return total_income, total_expense, income_categories, expense_categories
