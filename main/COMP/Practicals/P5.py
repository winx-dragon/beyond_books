n=int(input("Enter the limit:"))
Sum=0
for i in  range(1,n+1,2):
    for j in range(1,i+1,2):
        Sum+=j**2
print(Sum)
