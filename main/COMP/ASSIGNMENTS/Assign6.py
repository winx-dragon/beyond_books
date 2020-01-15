#Assignment NO.6
#TOPIC : for loop 
#Description : To find the perfect number
#DOS: 03-09-2019 
print("PERFECT NUMBER")
Sum=0
n=int(input("Enter a number: "))
for i in range(1,n):
        if n%i==0:
            Sum=Sum+i
if Sum==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
        
        
    
