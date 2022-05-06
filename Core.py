# INFS 1022 - PROJECT
# -- WEST MARCHES TRAVEL MANAGER --

# IMPORT MODULES
import random

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
## Random Encounters
typeLineNumber = 0
encounterTypeDir = 0

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

## Encounter Functions
### Generate encounter from type
def encounterGenerator(tableFile):
    encounterTxt = open(tableFile, "r")
    encounter = encounterTxt.readlines()
    print(encounter[random.randint(0,11)]) # 1-12 / roll 1d12
    encounterTxt.close()
    # Since it's only used for printing, doesn't need an associated number

### Generate type from terrain
def encounterTypeGenerator(tableTypeFile):
    encounterTypeTxt = open(tableTypeFile, "r")
    encounterType = encounterTypeTxt.readlines()
    typeLineNumber = 0
    # typeLineNumber = random.randint(0,7) # 1-8 / roll 1d8
    print(encounterType[typeLineNumber])
    typeLineNumberDir = int(typeLineNumber) + 9 # Looks for the file directory in the txt file.
    # print(typeLineNumberDir) These were for testing
    # print(encounterType[typeLineNumberDir])
    global encounterTypeDir
    encounterTypeDir = encounterType[typeLineNumberDir]
    encounterTypeDir = encounterTypeDir.strip()
    print(encounterTypeDir)
    encounterTypeTxt.close()

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
    # Option A -- Continue Overland Travel
    if menuInput in aList:
        print("You selected option A!")
        overland = True
        while overland == True:
            print("Begin Overland travel")
            input("")
            # finish this later lol.

    # Option D -- RANDOM ENCOUNTERS
    if menuInput in dList:
        print("You selected option D!")
        encounterMenu = True
        while encounterMenu == True:
            print(" == Random Encounter Menu ==")
            print('''
            a ) Generate a random encounter
            b ) Generate a random encounter by TERRAIN
            c ) Generate a random encounter by TYPE
            d ) Adjust random encounter chance
            ''')
            menuInput = input(">> ")
            if menuInput in aList:
                print("Generating a (completely) random encounter")
                rEncounterTerrain = 1
                # rEncounterTerrain = random.randint(1,8) # Determine random terrain type
                # rEncounterType = random.randint(1,8) # Determine type early.

                # 1 = BHM, 2 = Desert, 3 = Forest, 4 = grasslands, 5 = jungle,
                # 6 = Lake/River, 7 = Ocean/Sea, 8 = Swamp

                if rEncounterTerrain == 1: # Barren, Hills, Mountains (B)
                    print("Terrain: Barren, Hills, Mountains")
                    encounterTypeGenerator("b.txt")
                    input("Enter to Continue")
                    encounterGenerator(encounterTypeDir)


    # Option Z -- Test Menu
    elif menuInput in zList:
        print("You selected option Z: manual feature testing!")
        zMode = True
        while zMode == True:
            print("Test What?")
            print("a ) Generate Random Encounter")
            menuInput = input(">> ")
            # -- A -- Generate Encounter
            if menuInput in aList:
                zEncounter = True
                while zEncounter == True:
                    print("Print 1 random BHM - Humanoids?")
                    menuInput = input(">> ")
                    if menuInput in yesList:
                        encounterGenerator("b_humanoids.txt")
                        print("Generate another monster?")
                        menuInput = input(">> ")
                        if menuInput in yesList:
                            print("")
                        elif menuInput in noList:
                            zEncounter = False
            else:
                print("Something went wrong. Try yes.")
    else:
        print("Something went wrong.")