from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import random
import time
import tkinter.font as font
from moveset import Movesets

from chessSquareTest import ChessSquare
from chessPieceTest import ChessPiece


###########################################
#               CHESS BOARD
###########################################

class ChessScreen(tk.Frame):
    def __init__(self, parent, controller, boardState, playerColor):

        #=====================
        # FRAME CONFIGURATION
        #=====================
        self.width = parent.winfo_screenwidth()
        self.height = parent.winfo_screenheight()

        style = ttk.Style()
        style.configure('ChessFrame.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="ChessFrame.TFrame")

        self.boardState = []
        self.chessBoard = []
        self.controller = controller
        if len(boardState) == 0:
            for index in range(64):
                self.boardState.append("empty")
        else:
            self.boardState = boardState
            self.chessBoard = boardState

        self.playerColor = playerColor
        if self.playerColor == "black":
            self.cpuColor = "white"
            self.currentTurn = "CPU"
        else:
            self.cpuColor = "black"
            self.currentTurn = "Player"

        #=====================
        #   FRAME CONTENT
        #=====================

        


        #-------------------
        #  PIECE GRAVEYARD
        #-------------------
        style.configure('Graveyard.TFrame', background ="#44BEB7")
        graveyard = ttk.Frame(self, style='Graveyard.TFrame', width=self.width*0.15, height=self.height*0.95)
        graveyard.grid(column=0, row=0, padx = 20, pady = 20, rowspan=2)


        #FFCB67
        #-------------------
        #    CHESS BOARD
        #-------------------
        boardWidth = self.width*0.4
        boardHeight = self.height*0.46
        style.configure('ChessBoard.TFrame', background ="#00868B")
        board = ttk.Frame(self, style='ChessBoard.TFrame', width = boardWidth, height = boardHeight)
        board.grid(column=1, row=0, padx = 20, pady = 20, rowspan=2)


        # Creates the squares/buttons on the chess board. Each square is automatically populated with the "empty" chess piece
        chessSquares = []
        index = 0
        if len(self.chessBoard) > 0:
            for row in range(8):
                for col in range(8):
                    details = self.chessBoard[index].getDetails()
                    self.chessBoard[index] = ChessSquare(board, details[0],details[1],details[2],boardWidth,boardHeight,TRUE, self.chessBoard) 
                    index += 1

            # Sets all of the squares to perform the buttonPress function when clicked
            for square in self.chessBoard:
                square['command'] = lambda square=square: self.buttonPress(square)
                if square.getCoordinates() == "A1":
                    square['command'] = lambda square=square: controller.showFrame("Shop Screen",self.boardState)

        
        #-------------------
        #    MOVE LIST
        #-------------------
        mlWidth = self.width*0.2
        mlHeight = self.height*0.45
        style.configure('MoveList.TFrame', background ="#272525") #383737
        self.moveListFrame = ttk.Frame(self, style='MoveList.TFrame', width = mlWidth, height = mlHeight)
        self.moveListFrame.grid(column=3, row=0, padx = 20, pady = 20, sticky=N)


        



        #-------------------
        #  PIECE TOOLTIP
        #-------------------
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

        def resizeImage(self, image, newWidth, newHeight): 
            self.resizedImage = image.resize((newWidth, newHeight), Image.ANTIALIAS)
            self.newImage = ImageTk.PhotoImage(self.resizedImage)
            return self.newImage

        ptWidth = self.width*0.2
        ptHeight = self.height*0.3
        style.configure('ToolTip.TFrame', background ="white")
        self.toolTipFrame = ttk.Frame(self, style='ToolTip.TFrame', width = ptWidth, height = ptHeight)
        self.toolTipFrame.grid(column=3, row=1, padx = 20, pady = 10, sticky=(N,S,E,W))

        toolTipFont = font.Font(family='Roboto', size=32)
        descriptionFont = font.Font(family='Roboto', size=14)

        self.toolTipPiece = Label(self.toolTipFrame, bg="white",text="", font = toolTipFont)
        self.toolTipPiece.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))

        self.pawnDiagram = Image.open(getFilePath('img\\pieceDiagrams\\' + 'EmptyDiagram.png'))
        self.pawnDiagramImg = resizeImage(self, self.pawnDiagram, int(ptWidth*0.75), int(ptHeight*0.75))
        self.pieceDiagram = Label(self.toolTipFrame, bg = 'white', image=self.pawnDiagramImg)
        self.pieceDiagram.grid(column=0,row=1, padx=10, sticky=(N,S,E,W))

        self.toolTipDescription = Label(self.toolTipFrame,bg='white',text="", font = descriptionFont, wraplength=350)
        self.toolTipDescription.grid(column=0,row=2,padx=10, sticky=(N,S,E,W))

    

        



        #Will make CPU go first if CPU is playing with the white pieces
        if self.currentTurn == "CPU":
            self.after(1000,self.cpuMove())
            

    def updateToolTip(self, square):
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

        def resizeImage(self, image, newWidth, newHeight): 
            self.resizedImage = image.resize((newWidth, newHeight), Image.ANTIALIAS)
            self.newImage = ImageTk.PhotoImage(self.resizedImage)
            return self.newImage

        ptWidth = self.width*0.2
        ptHeight = self.height*0.3

        if square.getPiece().getType() == "Empty":
            self.toolTipPiece.configure(text='')
        else:
            self.toolTipPiece.configure(text=square.getPiece().getType())

        self.newDiagram = Image.open(getFilePath('img\\pieceDiagrams\\' + square.getPiece().getMovesetType() + 'Diagram.png'))
        self.pieceDiagramImg = resizeImage(self, self.newDiagram, int(ptWidth*0.75), int(ptHeight*0.75))
        self.pieceDiagram.configure(image=self.pieceDiagramImg)
        self.toolTipDescription.configure(text=Movesets().getDescription(square.getPiece()))


    def gameOver(self, winner):
        if winner == "Player":
            print("Winner: Player")
        if winner == "CPU":
            print("Winner: CPU")
        self.controller.showFrame("Shop Screen",self.boardState)

    #start == the square the piece is starting on
    #end == the square the piece is being moved to
    def movePiece(self,start, end):
        isGameOver = FALSE
        if end.getPiece().getType() == "King": #Checks if the piece being taken/moved to is the king
            isGameOver = TRUE

        #This code will run even if the game is over so that the King is shown as being taken     
        if end.getPiece().getType() != "Empty":
            start.getPiece().incrementPiecesTaken()
            if start.getPiece().getType() == "Mimic": 
                start.getPiece().setMovesetType(end.getPiece().getMovesetType())
        end.placePiece(start.getPiece())
        end.getPiece().incrementMoves() #increments the number of times the piece has been moved by one
        start.removePiece()
        end.updateMoveset(self.chessBoard, 'move')

        if isGameOver == TRUE:
            kingColor = end.getPiece().getColor()
            if kingColor == "black":
                self.gameOver("Player")
            else:
                self.gameOver("CPU")
        
        if self.currentTurn == "Player":
            self.currentTurn = "CPU"
            #cpuMove()
        elif self.currentTurn == "CPU":
            self.currentTurn = "Player"

    def cpuMove(self):
        if len(self.chessBoard) > 0:
            king = self.chessBoard[0]
            validMoves = []
            for square in self.chessBoard:
                if square.getPiece().getName() == "whiteKing":
                    king = square
                    king.updateMoveset(self.chessBoard,'update')

            for potentialMove in self.chessBoard: #This is gross, optimize it pls
                cord = [potentialMove.getCol(),potentialMove.getRow()]
                if cord in king.getMoveset():
                    validMoves.append(potentialMove)

            randIndex = random.randint(0,len(validMoves)-1) #picks a random valid move
            self.movePiece(king, validMoves[randIndex])
            
            self.currentTurn = "Player"

            
    

    #This resets all the squares to their original color before highlighting squares again.
    def resetSquares(self):
        for square in self.chessBoard:
            square['bg'] = square.setBackground(square.getIsActive())

    def highlightSquares(self, selection):
        for square in self.chessBoard:
            #Highlights all the squares that the selected pawn can move to
            cord = [square.getCol(),square.getRow()]
            if cord in selection.getMoveset():
                square.highlightSquare(selection)
            
        


    def buttonPress(self,event): #event refers to the button being pressed
        pieceMoved = False  
        self.resetSquares()
        #if event.getPiece().getType() != "Jester": #Prevents Jester from changing movesets everytime it's clicked (as opposed to only when moved. Currently does not stop Mimics who have captured a jester)
        event.updateMoveset(self.chessBoard, 'update') #updating here will adjust the moveset of pieces to reflect the pieces around them (i.e. if a pawn can go diagonally now since a piece has moved to where it can attack)
        if event.isSelected() == True:
            event.deselectSquare()
        else:
            #Marks whatever the previously clicked square is as deslected
            for square in self.chessBoard:
                if square.isSelected():
                    print(square.getCoordinates()) #Prints off the coordinates of the button pressed (remove when no longer needed for testing)
                    if event.isHighlighted() == True and event.getHighlightedBy() == square.getCoordinates(): #Will only allow a piece to be moved to a square if it is highlighted as a valid move
                        self.movePiece(square, event) #Square holds the piece being moved, event is the square being moved to
                        pieceMoved = True
                        event.update_idletasks() #This is necessary for the button to update/move the players piece before the CPU moves
                    square.setSelected(False)
                    event.setHighlighted(False)

            if pieceMoved == False: #if a button is pressed and no piece ends up getting moved, will instead select that square 
                event.selectSquare() #changes the color of the selected square
                self.updateToolTip(event) #Commented out for testing purposes
                if event.getPiece().getColor() == self.playerColor: 
                    self.highlightSquares(event) #highlights all the squares that can be moved to from the selected Square
            
            if self.currentTurn == "CPU":
                self.after(500,self.cpuMove()) #the number represents how long the CPU waits before moving
        return
        

                
    
