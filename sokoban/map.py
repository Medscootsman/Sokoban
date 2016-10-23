#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      murra_000
#
# Created:     11/11/2015
# Copyright:   (c) murra_000 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Map:

    def __init__(self):
        self.NoofDiamonds = 5
        self.NoofCrates = 5
        self.Restart = False
        self.CompleteLevel = False
        self.LockedCoords = []
        self.Map = [['#','#','#','#','#','#','#','#','#','#','#'],
                    ['#',' ',' ','@',' ',' ',' ','$',' ','#','#'],
                    ['#',' ',' ',' ',' ',' ',' ','$',' ',' ','#'],
                    ['#',' ',' ',' ',' ','$','@',' ',' ',' ','#'],
                    ['#','#','@',' ',' ',' ',' ',' ',' ',' ','#'],
                    ['#',' ',' ','#',' ',' ',' ','@','$',' ','#'],
                    ['#',' ',' ','#',' ',' ',' ',' ',' ',' ','#'],
                    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                    ['#',' ',' ',' ',' ','$',' ',' ',' ',' ','#'],
                    ['#','@',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                    ['#','#','#','#','#','#','#','#','#','#','#']]
                    # @ = diamond
                    # $ = crate
                    # # = wall

        self.height = 11
        self.width = 11
        self.NoofGoalCrates = 0


    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def GetCharAtPos(self, Row, Col):
        return self.Map[Row][Col]

    def getNoofGoals(self):
        return self.NoofGoalCrates

    def setNoofGoals(self, newvalue):
        self.NoofGoalCrates = newvalue

    def placePlayer(self, player, Row, Col):
        #place the player on the maze by getting it's loc coordinates
        #make sure to double check coordinate isn't a wall
        self.Map[Row][Col] = player


    def GetNoofDiamonds(self):
        return self.NoofDiamonds

    def GetNoofCrates(self):
        return self.NoofCrates

    def ClearatPositon(self, Row, Col, Char):
        #clears the positon of the Map with a specified char
        self.Map[Row][Col] = Char

    def CheckForDiamond(self, Row, Col):
        #checks to see if there's a diamond at the specified location
        if self.Map[Row][Col] == "@":
            return True
        else:
            return False

    def CheckforCrate(self, Row, Col):
        if self.Map[Row][Col] == "$":
            return True
        else:
            return False

    def CheckforPlayerOnCrate(self, Row, Col):
        if self.Map[Row][Col] == "&":
            return True
        else:
            return False


    def FindGoals(self):
        #when a crate is moved onto a diamond, it should take a note of the location so if the crate is moved
        #a 2nd time, it returns to the diamond char. This is to avoid disappearing acts. (@ is the diamond identifier)
        #First we find all the diamond coords
        Goals = 0
        currentcol = 1
        Row = 1
        while True:
            #First we check the Row, then we increment col by 1 up until 10.
            Col = currentcol
            if self.Map[Row][Col] == "&":
                Goals += 1
            if Row == self.height-1:
                currentcol += 1
                Row = 0
            if Col == self.width-1:
                return Goals
                break
            Row += 1

    def checkMove(self, Row, Col):
        if (self.Map[Row][Col] == '#'):
            return False
        else:
            return True
        Row = 1
        Col = 1
    def setupMap(self, Level):

        #Remember:
        # @ id for diamond end point.
        # $ id for crate
        # & id for crate on diamond point.
        # ' ' spacer
        if Level == 0:
            self.Map = [['#','#','#','#','#','#','#','#','#','#','#'],
                    ['#',' ',' ','@',' ',' ',' ','$',' ','#','#'],
                    ['#',' ',' ',' ',' ',' ',' ','$',' ',' ','#'],
                    ['#',' ',' ',' ',' ','$','@',' ',' ',' ','#'],
                    ['#','#','@',' ',' ',' ',' ',' ',' ',' ','#'],
                    ['#',' ',' ','#',' ',' ',' ','@','$',' ','#'],
                    ['#',' ',' ','#',' ',' ',' ',' ',' ',' ','#'],
                    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                    ['#',' ',' ',' ',' ','$',' ',' ',' ',' ','#'],
                    ['#','@',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                    ['#','#','#','#','#','#','#','#','#','#','#']]
        elif Level == 1:
            self.width = 11
            self.height = 11
            self.Map = [['#','#','#','#','#','#','#','#','#','#','#'],
                        ['#',' ',' ',' ',' ',' ',' ',' ',' ','#','#'],
                        ['#',' ',' ',' ',' ',' ',' ','$',' ',' ','#'],
                        ['#',' ',' ',' ',' ','$','@',' ',' ',' ','#'],
                        ['#','#','@','#',' ',' ',' ',' ',' ',' ','#'],
                        ['#',' ',' ','#',' ',' ',' ','@','$',' ','#'],
                        ['#',' ','$','#','#','#','#','#','#',' ','#'],
                        ['#',' ',' ',' ',' ',' ','@',' ',' ',' ','#'],
                        ['#',' ','#','#','#','#','#','#','#',' ','#'],
                        ['#',' ','#','#','#','#','@',' ','$',' ','#'],
                        ['#','#','#','#','#','#','#','#','#','#','#']]
            self.NoofCrates = 5
            self.NoofDiamonds = 5

        elif Level == 2:
            self.width = 10
            self.height = 10
            self.Map = [['#','#','#','#','#','/','/','/','/','/'],
                        ['#','@','#','@','#','/','/','/','/','/'],
                        ['#',' ',' ',' ','#','/','/','/','/','/'],
                        ['#','$','#','$','#','/','/','/','/','/'],
                        ['#',' ',' ',' ','#','/','/','/','/','/'],
                        ['#',' ','$',' ','#','/','/','/','/','/'],
                        ['#',' ',' ','$','#','/','/','/','/','/'],
                        ['#','@','#','@','#','/','/','/','/','/'],
                        ['#',' ','#',' ','#','/','/','/','/','/'],
                        ['#','#','#','#','#','/','/','/','/','/']]
            self.NoofCrates = 4
            self.NoofDiamonds = 4

        elif Level == 3:
            self.width = 11
            self.height = 11
            self.Map = [['#','#','#','#','#','#','#','#','#','#','#'],
                        ['#',' ','#',' ','#','/','#',' ',' ',' ','#'],
                        ['#',' ','@',' ','#','/','#',' ','$',' ','#'],
                        ['#',' ',' ','$','#','#','#',' ',' ','#','#'],
                        ['#',' ',' ',' ',' ','$','@',' ',' ','@','#'],
                        ['#',' ','$',' ','@','$',' ',' ',' ',' ','#'],
                        ['#','#',' ',' ','#','#','#',' ',' ','#','#'],
                        ['#',' ',' ',' ','#','/','#',' ','$',' ','#'],
                        ['#',' ','@',' ','#','/','#',' ',' ','@','#'],
                        ['#','#','#','#','#','#','#','#','#','#','#'],
                        ['/','/','/','/','/','/','/','/','/','/','/']]
            self.NoofDiamonds = 6
            self.NoofCrates = 6
        elif Level == 4:
            self.Map = [['#','#','#','#','#','#','#','#','#','#','#'],
                        ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#','@',' ','$',' ',' ',' ',' ','@',' ','#'],
                        ['#','#','#','#','#','#','#','#',' ',' ','#'],
                        ['#',' ','#',' ',' ',' ',' ','#',' ',' ','#'],
                        ['#',' ',' ',' ',' ','$',' ','#',' ',' ','#'],
                        ['#',' ','$','#','#',' ','@','#',' ','#','#'],
                        ['#',' ',' ','#','#','#','#','#',' ',' ','#'],
                        ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#','#','#','#','#','#','#','#','#','#','#']]
            self.NoofDiamonds = 3
            self.NoofCrates = 3

    def toString(self):
        printme = ""
        for i in range (0,len(self.Map)):
            for j in self.Map[i]:
                printme = printme + str(j)
            printme = printme + "\n"
        return printme
