# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:48:56 2023

@author: Christian
"""

acl=int(input("ingrese el # ACL"))
if acl >=1 and acl <=99:
    print("la ACL es standar")
elif acl >=100 and acl <=199:
    print("la ACL es extendida")
else:
    print("el # ingresado no es de un ACL")
    