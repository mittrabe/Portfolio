from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

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
        width = parent.winfo_screenwidth()
        height = parent.winfo_screenheight()

        style = ttk.Style()
        style.configure('ChessFrame.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="ChessFrame.TFrame")

        self.boardState = []
        self.chessBoard = []
        if len(boardState) == 0:
            for index in range(64):
                self.boardState.append("empty")
        else:
            self.boardState = boardState
            self.chessBoard = boardState

        self.playerColor = playerColor

        #=====================
        #   FRAME CONTENT
        #=====================


        #-------------------
        #  PIECE GRAVEYARD
        #-------------------
        style.configure('Graveyard.TFrame', background ="#44BEB7")
        graveyard = ttk.Frame(self, style='Graveyard.TFrame', width=width*0.15, height=height*0.95)
        graveyard.grid(column=0, row=0, padx = 20, pady = 20, rowspan=2)


        #FFCB67
        #-------------------
        #    CHESS BOARD
        #-------------------
        boardWidth = width*0.4
        boardHeight = height*0.46
        style.configure('ChessBoard.TFrame', background ="brown")
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
                square['command'] = lambda square=square: buttonPress(square)
                if square.getCoordinates() == 'E1':
                    square['command'] = lambda square=square: controller.showFrame("Shop Screen", self.boardState) 


        #start == the square the piece is starting on
        #end == the square the piece is being moved to
        def movePiece(start, end):
            end.placePiece(start.getPiece())
            end.getPiece().incrementMoves() #increments the number of times the piece has been moved by one
            end.updateMoveset(self.chessBoard)
            start.removePiece(self.chessBoard)
            

        #This resets all the squares to their original color before highlighting squares again.
        def resetSquares():
            for square in self.chessBoard:
                square['bg'] = square.setBackground(square.getIsActive())

        def highlightSquares(selection):
            for square in self.chessBoard:
                #Highlights all the squares that the selected pawn can move to
                cord = [square.getCol(),square.getRow()]
                if cord in selection.getMoveset():
                    square.highlightSquare(selection)
                

               


        def buttonPress(event): #event refers to the button being pressed
            pieceMoved = False # 
            resetSquares() 
            if event.isSelected() == True:
                event.deselectSquare()
            else:
                #Marks whatever the previously clicked square is as deslected
                for square in self.chessBoard:
                    if square.isSelected():
                        print(square.getCoordinates()) #Prints off the coordinates of the button pressed (remove when no longer needed for testing)
                        if event.isHighlighted() == True and event.getHighlightedBy() == square.getCoordinates(): #Will only allow a piece to be moved to a square if it is highlighted as a valid move
                            movePiece(square, event)
                            pieceMoved = True 
                        square.setSelected(False)
                        event.setHighlighted(False)

                if pieceMoved == False: #if a button is pressed and no piece ends up getting moved, will instead select that square 
                    event.selectSquare() #changes the color of the selected square 
                    highlightSquares(event) #highlights all the squares that can be moved to from the selected Square
            return
        

                

#-------------------
#    MOVE LIST
#-------------------
        style.configure('MoveList.TFrame', background ="#272525") #383737
        moveListFrame = ttk.Frame(self, style='MoveList.TFrame', width = width*0.2, height = height*0.45)
        moveListFrame.grid(column=3, row=0, padx = 20, pady = 20, sticky=N)



#-------------------
#  PIECE TOOLTIP
#-------------------
        style.configure('ToolTip.TFrame', background ="white")
        tootlTipFrame = ttk.Frame(self, style='ToolTip.TFrame', width = width*0.2, height = height*0.3)
        tootlTipFrame.grid(column=3, row=1, padx = 20, pady = 10, sticky=N)