#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      murra_000
#
# Created:     11/11/2015
# Copyright:   (c) murra_000 2015
# Licence:     <your licence>
#------------------------------------------------------------------------------
class Progression:
    def __init__(self):
        self.totalLevels = 5
        self.currentLevel = 1
        self.PreviousLevel = 0
        self.RestartGame = False
        self.GameComplete = False
        self.TotalMoves = 0
        self.GameSaved = False

    def NextLevel(self, levelNum):
        self.PreviousLevel  = self.currentLevel
        self.currentLevel = levelNum

    def IncrementMoves(self):
        self.TotalMoves += 1

    def RestartGame(self):
        pass

    def PreviousLevel(self):
        self.currentLevel = self.PreviousLevel
        self.PreviousLevel -= 1

    def completion(self, currentLevel):
        if currentLevel == self.totalLevels:
            print "You're winner!"
            return True
        else:
            return False

    def getPreviouslevel(self):
        return self.PreviousLevel

    def getCurrentLevel(self):
        return self.currentLevel

    def getTotallevels(self):
        return self.totalLevels

    def toString(self):
        string = "The current progress is:\n" + "Currently on level " + str(self.currentLevel) + " of " + str(self.totalLevels) + "."
        string = string + "The current moves for all levels is " + str(self.TotalMoves) + "."
        return string
