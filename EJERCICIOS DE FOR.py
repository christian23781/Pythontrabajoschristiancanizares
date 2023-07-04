# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:43:54 2023

@author: Christian
"""

for i in range (1,10+1,1):
    print(i)    
    
lista=["R1","R2","R3","S1","S2","S3","AP1","FW1"]

for i in lista:
    if "R"in i:
        print(i)

print(len(lista))
print(lista[0])
print(lista[1])


for i in lista:
    print(i, end="   ")

  