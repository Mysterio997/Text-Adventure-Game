HASCODE = "false"
STARTGAME = input("Please type {start}, to start the game. Any other input will end the program. ")
STARTGAME1 = "false"
CODE = "1"

if STARTGAME.lower() == ("start"):
    STARTGAME1 = "True"
    print("Starting Game Shortly. . .")
else: 
    print("Invalid input, program ending.")
    exit()

if STARTGAME1 == "True":
    print("You wake up in the middle of curry's after a crazy black friday sale and it is locked with nobody around, you must escape.")
    CONTINUE = input("Press {E} to continue.")
else: 
    print("STARTGAME ERROR")
    exit()

CONTINUE = CONTINUE.lower()

if CONTINUE.lower() == "e":
    print("There are 4 store sections: Electronics, Tills, Warehouse and Exit. You must find the code to escape the building.")
    CONTINUE = "True"
else: 
    print("E was not inputted, ending program.")
    exit()

if CONTINUE == "True":
    CHOICE1 = input(f"Where would you like to search? Electronics, Tills or Warehouse.")
else:
    print("Invalid input, program ending.")
    exit()
CHOICE1 = CHOICE1.lower()
if CHOICE1.lower() == "electronics":
    print("You head over to Electronics.")
    print("You search around Electronics and do not appear to find anything, you get fustrated and punch a laptop. You move on.")
    ELECTRONICSDONE = "True"
    TILLSDONE = "false"
    WAREHOUSEDONE = "false"
elif CHOICE1.lower() == "tills":
    print("You head over to the Tills.")
    print("You search around the tills and find nothing. You Move On")
    ELECTRONICSDONE = "false"
    TILLSDONE = "True"
    WAREHOUSEDONE = "false"
elif CHOICE1.lower() == "warehouse":
    print("You head over to the Warehouse.")
    print("You head over to the Warehouse and after a long time searching you find a note that says, in-case of locked in combination is 5164. You have the code.")
    ELECTRONICSDONE = "false"
    TILLSDONE = "false"
    WAREHOUSEDONE = "True"
    HASCODE = "True"
else:
    print("Invalid choice inputted, ending program.")
    exit()

if HASCODE == "True":
    print("You have found the code and you head out to the entrance, you reach the alarm system and it is asking you input the code.")
    CODE = input("Please insert the pin to unlock doors.")

if CODE == "5164" and HASCODE == "True":
    print("You unlock the door and leave Curry's, you are now free. However, a criminal noticed the unlocked door and robs the curry's.")
    print("Game over.")
    exit()
elif CODE != "5164" and HASCODE == "True":
    print("You input the wrong code and the alarms blare loudly, police show up and arrest you for burglary.")
    print("Game Over.")
    exit()

if HASCODE == "false":
    CHOICE2 = input(f"You have now searched {CHOICE1}, where would you like to search next? Electronics, Tills or Warehouse, you cannot return to a place you have already been.")

if CHOICE2.lower() == "electronics" and (ELECTRONICSDONE == "false"):
    print("You head over to Electronics.")
    print("You search around Electronics and do not appear to find anything, you get fustrated and punch a laptop -£2000. You move on.")
    PROPERTYDAMAGED = 2000
    ELECTRONICSDONE = "True"
elif CHOICE2.lower() == "tills" and TILLSDONE == "false":
    print("You head over to the Tills.")
    print("You search around the tills and find nothing. You Move On")
    TILLSDONE = "True"
elif CHOICE2.lower() == "warehouse" and WAREHOUSEDONE == "false":
    print("You head over to the Warehouse.")
    print("You head over to the Warehouse and after a long time searching you find a note that says, in-case of locked in combination is 5164. You have the code.")
    WAREHOUSEDONE = "True"
    HASCODE = "True"
elif CHOICE2.lower() == "electronics" and ELECTRONICSDONE == "True":
    print("You cannot search the same part of the store again, please try again.")
    exit()
elif CHOICE2.lower() == "tills" and TILLSDONE == "True":
    print("You cannot search the same part of the store again, please try again.")
    exit()
elif CHOICE2.lower() == "warehouse" and WAREHOUSEDONE == "True":
    print("You cannot search the same part of the store again, please try again.")
    exit()
else:
    print("Invalid choice inputted, ending program.")
    exit()

if HASCODE == "True":
    print("You have found the code and you head out to the entrance, you reach the alarm system and it is asking you input the code.")
    CODE = input("Please insert the pin to unlock doors.")

if CODE == "5164" and HASCODE == "True":
    print("You unlock the door and leave Curry's, you are now free. However, a criminal noticed the unlocked door and robs the curry's.")
    print("Game over.")
    exit()
elif CODE != "5164" and HASCODE == "True":
    print("You input the wrong code and the alarms blare loudly, police show up and arrest you for burglary.")
    print("Game Over.")
    exit()


if HASCODE == "false":
    CHOICE3 = input(f"You have now searched {CHOICE2}, where would you like to search next? Electronics, Tills or Warehouse, you cannot return to a place you have already been.")

if CHOICE3.lower() == "electronics" and ELECTRONICSDONE == "false":
    print("You head over to Electronics.")
    print("You search around Electronics and do not appear to find anything, you get fustrated and punch a laptop. You move on.")
    PROPERTYDAMAGED = 2000
    ELECTRONICSDONE = "True"
elif CHOICE3.lower() == "tills" and TILLSDONE == "false":
    print("You head over to the Tills.")
    print("You search around the tills and find nothing. You Move On")
    TILLSDONE = "True"
elif CHOICE3.lower() == "warehouse" and WAREHOUSEDONE == "false":
    print("You head over to the Warehouse.")
    print("You head over to the Warehouse and after a long time searching you find a note that says, in-case of locked in combination is 5164. You have the code.")
    WAREHOUSEDONE = "True"
    HASCODE = "True"
elif CHOICE3.lower() == "electronics" and ELECTRONICSDONE == "True":
    print("You cannot search the same part of the store again, please try again.")
    exit()
elif CHOICE3.lower() == "tills" and TILLSDONE == "True":
    print("You cannot search the same part of the store again, please try again.")
    exit()
elif CHOICE3.lower() == "warehouse" and WAREHOUSEDONE == "True":
    print("You cannot search the same part of the store again, please try again.")
    exit()
else:
    print("Invalid choice inputted, ending program.")
    exit()

if HASCODE == "True":
    print("You have found the code and you head out to the entrance, you reach the alarm system and it is asking you input the code.")
    CODE = input("Please insert the pin to unlock doors.")

if CODE == "5164" and HASCODE == "True":
    print("You unlock the door and leave Curry's, you are now free. However, a criminal noticed the unlocked door and robs the curry's.")
    print("Game over.")
    exit()
elif CODE != "5164" and HASCODE == "True":
    print("You input the wrong code and the alarms blare loudly, police show up and arrest you for burglary.")
    print("Game Over.")
    exit()
