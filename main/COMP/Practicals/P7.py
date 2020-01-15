print("ARITHMETIC CALCULATOR FOR COMPLEX NUMBERS")
con="y"
while con=="y":
    r1=int(input("Enter the real component of a number: "))
    i1=int(input("Enter the imaginary component of a number: "))
    r2=int(input("Enter the real component of another number: "))
    i2=int(input("Enter the imaginary component of another number: "))
    
    print("CALCULATOR")
    print("+ : ADDITION")
    print("x : MULTIPLICATION")   
    print('/ : DIVISION')
   
    choice=input("\nWhich operation would you like?")
    if choice =='+':
        print("\t   ",r1,"+",i1,"j",sep="")
        print("\t   ",r2,"+",i2,"j",sep="")
        print("\t + ____")
        print("\t = ",r1+r2,"+",i1+i2,"j",sep="")
   
        
    elif choice =='x':
       
        a=r1*r2
        c=i1*i2*-1
        b=r1*i2
        d=i1*r2
        finalr=a+c
        finali=b+d
        print("\t   ",r1,"+",i1,"j",sep="")
        print("\t   ",r2,"+",i2,"j",sep="")
        print("\t x ____")
        print("\t = ",finalr,"+",finali,"j",sep="")
        
        
        
    elif choice =='/':
         r3=r2
         i3=-i2
         a=r1*r3
         c=i1*i3*-1
         b=r1*i3
         d=i1*r3
         finalr=a+c
         finali=b+d
         div=r2**2+(i2**2)
         print("\t   ",r1,"+",i1,"j",sep="")
         print("\t   ____")
         print("\t   ",r2,"+",i2,"j", "=    ",(finalr/div),"+",(finali/div),"j",sep="")
         
         
         
    con=input("Do you wish to continue? ")
    if con=="n":
        print("THANK YOU")
        break
