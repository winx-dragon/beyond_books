n=int(input("enter the limit:"))
x=int(input("Enter the angle?"))
Sum=0
for i in range(1,n+1):
     for j in range(1,i+1):
        Sum=Sum+x**j
print("The sum is",Sum)
        