# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:26:35 2019

@author: comp
"""
print("Series")

op=int(input('Which series would you like?(1/2)'))
if op==1:
    
    
if op==2:
    spaces=40
    n=int(input("Enter the number of lines:"))
    for i in range(1,n+1):
        for sp in range(1,spaces+1):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end=" ")
        for k in range(i-1,0,-1):
            print(k,end=" ")
        print()
        spaces-=2
