
octal=input("Enter an octal number:")
for i in octal:
    if i=="8" or i=="9" :
        print("sorry not an octal number")
        break
else:
    octal=int(octal)
    power=0
    decimal=0
    rem=0
    digit=0
    while octal!=0:
           rem=octal%10
           digit=rem*(8**power)
           power+=1
           decimal=decimal+digit
           octal=octal//10
    print("The decimal number is",decimal)   