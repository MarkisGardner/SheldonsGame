# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def instructions():
    print("Rock wins against:")
    print("    Scissors")
    print("    Lizard")
    print("Paper wins against:")
    print("    Rock")
    print("    Spock")
    print("Scissors wins against:")
    print("    Paper")
    print("    Lizard")
    print("Lizard wins against:")
    print("    Paper")
    print("    Spock")
    print("Spock wins against:")
    print("    Scissors")
    print("    Rock")


def winning_info(result):
    print("You Win!")


def did_you_win(your_choice, computer_choice):
    if your_choice == "R":
        if computer_choice == 3:
            print("Your Rock crushes the computer's scissors!  You win!")
            return "W"
        elif computer_choice == 4:
            print("Your Rock crushes the computer's lizard!  You win! ")
            return "W"
        elif computer_choice == 5:
            print("The computer's Spock vaporizes your rock!  You lose!")
            return "L"
        elif computer_choice == 2:
            print("The computer's Paper covers your rock!  You lose!")
            return "L"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    elif your_choice == "P":
        if computer_choice == 3:
            print("Your Paper gets cut by the computer's scissors!  You lose!")
            return "L"
        elif computer_choice == 4:
            print("Your Paper gets eaten by the computer's lizard!  You lose! ")
            return "L"
        elif computer_choice == 5:
            print("Your paper disproves Spock!  You win!")
            return "W"
        elif computer_choice == 1:
            print("Your rock covers the computer's rock!  You win!")
            return "W"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
#start here tomorrow.
    elif your_choice == "R":
        if computer_choice == 3:
            print("Your Rock crushes the computer's scissors!  You win!")
            return "W"
        elif computer_choice == 4:
            print("Your Rock crushes the computer's lizard!  You win! ")
            return "W"
        elif computer_choice == 5:
            print("The computer's Spock vaporizes your rock!  You lose!")
            return "L"
        elif computer_choice == 2:
            print("The computer's Paper covers your rock!  You lose!")
            return "L"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    elif your_choice == "R":
        if computer_choice == 3:
            print("Your Rock crushes the computer's scissors!  You win!")
            return "W"
        elif computer_choice == 4:
            print("Your Rock crushes the computer's lizard!  You win! ")
            return "W"
        elif computer_choice == 5:
            print("The computer's Spock vaporizes your rock!  You lose!")
            return "L"
        elif computer_choice == 2:
            print("The computer's Paper covers your rock!  You lose!")
            return "L"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    elif your_choice == "R":
        if computer_choice == 3:
            print("Your Rock crushes the computer's scissors!  You win!")
            return "W"
        elif computer_choice == 4:
            print("Your Rock crushes the computer's lizard!  You win! ")
            return "W"
        elif computer_choice == 5:
            print("The computer's Spock vaporizes your rock!  You lose!")
            return "L"
        elif computer_choice == 2:
            print("The computer's Paper covers your rock!  You lose!")
            return "L"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    else:
        print("You can't follow instructions - you lose!")
        instructions()
        return "L"

def play_game(times):
    for i in range(times):
        print("Enter your choice:  (R)ock, (P)aper, (S)cissors, (L)izard, (Sp)ock")
        your_try = input()
        number = random.randint(1, 5)
        print("I is ", i)
        win = did_you_win(your_try, number)
        tally[i] = win


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Please enter the number of rounds you want play or enter I for instructions.")
ans = int(input())
# Note: I am not going to do much testing to make sure they enter a number or I.
if ans == 'I':
    instructions()
    print("Thank you for playing!")
    quit(0)
else:
    play_game(ans)
