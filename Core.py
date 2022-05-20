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
    # E ) 80%
    # F ) 20%
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

## Movement
### Terrain
terrainMovement = True

### Weather
activeWeather = True
weatherCondition = 100
weatherConditionBase = 100
weatherValue = 10

# Functions
# def rationCheck():
#     if rations < 0:

## Dice-roller function from scratch (GOD)
def diceRoller(dX, Xd):
    global dieTotal
    dieTotal = 0
    for dieResult in range(dX):
        dieResult = random.randint(1, Xd)
        dieTotal = dieTotal + dieResult
        print(dieResult)
    else:
        print("total: " + str(dieTotal))

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
    b ) Adjust Movement Rate [4 hexes/day]
    c ) Configure Feature Discovery [ OFF ]
    d ) Manage Random Encounters [1-in-''' + str(encounterChance[1]) + ''']
    e ) Manage Weather Generation [''' + str(activeWeather) + ''']
    f ) Resource Management
    g ) Terrain Overview
    ''')

    # Options with brackets on the end will be later subsituted with stringified variables.

    menuInput = input(">> ")

    ###############################################
    # Option A -- CONTINUE OVERLAND TRAVEL        # #
    ###############################################

    if menuInput in aList:
        print("You selected option A!")
        overland = True
        while overland == True:
            print("")
            print("Begin Overland travel")
            input("")
            # finish this later lol.

    ###############################################
    # Option D -- RANDOM ENCOUNTERS               # # # # #
    ###############################################

    if menuInput in dList:
        print("You selected option D!")
        encounterMenu = True
        while encounterMenu == True:
            print("")
            print(" == Random Encounter Menu == ")
            print('''Random Encounter checks are made every day and every night when the party camps.

            a ) Generate a random encounter
            b ) Generate a random encounter by TERRAIN
            c ) Make a random encounter check
            d ) Adjust random encounter chance
            z ) Exit
            ''')
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
                    print('''
                    Generating an encouter by TERRAIN:)             
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

            # OPTION C: Random encounter check
            elif menuInput in cList:
                # Random Encounter check using 'encounterChance'
                print("Making an encounter check:")
                encounterCheck = random.randint(encounterChance[0], encounterChance[1])
                print(encounterCheck)
                if encounterCheck == 1:
                    print("A random encounter has occured!")
                else:
                    print("No random encounter.")

            # OPTION D: Adjust encounter chances
            elif menuInput in dList:
                # Adjusts what 'die' is rolled. result is stored in 'encounterChance'
                print("")
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
                    print("To turn off random encounters, put '0'.")
                    customChance = input(">> ")
                    encounterChance = dCustom
                    dCustom = [1, customChance]
                print(encounterChance)
                
    ###############################################
    # Option E -- WEATHER GENERATION              # # # # # #
    ###############################################

    elif menuInput in eList:
        print("")
        print("You selected Option E!")
        weatherMenu = True
        while weatherMenu == True:
            print("")
            print(" == Weather Menu == ")
            print("Weather: " + str(activeWeather))
            print('''Weather checks are made at the beginning of every day, and may impact then movement rate of the party when travelling.
            
            a) Make a weather check
            b) Look at the weather table
            c) Manually set weather for the day
            d) Toggle weather checks
            z) Back
            ''')
            menuInput = input(">> ")
            if menuInput in zList:
                weatherMenu = False
            elif menuInput in aList:
                # Option A: Weather check
                print("Rolling 3d6 to determine weather") # 2d6 in order to generate a bell-curve probability (more likely to get ~7, least likely to get 2 or 12).
                diceRoller(2,6)
                weatherValue = dieTotal
                if weatherValue <= 2:
                    # Extreme Weather
                    print("Extreme Weather!")
                    print("This usually means that there is currently a storm of blizzard, making travel extremely difficult and unpleasant.")
                    print("")
                    print("The party's movement rate while travelling is reduced by 50%.")
                    weatherCondition = 0.5
                    print("")
                elif weatherValue <= 5:
                    # Disruptive Weather
                    print("Disruptive Weather.")
                    print("This usually means that it is currently raining or snowing with potentially strong winds, making travel slightly more difficult.")
                    print("")
                    print("The party's movement rate while travelling is reduced by 33%.")
                    weatherCondition = 0.67
                    print("")
                else:
                    # Normal 'Standard' Weather
                    print("Normal weather.")
                    print("It is either sunny or overcast.")
                    print("")
                    print("Travel is made at a normal rate.")
                    weatherCondition = 0
                    print("")
            elif menuInput in bList:
                print("Weather Table:")
                print('''
                1-2:   Extreme Weather......(-50% Travel Speed)
                3-5:   Disruptive Weather...(-33% Travel Speed)
                6-12:  Normal Weather.......(No Travel Speed Penalty)
                ''')

    ###############################################
    # Option F -- RESOURCE MANAGEMENT             #
    ###############################################

    ###############################################
    # Option G -- TERRAIN OVERVIEW                #
    ###############################################
    # Terrain is actually handled at the top of the document under ##variables.
    elif menuInput in gList:
        terrainMenu = True
        while terrainMenu == True:
            print("")
            print(" == Terrain Overview == ")
            print('''
            -----------------------------------------
            Plains/Grasslands:..........Full Movement
            Maintained Roads:...........+33% Movement
            -----------------------------------------
            Barren/Hills:...............-33% Movement
            Forests:....................-33% Movement
            -----------------------------------------
            Swamps:.....................-50% Movement
            Mountains:..................-50% Movement
            Jungle:.....................-50% Movement
            -----------------------------------------
            
            a ) Toggle Terrain [Currently: ''' + str(terrainMovement) + ''']
            z ) Back
            ''')
            menuInput = input(">> ")
            if menuInput in zList:
                terrainMenu = False
            elif menuInput in aList:
                # Toggle terrain movement penalty 
                if terrainMovement == True:
                    terrainMovement = False
                else:
                    terrainMovement = True
        
    ###############################################
    # Option Z -- TEST MENU                       #
    ###############################################

    elif menuInput in zList:
        print("You selected option Z: manual feature testing!")
        zMode = True
        while zMode == True:
            print('''
            Test What?
            a ) Generate Random Encounter
            b ) DieRoller
            z ) Back''')
            menuInput = input(">> ")
            # -- A -- Generate 
            if menuInput in zList:
                zMode = False
            elif menuInput in aList:
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
            elif menuInput in bList:
                print("Die Roller. Formula is equal to = XdY")
                dx = input("X = ")
                dy = input("Y = ")
                diceRoller(int(dx), int(dy))
            else:
                print("Something went wrong. Try again.")
    else:
        print("Something went wrong. Try again.")