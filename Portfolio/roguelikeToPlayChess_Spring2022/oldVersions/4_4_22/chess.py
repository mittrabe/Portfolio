from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

from titleScreen import TitleScreen
from loginScreen import LoginScreen
from menuScreen import MenuScreen
from shopScreen import ShopScreen
from chessScreen import ChessScreen


###########################################
#             RESOURCES USED
###########################################
#https://www.journaldev.com/48165/tkinter-working-with-classes
#https://stackoverflow.com/questions/31360480/tkinter-label-image-without-border/49857791 

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

 
        # Dictionary of Frames
        self.frames = []
        self.frameNames = ["Title Screen", "Login Screen", "Menu Screen", "Shop Screen", "Chess Screen"]
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (TitleScreen, LoginScreen, MenuScreen, ShopScreen, ChessScreen):
            if F == ChessScreen:
                boardState = []
                frame = F(self.window,self, boardState, 'black')
            elif F == ShopScreen:
                boardState = []
                #[1]self, [2]parent, [3]controller, [4]boardState, [5]numCoins, [6]maxNumCoins, [7]numLives, [8]numWins, [9]pieceValue, [10]maxPieceValue, [11]numRows, [12]playerColor
                frame = F(self.window, self, boardState, 10, 10, 5, 5, 0, 10, 2, 'black')  
            else:
                frame = F(self.window, self)
 
            # the windows class acts as the root window for the frames.
            self.frames.append(frame)
            frame.grid(column=0, row=0, sticky=(N, W, E, S))
 
        # Using a method to switch frames
        self.showFrame("Title Screen")

    #Method used to switch which frame is currently visible
    def showFrame(self, cont, *args):
        frameIndex = self.frameNames.index(cont)

        if cont == 'Chess Screen':
            self.frames[frameIndex] = ChessScreen(self.window, self, args[0],'black')
        elif cont == 'Shop Screen':
            #[1]self, [2]parent, [3]controller, [4]boardState, [5]numCoins, [6]maxNumCoins, [7]numLives, [8]numWins, [9]pieceValue, [10]maxPieceValue, [11]numRows, [12]playerColor
            self.frames[frameIndex] = ShopScreen(self.window, self, args[0], 10, 10, 5, 0, 0, 10, self.frames[frameIndex].getNumRows(), 'black')

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