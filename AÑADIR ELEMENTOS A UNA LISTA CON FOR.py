# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:00:19 2023

@author: Christian
"""
LISTAR=[]
lista=["R1","R2","R3","S1","S2","S3","AP1","FW1"]
r=input("INGRESE QUE EQUIPO DESEA AÑADIR: R,S,AP,FW ")

for i in lista:
    if r == "R"in i:
         
        LISTAR.append(i)
        print(LISTAR)
    elif r== "S" in i:
        LISTAR.append(i)
        print(LISTAR)
    elif r== "AP" in i:
        LISTAR.append(i)
        print(LISTAR)
    elif r== "FW" in i:
        LISTAR.append(i)
        print(LISTAR)
      