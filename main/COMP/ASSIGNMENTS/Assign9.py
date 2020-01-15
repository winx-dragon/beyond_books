#Assignment NO.9
#TOPIC : for loop 
#Description : To print the series:
#          A
#     A    B    A
# A   B    C    B    A     for n number of lines
#DOS: -09-2019
print("PRINTING SERIES")
spaces=40
alphabet={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',}
n=int(input("Enter the number of lines: "))
for i in range(1,n+1):
    for sp in range(1,spaces+1):
             print(' ',end='')
    for j in range(1,i+1,):
             print(alphabet[j],end=' ')
             
    print()
    spaces-=1
