import random 
guess=random.randint(0,50)
chance=5
print("You have 5 chances")
print("Score = 50")
for i in range(1,chance+1):
    user=int(input("Please enter your guess!"))
    if user==guess:
        print("Yay! You have guessed the right number")
        print('Congratstttsttstst')
        print("You took",i,"chances")
        break
    elif user>guess:
        print("Better try a smaller number!")
        print("You have",chance-i,"chances")
    else:
        print("Try a bigger number!")
        print("You have",chance-i,"chances left")
else:
     print("YOU LOSE!")
print("Score =",50-i*10)