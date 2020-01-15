n=int(input("Enter a number:"))
rem=0
reverse=0
Sum=0
while n!=0:
    rem=n%10
    Sum=rem**3+Sum
    reverse=reverse*10+rem
    n=n//10
print("The reversed number is",reverse)
if Sum==reverse:
    print("Armstrong no")
else:
    print("Not Armstrong")
