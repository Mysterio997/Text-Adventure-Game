STARTGAME1 = False
HASCODE = False
HASOBJECT = False
START = False

STARTGAME = input("Please type {start}, to start the game.")

while START == False:
    if STARTGAME.lower() == "start":
        print("Starting Game Shortly. . .")
        START = True
    elif STARTGAME.lower() == "c":
        print("Exiting Program Shortly. . .")
        exit()
    else:
        STARTGAME = input("You did not input {start}, please input it again or type {C} to cancel.")

if START == True:
    print("You wake up in the middle of curry's after a crazy black friday sale and it is locked with nobody around, you must escape.")
    CONTINUE = input("Press {E} to continue.")
    CONTINUEGAME = True
else: 
    print("STARTGAME ERROR, Line 22")

while CONTINUEGAME == True:
    if CONTINUE.lower() == "e":
        START = True
        CONTINUEGAME = False
    elif CONTINUE.lower() == "c":
        print("Exiting Program Shortly. . .")
        exit()
    else:
        CONTINUE = input("You did not input {E}, please input it again or type {C} to cancel.")

VISITEDELECTRONICS = False
VISITEDWAREHOUSE = False
VISITEDTILLS = False
HASTOOL = False
CODE = 4785
INPUTSAID = False
USEITEM = ""
DOORINPUT = ""
VISITEDDOORS = False
WAREHOUSECHECK = True

while HASCODE == False and WAREHOUSECHECK == True:
    while HASCODE == False and INPUTSAID == False:
        CHOICE = input("There are four store sections you can search in order to attempt to escape, please choose one of the following. Tills, Warehouse, Electronics or Doors.")
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
    elif CHOICE.lower() == "doors" and HASCODE == False:
        print("You cannot go to the doors without a code.")
        CHOICE = ""
        INPUTSAID = False
    elif DOORINPUT == 4785 and HASCODE == True:
        print("You have inputted the correct code, game over. Thanks for playing!")
        exit()
    elif DOORINPUT.lower() not in ["c", 4785] and VISITEDDOORS == True:
        print("You have not inputted a correct code, please find it.")
        INPUTSAID = False
    elif CHOICE.lower() == "warehouse" and VISITEDWAREHOUSE == True:
        INPUTSAID = False
        print("You have already been to the Warehouse.")
    elif CHOICE.lower() == "warehouse" and VISITEDWAREHOUSE == False:
        WAREHOUSECHECK = False
    elif CHOICE.lower() == "tills" and VISITEDTILLS == True:
        INPUTSAID = False
        print("You have already been to the Tills.")
    elif CHOICE.lower() == "electronics" and VISITEDELECTRONICS == True:
        INPUTSAID = False
        print("You have already been to Electronics.")
else: 
    print("Error")

while WAREHOUSECHECK == False:
    if CHOICE.lower() == "warehouse" and VISITEDWAREHOUSE == False:
        print("You arrive at the Warehouse and notice it is boarded up, you need some form of item to get in. You Must Continue Looking Elsewhere.")
        USEITEM = input("If you have a item to break in, input {E}.")
        VISITEDWAREHOUSE = False
        INPUTSAID = False
        CHOICE = ""
    elif USEITEM.lower() == "e" and HASTOOL == False:
        print("You do not have a item to break in, look around.")
        USEITEM = ""
        INPUTSAID = False
        WAREHOUSECHECK = False
    elif USEITEM.lower() == "e" and HASTOOL == True:
        print("You Break In And Find A Note Containing The Numbers {4745} alongside some words that read Front Door Code. Maybe Try This On The Front Door.")
        INPUTSAID = False
        HASCODE = True
        WAREHOUSECHECK = False

while HASCODE == True:
    if DOORINPUT == 4785 and HASCODE == True:
        print("You have inputted the correct code, game over. Thanks for playing!")
        exit()
    elif DOORINPUT.lower() not in ["c", 4785] and VISITEDDOORS == True:
        print("You have not inputted a correct code, please find it.")
        INPUTSAID = False
    else: 
        print("Error.")
