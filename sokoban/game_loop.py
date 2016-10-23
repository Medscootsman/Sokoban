#--------------.-----------------------------------------------------------------
# Name:        module1
# Purpose:      videogames
#
# Author:      murra_000
#
# Created:     02/12/2015
# Copyright:   (c) murra_000 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random, sys, copy, os, pygame, pygame.image
from pygame.locals import *
from player import Player
from map import Map
from progression_WIP import Progression
from movvable_object import Movvable_Object

FPS = 60 #Melee speed yo. Frames per second to update the screen.
WINWIDTH = 1280 # width of the program's window, in pixels
WINHEIGHT = 720 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2) #you need to know 1/2 sizes so you can
HALF_WINHEIGHT = int(WINHEIGHT / 2) #place things centrally

# The total width and height of each tile in pixels.
TILEWIDTH = 64
TILEHEIGHT = 64
TILEFLOORHEIGHT = 64

BRIGHTBLUE = (  0, 170, 255)
WHITE      = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

#Set up objects
player = Player()
map_obj = Map()
progress = Progression()

#cplayere will go here when we make it
#diamond too prolly

def MoveRight():
    crate = False
    crateonGoal = False
    Diamond = False
    player.setCanMove(False) #Set to false every time everytime it's called
    x = player.getCol()
    y = player.getRow()
    #First, find out if the player can actually move to the right
    if (map_obj.checkMove(y, x+1)):
        player.setCanMove(True)
    #Now check if the player is next to a crate, if so keep a note of it.
        if (map_obj.CheckforCrate(y, x+1) or (map_obj.CheckforPlayerOnCrate(y, x+1))):
            crate = True

            if (map_obj.checkMove(y, x+2)): #Check for walls.
                crate = True
                player.setCanMove(True)

            else:
                crate = False
                player.setCanMove(False)

            if map_obj.CheckForDiamond(y,x+2):
                crateonGoal = True
        if (map_obj.CheckforPlayerOnCrate(y, x+1)):
            crate = True
            Diamond = True #So we don't end up moving the diamond

            #Make sure there isn't a crate next to it.
            if (map_obj.CheckforCrate(y, x+2) or (map_obj.CheckforPlayerOnCrate(y, x+2))):
                crate = False
                player.setCanMove(False)

            if (map_obj.checkMove(y, x+2) == False):
                crate = False
                player.setCanMove(False)


        #Now make sure there isn't a crate next to the crate.
        if(map_obj.CheckforCrate(y, x+1) or (map_obj.CheckforPlayerOnCrate(y, x+1))):
            if (map_obj.CheckforCrate(y, x+2)or (map_obj.CheckforPlayerOnCrate(y,x+2))):
                crate = False
                player.setCanMove(False)


    if (crate == True):
        map_obj.ClearatPositon(y, x+1, ' ')
        if crateonGoal == True:
            map_obj.ClearatPositon(y, x+2, "&")
        else:
            map_obj.ClearatPositon(y, x+2, '$')
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())

    if (player.CanMove == True):
        if (player.getDiamond()):
            map_obj.ClearatPositon(y, x, "@")
            player.setOnDiamond(False)
        else:
            if (map_obj.CheckForDiamond(y, x+1)) or Diamond == True:
                player.setOnDiamond(True)
            map_obj.ClearatPositon(y, x, ' ')
        player.MoveRight()
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())
        player.IncrementTurn() #Increment when a move is made
        progress.IncrementMoves() #Keeps total moves used during session.

