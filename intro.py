#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:56:28 2019

@author: huihui
"""

import math

r = input('请输入圆的半径： ')

def area(r):
    try:
        area = int(r) ** 2 * math.pi
        
    except ValueError:
        print('请输入整数数值作为半径')
        exit()
    
    print('圆的面积等于 {:.2f}'.format(area))
    
if __name__ == '__main__':
    area(r)