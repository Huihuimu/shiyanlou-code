# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys


def calculator(salary_orig):
    """计算税后薪资的函数，参数为原始收入"""
    start_point = 5000
    # 应纳税所得额为收入减5000
    social_security_rate = 0.08 + 0.02 + 0.005 + 0.06 
    
    shouldPay = salary_orig (1 - social_security_rate ) - start_point

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
    salary = salary_orig(1 - social_security_rate) - tax
    # 返回最终收入
    return '{:.2f}'.format(salary)

def calculate():
    """
    对命令行传入的每一个用户，依次调用计算器计算纳税额
    """
    for item in sys.argv[1:]:
        id, salary_orig = item.split(':')
        try:
            salary_orig = int(salary_orig)
        except ValueError:
            print('请在薪资的位置输入数字')
            continue
            
        print('{}:{}'.format(id,calculator(salary_orig)))

if __name__ == '__main__':
    main()

