# INFS 1022 - PROJECT
# -- WEST MARCHES TRAVEL MANAGER --

# IMPORT MODULES
import random
import os

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
encounterCheck = 0
encounterCheckMade = False

## Random Encounters
typeLineNumber = 0
encounterTypeDir = 0

encounterChance = d6

## Party Members
eaters = 4
drinkers = 1

## Rations and Water
rations = 10
rationConsumption = True
if rationConsumption == False:
    rationLabel = "--"
else:
    rationLabel = str(rations)
rationDuration = rations / eaters

## Movement
global movement
movement = 0
movementRate = 24
movementSegment = 6
movementEncounterCheck = movementRate / 2

### Modifiers
totalModifier = 1
varModifier = 1

roads = False
roadsMod = 1.33
hazard = False
hazardMod = 0.67
e_Hazard = False
e_HazardMod = 0.50

### Terrain
terrainMovement = True
terrainType = ["",0,""]
terrainDesert = ["Desert", 1.34, "d.txt"]
terrainHills = ["Hills", 1.34, "b.txt"]
terrainMountains = ["Mountains", 1.5, "b.txt"]
terrainBarren = ["Barren", 1.34, "b.txt"]
terrainSwamp = ["Swamp", 1.5, "s.txt"]
terrainForest = ["Forests", 1.34, "f.txt"]
terrainJungle = ["Jungle", 1.5, "j.txt"]
terrainPlains = ["Grasslands", 1.0, "g.txt"]
terrainOcean = ["Ocean/Sea", 1.0, "o.txt"]
terrainRiver = ["Lake/River", 1.0, "l.txt"]
terrainNothing = [terrainType[0], 0, terrainType[2]]

### Weather
weather = True
activeWeather = "Clear"
weatherCondition = 1
weatherConditionBase = 1

# Functions
# def rationCheck():
#     if rations < 0:

## Dice-roller function from scratch (GOD)
def diceRoller(dX, Xd, displayPrint):
    global dieTotal
    dieTotal = 0
    for dieResult in range(dX):
        dieResult = random.randint(1, Xd)
        dieTotal = dieTotal + dieResult
        if displayPrint == True:
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
    # typeLineNumber = 0
    typeLineNumber = random.randint(0,7)
    print(encounterType[typeLineNumber])
    typeLineNumberDir = int(typeLineNumber) + 9 # Looks for the file directory in the txt file.
    global encounterTypeDir
    encounterTypeDir = encounterType[typeLineNumberDir]
    encounterTypeDir = encounterTypeDir.strip()
    encounterTypeTxt.close()

### Select which terrain to use. Repeated for random terrain selector
def encounterTerrainSelect(terrainName, terrainFile):
    print("Terrain: " + terrainName)
    encounterTypeGenerator(terrainFile)
    input("Enter to Continue...")
    print("")
    encounterGenerator(encounterTypeDir)

# Random Encounter check using 'encounterChance'
def makeEncounterCheck():
    global encounterCheck
    print("Making an encounter check...")
    encounterCheck = random.randint(encounterChance[0], encounterChance[1])
    print(encounterCheck)
    if encounterCheck == 1:
        print("A random encounter has occured!")
        print("")
    else:
        print("No random encounter.")
        print("")

## Time/Turn Checker
# Increments the turn counter by 1, makes an encounter check.
def turnTracker():
    global movement
    global rations
    global eaters
    global encounterCheckMade
    global encounterCheck # ?
    global rationLabel
    movement += totalMovement
    if movement >= int(movementEncounterCheck) and encounterCheckMade == False:
        encounterCheckMade = True
        # Random Encounter Check
        makeEncounterCheck()
        if encounterCheck == 1:
            encounterTerrainSelect(terrainType[0], terrainType[2])

    elif movement >= (int(movementEncounterCheck) * 2):
        # End of Day, Encounter Check + Rations
        makeEncounterCheck()
        if encounterCheck == 1:
            encounterTerrainSelect(terrainType[0], terrainType[2])
        
        print("End of Day.")
        if rationConsumption == True:
            rations -= eaters
            print("Consumed " + str(eaters) + " ration(s).")
            print("")
            rationLabel = str(rations)
            randomWeather()
        
        movement = 0
        encounterCheckMade = False

# Random Weather Generator
def randomWeather():
    diceRoller(2,6,False)
    weatherValue = dieTotal
    global weatherCondition
    global activeWeather
    if weatherValue <= 2:
        # Extreme Weather
        print('''
    Extreme Weather!

    This usually means that there is currently a storm or
    blizzard, making travel extremely difficult and unpleasant.

    The party's movement rate while travelling is reduced by 50%.
    ''')
        activeWeather = "Extreme"
        weatherCondition = 1.5
    elif weatherValue <= 5:
        # Disruptive Weather
        print('''
    Disruptive Weather.

    This usually means that it is currently raining or
    snowing with potentially strong winds, making travel
    slightly more difficult.

    The party's movement rate while travelling is reduced by 33%.
    ''')
        activeWeather = "Disruptive"
        weatherCondition = 1.34
    else:
        # Normal 'Standard' Weather
        activeWeather = "Clear"
        print('''
    Normal Weather.

    It is either sunny or overcast.

    Travel is made at a normal rate.
        ''')
        weatherCondition = 1

    # --------------------------------------- #
    #                MAIN CODE                #
    # --------------------------------------- #

