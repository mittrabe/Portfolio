from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

from chessPieceTest2 import ChessPiece

#https://stackoverflow.com/questions/24050068/tkinter-making-classes-for-buttons-and-labels
class ChessSquare(tk.Button):

    def buttonCommand(self):
        print(self.getCoordinates())

   
    def setBackground(self):
            if (self.row+self.column)%2 == 0:
                return '#B58863'
            else:
                return '#F0D9B5'

    def __init__(self, parent, piece, row, col, width, height, **kwargs):
        tk.Button.__init__(self, parent)

        style = ttk.Style()
        style.configure('lightSquare.TFrame', background ="#B58863")
        style.configure('darkSquare.TFrame', background ="#F0D9B5")

        self.piece = piece
        self.row = row
        self.column = col
        self.width = width
        self.height = height
        self.selected = False
        self.highlighted = False
        self['bg'] = self.setBackground()
        self['highlightthickness'] = 0
        self['borderwidth'] = 0

        self['height'] = int(self.height/4)
        self['width'] = int(self.height/4)

        self.placePiece(self.piece)

        self.highlightedBy = 'A0' #A0 is the equivalent to NA or empty 

        self.grid(row=self.row, column=self.column)
    
    def getRow(self):
        return self.row
    def setRow(self, newRow):
        self.row = newRow

    def getCol(self):
        return self.column
    def setCol(self, newColumn):
        self.column = newColumn

    def getCoordinates(self):
            letters = ['A','B','C','D','E','F','G','H']
            return str(letters[self.column]) + str(self.row+1)

    def getPiece(self):
        return self.currentPiece
    def setPiece(self, newPiece):
        self.currentPiece = newPiece

    def getFilePath(self, filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

    def resizeImage(self, image): 
        pieceWidth = int(self['width']*0.7)
        pieceHeight = int(self['height']*0.7)

        self.resizedImage = image.resize((pieceWidth, pieceHeight), Image.ANTIALIAS)
        self.newPiece = ImageTk.PhotoImage(self.resizedImage)
        return self.newPiece

    def placePiece(self, piece):
        self.currentPiece = piece
        pieceImage = piece.getImage()
        resizedPieceImage = self.resizeImage(pieceImage)
        self['image'] = resizedPieceImage
    
    
    def removePiece(self):
        emptySquare = ChessPiece('empty','empty',0)
        self.placePiece(emptySquare)


    def isHighlighted(self):
        return self.highlighted
    def setHighlighted(self, newState):
        self.highlighted = newState

    def getHighlightedBy(self):
        return self.highlightedBy
    def setHighlightedBy(self, coords):
        self.highlightedBy = coords

    #F47C6C <-- piece capture color
    def highlightSquare(self, selectedSquare): 
        lightSquareHighlight = "#FFCB67"
        darkSquareHighlight = "#EEBD5F"

        if (self.row+self.column)%2 == 0:
            self['bg'] = lightSquareHighlight
        else:
            self['bg'] = darkSquareHighlight
        
        self.setHighlighted(True)
        self.setHighlightedBy(selectedSquare.getCoordinates())


    def isSelected(self):
        return self.selected

    def setSelected(self, newState):
        self.selected = newState

    def selectSquare(self):
        style = ttk.Style()
        style.configure('selectedSquare.TFrame', background ="#E59639")
        selectedSquareColor = "#E59639"

        if self['bg'] == selectedSquareColor:
            self['bg'] = self.setBackground()
        else:
            self['bg'] = selectedSquareColor
            self.setSelected(True)
        
        

    def deselectSquare(self):
        self['bg'] = self.setBackground()
        self.setSelected(False)




