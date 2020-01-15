#Assignment NO.8
#TOPIC : looping 
#Description : To convert binary to decimal number
#DOS: -0-2019
print("FINDING THE DECIMAL NUMBER")
binary=int(input("Enter a binary number:"))
power=0
Sum=0
rem=0
d=0
while binary!=0:
    rem=binary%10
    d=rem*(2**power)
    power+=1
    Sum=Sum+d
    binary=binary//10
print("The decimal number is",Sum)    
