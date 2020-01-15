print("CONVERT NUMBERS")
con="y"
while con=="y":
    print("1: DECIMAL TO BINARY")
    print("2: BINARY TO DECIMAL")
    choice=input("Which operation would you like?(1/2)")
    if choice=="1":
        number=int(input("Enter a number:"))
        binary=0
        place=1
        while number!=0:
            rem=number%2
            binary=rem*place+binary
            number=number//2
            place*=10
        print("The binary number is",binary) 
    if choice=="2":
        binary=int(input("Enter a binary number:"))
        power=0
        decimal=0
        rem=0
        digit=0
        while binary!=0:
            rem=binary%10
            digit=rem*(2**power)
            power+=1
            decimal=decimal+digit
            binary=binary//10
        print("The decimal number is",decimal)    
    
    con=input("Do you wish to continue?(y/n)")
    if con=="n":
        print("THANK YOU")
        break

        