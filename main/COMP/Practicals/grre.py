n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
Sum=0
if n1>n2 and n1>n3:
 print (n1,"is the largest")
if n2>n1 and n2>n3:
 print (n2,"is the largest")
if n3>n1 and n3>n2:
 print (n3,"is the largest")
for i in (n1,n2,n3):
 store=i
 while i!=0:
    rem=i%10
    Sum+=rem**3
    i//=10
 if Sum==store:
    print (store,"is an armstrong number")
    break
 else:
    print (store,"is not an armstrong number")
    break