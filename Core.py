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
    1/a ) Continue Overland Movement
    2/b ) Adjust movement rate [4 hexes/day]
    3/c ) Configure feature discovery [ X ]
    4/d ) Manage random encounters [1-in-6]
    5/e ) Manage weather generation [Generic]
    6/f ) Resource management
    7/g ) Terrain overview
    ''')

    # Options with brackets on the end will be later subsituted with stringified variables.

    menuInput = input(">> ")
    if menuInput == "a":
        print("You selected option A!")
    else:
        print("Something went wrong.")