def MoveLeft():
    crate = False
    crateonGoal = False
    Diamond = False
    player.setCanMove(False) #Set to false every time everytime it's called
    x = player.getCol()
    y = player.getRow()
    #First, find out if the player can actually move to the right
    if (map_obj.checkMove(y, x-1)):
        player.setCanMove(True)
    #Now check if the player is next to a crate, if so keep a note of it.
        if (map_obj.CheckforCrate(y, x-1) or (map_obj.CheckforPlayerOnCrate(y, x-1))):
            crate = True

            if (map_obj.checkMove(y, x-2)): #Check for walls.
                crate = True
                player.setCanMove(True)

            else:
                crate = False
                player.setCanMove(False)

            if map_obj.CheckForDiamond(y,x-2):
                crateonGoal = True
        if (map_obj.CheckforPlayerOnCrate(y, x-1)):
            crate = True
            Diamond = True #So we don't end up moving the diamond

            #Make sure there isn't a crate next to it.
            if (map_obj.CheckforCrate(y, x-2) or (map_obj.CheckforPlayerOnCrate(y, x-2))):
                crate = False
                player.setCanMove(False)

            if (map_obj.checkMove(y, x-2) == False):
                crate = False
                player.setCanMove(False)


        #Now make sure there isn't a crate next to the crate.
        if(map_obj.CheckforCrate(y, x-1) or (map_obj.CheckforPlayerOnCrate(y, x-1))):
            if (map_obj.CheckforCrate(y, x-2)or (map_obj.CheckforPlayerOnCrate(y,x-2))):
                crate = False
                player.setCanMove(False)


    if (crate == True):
        map_obj.ClearatPositon(y, x-1, ' ') #Crate movement
        if crateonGoal == True:
            map_obj.ClearatPositon(y, x-2, "&")
        else:
            map_obj.ClearatPositon(y, x-2, '$')
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())

    if (player.CanMove == True): #Player and diamond movement
        if (player.getDiamond()):
            map_obj.ClearatPositon(y, x, "@")
            player.setOnDiamond(False)
        else:
            if (map_obj.CheckForDiamond(y, x-1)) or Diamond == True:
                player.setOnDiamond(True)
            map_obj.ClearatPositon(y, x, ' ')
        player.MoveLeft()
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())
        player.IncrementTurn() #Increment every time.
        progress.IncrementMoves() #keeps total moves used during session

def MoveDown():
    crate = False
    crateonGoal = False
    Diamond = False
    player.setCanMove(False) #Set to false every time everytime it's called
    x = player.getCol()
    y = player.getRow()
    #First, find out if the player can actually move to the right
    if (map_obj.checkMove(y+1, x)):
        player.setCanMove(True)
    #Now check if the player is next to a crate, if so keep a note of it.
        if (map_obj.CheckforCrate(y+1, x) or (map_obj.CheckforPlayerOnCrate(y+1, x))):
            crate = True

            if (map_obj.checkMove(y+2, x)): #Check for walls.
                crate = True
                player.setCanMove(True)

            else:

                crate = False
                player.setCanMove(False)

            if map_obj.CheckForDiamond(y+2,x):
                crateonGoal = True
        if (map_obj.CheckforPlayerOnCrate(y+1, x)):
            crate = True
            Diamond = True #So we don't end up moving the diamond
            #Make sure there isn't a crate next to it.
            if (map_obj.CheckforCrate(y+2, x) or (map_obj.CheckforPlayerOnCrate(y, x-2))):
                crate = False
                player.setCanMove(False)

            if (map_obj.checkMove(y+2, x) == False):
                crate = False
                player.setCanMove(False)


        #Now make sure there isn't a crate next to the crate.
        if(map_obj.CheckforCrate(y+1, x) or (map_obj.CheckforPlayerOnCrate(y+1, x))):
            if (map_obj.CheckforCrate(y+2, x)or (map_obj.CheckforPlayerOnCrate(y+2,x))):
                crate = False
                player.setCanMove(False)


    if (crate == True):
        map_obj.ClearatPositon(y+1, x, ' ')
        if crateonGoal == True:
            map_obj.ClearatPositon(y+2, x, "&")
        else:
            map_obj.ClearatPositon(y+2, x, '$')
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())

    if (player.CanMove == True):
        if (player.getDiamond()):
            map_obj.ClearatPositon(y, x, "@")
            player.setOnDiamond(False)
        else:
            if (map_obj.CheckForDiamond(y+1, x)) or Diamond == True:
                player.setOnDiamond(True)
            map_obj.ClearatPositon(y, x, ' ')
        player.MoveDown()
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())
        player.IncrementTurn()
        progress.IncrementMoves()

