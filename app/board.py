from slot import Slot

class C4Board:
    def __init__(self, rows, columns):
        self.CSlots = []
        self.Row = rows
        self.Column = columns

    def build(self):
        for r in range(1, self.Row+1):
            for c in range(1, self.Column+1):
                self.CSlots.append(Slot(r,c))

    def layout(self):
        for s in range(0, len(self.CSlots)):
            slot = self.CSlots[s]
            stat = str(slot) + ('\t\t' if slot.Column % self.Column > 0 else '\n')
            print stat,

    
