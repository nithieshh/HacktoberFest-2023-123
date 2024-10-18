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

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

# First choice: Crossroad
choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right" \n').lower()

if choice1 == "left":
    # Second choice: Lake
    choice2 = input('You arrived at a lake. There is an island in the middle. Do you want to "swim" or "wait"? \n').lower()
    
    if choice2 == "wait":
        # Third choice: Island with doors
        choice3 = input('You finally arrived at the island. There is a house with three doors: "Red", "Green", and "Blue". Choose one door. \n').lower()
        
        if choice3 == "red":
            print("Game Over! You just fell into a dark hole...")
        elif choice3 == "green":
            print("Congratulations! You Win. You found the treasure worth $5 million!")
        elif choice3 == "blue":
            print("Game Over! You entered a room with fire...")
        else:
            print("Invalid choice. Game Over!")
    elif choice2 == "swim":
        print("Game Over! You are attacked by wild dogs while swimming...")
    else:
        print("Invalid choice. Game Over!")
        
elif choice1 == "right":
    print("Game Over! You are attacked by a beast on the right path...")
else:
    print("Invalid choice. Game Over!")
