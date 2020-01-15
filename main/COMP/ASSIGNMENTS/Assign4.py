"""
Assignment 4
Topic: Mathematical functions
Description: To find work done by gravity
D.O.S: 09/07/2019
"""
import math
print("\n\tFINDING WORK DONE BY GRAVITY")
m=int(input('Enter the mass of the object (in kg): '))
h=int(input('Enter the height from the earth\'s surface (in metres): '))
angle=int(input('Enter the angle that the object makes when it falls (in degrees): '))
rad=math.radians(angle)
cosine=math.cos(rad)
work=m*9.8*h*cosine
print("\nThe work done by gravity is", work,'J')

"""
Description: To find period of the pendulam 
"""
print("\n\n\tFINDING PERIOD OF THE PENDULAM")
a=1
while a<=5:
    l=int(input('Enter the length of the pendulam (in cm): '))
    ang=int(input('Enter the angle of deplacement of the pendulam (in degree): '))
    rad=math.radians(ang)
    sine=(math.sin(rad/2))**2
    p=2*math.pi*math.sqrt(l/980)*(1/4*sine+1)
    print("The time period of the pendulam is",p,"s")
    a=a+1
