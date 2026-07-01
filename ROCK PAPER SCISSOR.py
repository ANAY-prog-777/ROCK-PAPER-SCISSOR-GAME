import random

print("HII!!!")
print("WELCOME TO THE ROCK PAPER AND SCISSORS GAME!!")
print("HOPE U WILL ENJOY THIS GAME!!")

print("----------------------------------------------------------------------------------------")
print("RULES OF THE GAME:_")
print("1. ROCK BEATS SCISSORS")
print("2. SCISSORS BEATS PAPER")
print("3. PAPER BEATS ROCK")
print("----------------------------------------------------------------------------------------") 

print("SELECT 0 FOR ROCK, 1 FOR PAPER, 2 FOR SCISSORS")

user_choice = int(input("ENTER YOUR CHOICE IN NUMBER :--->"))

if user_choice < 0 or user_choice > 2:
    print("INVALID INPUT!! PLEASE ENTER A VALID NUMBER OR U WILL NOT BE ABLE TO ENJOY THE GAME!!")
else:
    computer_choice = random.randint(0,2)

    if user_choice == 0:
        print("YOU CHOSE ROCK")
    elif user_choice == 1:
        print("YOU CHOSE PAPER")
    else:
        print("YOU CHOSE SCISSORS")

    if computer_choice == 0:
        print("COMPUTER CHOOSE ROCK")
    elif computer_choice == 1:
        print("COMPUTER CHOSE PAPER")
    else:
        print("COMPUTER CHOOSE SCISSORS")

    if user_choice == computer_choice:
        print("ITS A TIE!!!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("USER WINS!!")
    else:
        print("COMPUTER WINS!!")

    print("YOU CAN PLAY AGAIN!!") 
    print("THANKS FOR PLAYING!! HOPE U ENJOYED THE GAME!!")
    print("BYE!!")
    print("----------------------------------------------------------------------------------------")