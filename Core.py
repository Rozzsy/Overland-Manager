# INFS 1022 - PROJECT
# -- WEST MARCHES TRAVEL MANAGER --

# IMPORT MODULES
import random
import time

# DESIGN:
    # Overland travel movement allowance
    # Overland random encounters & occurance
    # Discovery of features (overt & hidden)
    # Management of resources (rations/water)
    # Automation of weather encounters and adjustments to travel

# Chances are I'm going to use textfiles located in the same folder to load up tables in combination with the (random) module.

# Agreement lists
yesList = ["yes", "y"]
noList = ["no", "n"]

aList = ["a", "A"]
bList = ["b", "B"]
cList = ["c", "C"]
dList = ["d", "D"]
eList = ["e", "E"]
fList = ["f", "F"]
gList = ["g", "G"]
hList = ["h", "H"]
iList = ["i", "I"]
jList = ["j", "J"]
zList = ["z", "Z"]

#Variables
## Party Members
eaters = 4
drinkers = 4

## Rations and Water
rations = 28
if rations == -100:
    rationLabel = "--"
else:
    rationLabel = str(rations)
rationDuration = rations / eaters

water = -100
if water == -100:
    waterLabel = "--"
else:
    waterLabel = str(water)



# Functions
# def rationCheck():
#     if rations < 0:


# Main code
program = True
while program == True:
    print('''
    HEX-CRAWL TOOL
    ================''')
    print("RESOURCES:")
    print("RTN: " + str(rationLabel))
    print("WTR: " + str(waterLabel))
    print(("Consume ") + str(eaters) + (" rations and ") + str(drinkers) + (" water per day. This will last ") + str(rationDuration) + (" days."))

    print('''
    OPTIONS:
    a ) Continue Overland Movement
    b ) Adjust movement rate [4 hexes/day]
    c ) Configure feature discovery [ X ]
    d ) Manage random encounters [1-in-6]
    e ) Manage weather generation [Generic]
    f ) Resource management
    g ) Terrain overview
    z ) Test Menu
    ''')

    # Options with brackets on the end will be later subsituted with stringified variables.

    menuInput = input(">> ")
    if menuInput in aList:
        print("You selected option A!")
        overland = True
        while overland == True:
            print("Begin Overland travel")

    elif menuInput in zList:
        print("You selected option Z: feature testing!")
        zMode = True
        while zMode == True:
            print("Test What?")
            print("a ) Generate Random Encounter")
            menuInput = input(">> ")
            if menuInput in aList:
                zEncounter = True
                while zEncounter == True:
                    print("Print 1 random BHM - Humanoids?")
                    menuInput = input(">> ")
                    if menuInput in yesList:
                        bhmHumanmoids = open("bhm_humanoids.txt", "r")
                        bhmHumanoidsEncounter = bhmHumanmoids.readlines()
                        print(bhmHumanoidsEncounter[random.randint(0,11)])
                        bhmHumanmoids.close()
                        input(">> ")
            else:
                print("Something went wrong. Try yes.")
    else:
        print("Something went wrong.")