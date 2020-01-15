n=int(input("Enter the number:"))
m=int(input("Enter the limit:"))
for i in range(m,n-1,-1):
    if i%2!=0:
        print(i)
        binary=0
        place=1
        while i!=0:
            rem=i%2
            binary=rem*place+binary
            i=i//2
            place*=10
        print("The binary number is",binary) 
    