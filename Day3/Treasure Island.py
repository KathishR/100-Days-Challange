print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
print("Welcome to the Treasure Island.\n")
print("Your mission is to find the treasure.\n")
left=input("You are at a cross road.Where do you want to go? Type \"left\" or \"right\"\n")
if left== "left":
    print("left\n")


    wait=input("You come to lake.There is on island in the middle of the lake.Type \"wait\" to wait for a boat.Type \"swim\" to swim across.\n")
    if(wait=="wait"):
        print("wait.")

        colour=input("You arrive at the island unharmed.There is a house with 3 doors.One red,one yellow and one blue.Which colour do you choose ?\n")
        if (colour == "blue"):
            print("You entered room of beasts.Game over.")
        elif (colour == "red"):
            print("You entered room of beasts.Game over.")
        elif (colour == "yellow"):
            print("You won the Game.")

    elif(wait == "swim"):
        print("Game over.")


elif(left=="right"):
    print("Game over.")

