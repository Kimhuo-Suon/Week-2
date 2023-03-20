from random import randint

print("1 = Rock, 2 = Paper, 3 = Scisscor \n")
a = input("please enter your choice: ")
computer = randint(0, 3)
print("computer choice: ", b)

if computer == 0:
    Bot = "rock"
elif computer == 1:
    Bot = "Papaer"
else:
    Bot = "Scissors"
player = input("player : ").Lower()

if player == Bot:
    print("Bot: ",Bot)
    print("Tie")

elif player == "rock":
   if Bot == "paper":
       print("Bot: ",Bot)
       print("you lose")
   else:
       print("you win")
elif player == "scissor":
    if Bot == "rock":
        print("Bot: ",Bot)
        print("you lose")
    else:
        print("you win")
elif player == "paper":
    if Bot == "scissors":
        print("Bot: ",Bot)
        print("you win")
    else:
        print("Bot:", Bot)
        print("you lose")
else:
    print("you move is not valid")
