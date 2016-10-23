#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      murra_000
#
# Created:     04/11/2015
# Copyright:   (c) murra_000 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from map import Map
M = Map()
class Movvable_Object:

    def __init__(self, x, r, c):
        self.Row = r
        self.Col = c
        self.Char = x
        self.CanMove = False
        self.Loc = self.Row, self.Col

    def getRow(self):
        return self.Row

    def getCol(self):
        return self.Col

    def getChar(self):
        return self.Char

    def getCanMove(self):
        return self.getCanMove

    def getLoc(self):
        return self.Loc

    def setRow(self, newvalue):
        self.Row = newvalue

    def setCol(self, newvalue):
        self.Col = newvalue

    def setChar(self, newvalue):
        self.Char = newvalue

    def setCanMove(self, newvalue):
        self.CanMove = newvalue

    def MoveUp(self):
        self.Row -= 1

    def MoveDown(self):
        self.Row += 1

    def MoveRight(self):
        self.Col += 1

    def MoveLeft(self):
        self.Col -= 1

    def toString(self):
        string = "This is the movvable object class, apply this to objects that require movement. It is so far applied to player and crate"
        return string





