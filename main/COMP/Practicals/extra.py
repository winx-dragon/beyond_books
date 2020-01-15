# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:20:37 2019

@author: comp
"""
import math
n=int(input("Enter a number:"))
Factor=2
if n==1:
        print("Neither p nor comp")
else:
    while Factor<=math.sqrt(n):
        if n%Factor==0 :
            print("not")
            break
        Factor+=1
    else:
            print(n," is a Prime")