#Assignment 2
#Topic: 
#Description: Program displaying information about the given figure
#D.O.S: 26/06/2019

import math
print('\t\t\t\t DIMENSIONS OF AN ANNULUS')
outer_radius=float(input("Enter the outer radius of the annulus (in cm):  "))
inner_radius=float(input("Enter the inner radius of the annulus (in cm):  "))
width=outer_radius-inner_radius
avg_radius=(inner_radius+outer_radius)/2
pi=math.pi
area=pi*((outer_radius**2) - (inner_radius**2))
print("\nThe width of the annulus is",width,'cm')
print("\nThe area of the annulus is",area,'sq.cm')
print("\nThe average radius of the annulus is",avg_radius,'cm')



#Topic: To find the LSA and TSA of the hemisphere
#Description: Program displaying information of the given figure
#D.O.S: 26/06/2019

import math
print('\n\n\t\t\t\tDIMENSIONS OF A HEMISPHERE')
radius=float(input("Enter the radius of the hemisphere (in cm):  "))
pi=math.pi
lsa=2*pi*radius**2
tsa=3*pi*radius**2
print("\nThe lateral suraface area of the hemisphere is",lsa,'sq.cm')
print("\nThe total surface area of the hemisphere is",tsa,'sq.cm')