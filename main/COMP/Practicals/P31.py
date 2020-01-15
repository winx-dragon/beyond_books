n=int(input("Enter a number:"))
x=n+1
import math
while 1:
    d=0
    n=x
    while n!=0:
        r=n%10
        d=d*10+r
        n=n//10
    if d==x:
        Factor=2
        while Factor<=math.sqrt(x):
            if x%Factor==0 :
                   x+=1
                   break
            Factor+=1
        else:
              print(x," is the next Prime Palidrome")
              break
    else:
             x=x+1