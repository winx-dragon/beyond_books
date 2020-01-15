y=int(input("Enter the year"))
m=int(input("Enter the month"))
d=int(input("Enter the day"))
year=0
month=0
newday=0
print("The given date is:",d,"/",m,"/",y)
days=int(input("ENter the number of days to be added:"))
year=days//365
month=days//30
newday=(days%30)
finalyear=year+y
finalmonth=month+m
finald=d+newday
print(finald,finalmonth,finalyear)
