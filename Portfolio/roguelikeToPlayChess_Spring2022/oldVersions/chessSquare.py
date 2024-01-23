from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

#https://stackoverflow.com/questions/24050068/tkinter-making-classes-for-buttons-and-labels
class ChessSquare(ttk.Button):

    def buttonCommand(self):
        print(self.getCoordinates())

   
    def setStyle(self):
            if (self.row+self.column)%2 == 0:
                return 'lightSquare.TFrame'
            else:
                return 'darkSquare.TFrame'

    def __init__(self, parent, row, col, width, height, **kwargs):
        ttk.Button.__init__(self, parent)

        style = ttk.Style()
        #style.theme_use('alt')
        style.configure('lightSquare.TFrame', background ="#B58863")
        style.configure('darkSquare.TFrame', background ="#F0D9B5")

        self.row = row
        self.column = col
        self.width = width
        self.height = height
        self.selected = False

        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

        #self.testIMG = ImageTk.PhotoImage(Image.open(getFilePath('img\\squarePNG.png')).resize((50, 50), Image.ANTIALIAS))
        #self['image'] =  self.testIMG
        #self.command = self.buttonCommand
        #self.command = squareCommand
        #self['command'] = self.command
        self['style'] = self.setStyle()
        self.grid(row=self.row, column=self.column, ipadx=self.height/8,ipady=self.height/8)
    
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


    def isSelected(self):
        return self.selected

    def setSelected(self, newState):
        self.selected = newState

    #F47C6C <-- piece capture color
    def highlightSquare(self): 
        style = ttk.Style()
        style.configure('highlightedSquare.TFrame', background ="#FFCB67")
        style.configure('highdarkedSquare.TFrame', background ="#EEBD5F")

        if self['style'] == 'highlightedSquare.TFrame':
            self['style'] = self.setStyle()
        else:
            if (self.row+self.column)%2 == 0:
                self['style'] = 'highdarkedSquare.TFrame'
            else:
                self['style'] = 'highlightedSquare.TFrame'

    def selectSquare(self):
        style = ttk.Style()
        style.configure('selectedSquare.TFrame', background ="#E59639")

        if self['style'] == 'selectedSquare.TFrame':
            self['style'] = self.setStyle()
        else:
            self['style'] = 'selectedSquare.TFrame'
            self.setSelected(True)
        
        

    def deselectSquare(self):
        self['style'] = self.setStyle()
        self.setSelected(False)


#class My_Button(Button):
 #   def __init__(self, text, row, col, command, color=None, **kwargs):
  #      self.text = text
   ##    self.column = col
     #   self.command = command
      #  self.color = color
      #  super().__init__()
      #  self['bg'] = self.color
      #  self['text'] = self.text
      #  self['command'] = self.command
      #  self.grid(row=self.row, column=self.column)

