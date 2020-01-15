print("TO ROTATE A STRING")
string=input("Enter a string:\n")
store=""
store1=""
for i in range(1,len(string)+1):
    store=string[len(string)-1:]
    store1=store+string[0:len(string)-1]
    print(store1)
    string=store1

