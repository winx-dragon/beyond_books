#Assignment NO.5
#TOPIC : if condition
#Description : Program displaying given date
#DOS: 20-08-2019 
print("PRINTING THE DATE")
d=int(input("Enter the day: "))
m=int(input("Enter the month: "))
y=int(input("Enter the year: "))
n=0
if 0>=d or d>31:
    print("ERROR IN DAY: A DAY IS BETWEEN 1 AND 31")
elif 0>=m or m>12:
    print("ERROR IN MONTH")
elif 0>=y:
    print("ERROR IN YEAR")
elif d==31 and (m==4 or m==6 or m==9 or m==11) :
    print("ERROR:THIS MONTH HAS ONLY 30 DAYS")
elif m==2 and d==29 and y%4!=0:
    print("ERROR: FEBRUARY HAS 28 DAYS IN",y,)
elif m==2 and d==29 and y%100==0 and y%400!=0:
    print("ERROR: FEBRUARY HAS 28 DAYS IN",y,)
else:
                if m==1:
                    n="JANUARY"
                if m==2:
                    n="FEBRUARY"
                if m==3:
                    n="MARCH"
                if m==4:
                    
                    n="APRIL"
                if m==5:
                    n="MAY"
                if m==6:
                    n="JUNE"
                if m==7:
                    n="JULY"
                if m==8:
                    n="AUGUST"
                if m==9:
                    n="SEPTEMBER"
                if m==10:
                    n="OCTOBER"
                if m==11:
                    n="NOVEMBER"
                if m==12:
                    n="DECEMBER"
                if d==1 or d==21 or d==31:
                    suffix="st"
                elif d==2 or d==22:
                    suffix="nd"
                elif d==3 or d==23:
                     suffix="rd"
                else:
                     suffix="th"

                print(d,suffix,' ', n,",",' ', y,sep='')
        
        


                
    


    
         