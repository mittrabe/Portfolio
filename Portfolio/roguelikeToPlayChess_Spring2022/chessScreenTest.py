from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
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
    def __init__(self, parent, controller, boardState, playerColor, numWins, numLives, cpuUsername):

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
        self.numWins = numWins
        self.numLives = numLives 
        self.cpuUsername = cpuUsername
        self.bonusGold = 0
        self.livesLost = 0
        self.winsAdded = 0
        self.winner = ''
        self.isGameOver = FALSE
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
        graveyardWidth = self.width*0.15
        graveyardHeight = self.height*0.95
        style.configure('Graveyard.TFrame', background ="#44BEB7")
        self.graveyard = ttk.Frame(self, style='Graveyard.TFrame', width=graveyardWidth, height=graveyardHeight)
        self.graveyard.grid(column=0, row=0, padx = 20, pady = 20, rowspan=2, sticky = (N,S,E,W))

        graveWidth = graveyardWidth*0.15
        graveHeight = graveyardHeight*0.05
        style.configure('divider.TFrame', background ="black")
        style.configure('graves.TFrame', background ="#44BEB7")

        self.cpuGraveyard = ttk.Frame(self.graveyard,style='graves.TFrame', width = graveyardWidth,height = graveyardHeight*0.45)
        self.cpuGraveyard.grid(row=0, column=0, padx=5, sticky=(N,S,E,W))
        
        self.dividerFrame = ttk.Frame(self.graveyard, style='Spacer.TFrame', width=graveyardWidth, height=5)
        self.dividerFrame.grid(row=1, column=0, padx=5)

        self.playerGraveyard = ttk.Frame(self.graveyard,style='graves.TFrame', width = graveyardWidth,height = graveyardHeight*0.45)
        self.playerGraveyard.grid(row=2, column=0, padx=5,sticky=(N,S,E,W))


        self.deadCpuPieces = []
        self.deadPlayerPieces = []

        self.graveyardData = [self.cpuGraveyard, self.playerGraveyard, self.deadCpuPieces, self.deadPlayerPieces]

        

        
    
    
        #-------------------
        #    CHESS BOARD
        #-------------------
        boardWidth = self.width*0.4
        boardHeight = self.height*0.46
        style.configure('ChessBoard.TFrame', background ="#00868B")
        
        board = ttk.Frame(self, style='ChessBoard.TFrame', width = boardWidth, height = boardHeight)
        board.grid(column=1, row=0, padx = 20, pady = 20, rowspan=2)
        cpuFont = font.Font(family='Roboto', size=24)
        cpuLabel = Label(board, text=self.cpuUsername, font = cpuFont,bg='#00868B',fg='white')
        cpuLabel.grid(column=0,row=0, columnspan=3)


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


        
        #-------------------
        #    MOVE LIST (not implemented)
        #-------------------
        mlWidth = self.width*0.2
        mlHeight = self.height*0.45
        style.configure('MoveList.TFrame', background ="#272525") #383737
        self.moveListFrame = ttk.Frame(self, style='MoveList.TFrame', width = mlWidth, height = mlHeight)
        self.moveListFrame.grid(column=3, row=0, padx = 20, pady = 20, sticky=N)


        
        #-------------------
        #  PIECE TOOLTIP
        #-------------------
        ptWidth = self.width*0.2
        ptHeight = self.height*0.3
        style.configure('ToolTip.TFrame', background ="white")
        self.toolTipFrame = ttk.Frame(self, style='ToolTip.TFrame', width = ptWidth, height = ptHeight)
        self.toolTipFrame.grid(column=3, row=1, padx = 20, pady = 10, sticky=(N,S,E,W))

        toolTipFont = font.Font(family='Roboto', size=32)
        descriptionFont = font.Font(family='Roboto', size=14)

        self.toolTipPiece = Label(self.toolTipFrame, bg="white",text="", font = toolTipFont)
        self.toolTipPiece.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))

        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'
        def resizeImage(self, image, newWidth, newHeight): 
            self.resizedImage = image.resize((newWidth, newHeight), Image.ANTIALIAS)
            self.newImage = ImageTk.PhotoImage(self.resizedImage)
            return self.newImage

        self.diagram = Image.open(getFilePath('img\\pieceDiagrams\\' + 'EmptyDiagram.png'))
        self.pawnDiagramImg = resizeImage(self, self.diagram, int(ptWidth*0.75), int(ptHeight*0.75))
        self.pieceDiagram = Label(self.toolTipFrame, bg = 'white', image=self.pawnDiagramImg)
        self.pieceDiagram.grid(column=0,row=1, padx=10, sticky=(N,S,E,W))

        self.toolTipDescription = Label(self.toolTipFrame,bg='white',text="", font = descriptionFont, wraplength=350)
        self.toolTipDescription.grid(column=0,row=2,padx=10, sticky=(N,S,E,W))

        #Will make CPU go first if CPU is playing with the white pieces
        if self.currentTurn == "CPU":
            self.after(1000,self.cpuMove())





    def getBonusGold(self):
        return self.bonusGold
    
    def getLivesLost(self):
        return self.livesLost
    
    def getWinsAdded(self):
        return self.winsAdded

    def getFilePath(self, filename):
        return os.path.realpath(__file__)+f'\\..\\{filename}'

    def resizeImage(self, image, newWidth, newHeight): 
        self.resizedImage = image.resize((newWidth, newHeight), Image.ANTIALIAS)
        self.newImage = ImageTk.PhotoImage(self.resizedImage)
        return self.newImage


    '''
    CHECKS IF KING IS IN THE GRAVEYARD/HAS BEEN TAKEN
    '''
    def checkGraveyard(self):
        for piece in self.deadPlayerPieces:
            if piece.getType() == "King":
                self.gameOver("CPU")
                self.isGameOver = True
                break
        for piece in self.deadCpuPieces:
            if piece.getType() == "King":
                self.gameOver("Player")
                self.isGameOver = True
                break
    
    '''
    INCREMENTS THE NUMBER OF WINS/LIVES BASED ON IF THE PLAYER ONE OR NOT AND RETURNS TO THE SHOP
    '''
    def gameOver(self, winner):
        self.winner = winner
        if winner == "Player":
            self.winsAdded = 1
            self.livesLost = 0
        if winner == "CPU":
            self.winsAdded = 0
            self.livesLost = 1
        if self.numWins + self.winsAdded == 5 or self.numLives - self.livesLost == 0:
            self.controller.showFrame("Game Over Screen", self.winner)
        else:
            self.controller.showFrame("Shop Screen",self.boardState)


    '''
    ADDS A PIECE TO THE GRAVEYARD
    '''
    def addToGraveyard(self, piece):
        graveyardWidth = self.width*0.15
        graveyardHeight = self.height*0.95
        graveWidth = graveyardWidth*0.15
        graveHeight = graveyardHeight*0.05
        
        if piece.getOwner() == "Player":
            self.deadPlayerPieces.append(piece)

            colNum = 0
            rowNum = 0 
            for deadPiece in self.deadPlayerPieces:
                if colNum >= 5: 
                    rowNum += 1
                    colNum = 0
                Label(self.playerGraveyard, bg = '#44BEB7', image=deadPiece.resizePiece(deadPiece.getImage(), int(graveWidth), int(graveHeight))).grid(column=colNum,row=rowNum, padx=3, sticky=(N,S,E,W))
                colNum += 1

            #Label(self.playerGraveyard, bg = '#44BEB7', image=self.deadPieceImg).grid(column=len(self.deadPlayerPieces),row=0, padx=3, sticky=(N,S,E,W))

        elif piece.getOwner() == 'CPU':
            self.deadCpuPieces.append(piece)

            colNum = 0
            rowNum = 0 
            for deadPiece in self.deadCpuPieces:
                if colNum >= 5: 
                    rowNum += 1
                    colNum = 0
                Label(self.cpuGraveyard, bg = '#44BEB7', image=deadPiece.resizePiece(deadPiece.getImage(), int(graveWidth), int(graveHeight))).grid(column=colNum,row=rowNum, padx=3, sticky=(N,S,E,W))
                colNum += 1


            

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
            self.toolTipPiece.configure(text=square.getPiece().getType() + " [" + str(square.getPiece().getValue()) + "]")

        self.newDiagram = Image.open(getFilePath('img\\pieceDiagrams\\' + square.getPiece().getMovesetType() + 'Diagram.png'))
        self.pieceDiagramImg = resizeImage(self, self.newDiagram, int(ptWidth*0.75), int(ptHeight*0.75))
        self.pieceDiagram.configure(image=self.pieceDiagramImg)
        self.toolTipDescription.configure(text=Movesets().getDescription(square.getPiece()))


    #brings the highest value piece in the graveyard back to life when a necromancer is taken
    def summonUndead(self, necromancer):
        if necromancer.getPiece().getOwner() == "Player":
            highestValuePieces = self.deadPlayerPieces[0]
            highestValue = highestValuePieces.getValue()
            
            for piece in self.deadPlayerPieces:
                if piece != highestValuePieces and piece != necromancer.getPiece():
                    if piece.getValue() > highestValue:
                        highestValuePieces = piece
                        highestValue = piece.getValue()

            undead = highestValuePieces
            self.deadPlayerPieces.remove(undead)

        elif necromancer.getPiece().getOwner() == "CPU":
            highestValuePieces = self.deadCpuPieces[0]
            highestValue = highestValuePieces.getValue()
            
            for piece in self.deadCpuPieces:
                if piece != highestValuePieces and piece != necromancer:
                    if piece.getValue() > highestValue:
                        highestValuePieces = piece
                        highestValue = piece.getValue()
                    elif piece.getValue() == highestValue:
                        highestValuePieces.append(piece)
            
            undead = highestValuePieces
            self.deadCpuPieces.remove(undead)
            
        return undead



    #start == the square the piece is starting on
    #end == the square the piece is being moved to
    def movePiece(self,start, end):

        #This code will run even if the game is over so that the King is shown as being taken (Doesn't actually do that rn tho)   
        if end.getPiece().getType() != "Empty":
            if start.getPiece().getType() == "Thief": #if piece taken by Thief, bonus gold for next shop is increased by 1
                self.bonusGold += 1
            self.addToGraveyard(end.getPiece())
            end.killPiece(self.chessBoard, self.graveyardData, start)
            start.getPiece().incrementPiecesTaken()
            if start.getPiece().getType() == "Mimic": 
                start.getPiece().setMovesetType(end.getPiece().getMovesetType())


        """
        Piece Specific Abilities
        """
        if start.getPiece().getType() == "Diplomat" and end.getPiece().getType() != "Empty":
            tempPiece = end.getPiece()
            end.placePiece(start.getPiece())
            end.getPiece().incrementMoves()
            tempPiece.changeOwner()
            start.placePiece(tempPiece)

        elif end.getPiece().getType() == "TrojanHorse": 
            trojan = ChessPiece(end.getPiece().getColor() + 'Trojan',end.getPiece().getOwner(),'Trojan', 0, 0,'Empty', end.getPiece().getColor(), 0)
            end.placePiece(start.getPiece())
            end.getPiece().incrementMoves() #increments the number of times the piece has been moved by one
            start.placePiece(trojan)
            
        elif end.getPiece().getType() == "Necromancer": 
            undeadPiece = self.summonUndead(end)
            end.placePiece(start.getPiece())
            end.getPiece().incrementMoves() #increments the number of times the piece has been moved by one
            start.placePiece(undeadPiece)
        
        elif end.getPiece().getType() == "Dynamite": 
            end.placePiece(start.getPiece())
            end.getPiece().incrementMoves() #increments the number of times the piece has been moved by one
            start.removePiece()
            for square in self.chessBoard:
                if square == end:
                    self.addToGraveyard(square.getPiece())
                    square.removePiece()
                    square.setIsDestroyed(True)
            self.resetSquares()

        elif end.getPiece().getType() == "LandMine": 
            end.placePiece(start.getPiece())
            end.getPiece().incrementMoves() #increments the number of times the piece has been moved by one
            start.removePiece()
            for square in self.chessBoard:
                destroy = False
                if square == end:
                    destroy = True
                elif square.getRow() == end.getRow()+1 and square.getCol() == end.getCol():
                    destroy = True
                elif square.getRow() == end.getRow()-1 and square.getCol() == end.getCol():
                    destroy = True
                elif square.getRow() == end.getRow() and square.getCol() == end.getCol()+1:
                    destroy = True
                elif square.getRow() == end.getRow() and square.getCol() == end.getCol()-1:
                    destroy = True
                
                if destroy == True:
                    self.addToGraveyard(square.getPiece())
                    square.removePiece()
                    square.setIsDestroyed(True)
            self.resetSquares()

        else:
            end.placePiece(start.getPiece())
            end.getPiece().incrementMoves() #increments the number of times the piece has been moved by one   
            start.removePiece()
        end.updateMoveset(self.chessBoard, 'move')

        self.checkGraveyard() #check if king has been taken

        
        #Sets the turn as the other player
        if self.currentTurn == "Player":
            self.currentTurn = "CPU"

        elif self.currentTurn == "CPU":
            self.currentTurn = "Player"

    def calculateBoardValue(self):
        self.boardValue = 0
        for square in self.chessBoard:
            if square.getPiece().getType() != 'Empty':
                if square.getPiece().getOwner() == 'CPU':
                    self.boardValue -= square.getPiece().getValue()
                elif square.getPiece().getOwner() == 'Player':
                    self.boardValue += square.getPiece().getValue()
        return self.boardValue

    """
    CALCULATES THE 'BEST' MOVE THE CPU CAN MAKE
    """
    def calculateBestMove(self):
        cpuPieces = [] 
        validMoves = []
        for square in self.chessBoard:
            if square.getPiece().getOwner() == 'CPU':
                cpuPieces.append(square) 
                cpuPiece = square
                cpuPiece.updateMoveset(self.chessBoard,'update')
            
        bestMoves = []
        for piece in cpuPieces:
            bestMove = ''
            equalBestMoves = []
            bestMoveValue = 100000
            for potentialMove in self.chessBoard:
                cord = [potentialMove.getCol(),potentialMove.getRow()]
                if cord in piece.getMoveset():
                    if potentialMove.getPiece().getType() != 'Empty':
                        if potentialMove.getPiece().getOwner() == 'CPU': #if piece taken is own piece
                            moveValue = self.boardValue + potentialMove.getPiece().getValue()

                        elif potentialMove.getPiece().getOwner() == 'Player': #if piece taken is players piece
                            moveValue = self.boardValue - potentialMove.getPiece().getValue()
                            if potentialMove.getPiece().getType() == "King": #make taking the king the most valuable move
                                moveValue -= 10000
                    else:
                        moveValue = self.boardValue

                    if moveValue < bestMoveValue:
                        bestMove = potentialMove
                        bestMoveValue = moveValue
                        equalBestMoves = []
                        equalBestMoves.append(potentialMove)
                    if moveValue == bestMoveValue:
                        equalBestMoves.append(potentialMove)

            #Selects a random move out of all of the possible best moves a piece can make
            if len(equalBestMoves) >= 1:
                randIndex = random.randint(0,len(equalBestMoves)-1)
                bestMove = equalBestMoves[randIndex]
                
            bestMoves.append([piece,bestMove,bestMoveValue])
        equalMoves = []
        if len(bestMoves) > 0:
            bestBestMove = bestMoves[0]
            bestBestMoveValue = bestMoves[0][2]
            for move in bestMoves:
                if move[2] < bestBestMoveValue:
                    bestBestMoveValue = move[2]
                    bestBestMove = move
                    equalMoves = []
                    equalMoves.append(move)

                elif move[2] == bestBestMoveValue:
                    equalMoves.append(move)

            return equalMoves



    #the CPU will make whatever move will make the overall value of the board tip in the CPUs direction (i.e it will take incentivize taking player pieces over random moves)
    def cpuMove(self):
        if len(self.chessBoard) > 0:
            self.calculateBoardValue()
            moveList = self.calculateBestMove()
            if len(moveList) > 1:
                randIndex = random.randint(0,len(moveList)-1)
                selectedMove = moveList[randIndex]
            else:
                selectedMove = moveList[0]
            self.movePiece(selectedMove[0],selectedMove[1])
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
                if square.getIsDestroyed() != True: #This line is used for preventing pieces from moving onto squares destroyed by a landmine
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

            if self.isGameOver != True: #Prevents the CPU from continuing to play after the game has ended
                if self.currentTurn == "CPU":
                    self.after(500,self.cpuMove()) #the number represents how long the CPU waits before moving
        return
        

                
    
