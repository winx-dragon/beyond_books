"""
Assignment 3
Topic: Arithmetic Binary Operations
Description: Program to add 2 English distances
D.O.S: 02/07/2019
"""
print("\n\tADDING 2 ENGLISH DISTANCES")
y1=int(input('Enter the number of yards : '))
f1=int(input('Enter the number of feet : '))
i1=int(input('Enter the number of inches : '))
y2=int(input('Enter another number of yards to be added: '))
f2=int(input('Enter another number of feet to be added: '))
i2=int(input('Enter another number of inches to be added: '))
ti=(i1+i2)%12
remaini=(i1+i2)//12
tfeet=(f1+f2+remaini)%3
remainf=(f1+f2+remaini)//3
tyard=y1+y2+remainf
print("\n\t",y1,"yards",f1,"\'",i1,"\"") 
print("\n\t+",y2,"yards",f2,"\'",i2) 
print("\t_________________\n\t=",tyard,"yards",tfeet,"\'",ti,"\"")
print("\nThe total distance is",tyard,"yards",tfeet,"\'",ti,"\"")