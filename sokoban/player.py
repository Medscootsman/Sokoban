#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      murra_000
#
# Created:     02/12/2015
# Copyright:   (c) murra_000 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from movvable_object import Movvable_Object
from map import Map
m = Map()
class Player(Movvable_Object):
    def __init__(self):
        Movvable_Object.__init__(self, "X", 5, 5)
        self.TurnNum = 0 #increment everytime a move is made.
        self.OnDiamond = False
        self.StartRow = 5
        self.StartCol = 5

    def Resetpos(self, StartCol, StartRow, Player):
        if self.Restart == True:
            m.placePlayer(Player, StartRow, StartCol)
        else:
            pass

    def IncrementTurn(self):
        self.TurnNum += 1

    def ResetTurnNumber(self):
        """ Reset the turn count"""
        self.TurnNum = 0

    def setOnDiamond(self, newvalue):
        self.OnDiamond = newvalue

    def getDiamond(self):
        return self.OnDiamond

    def getPlayerTurn(self):
        return self.TurnNum

    def ChangeSpawn(self, newRow, newCol):
        """ Change the players spawn for specific levels """
        self.StartCol = newCol
        self.StartRow = newRow
    def toString(self):
        string = "The player is current on location " + str(self.Col) + "." + str(self.Row) + "\n"
        string = string + "The player has moved " + str(self.TurnNum) + " times on this level."
        return string