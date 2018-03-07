def refree(board, recentSlot):
    ind = board.CSlots.index(recentSlot)
    """ check vertical"""
    rt = checkHorizontal(board,'r',ind)
    hcount=1z
    hcount+= checkHorizontal(board,'r', ind)
    hcount+= checkHorizontal(board,'l', ind)

    if hcount >=4:
        p=recentSlot.status.Player
        print str(p) + ' WINS!!!'
    
    
    
def checkHorizontal(board, direction, index):
    count = 0
    print str(index)

    while(True):
        if(direction == 'r' and index+board.Column < board.Row*board.Column):
            rt = board.CSlots[index+board.Column]
            if(rt.getStatus() and r53t.status.Player == board.CSlots[index].status.Player):
                index = index+board.Column 
                count+=1
            else:
                break
        elif(direction == 'l' and index-board.Column > -1):
            rt = board.CSlots[index-board.Column]
            if(rt.getStatus() and rt.status.Player == board.CSlots[index].status.Player):
                index = index-board.Column 
                count+=1
            else:
                break
        else:
            break
    return count

