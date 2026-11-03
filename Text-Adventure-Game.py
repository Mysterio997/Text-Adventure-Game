class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'

STARTGAME1 = False
HASCODE = False
HASOBJECT = False
START = False

STARTGAME = input("Please type {start}, to start the game. ")

while START == False:
    if STARTGAME.lower() == "start":
        print(bcolors.WARNING + "Starting Game Shortly. . ." + bcolors.ENDC)
        START = True
    elif STARTGAME.lower() == "c":
        print(bcolors.WARNING + "Exiting Program Shortly. . ." + bcolors.ENDC)
        exit()
    else:
        STARTGAME = input("You did not input {start}, please input it again or type {C} to cancel. ")

if START == True:
    print("You wake up in the middle of curry's after a crazy black friday sale and it is locked with nobody around, you must escape. ")
    CONTINUE = input("Press {E} to continue.")
    CONTINUEGAME = True
else: 
    print(bcolors.WARNING + "STARTGAME ERROR, Line 22" + bcolors.ENDC)

while CONTINUEGAME == True:
    if CONTINUE.lower() == "e":
        START = True
        CONTINUEGAME = False
    elif CONTINUE.lower() == "c":
        print(bcolors.WARNING + "Exiting Program Shortly. . ." + bcolors.ENDC)
        exit()
    else:
        CONTINUE = input("You did not input {E}, please input it again or type {C} to cancel. ")

VISITEDELECTRONICS = False
VISITEDWAREHOUSE = False
VISITEDTILLS = False
HASTOOL = False
CODE = 4785
INPUTSAID = False
USEITEM = ""
DOORINPUT = ""
VISITEDDOORS = False
WAREHOUSECHECK = False
DOORCODE = ""
HASCODE1 = False

while HASCODE == False and WAREHOUSECHECK == False and HASCODE1 == False:
    while HASCODE == False and INPUTSAID == False:
        CHOICE = input(bcolors.OKBLUE + "There are four store sections you can search in order to attempt to escape, please choose one of the following. Tills, Warehouse, Electronics or Doors." + bcolors.ENDC)
        INPUTSAID = True
    if CHOICE.lower() == "tills" and VISITEDTILLS == False:
        print("You arrive at the destroyed Tills and notice a bat, you pick it up, this could be useful. You must continue looking.")
        VISITEDTILLS = True
        HASTOOL = True
        INPUTSAID = False
        # Electronics First Time
    elif CHOICE.lower() == "electronics" and VISITEDELECTRONICS == False:
        print("You arrive at electronics and look around, you find nothing. You Must Continue Looking Elsewhere.")
        VISITEDELECTRONICS = True
        INPUTSAID = False
        # Doors First Time
    elif CHOICE.lower() == "doors" and HASCODE11 == True:
        print(bcolors.WARNING + "You head to the doors." + bcolors.ENDC)
        DOORCODE = True
        HASCODE = True
    elif CHOICE.lower() == "doors" and HASCODE1 == False:
        print(bcolors.WARNING + "You cannot go to the doors without a code." + bcolors.ENDC)
        CHOICE = ""
        INPUTSAID = False
    elif CHOICE.lower() == "warehouse" and VISITEDWAREHOUSE == True:
        INPUTSAID = False
        print(bcolors.WARNING + "You have already been to the Warehouse.")
    elif CHOICE.lower() == "warehouse" and VISITEDWAREHOUSE == False:
        WAREHOUSECHECK = True
    elif CHOICE.lower() == "tills" and VISITEDTILLS == True:
        INPUTSAID = False
        print(bcolors.WARNING + "You have already been to the Tills." + bcolors.ENDC)
    elif CHOICE.lower() == "electronics" and VISITEDELECTRONICS == True:
        INPUTSAID = False
        print(bcolors.WARNING + "You have already been to Electronics." + bcolors.ENDC)
    while WAREHOUSECHECK == True:
        if CHOICE.lower() == "warehouse" and VISITEDWAREHOUSE == False:
            print("You arrive at the Warehouse and notice it is boarded up, you need some form of item to get in. You Must Continue Looking Elsewhere.")
            USEITEM = input("If you have a item to break in, input {E}.")
            VISITEDWAREHOUSE = False
            INPUTSAID = False
            CHOICE = ""
            WAREHOUSECHECK = True
        elif USEITEM.lower() == "e" and HASTOOL == False:
            print(bcolors.WARNING + "You do not have a item to break in, look around in other parts of the store for a item." + bcolors.ENDC)
            USEITEM = ""
            INPUTSAID = False
            WAREHOUSECHECK = False
        elif USEITEM.lower() == "e" and HASTOOL == True:
            print("You Break In And Find A Note Containing The Numbers {4745} alongside some words that read Front Door Code. Maybe Try This On The Front Door.")
            INPUTSAID = False
            HASCODE11 = True
            WAREHOUSECHECK = False
        else:
            print("Invalid input.")

while DOORCODE == True:
    DOORINPUT = input("Please input the door code.")
    if DOORINPUT == "4745" and HASCODE == True:
        print("You have inputted the correct code, game over. Thanks for playing!")
        exit()
    elif DOORINPUT != 4745 and HASCODE == True:
        print("Incorrect code, please try again.")
    else: 
        print(bcolors.WARNING + "Error with HAS CODE LOOP LINE 107." + bcolors.ENDC)
