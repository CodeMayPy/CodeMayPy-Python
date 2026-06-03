# Make a program that plays odd or even with the computer. The game will only stop when the player loses, showing the
# total number of consecutive wins he has achieved at the end of the game.
from random import randint
w = 0
while True:
    player = int(input("Enter a number:"))
    computer = randint(0,10)
    total = player + computer
    tpe = ' '
    while tpe not in "EO":
        tpe = str(input("Ear or odd? [E/O]")).strip().upper()[0]
    print(f"You played {player} and the computer {computer}. the total is {total}")
    if tpe == "E":
        if total % 2 == 0:
            print("You Win!")
            w += 1
        else:
            print(" You Lost!!")
            break
    elif tpe == "O" :
        if total % 2 == 1:
            print("You Win!")
            w += 1
        else:
            print("You lost!!")
            break
    print("Let's play again...")
print(f"You win {w} times.")
