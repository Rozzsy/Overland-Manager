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

# TO-DO
    # A ) 1%
    # B ) 0%
    # C ) 0%
    # D ) 100%
    # E ) 0%
    # F ) 0%
    # G ) 0%
    # Z ) 20% (not that it matters)

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

# Dice-range list
d4 = [1,4]
d6 = [1,6]
d8 = [1,8]
d10 = [1,10]
d12 = [1,12]
d20 = [1,20]
d100 = [1,100]

customChance = 0
dCustom = [1, customChance]

followThrough = zList

#Variables
## Random Encounters
typeLineNumber = 0
encounterTypeDir = 0

encounterChance = d6

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
    # print(typeLineNumberDir)
    # print(encounterType[typeLineNumberDir]) These were for testing
    global encounterTypeDir
    encounterTypeDir = encounterType[typeLineNumberDir]
    encounterTypeDir = encounterTypeDir.strip()
    # print(encounterTypeDir) # Remove/Comment out once its no longer needed for testing
    encounterTypeTxt.close()

### Select which terrain to use. Repeated for random terrain selector
def encounterTerrainSelect(terrainName, terrainFile):
    print("Terrain: " + terrainName)
    encounterTypeGenerator(terrainFile)
    input("Enter to Continue")
    print("")
    encounterGenerator(encounterTypeDir)

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
    c ) Configure feature discovery [ OFF ]
    d ) Manage random encounters [1-in-''' + str(encounterChance[1]) + ''']
    e ) Manage weather generation [Generic]
    f ) Resource management
    g ) Terrain overview
    ''')

    # Options with brackets on the end will be later subsituted with stringified variables.

    menuInput = input(">> ")

    ###############################################
    # Option A -- CONTINUE OVERLAND TRAVEL        #
    ###############################################
    if menuInput in aList:
        print("You selected option A!")
        overland = True
        while overland == True:
            print("Begin Overland travel")
            input("")
            # finish this later lol.

    ###############################################
    # Option D -- RANDOM ENCOUNTERS               #
    ###############################################
    if menuInput in dList:
        print("You selected option D!")
        encounterMenu = True
        while encounterMenu == True:
            print(" == Random Encounter Menu ==")
            print('''Random Encounter checks are made every day and every night when the party camps.

            a ) Generate a random encounter
            b ) Generate a random encounter by TERRAIN
            c ) Make a random encounter check
            d ) Adjust random encounter chance
            z ) Exit
            ''')
            # A = Done
            # B = Not done
            # C = Not done
            # D = Done
            # E = Done
            menuInput = input(">> ")
            if menuInput in zList:
                encounterMenu = False
            
            # OPTION A: Completely random encounter
            elif menuInput in aList:
                print("Generating a (completely) random encounter:")
                rEncounterTerrain = random.randint(1,8) # Determine random terrain type
                rEncounterType = random.randint(1,8) # Determine type early.

                # 1 = BHM, 2 = Desert, 3 = Forest, 4 = Grasslands, 5 = Jungle,
                # 6 = Lake/River, 7 = Ocean/Sea, 8 = Swamp

                if rEncounterTerrain == 1: # Barren, Hills, Mountains (B)
                    encounterTerrainSelect("Barren, Hills, Mountains", "b.txt")
                elif rEncounterTerrain == 2: # Desert (D)
                    encounterTerrainSelect("Desert", "d.txt")
                elif rEncounterTerrain == 3: # Forest (F)
                    encounterTerrainSelect("Forest", "f.txt")
                elif rEncounterTerrain == 4: # Grasslands (G)
                    encounterTerrainSelect("Grasslands", "g.txt")
                elif rEncounterTerrain == 5: # Jungle (J)
                    encounterTerrainSelect("Jungle", "d.txt")
                elif rEncounterTerrain == 6: # Lake/River (L)
                    encounterTerrainSelect("Lake/River", "l.txt")
                elif rEncounterTerrain == 7: # Ocean/Sea (O)
                    encounterTerrainSelect("Ocean/Sea", "o.txt")
                elif rEncounterTerrain == 8: # Swamp (S)
                    encounterTerrainSelect("Swamp", "s.txt")

            # OPTION B: Encounter by TERRAIN
            elif menuInput in bList:
                generateByTerrain = True
                while generateByTerrain == True:
                    print('''Generating an encouter by TERRAIN:)             
                    a ) Barren, Hills, Mountain
                    b ) Desert
                    c ) Forest
                    d ) Grassland
                    e ) Jungle
                    f ) Lake/River
                    g ) Oceans/Sea
                    h ) Swamp
                    z ) Back
                    ''')
                    menuInput = input(">> ")
                    if menuInput in zList:
                        generateByTerrain = False
                    elif menuInput in aList:
                        encounterTerrainSelect("Barren, Hills, Mountains", "b.txt")
                    elif menuInput in bList:
                        encounterTerrainSelect("Desert", "d.txt")
                    elif menuInput in cList:
                        encounterTerrainSelect("Forests", "f.txt")
                    elif menuInput in dList:
                        encounterTerrainSelect("Grasslands","g.txt")
                    elif menuInput in eList:
                        encounterTerrainSelect("Jungle","j.txt")
                    elif menuInput in fList:
                        encounterTerrainSelect("Lake/River","l.txt")
                    elif menuInput in gList:
                        encounterTerrainSelect("Ocean/Sea","o.txt")
                    elif menuInput in hList:
                        encounterTerrainSelect("Swamp", "s.txt")

            # # OPTION C: Encounter by TYPE
            # elif menuInput in cList:
            #     generateByType = True
            #     while generateByType == True:
            #         print('''Generating an encouter by TYPE:)             
            #         a ) Animal
            #         b ) Dragon
            #         c ) Flyer
            #         d ) Insect
            #         e ) Human
            #         f ) Humanoid
            #         g ) Swimmer
            #         h ) Undead
            #         i ) Unusual
            #         z ) Back
            #         ''')
            #         menuInput = input(">> ")
            #         if menuInput in zList:
            #             generateByTerrain = False
            #         elif menuInput in aList:
            #             randomType = random.randint(1,6)
            #             encounterTypeGenerator()
            #         elif menuInput in bList:
            #             encounterTypeGenerator()
            #         elif menuInput in cList:
            #             encounterTypeGenerator()
            #         elif menuInput in dList:
            #             encounterTypeGenerator()
            #         elif menuInput in eList:
            #             encounterTypeGenerator()
            #         elif menuInput in fList:
            #             encounterTypeGenerator()
            #         elif menuInput in gList:
            #             encounterTypeGenerator()
            #         elif menuInput in hList:
            #             encounterTypeGenerator()
            #         elif menuInput in iList:
            #             encounterTypeGenerator()

            # OPTION D: Random encounter check
            elif menuInput in dList:
                # Random Encounter check using 'encounterChance'
                print("Making an encounter check:")
                encounterCheck = random.randint(encounterChance[0], encounterChance[1])
                print(encounterCheck)
                if encounterCheck == 1:
                    print("A random encounter has occured!")
                else:
                    print("No random encounter.")

            elif menuInput in eList:
                # Adjusts what 'die' is rolled. result is stored in 'encounterChance'
                print("Adjusting encounter chance:")
                print("Current: " + str(encounterChance))
                print('''What die is rolled for the new encounter chance? (1-in-x) In order to roll a random encounter, a 1 must be rolled.
                a ) Always encounter (100%)
                b ) 1d4 (25%)
                c ) 1d6 (16.66%, default)
                d ) 1d8 (12.5%)
                e ) 1d10 (10%)
                f ) 1d12 (8.33%)
                g ) 1d20 (5%)
                h ) Custom (1dX)
                z ) Back
                ''')
                menuInput = input(">> ")
                if menuInput in zList:
                    print("")
                elif menuInput in aList:
                    encounterChance = 1
                elif menuInput in bList:
                    encounterChance = d4
                elif menuInput in cList:
                    encounterChance = d6
                elif menuInput in dList:
                    encounterChance = d8
                elif menuInput in eList:
                    encounterChance = d10
                elif menuInput in fList:
                    encounterChance = d12
                elif menuInput in gList:
                    encounterChance = d20
                elif menuInput in hList:
                    print("enter the new encounter chance (1-in-X)")
                    print("To turn of random encounters, put '0'.")
                    customChance = input(">> ")
                    encounterChance = dCustom
                    dCustom = [1, customChance]
                print(encounterChance)
                
    ###############################################
    # Option E -- WEATHER GENERATION              #
    ###############################################
    elif menuInput in eList:
        print("You selected Option E!")
        weatherMenu = True
        # while weatherMenu == True:


    ###############################################
    # Option Z -- TEST MENU                       #
    ###############################################
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
                print("Something went wrong. Try again.")
    else:
        print("Something went wrong.")