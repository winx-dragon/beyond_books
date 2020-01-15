
line=int(input("Enter a "))
spaces=40
for n in range(0,line+1):
    for sp in range(1,spaces+1):
        print('',end='')
    for r in range(0,n+1):
        nfact=1
        for i in range(1,n+1):
                nfact*=i
        rfact=1
        for j in range(1,r+1):
            rfact*=j
        nrfact=1
        for k in range(1,n-r+1):
            nrfact*=k
    print(nfact//(rfact*nfact), ' ',end=' ')
    print()
    spaces-=2