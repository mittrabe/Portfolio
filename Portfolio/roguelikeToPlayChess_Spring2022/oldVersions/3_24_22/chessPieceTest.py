from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

from moveset import Movesets

#https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/ImageTk.html
#https://stackoverflow.com/questions/60321170/correctly-extend-a-tkinter-widget-using-inheritances
#https://stackoverflow.com/questions/53438133/using-an-image-as-an-class-object-attribute-then-opening-that-image-in-a-tkinte

class ChessPiece:

    def getFilePath(self, filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'


    def setImagePath(self, path):
        self.imagePath = path
    def getImagePath(self):
        return self.imagePath


    def setPieceName(self, newName):
        self.pieceName = newName
    def getPieceName(self):
        return self.pieceName


    def setPieceType(self, newType):
        self.pieceType = newType
    def getPieceType(self):
        return self.pieceType

    def getImage(self):
        return self.image
    def setImage(self, pieceName):
        self.image = Image.open(self.getFilePath('Chess Pieces\\' + str(pieceName) + '.png'))
    
    def getTimesMoved(self):
        return self.timesMoved
    def incrementMoves(self):
        self.timesMoved = self.timesMoved + 1

    def getPiecesTaken(self):
        return self.piecesTaken
    def incrementPiecesTaken(self):
        self.piecesTaken = self.piecesTaken + 1
        
    def getPieceColor(self):
        return self.pieceColor
    def setPieceColor(self, newColor):
        self.pieceColor = newColor

    def getPieceValue(self):
        return self.pieceValue

    def getGamesPlayed(self):
        return self.gamesPlayed

    def setPieceValue(self, pieceType):
        value0 = [0,'King','Empty']
        value1 = [1,'Pawn', 'Boulder', 'FootSoldier']
        value1_5 = [1.5,'Samurai','Farmer']
        value2 = [2,'Pikeman','Trojan','Martyr','AltarBoy','Donkey']
        value2_5 = [2.5,'Priest']
        value3 =[3,'Bishop','Knight','Thief','General','land-mine','Clubs']
        value4 = [4,'Chariot','AI','Mimic','Hearts','Spade','Diamond']
        value5 = [5,'Rook','TrojanHorse','Fortress','BatteringRam','Fencer','Necromancer','Pope','Dragoon']
        value6 = [6,'Vampire','Jester']
        value7 = [7,'Diplomat','Princess','Prince']
        value8 = []
        value9 = [9,'Queen']
        valueList = [value0,value1,value1_5,value2,value2_5,value3,value4,value5,value6,value7,value8,value9]
        
        for value in valueList:
            if pieceType in value:
                self.pieceValue = value[0]

    def getHomeSquare(self):
        return self.homeSquare
    def setHomeSquare(self, square):
        self.homeSquare = square

    def updatePiece(self):
        self.timesMoved = 0
        self.piecesTaken = 0
        self.gamesPlayed += 1


    #Need to add: piecesTaken, pieceColor, pieceValue
    def __init__(self, pieceName, pieceType, timesMoved, piecesTaken, pieceColor, gamesPlayed):

        self.pieceName = pieceName
        self.setImage(pieceName)
        self.pieceType = pieceType
        self.timesMoved = timesMoved
        self.piecesTaken = piecesTaken
        self.pieceColor = pieceColor
        self.setPieceValue(self.pieceType)
        self.gamesPlayed = gamesPlayed
        
    

    

    


        


