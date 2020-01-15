#Assignment NO.7
#TOPIC : loop else
#Description : Program to check whether a number is a happy number or not
#DOS: 03-09-2019 

print("HAPPY NUMBER")
n=int(input("Enter a number:"))
t=n
rem=0
count=1
while count<=1000 :
    Sum=0
    while n!=0:
        rem=n%10
        d=rem**2
        Sum=Sum+d
        n=n//10
    if Sum==1:
        print(t,"is a happy number")
        break
    else:
          n=Sum
    count+=1
else:
    print(t,"is not a happy number")
        
