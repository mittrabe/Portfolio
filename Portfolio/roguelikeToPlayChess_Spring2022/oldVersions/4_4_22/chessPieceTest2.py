from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

#https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/ImageTk.html
#https://stackoverflow.com/questions/60321170/correctly-extend-a-tkinter-widget-using-inheritances
#https://stackoverflow.com/questions/53438133/using-an-image-as-an-class-object-attribute-then-opening-that-image-in-a-tkinte
    #import tkinter as tk

    #class PicTest:
        #def __init__(self, name, image):
            #self.name = name
            #self.image = tk.PhotoImage(file=image)

    #root = tk.Tk()
    #foo = PicTest('foo', '/path/to/image/file')

    #def testwindow():
        #foo_testlabel = tk.Label(root, image=foo.image)
        #foo_testlabel.pack()

    #testwindow()
    #root.mainloop()

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
        
    
    def __init__(self, pieceName, pieceType, timesMoved):

        self.pieceName = pieceName
        self.setImage(pieceName)
        self.pieceType = pieceType
        self.timesMoved = timesMoved

       #print(type(self.setImage(self.pieceName)))
        #self.image = self.setImage(self.pieceName)

    


        


