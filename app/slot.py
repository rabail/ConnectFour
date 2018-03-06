class Slot:
    def __init__(self,rownum, colnum):
        self.Row = rownum
        self.Column = colnum
        self.status = SlotStatus()

    def setOccupied(self, player):
        self.status.isOccupied = True
        self.status.Player = player

    def getStatus(self):
        return self.status.isOccupied

    def __str__(self):
        if(self.status.isOccupied):
            return "X"
        else:
            return str(self.Row)+str(self.Column)

    
class SlotStatus:
    def __init__(self):
        self.Player = ''
        self.isOccupied = False