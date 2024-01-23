from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np

from titleScreen import TitleScreen
from loginScreen import LoginScreen
from menuScreen import MenuScreen
from shopScreenTest import ShopScreen
from chessScreenTest import ChessScreen
from gameOverScreen import GameOverScreen

###########################################
#                TO DO
###########################################
# Implement Shop Pool Upgrade Message
# Implement check/checkmate
# previous move displayer
# Stop tooltips from lingering in shop
# remove undeaad pieces from graveyard
# Pieces captured by diplomat showing as wrong color in shop
# Do the Princess and Prince even work?
# Dynamite Piece Diagram
# Prevent yourself from playing against yourself
# display CPU name
# setup password hashing
# game over screen
# round over screen
# saving/loading game
# settings/escape screen
# make CPU recognize when it's in check
# Make 'how to play' screen
# Make add log out to main menu
# Incrememental shop options 
# Mimic capturing mimic breaks the game


#ACTUALLY NEED TO DO:
# debugging
# Clean clode/make method comments
# Unit testing
# prevent against SQL injection
# round over screens
# Make CPU recognize when its in check

###########################################
#             RESOURCES USED
###########################################
#https://www.journaldev.com/48165/tkinter-working-with-classes
#https://stackoverflow.com/questions/31360480/tkinter-label-image-without-border/49857791 
#https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
#https://docs.sqlalchemy.org/en/14/core/engines.html#postgresql

#tk vs ttk
# highlightthickness is only tk
# styles are only ttk
class windows(tk.Tk):

###########################################
#             PROGRAM WINDOW
###########################################
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Would You Roguelike To Play Chess?")
 
        self.attributes("-fullscreen", 1)
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        # creating a frame and assigning it to container
        self.window = ttk.Frame(self)
        # specifying the region where the frame is packed in root
        self.window.grid(column=0, row=0, sticky=(N, W, E, S))
 
        # configuring the location of the container using grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Exits program when escape is hit
        def close_win(e):
            self.destroy()
        self.bind('<Escape>', lambda e: close_win(e))

        self.pieceState = []
 
        # Dictionary of Frames
        self.frames = []
        self.frameNames = ["Title Screen", "Login Screen", "Menu Screen", "Shop Screen", "Chess Screen", "Game Over Screen"]
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (TitleScreen, LoginScreen, MenuScreen, ShopScreen, ChessScreen, GameOverScreen):
            if F == ChessScreen:
                boardState = []
                frame = F(self.window,self, boardState, 'black', 0,5,'')
            elif F == ShopScreen:
                boardState = []
                #[1]self, [2]parent, [3]controller, [4]boardState, [5]numCoins, [6]maxNumCoins, [7]numLives, [8]numWins, [9] numTurns, [10]pieceValue, [11]maxPieceValue, [12]numRows, [13]playerColor, [14] frozenPieces, [15] username
                frame = F(self.window, self, boardState, 10, 10, 5, 0, 0, 1, 10, 2, 'black', self.pieceState, [], '') 
            elif F == GameOverScreen:
                frame = F(self.window,self, "")
            else:
                frame = F(self.window, self)
 
            # the windows class acts as the root window for the frames.
            self.frames.append(frame)
            frame.grid(column=0, row=0, sticky=(N, W, E, S))
 
        # Using a method to switch frames
        self.showFrame("Title Screen")
            
    #Method used to switch which frame is currently visible
    def showFrame(self, cont, *args):
        if cont == 'New Game':
            frameIndex = 3
        else:
            frameIndex = self.frameNames.index(cont)

        if cont == 'Chess Screen':
            self.pieceState = args[1] #an instance of every single piece is saved when leaving the shop so they can be reapplied when the shop is next loaded
            self.frames[frameIndex] = ChessScreen(self.window, self, args[0],args[2], self.frames[frameIndex-1].getNumWins(), self.frames[frameIndex-1].getNumLives(),self.frames[frameIndex-1].getCpuUsername())

        elif cont == 'New Game':
            boardState = []
            self.frames[frameIndex] = ShopScreen(self.window, self, boardState, 10, 10, 5, 0, 1, 0, 10, 2, 'white', self.pieceState, [], self.frames[frameIndex-2].getUsername()) 
        elif cont == 'Shop Screen':
            #[1]self, [2]parent, [3]controller, [4]boardState, [5]numCoins, [6]maxNumCoins, [7]numLives, [8]numWins, [9]pieceValue, [10]maxPieceValue, [11]numRows, [12]playerColor, [13], pieceState, [14] frozenPiecess
            self.frames[frameIndex] = ShopScreen(self.window, self, args[0], 10 + self.frames[frameIndex+1].getBonusGold(), 10, self.frames[frameIndex].getNumLives() - self.frames[frameIndex+1].getLivesLost(), self.frames[frameIndex].getNumWins() + self.frames[frameIndex+1].getWinsAdded(), self.frames[frameIndex].getNumTurns()+1, self.frames[frameIndex].getPiecesValue(), self.frames[frameIndex].getMaxPiecesValue(), self.frames[frameIndex].getNumRows(), 'white', self.pieceState, self.frames[frameIndex].getFrozenPieces(), self.frames[frameIndex-2].getUsername())
        elif cont == 'Game Over Screen':
            self.frames[frameIndex] = GameOverScreen(self.window, self, args[0])

        frame = self.frames[frameIndex]
        frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # raises the current frame to the top
        frame.tkraise()

    
###########################################
#               RUNNER
###########################################
if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()