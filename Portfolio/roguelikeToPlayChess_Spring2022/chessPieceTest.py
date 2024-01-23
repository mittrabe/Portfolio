from tkinter import *
import os
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

    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name


    def setType(self, newType):
        self.type = newType
    def getType(self):
        return self.type

    def changeOwner(self):
        if self.owner == "Player":
            self.owner = "CPU"
        elif self.owner == "CPU":
            self.owner = "Player"
        self.changeColor()
    def getOwner(self):
        return self.owner
    
    def changeColor(self):
        if self.color == "black":
            self.color = "white"
        elif self.color == "white":
            self.color = "black"

        self.name = self.color + self.type
        self.setImage(self.name)

    def getImage(self):
        return self.image
    def setImage(self, pieceName):
        self.image = Image.open(self.getFilePath('Chess Pieces\\' + str(pieceName) + '.png'))
    
    def resizePiece(self, image, newWidth, newHeight): 
        self.resizedImage = image.resize((newWidth, newHeight), Image.ANTIALIAS)
        self.newImage = ImageTk.PhotoImage(self.resizedImage)
        return self.newImage
    
    def getTimesMoved(self):
        return self.timesMoved
    def incrementMoves(self):
        self.timesMoved = self.timesMoved + 1

    def getPiecesTaken(self):
        return self.piecesTaken
    def incrementPiecesTaken(self):
        self.piecesTaken = self.piecesTaken + 1
        


    def getColor(self):
        return self.color
    def setColor(self, newColor):
        self.color = newColor

    def getGamesPlayed(self):
        return self.gamesPlayed

    def getValue(self):
        return self.value

    def setValue(self, pieceType):
        value0 = [0,'King','Empty']
        value1 = [1,'Pawn','Boulder', 'FootSoldier','Samurai','Farmer']
        value2 = [2,'Pikeman','Trojan','Martyr','AltarBoy','Donkey','Club'] #To be Added: Priest
        value3 =[3,'Bishop','Knight','Thief','General','Dynamite']
        value4 = [4,'Chariot','Ai','Mimic','Heart','Spade','Diamond']
        value5 = [5,'Rook','TrojanHorse','BatteringRam','Fencer','Fortress','Necromancer','Pope','Dragoon']
        value6 = [6,'Vampire','Jester', 'LandMine']
        value7 = [7,'Diplomat', 'Princess', 'Prince'] #To be added: Princess, Prince
        value8 = []
        value9 = [9,'Queen']
        self.valueList = [value0,value1,value2,value3,value4,value5,value6,value7,value8,value9]
        
        for value in self.valueList:
            if pieceType in value:
                self.value = value[0]
    
    def getValueList(self):
        return self.valueList

    def getHomeSquare(self):
        return self.homeSquare
    def setHomeSquare(self, square):
        self.homeSquare = square

    def updatePiece(self, row):
        self.timesMoved = 0
        self.piecesTaken = 0
        self.teamPiecesTaken = 0
        self.gamesPlayed += 1
        if self.owner == "CPU" and row >= 4: #reverts any of the player's pieces that were converted to the CPUs by a diplomat back to the player's
            self.changeOwner()
    
    def getLastPieceTaken(self):
        return self.lastPieceTaken
    def setLastPieceTaken(self, newPiece):
        self.lastPieceTaken = newPiece

    def getMovesetType(self):
        return self.movesetType
    def setMovesetType(self, newType):
        self.movesetType = newType

        


    def __init__(self, pieceName, pieceOwner, pieceType, timesMoved, piecesTaken, lastPieceTaken, pieceColor, gamesPlayed):

        self.name = pieceName
        self.setImage(pieceName)
        self.type = pieceType
        self.owner = pieceOwner #who currently controls the piece
        self.timesMoved = timesMoved
        self.piecesTaken = piecesTaken
        self.color = pieceColor
        self.setValue(self.type)
        self.gamesPlayed = gamesPlayed
        self.lastPieceTaken = lastPieceTaken
        self.movesetType = pieceType
        self.teamPiecesTaken = 0