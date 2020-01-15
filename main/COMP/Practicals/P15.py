n=int(input("Enter limit:"))
m=int(input("Enter limit:"))
import math
for i in range(n,m+1):
    Factor=2
    if i==1:
        print("Neither p nor comp")
    else:
        while Factor<=math.sqrt(i):
            if i%Factor==0 :
               break
            Factor+=1
        else:
            print(i,end=" ")