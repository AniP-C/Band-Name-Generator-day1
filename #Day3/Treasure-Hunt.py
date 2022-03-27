from re import L


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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

way = input("There are 2 ways where you want to go ? 'L' for left 'R' for right")
if way == 'L':
    river = input("There is a river , you wanted to swim or wait ?")
    if river == 'wait' :
        door = input('There are 3 doors here, of RED , GREEN , BLUE color, which one you want to open (R,G,B)')
        if door == 'R':
            print("Fire of hell burnt you down to ashes")       
        elif door == 'G':
            print("You stepped into room of beasts, You lose")
        elif door == 'B' :
            print("You won this game !")
        else :
            print("You lose")
    elif river == 'swim':
        print("The crocodiles stomach is full, they are thanking you, GAME OVER")
    else :
        print("You die")
else:
    print("you fall into a hole , GAME OVERY MF")
   