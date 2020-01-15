print("Series")

op=int(input('Which series would you like?(1/2)'))
if op==1:
    alphabet={0:"A",1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',}
    spaces=40
    n=int(input("Enter the number of lines:"))
    for i in range(1,2*n,2):
        for sp in range(1,spaces+1):
            print(" ",end="")
        for j in range(1,i+1):
            print(alphabet[j],end=" ")
        print()
        spaces-=2

    
    
