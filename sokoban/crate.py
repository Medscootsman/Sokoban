#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      murra_000
#
# Created:     10/12/2015
# Copyright:   (c) murra_000 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from movvable_object import Movvable_Object
class Crate(Movvable_Object):
    def __init__(self, SpecifiedRow, SpecifiedCol, id):
        Movvable_Object.__init__(self, "$", SpecifiedRow, SpecifiedCol)
        self.CanMove = False
        self.OnDiamond = False
        self.CrateID = id

    def SetCanMove(self, value):
        self.CanMove = value

    def SetOnDiamond(self, value):
        self.OnDiamond = value


