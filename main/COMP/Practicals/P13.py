limit=int(input("How many numbers do you wish to compare?"))
n=int(input("Enter the number"))
small=n
big=n
for i in range(limit-1):
    n1=int(input("Enter the number"))
    if n1<small:
        small=n1
    if n1>big:
        big=n1
print(big)
print(small)

