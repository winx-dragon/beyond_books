import math 
limit=int(input("Enter the limit:"))
first,second=0,1
print(first)
print(second)
for i in range(1,limit-1):
    third=first+second
    print(third,end="\n")
    first=second
    second=third
    Factor=2
    if third==1:
            continue
    else:
        while Factor<=math.sqrt(third):
            if third%Factor==0 :
                break
            Factor+=1
        else:
            print("\bis a Prime number")
       