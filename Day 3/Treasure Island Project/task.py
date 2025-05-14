print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("After hearing about a treasure while eavesdropping in a bar, you decide to leave the city")
first_choice = input('''You have been walking for several hours and are now at a crossroad.
Do you want to go "right" or "left"?\n ''')
if first_choice.lower() == "left":
    second_choice = input('''You keep walking for about two hours and arrive in front of a lake. In the horizon 
        you can see an island and a boat, but the boat is very far. 
        Would you like to "swim" to the island or "wait" for the boat? \n''')
    if second_choice.lower() == "wait":
        third_choice = input('''After waiting for a while, the boat finally arrives.
            The boat slowly takes you to the island. Once on the island you see a giant castle. 
            Eager to find the treasure, you walk all the way to the castle. 
            Once at the entrance, you notice that there are three doors, 
            a "yellow" door, a "red" door and a "blue" door. 
            Which door would you like to open? \n''')
        if third_choice.lower() == "red":
            print('''You open up the red door. As soon as you open the door
                you are face to face with a massive red dragon.
                He spits fire at you without hesitation.
                You have died.''')
        elif third_choice.lower() == "blue":
            print('''You open up the blue door.
                You see a magnificent deer with skin like crystal.
                It gently walks up to you.
                As you reach to pet it, it suddenly opens up its giant maw and eats you alive.
                You have died.''')
        elif third_choice.lower() == "yellow":
            print('''You open up the yellow door.
                The room is fully dark. You enter and walk slowly.
                As you keep walking, a light suddenly turns on.
                You notice a massive treasure a few meters from you.
                Cautiously, you open the treasure.
                It is filled with gold.
                You have won.
                  ___________
                 '._==_==_=_.'
                 .-\:      /-.
                | (|:.     |) |
                 '-|:.     |-'
                   \::.    /
                    '::. .'
                      ) (
                    _.' '._
                   `"""""""`''')
        else:
            print('''You refuse to open any of the doors.
                Suddenly you notice a presence looking at you from above.
                A soldier is staring at you from a window.
                He shoots you with a crossbow.
                You have died.''')
    else:
        print('''You decide to try swimming to the island. You rapidly notice
            that there are piranahas in the water. You have died.''')
else:
    print('''You walk again for several hours and realise that you are walking endlessly with no end in sight. 
    Suddenly a bear comes and attacks you. You have died.''')
