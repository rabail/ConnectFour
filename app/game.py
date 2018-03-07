from board import C4Board as C4Board
from slot import Slot as Slot
from engine import Engine as Engine
import refree

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
            self.player1 = raw_input("Player 1 : ")
            self.player2 = raw_input("Player 2 : ")

            if(self.player1 == self.player2):
                print 'Please enter the different players'
            else:
                print 'Lets start the game!!!'


    def startGame(self):
        turnNo = 0
        while(True):
            self.board.layout()
            p = self.player1 if turnNo%2 == 0 else self.player2
            position = input('select a position' + p + ' : ')
            engine = Engine(self.board)
            if(engine.dropBall(str(position), p )):
                turnNo+=1
                continue
            else:
                print 'oops, occupied!!! try again'
                continue


