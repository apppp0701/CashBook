import json
import matplotlib.pyplot as plt

# 从 data/records.json 文件中加载数据
def load_records():
    with open('data/records.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 显示收入和支出的图表
def display_income_expense_chart():
    records = load_records()
    
    # 初始化收入和支出总额
    total_income = 0
    total_expense = 0
    
    # 计算收入和支出总额
    for record in records:
        amount = float(record['amount'])
        if amount >= 0:
            total_income += amount
        else:
            total_expense += abs(amount)
    
    # 绘制柱状图
    categories = ['收入', '支出']
    values = [total_income, total_expense]
    
    plt.figure(figsize=(6, 4))
    plt.bar(categories, values, color=['green', 'red'])
    plt.title('收入和支出概览')
    plt.xlabel('类别')
    plt.ylabel('金额')
    plt.show()
