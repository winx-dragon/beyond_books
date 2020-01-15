spaces=40
n=int(input("Enter the number of lines:"))
for i in range(1,n//2+2):
    for sp in range(1,spaces+1):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end=" ")
    print()
    spaces-=2
spaces+=4
for i in range(1,n//2+1):
    for sp in range(1,spaces+1):
        print(" ",end="")
    for j in range(1,(n-2*i)+1):
        print("*",end=" ")
    print()
    