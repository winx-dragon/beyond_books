n=int(input("Enter a number"))
Sum=0
for i in range(1,n):
       if n%i==0:
           print(i,end=" ")
           Sum=Sum+i
print(n)
if Sum==n:
       print(n,"is a perfect number")
else:
       print(n,"is not a perfect number")
        
                   