def MoveUp():
    crate = False
    crateonGoal = False
    Diamond = False
    player.setCanMove(False) #Set to false every time everytime it's called
    x = player.getCol()
    y = player.getRow()
    #First, find out if the player can actually move to the right
    if (map_obj.checkMove(y-1, x)):
        player.setCanMove(True)
    #Now check if the player is next to a crate, if so keep a note of it.
        if (map_obj.CheckforCrate(y-1, x) or (map_obj.CheckforPlayerOnCrate(y-1, x))):
            crate = True

            if (map_obj.checkMove(y-2, x)): #Check for walls.
                crate = True
                player.setCanMove(True)

            else:

                crate = False
                player.setCanMove(False)

            if map_obj.CheckForDiamond(y-2,x):
                crateonGoal = True

        #Now we check for crates on a goal, since they use different characters.
        if (map_obj.CheckforPlayerOnCrate(y-1, x)):
            crate = True
            Diamond = True #So we don't end up moving the diamond
            #Make sure there isn't a crate next to it.
            if (map_obj.CheckforCrate(y-2, x) or (map_obj.CheckforPlayerOnCrate(y, x-2))):
                crate = False
                player.setCanMove(False)

            if (map_obj.checkMove(y-2, x) == False): #Double check for walls
                crate = False
                player.setCanMove(False)


        #Now make sure there isn't a crate next to the crate.
        if(map_obj.CheckforCrate(y-1, x) or (map_obj.CheckforPlayerOnCrate(y-1, x))):
            if (map_obj.CheckforCrate(y-2, x)or (map_obj.CheckforPlayerOnCrate(y-2,x))):
                crate = False
                player.setCanMove(False)


    if (crate == True):
        map_obj.ClearatPositon(y-1, x, ' ')
        if crateonGoal == True:
            map_obj.ClearatPositon(y-2, x, "&")
        else:
            map_obj.ClearatPositon(y-2, x, '$')
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())

    if (player.CanMove == True):
        if (player.getDiamond()):
            map_obj.ClearatPositon(y, x, "@")
            player.setOnDiamond(False)
        else:
            if (map_obj.CheckForDiamond(y-1, x)) or Diamond == True:
                player.setOnDiamond(True)
            map_obj.ClearatPositon(y, x, ' ')

        player.MoveUp()
        map_obj.placePlayer(player.getChar(), player.getRow(), player.getCol())
        player.IncrementTurn()
        progress.IncrementMoves()

def ResetLevel(levels, levelNum):
    map_obj.ClearatPositon(player.getCol(), player.getRow(), " ")
    map_obj.setupMap(levelNum) #load the new map

    if levelNum == 2:
        player.ChangeSpawn(2,2) #Specific spawn point
    elif levelNum == 3:
        player.ChangeSpawn(1,1) #as above
    player.setCol(player.StartCol)
    player.setRow(player.StartRow)
    progress.NextLevel(levelNum)
    map_obj.placePlayer("X", player.StartRow, player.StartCol)
    setUpLevels()
    player.ResetTurnNumber()

def Main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT

    # Pygame initialization and basic set up of the global variables.
    pygame.init()
    #set the frameplayere
    FPSCLOCK = pygame.time.Clock()

    # set up the display window
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Sokoban')

    #set up a font, if you want a different font, put it in the folder with all the other stuff
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    #A dictionary of the images used.  You can then use
    #floor, wall etc in place of the whole pathname

    IMAGESDICT = {'Floor': pygame.image.load("Ground_Concrete.png"),
                  'Wall': pygame.image.load("Wall_Black.png"),
                  'Crate':pygame.image.load("Crate_Brown.png"),
                  'Player': pygame.image.load("Character5.png"),
                  'Diamond':pygame.image.load("EndPoint_Yellow.png"),
                  'CrateOnGoal':pygame.image.load("CrateDark_Brown.png"),
                  'Spacer':pygame.image.load("Ground_Grass.png")}

    TILEMAPPING = {'#': IMAGESDICT['Wall'],
                   '$': IMAGESDICT['Crate'],
                   'X': IMAGESDICT['Player'],
                   '@': IMAGESDICT['Diamond'],
                   ' ': IMAGESDICT['Floor'],
                   '&': IMAGESDICT['CrateOnGoal'],
                   '/': IMAGESDICT['Spacer']}
    #Set up the game.
    levels = setUpLevels()
    progress.currentLevel = 0

    # The main game loop. This loop runs a single level, when the user
    # finishes that level, the next/previous level is loaded.
    while True: # main game loop
        # Run the level to actually start playing the game:
        result = runLevel(levels, progress.currentLevel)


