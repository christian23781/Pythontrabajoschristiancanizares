# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:15:02 2023

@author: Christian
"""

n=int(input("ingrese un número:"))
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
for x in range(n):
    print(fibo(x))