program = True
while program == True:

    if rationConsumption == False:
        rationLabel = "--"
        rationDuration = "an infinite amount"
    else:
        rationLabel = str(rations)
        rationDuration = rations / eaters

    os.system("cls")
    print('''
    ______________________

        HEX-CRAWL TOOL
    ______________________

    RESOURCES:
    PARTY: ''' + str(eaters) + '''
    RATIONS: ''' + str(rationLabel) + '''

    Consuming ''' + str(eaters) + " rations per day. This will last " + str(rationDuration) + ''' days.

    OPTIONS:
    a ) Continue Overland Movement
    b ) Manage Random Encounters [1-in-''' + str(encounterChance[1]) + ''']
    c ) Manage Weather Generation [''' + str(weather) + ''']
    d ) Resource Management
    e ) Terrain Overview
    ''')
    menuInput = input(">> ")

    ###############################################
    # Option A -- CONTINUE OVERLAND TRAVEL        #
    ###############################################

    if menuInput in aList:
        print("You selected option A!")
        overland = True
        while overland == True:
            print("")
            os.system("cls")
            print(" == Active Overland Travel ==")
            print('''
            Movement Used.......... ''' + str(movement) + '''
            ------------------------------------------
            Rations................ ''' + str(rationLabel) + '''
            Hex Terrain............ ''' + str(terrainType) + '''
            Current Weather........ ''' + str(activeWeather) + '''
            Movement Rate.......... ''' + str(movementRate) + ''' miles/day
            Random Encounters...... 1-in-''' + str(encounterChance[1]) + '''
            ------------------------------------------
            Modifiers:''')

            if roads == True:
                print('''
                +Roads''')
            elif hazard == True:
                print('''
                +Hazardous''')
            elif e_Hazard == True:
                print('''
                +Extremely Hazardous''')
            
            if activeWeather == str("Disruptive") or str("Extreme"):
                print('''
                +''' + str(activeWeather))

            print('''
            What hex is the party moving into?
            ------------------------------------------
            a ) Plains/Grasslands
            b ) Forest
            c ) Hills
            d ) Mountains
            e ) Desert
            f ) Swamp
            g ) Barren
            h ) Jungle
            i ) Ocean/Sea
            j ) River/Lake
            ------------------------------------------
            1 ) Toggle roads (33% faster)
            2 ) Toggle hazardous terrain (33% slower)
            3 ) Toggle extremely hazardous terrain (50% slower)

            Current Modifier: x''' + str(varModifier) + '''
            ------------------------------------------
            z ) Back''')

            menuInput = input(">> ")

            # In order:
            # 1. Determine terrain of the hex being moved into
            # 2. Update Time Record
            # 3. @ 1/2 movement make encounter check
            # 4. Repeat until out of movement -->
            # 5. Encounter Check 2
            # 6. Roll Weather

            if menuInput in zList:
                overland = False
            else:

                # Modifier Options
                if menuInput == "1":
                    roads = not roads
                    hazard = False
                    e_Hazard = False
                    if roads == True:
                        varModifier = 0.66
                    else:
                        varModifier = 1

                elif menuInput == "2":
                    hazard = not hazard
                    roads = False
                    e_Hazard = False
                    if hazard == True:
                        varModifier = 1.34
                    else:
                        varModifier = 1
                    
                elif menuInput == "3":
                    e_Hazard = not e_Hazard
                    roads = False
                    hazard = False
                    if e_Hazard == True:
                        varModifier = 1.5
                    else:
                        varModifier = 1

                # Terrain Options
                elif menuInput in aList:
                    terrainType = terrainPlains
                elif menuInput in bList:
                    terrainType = terrainForest
                elif menuInput in cList:
                    terrainType = terrainHills
                elif menuInput in dList:
                    terrainType = terrainMountains
                elif menuInput in eList:
                    terrainType = terrainDesert
                elif menuInput in fList:
                    terrainType = terrainSwamp
                elif menuInput in gList:
                    terrainType = terrainBarren
                elif menuInput in hList:
                    terrainType = terrainJungle
                elif menuInput in iList:
                    terrainType = terrainOcean
                elif menuInput in jList:
                    terrainType = terrainRiver
                else:
                    terrainType = terrainNothing
                print("")
                totalModifier = terrainType[1] * varModifier * weatherCondition
                print("Hex Terrain: " + terrainType[0])
                print("Total Movement Modifier: " + str(totalModifier))
                totalMovement = totalModifier * movementSegment
                totalMovement = round(totalMovement)
                print("Total Movement: " + str(totalMovement))
                print("")
                turnTracker()
                input("Press Enter to Continue...")
                        


    ###############################################
    # Option B -- RANDOM ENCOUNTERS               #
    ###############################################

    if menuInput in bList:
        print("Selected option B!")
        encounterMenu = True
        while encounterMenu == True:
            print('''
    == Random Encounter Menu ==
    Random Encounter checks are made every day and
    every night when the party camps.

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
    Generating an encouter by TERRAIN:

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
                    def encounterByTerrainFunc(menuInput):
                        if menuInput in aList:
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
                    encounterByTerrainFunc(menuInput)

            # OPTION C: Random encounter check
            elif menuInput in cList:
                # See Functions
                makeEncounterCheck()

            # OPTION D: Adjust encounter chances
            elif menuInput in dList:
                # Adjusts what 'die' is rolled. result is stored in 'encounterChance'
                print("")
                print("Adjusting encounter chance:")
                print("Current: " + str(encounterChance))
                print('''
    What die is rolled for the new encounter chance?
    (1-in-x) In order to roll a random encounter, 
    a 1 must be rolled.

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
    # Option C -- WEATHER GENERATION              #
    ###############################################

    elif menuInput in cList:
        print("")
        print("Selected Option C!")
        weatherMenu = True
        while weatherMenu == True:
            print('''
    == Weather Menu ==
    Weather Enabled: ''' + str(weather) + '''
    Weather: ''' + str(activeWeather) + '''
            
    Weather checks are made at the beginning of every day,
    and may impact then movement rate of the party when travelling.
            
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
                print("Rolling 2d6 to determine weather") # 2d6 in order to generate a bell-curve probability (more likely to get ~7, least likely to get 2 or 12).

                # Moved, see #Functions
                randomWeather()

            elif menuInput in bList:
                print("Weather Table:")
                print('''
                1-2:   Extreme Weather.......-50% Travel Speed)
                3-5:   Disruptive Weather....-33% Travel Speed)
                6-12:  Normal Weather........No Travel Speed Penalty)
                ''')

            elif menuInput in cList:
                manualWeather = True
                while manualWeather == True:
                    print("Manual Weather")
                    print('''
                    a ) Clear Weather
                    b ) Disruptive Weather
                    c ) Extreme Weather

                    Current Weather: ''' + str(activeWeather) + ''' Weather

                    z ) Back
                    ''')
                    menuInput = input(">> ")
                    if menuInput in zList:
                        manualWeather = False
                    elif menuInput in aList:
                        activeWeather = "Clear"
                        weatherCondition = 1.0
                    elif menuInput in bList:
                        activeWeather = "Disruptive"
                        weatherCondition = 1.34
                    elif menuInput in cList:
                        activeWeather = "Extreme"
                        weatherCondition = 1.5
            elif menuInput in dList: 
                if weather == True:
                    weather = False
                    activeWeather = "None"
                    weatherCondition = 1.0
                else:
                    weather = True


    ###############################################
    # Option D -- RESOURCE MANAGEMENT             #
    ###############################################
    elif menuInput in dList:
        resourceMenu = True
        while resourceMenu == True:
            print('''
    == Resource Menu ==

    Ration Consumption: ''' + str(rationConsumption) + '''
    Rations Total: ''' + str(rations) + '''

    Party Members: ''' + str(eaters) + '''

    a ) Add rations
    b ) Turn off ration consumption
    c ) Adjust party size
    z ) Back
    ''')
            menuInput = input(">> ")
            if menuInput in zList:
                resourceMenu = False
            elif menuInput in aList:
                print('''
    Add how many rations?
    (Can be positive or negative)
                ''')
                menuInput = input(">> ")
                if menuInput == "":
                    rations += 0
                else:
                    rations += int(menuInput)
            elif menuInput in bList:
                if rationConsumption == True:
                    print("Ration consumption disabled!")
                    rationConsumption = False
                else:
                    print("Ration consumption enabled!")
                    rationConsumption = True
            elif menuInput in cList:
                print('''
    How many party members?
    ''')
                menuInput = input(">> ")
                if menuInput == "":
                    eaters += 0
                else:
                    eaters = menuInput

    ###############################################
    # Option E -- TERRAIN OVERVIEW                #
    ###############################################
    # Terrain is actually handled at the top under ##variables.
    elif menuInput in eList:
        terrainMenu = True
        while terrainMenu == True:
            print('''
    == Terrain Overview ==
    ------------------------------------------
    Plains/Grasslands:...........Full Movement
    Maintained Roads:............+33% Movement
    ------------------------------------------
    Barren/Hills:................-33% Movement
    Forests:.....................-33% Movement
    Deserts:.....................-33% Movement
    ------------------------------------------
    Swamps:......................-50% Movement
    Mountains:...................-50% Movement
    Jungle:......................-50% Movement
    ------------------------------------------

    z ) Back
    ''')
            menuInput = input(">> ")
            if menuInput in zList:
                terrainMenu = False