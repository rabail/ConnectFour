from board import C4Board
from slot import Slot
from engine import Engine

class Game:
    def __init__(self):
        self.board = C4Board(6,7)
        self.board.build()
        self.board.layout()
        self.player1=''
        self.player2=''
        self.get_players()
        self.startGame()

    def get_players(self):
        while(self.player1 == self.player2):
            self.player1 = input("Player 1 : ")
            self.player2 = input("Player 2 : ")

            if(self.player1 == self.player2):
                print("Please enter the different players")
            else:
                print("Lets start the game!!!")


    def startGame(self):
        turnNo = 0
        while(True):
            self.board.layout()
            p = self.player1 if turnNo%2 == 0 else self.player2
            position = input('select a position' + p + ' : ')
            engine = Engine()
            if(engine.dropBall(self.board, position, p )):
                turnNo+=1
                continue
            else:
                print('oops, occupied!!! try again')
                continue


