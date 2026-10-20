# 4 different places
# item they can pick up and use
# one way to lose
# number input 
# input error handling / validation
LORE = "You wake up feeling dizzy and tired in the middle of the street outside your house. " \
"You do not know why you are asleep in the road but you notice all the houses are abondoned aside yours which is glowing brightly with apadlock and chain surrounding its entrances. " \
"You must get home." 
STARTGAME = "false"
START = input("To Start The Game, Type Start.")
HOUSE = "1"
GONETOHOUSE1 = "false"
GONETOHOUSE2 = "false"
GONETOHOUSE3 = "false"
GONETOHOUSE11 = "false"
GONETOHOUSE22 = "false"
GONETOHOUSE33 = "false"
HASKEY = "false"



if START.lower() == ("start"):
    STARTGAME = "true"
    print()
    print("Game Is Now Starting...")
    print()
else:
    print("You did not type start, please restart the game.")

while HASKEY == "false":
    if STARTGAME == ("true"):
        print(f"{LORE}")
        HOUSE = input("You have 3 houses that look eerie and abondoned but may posses a key to your home which one will you enter first? Please input 1,2 or 3. ")
        if HOUSE == ("1"):
            print(f"You have chosen House {HOUSE}")
            GONETOHOUSE11 = "true"
        elif HOUSE == ("2"):
            print(f"You have chosen House {HOUSE}")
            GONETOHOUSE22 = "true"
        elif HOUSE == ("3"):
            print(f"You have chosen House {HOUSE}")
            GONETOHOUSE33 = "true"
        elif HOUSE == ("4") and (HASKEY == "false"):
            print(f"You have your locked home but you do not have a key, please restart the game.")
        else:
            print("You did not choose a house, please restart the game.")
            break
        if GONETOHOUSE11 == "true":
            print("You head into the 1st House and try the door, it is unlocked and upon opening it a musky smell surrounds you.")
            print("You search around the home and find a rock with a engraving on it, the rock has the words LEAVE etched into it's surface.")
            print("After a while of searching the home you find nothing of use, you decide to leave.")
            GONETOHOUSE1 = "true"
        elif GONETOHOUSE22 == "true":
            print("You head into the 2nd House and try the door, it is unlocked and upon opening it a musky smell surrounds you.")
            print("You search around the home and find a old note with 4 numbers on it, the note has the numbers 2059 written on it. What does this number mean?")
            print("After finding the note you decide to leave the home.")
            GONETOHOUSE2 = "true"
        if GONETOHOUSE33 == "true":
            print("You head into the 3rd House and try the door, it is unlocked and upon opening it a musky smell surrounds you.")
            print("You search around the home and find a old safe that is stashed away with a keypad to open it, what could the code be?")
            CODE = input("Please input a 4 digit code.")
        if CODE == "2059":
            print("The safe opens and a key is inside of it, maybe this opens the padlock. You leave the house and head home.")
            HASKEY == "true"
else: 
    print("The code is wrong and the safe sounds a alarm gaining interest from some nearby zombies, they attack you.")
    print("You Lose.")
    exit()