def runLevel(levels, levelNum):
    global currentImage, playerx, playery
    levelObj = levels[levelNum] #starts off as level 0 which we declared further up
    gameStateobj = copy.deepcopy(levelObj['gameState']) #preserves the current map
    mapneedsredraw = True #set to true to call Drawmap()

    countText = BASICFONT.render('Total moves: ' + str(player.getPlayerTurn()), 1, TEXTCOLOR)
    levelRect2 = countText.get_rect()
    levelRect2.bottomleft = (20, WINHEIGHT - 15)

    mapWidth = map_obj.getWidth() * TILEWIDTH
    mapHeight = map_obj.getHeight() * TILEFLOORHEIGHT + TILEHEIGHT
    levelIsComplete = False

    while True: #Main game loop for sokoban.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    MoveLeft()
                elif event.key == K_RIGHT:
                    MoveRight()
                elif event.key == K_UP:
                    MoveUp()
                elif event.key == K_DOWN:
                    MoveDown()
                elif event.key == K_SPACE:
                    ResetLevel(levels, levelNum)

            mapneedsredraw = True

        #Thread 2: Diamond checking thread and completion code
        #Check to see if there's been changes to the state of the diamonds.
        #If the amount of crates = equal the fixed set amount of diamonds, then the level is complete. Find all the boxes first
        #Now check if it is equal, if yes, end the level.
        #Check every time if the max number of levels is reached. If true, end the game.

        goal = map_obj.FindGoals()
        map_obj.setNoofGoals(goal)
        if (map_obj.GetNoofDiamonds() == map_obj.getNoofGoals()):
            levelNum += 1
            progress.NextLevel(levelNum)
            ResetLevel(levels, levelNum)
            print "Current progress:  " + str(progress.getPreviouslevel()) + " of" + " 5 completed"
            if (progress.completion(progress.getPreviouslevel())):
                print"Game over"
                terminate()


        #Thread 3: redraw the screen every frame.
        DISPLAYSURF.fill(BGCOLOR) #draws a background. Will change overtime.
        #If something happens ingame redraw the screen.
        if mapneedsredraw:
            mapSurf = drawMap(map_obj, gameStateobj, levelObj)
            mapneedsredraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        # Draw the map on the DISPLAYSURF object.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        #draw the level progress rectangle on the DISPLAYSURF object.
        currentlevel = progress.getCurrentLevel() + 1
        levelSurf = BASICFONT.render("Level " + str(currentlevel) + " of " + str(progress.getTotallevels()), 1, TEXTCOLOR)
        levelRect = levelSurf.get_rect()
        levelRect.bottomleft = (20, WINHEIGHT - 35)#places the text

        DISPLAYSURF.blit(levelSurf, levelRect)

        #Draw the counter
        countText = BASICFONT.render('Total moves: ' + str(player.getPlayerTurn()), 1, TEXTCOLOR)
        levelRect2 = countText.get_rect()
        levelRect2.bottomleft = (20, WINHEIGHT - 15)
        DISPLAYSURF.blit(countText, levelRect2)
        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick() #Move on to the next frame
def setUpLevels():

    global map_obj, playerx, playery

    levels = [] # Will contain a list of level objects.

    playerx = player.getCol()
    playery = player.getRow()

    map_obj.placePlayer(player.getChar(), playerx, playery)

    diamonds = map_obj.GetNoofDiamonds()
    Crates = map_obj.GetNoofCrates()
    mapwidth = map_obj.getWidth()
    mapheight = map_obj.getHeight()

    gameStateObj = {'player': (playerx, playery),
                    'diamonds': (diamonds),
                    'Crates': Crates
                    }

    levelObj = {'width': mapwidth,
                'height': mapheight,
                'map_obj': map_obj,
                'gameState': gameStateObj}

    levels.append(levelObj)

    return levels


def drawMap(map_obj, gameStateObj, levelObj):
    """Draws the map to a Surface object, including the player and
    sprouts. This function does not call pygame.display.update(), nor
    does it draw the "Level" text."""

    # mapSurf will be the single Surface object that the tiles are drawn
    # on, so that it is easy to position the entire map on the DISPLAYSURF
    # Surface object. First, the width and height must be calculated.
    mapSurfWidth = map_obj.getWidth() * TILEWIDTH
    mapSurfHeight = map_obj.getHeight() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR) # start with a blank color on the surface.

    #draw the tile sprites onto this surface.
    #this creates the visual map!
    for y in range(map_obj.getHeight()):
        for x in range(map_obj.getWidth()):
            spaceRect = pygame.Rect((y * TILEWIDTH, x * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if map_obj.GetCharAtPos(x,y) in TILEMAPPING:
                #checks in the TILEMAPPING directory above to see if there is a
                #matching picture, then renders it
                baseTile = TILEMAPPING[map_obj.GetCharAtPos(x,y)]

            # Draw the tiles for the map.
            mapSurf.blit(baseTile, spaceRect)
    return mapSurf



def terminate():
    #shutdown routine
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    Main()


