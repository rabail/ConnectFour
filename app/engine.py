from board import C4Board
from slot import Slot
import refree

class Engine:
    def __init__(self, board):
        self.board = board

    def dropBall(self, positionString, player):
        print positionString
        """print str(positionString[0])"""
        """print str(positionString[1])"""
        selectedSlot = list(filter(lambda x: str(x.Row) == str(positionString[0]) and str(x.Column) == str(positionString[1]), self.board.CSlots))[0]
        select = self.pushBall(selectedSlot, player)
        if (select!=None):
            refree.refree(self.board,select)
            return True
        else:
            return False
        
    def pushBall(self, selectedSlot, player):
        if selectedSlot.getStatus():
            return None

        if selectedSlot.Row + 1 <= self.board.Row:
            newSlot = list(filter(lambda x: str(x.Row) == str(selectedSlot.Row + 1) and str(x.Column) == str(selectedSlot.Column), self.board.CSlots))[0]
            if(newSlot.getStatus()):
                selectedSlot.setOccupied(player)
                return selectedSlot
            else:
                return self.pushBall(newSlot,player)
        else:
            selectedSlot.setOccupied(player)
            return selectedSlot