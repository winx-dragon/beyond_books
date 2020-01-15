print ("DECIMAL TO REVERSE HEXADECIMAL")
n=int(input("Enter a decimal number"))
place=1
hexad=""
while n!=0:
    rem=n%16
    if rem==10:
        rem="A"
    elif rem==11:
        rem="B"
    elif rem==12:
        rem="C"
    elif rem==13:
        rem="D"
    elif rem==14:
         rem="E"
    elif rem==15:
        rem="F"
    hexad+=str(rem)
    n//=16
    place*=10
print (hexad)