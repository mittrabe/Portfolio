from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

import random #for testing, remove after

###########################################
#              SHOP SCREEN
###########################################
class ShopScreen(ttk.Frame):
    def __init__(self, parent, controller):

#=====================
# FRAME CONFIGURATION
#=====================
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="Menu.TFrame")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

#=====================
#   FRAME CONTENT
#=====================
        titleCanvas = Canvas(self, background="red")
        titleCanvas.grid(column=0, row=0, sticky=(N, W, E, S))
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.titleScreenImg = ImageTk.PhotoImage(Image.open(getFilePath('img\\shopScreen.png')).resize((width, height), Image.ANTIALIAS))
        titleBackground = titleCanvas.create_image(0, 0, anchor=NW, image=self.titleScreenImg)


        
        self.playerPieces = []

        self.boardState = []
        lastRow = ['whiteRook','whiteKnight','whiteBishop','whiteQueen','whiteKing','whiteBishop','whiteKnight','whiteRook']
        pieceTypes = ['Pawn','Bishop','Knight','Rook','Queen','King']

        for row in range(8):
            for col in range(8):
                if row+1 == 8: 
                    randIndex = random.randint(0,len(pieceTypes)-1)
                    self.boardState.append("white" + pieceTypes[randIndex])
                else:
                    self.boardState.append("empty")



        self.continueButton = ImageTk.PhotoImage(Image.open(getFilePath('img\\clickToContinue.png')).resize((400, 50), Image.ANTIALIAS))
        
        continueBtn = tk.Button(
            self, 
            command=lambda: controller.showFrame("Chess Screen", self.boardState),
            image = self.continueButton,
            borderwidth= 0
        ).grid(row=0,column=0, sticky=S)

    def getBoardState(self):
        return self.boardState
    def setBoardState(self, newBoardState):
        self.boardState = newBoardState
