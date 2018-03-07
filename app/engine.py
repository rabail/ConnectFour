from board import C4Board
from slot import Slot

class Engine:
    def dropBall(self, board, positionString, player):
        print(positionString[0])
        print(positionString[1])
        selectedSlot = list(filter(lambda x: str(x.Row) == positionString[0] and str(x.Column) == positionString[1], board.CSlots))
        if selectedSlot[0].status.isOccupied:
            return False
        else:
            selectedSlot[0].setOccupied(player)
            return True
        