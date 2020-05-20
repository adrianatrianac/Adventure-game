import time
import random
enemy = ["Ogre", "Pirate", "Troll"]
items = []
current_enemy = random.choice(enemy)


def printpause(string):
    print(string)
    time.sleep(2)


def valid_input(question, option1, option2):
    while True:
        answer = input(question)
        if option1 == answer:
            break
        elif option2 == answer:
            break
    return answer


def intro():
    printpause("You find yourself in a rocky mountain.")
    printpause("In front of you are two passageways.")


def choose_path():
    answer = valid_input("Enter 1 to knock on the door of the house.\n"
                         "Enter 2 to peer into the cave.\n"
                         "What would you like to do?\n"
                         "(Please enter 1 or 2)\n", "1", "2")
    if answer == "1":
        house()
    elif answer == "2":
        cave()


def play_again():
    answer = valid_input("Would you like to play again? (y/n) \n", "y", "n")
    if answer == "n":
        printpause("Thank you for playing! See you next time.")
    elif answer == "y":
        printpause("Excellent! Restarting the game ...")
        play_game()


def house():
    printpause("You approach the house.")
    printpause("You are about to knock when the door opens and out steps "
               "a giant " + current_enemy)
    answer = valid_input("Would you like to (1) Fight or (2) Run away?\n",
                         "1", "2")
    if answer == '2':
        printpause("You run back into the field. Luckily, you dont seem "
                   "to have been followed.")
        choose_path()
    elif answer == "1":
        if "sword" in items:
            printpause("As the " + current_enemy + "moves to attack,"
                       " you unsheath your new sword")
            printpause("But he takes one look at your shiny sword and runs"
                       "away!")
            printpause("You have rid the town of the beast. You are"
                       " victorius!")
            play_again()
        else:
            printpause("You feel extremely scared and under-prepared since you"
                       " have nothing to denfend yourself with")
            printpause("You do your best, but your strength is nothing "
                       "compared to his.")
            printpause("You have been defeated!")
            play_again()


def cave():
    if "sword" in items:
        printpause("You already got the good stuff, it's just an empty cave")
        printpause("You walk back into the field")
        choose_path()
    else:
        printpause("You peer into the cave, it's very dark and small")
        printpause("You see nothing, but a shiny metal behind a rock")
        printpause("You just found a big, sharp sword, so you pick it "
                   "up and go back out.")
        items.append("sword")
        choose_path()


def play_game():
    intro()
    choose_path()


play_game()
