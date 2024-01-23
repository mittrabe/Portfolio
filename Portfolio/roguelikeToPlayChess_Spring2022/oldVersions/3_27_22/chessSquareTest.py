from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

from chessPieceTest import ChessPiece
from moveset import Movesets

#https://stackoverflow.com/questions/24050068/tkinter-making-classes-for-buttons-and-labels
class ChessSquare(tk.Button):

    def buttonCommand(self):
        print(self.getCoordinates())

   
    def setBackground(self, active):
        if (self.row+self.column)%2 == 0:
            if active == TRUE:
                return '#B58863'
            elif active == FALSE:
                return '#564130'
        else:
            if active == TRUE:
                return '#F0D9B5'
            elif active == FALSE:
                return '#807668'  
    
    def getDetails(self):
        details = [self.piece, self.row, self.column, self.width, self.height, self.isActive]
        return details

    def updateMoveset(self, board):
        self.moveset = Movesets().getMoveset(self.getPiece(), self.column,self.row, board)

    def __init__(self, parent, piece, row, col, width, height, isActive, board, **kwargs):
        tk.Button.__init__(self, parent)

        self.piece = piece
        self.row = row
        self.column = col
        self.width = width
        self.height = height
        self.selected = False
        self.highlighted = False
        self.isActive = isActive
        self['bg'] = self.setBackground(isActive)
        self['highlightthickness'] = 0
        self['borderwidth'] = 0
        self.updateMoveset(board)


        self['height'] = int(self.height/4)
        self['width'] = int(self.height/4)

        self.placePiece(self.piece)

        self.highlightedBy = 'A0' #A0 is the equivalent to NA or empty 

        self.grid(row=self.row, column=self.column)
    
    def getMoveset(self):
        return self.moveset

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

    def getIsActive(self):
        return self.isActive
    def setIsActive(self, newActive):
        self.isActive = newActive


    def getPiece(self):
        return self.piece
    def setPiece(self, newPiece):
        self.piece = newPiece

    def getFilePath(self, filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

    def resizeImage(self, image): 
        pieceWidth = int(self['width']*0.7)
        pieceHeight = int(self['height']*0.7)

        self.resizedImage = image.resize((pieceWidth, pieceHeight), Image.ANTIALIAS)
        self.newPiece = ImageTk.PhotoImage(self.resizedImage)
        return self.newPiece

    def placePiece(self, piece):
        self.piece = piece
        pieceImage = piece.getImage()
        resizedPieceImage = self.resizeImage(pieceImage)
        self['image'] = resizedPieceImage
    
    
    def removePiece(self):
        emptySquare = ChessPiece('empty','Empty',0,0,'empty',0)
        self.placePiece(emptySquare)
        self.updateMoveset(self)


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
            self['bg'] = self.setBackground(self.isActive)
        else:
            self['bg'] = selectedSquareColor
            self.setSelected(True)
        
        

    def deselectSquare(self):
        self['bg'] = self.setBackground(self.isActive)
        self.setSelected(False)




