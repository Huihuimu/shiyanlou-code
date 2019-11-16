# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


## 定义下面的变量

# 原始收入，获取用户输入，转换为 int
income = int(input('Please add your salary: '))

# 税后收入
salary = 0  

# 应纳税所得额
shouldPay = 0

# 纳税金额
tax = 0 

def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""

    # 应纳税所得额为收入减5000
    shouldPay = num - 5000

    # 用条件判断语句，根据扣税表写出不同薪资的扣税公式
    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    # 下面的请你补充
    elif 3000 < shouldPay <= 12000:
        tax = shouldPay * 0.10 - 210
    elif 12000 < shouldPay <= 25000:
        tax = shouldPay * 0.20 - 1410
    elif 25000 < shouldPay <= 35000:
        tax = shouldPay * 0.25 - 2660
    elif 35000 < shouldPay <= 55000:
        tax = shouldPay * 0.30 - 4410
    elif 55000 < shouldPay <= 80000:
        tax = shouldPay * 0.35 - 7160
    elif 80000 < shouldPay:
        tax = shouldPay * 0.45 - 15160
        
    # 最终收入为税前收入减去税款，并保留两位小数
    salary = income - tax
    # 返回最终收入
    return '{:.2f}'.format(salary)

# 打印
print('你的税后收入是：{}'.format(calculator(income)))
