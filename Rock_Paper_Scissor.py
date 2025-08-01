import random
import time
run = True
while run:
    comp = random.choice(["rock", "paper", "scissors"])
    player = str(input("Rock, paper or scissors: "))
    print("Computer analysing.....")
    time.sleep(3)
    print(f"And he choose {comp}")
    time.sleep(2)

    print(f"Computer = {comp} VS Player = {player}")
    if player.lower() == "rock":
        if comp == "paper":
            print("House wins!")
        elif comp == "scissors":
            print("You won!")
    elif player.lower() == "paper":
        if comp == "rock":
            print("You won!")
        elif comp == "scissors":
            print("House wins!")
    elif player.lower() == "scissors":
        if comp == "rock":
            print("House wins!")
        elif comp == "paper":
            print("You won!")
    if player.lower() == comp:
        print("Its a tie!")
    play = int(input("Enter 1 to play again and 0 to exit: "))
    if play == 1:
        continue
    elif play == 0:
        run = False