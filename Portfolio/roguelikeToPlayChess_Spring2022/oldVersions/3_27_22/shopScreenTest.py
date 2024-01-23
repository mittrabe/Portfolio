from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font

import random #for testing, remove after
from chessSquareTest import ChessSquare
from chessPieceTest import ChessPiece


###########################################
#             RESOURCES USED
###########################################
#https://pythonexamples.org/python-tkinter-button-change-font/


###########################################
#              SHOP SCREEN
###########################################
class ShopScreen(tk.Frame):

    # negative cost == spending money; postive cost == gaining moeny
    def makePurchase(self, cost):
        self.numCoins += cost

    def getNumCoins(self):
        return self.numCoins

    def buyPiece(self, piece):
        self.makePurchase(-3) #cost of buying a piece is 3
        self.piecesValue = self.piecesValue + piece.getPieceValue()
        self.updateUI()

    
    def getPiecesValue(self):
        return self.piecesValue
    def setPiecesValue(self, newValue):
        self.piecesValue = newValue
    def getMaxPiecesValue(self):
        return self.maxPiecesValue

    def addPieceValue(self):
        upgradeCost = 3
        if self.numCoins >= upgradeCost:
            self.maxPiecesValue = self.maxPiecesValue + 5
            self.makePurchase(-upgradeCost)
            self.updateUI()

    def getNumRows(self):
        return self.numRows
    def unlockRow(self):
        upgradeCost = 6
        if self.numCoins >= upgradeCost and self.numRows < 4:
            self.numRows = self.numRows + 1
            self.makePurchase(-upgradeCost)
            self.updateUI()

            for square in self.boardState:
                if square.getRow() >= 8-self.numRows:
                    square.setIsActive(TRUE)
                    square['bg'] = square.setBackground(square.getIsActive())

    def getPlayerColor(self):
        return self.playerColor
    def setPlayerColor(self, newColor):
        self.playerColor = newColor

    #Updates the values shown in the UI for number of coins, lives, wins, etc.
    def updateUI(self):
        self.coinText.configure(text = str(self.numCoins) + "/" + str(self.maxNumCoins))
        self.livesText.configure(text = str(self.numLives) + "/5")
        self.winsText.configure(text = str(self.numWins) + "/5")
        self.piecesValueText.configure(text = str(self.piecesValue) + "/" + str(self.maxPiecesValue))
        self.numRowsText.configure(text = str(self.numRows) + "/4")
        

    def __init__(self, parent, controller, boardState, numCoins, maxNumCoins, numLives, numWins, piecesValue, maxPiecesValue, numRows, playerColor, pieceState): #NEED TO IMPLEMENT # OF GAMES PLAYED
        #self.boardState = boardState
        self.numCoins = numCoins #number of coins they have left to spend
        self.maxNumCoins = maxNumCoins
        self.numLives = numLives #number of lives they have left
        self.numWins = numWins #number of wins they have 
        self.piecesValue = piecesValue #the current combined value of the pieces on their board
        self.maxPiecesValue = maxPiecesValue #The current max combined piece value they can place on the board
        self.numRows = numRows #The number of rows they have unlocked for placing pieces
        self.playerColor = playerColor

        #Populating the initial shop board with blank squares
        #for row in range(8):
            #for col in range(8):
                #self.boardState.append("empty") #needs to be lowercase 'empty'
        self.boardState = []
        self.pieceState = pieceState
        

        #FOR TESTING, DELETE AFTER
        self.fullBoardState = [] 
        for index in range(64):
            self.fullBoardState.append("empty") 


#=====================
# FRAME CONFIGURATION
#=====================
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="Menu.TFrame")
        
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

        def resizeImage(self, image, newWidth, newHeight): 
            self.resizedImage = image.resize((newWidth, newHeight), Image.ANTIALIAS)
            self.newImage = ImageTk.PhotoImage(self.resizedImage)
            return self.newImage

#=====================
#   FRAME CONTENT
#=====================
        width = parent.winfo_screenwidth()
        height = parent.winfo_screenheight()

        #~~~~~~~~~~~~~~~~~~~
        #      TOP UI
        #~~~~~~~~~~~~~~~~~~~
        #STYLES AND FONTS
        style.configure('ShopUI.TFrame', background ="white")
        style.configure('Spacer.TFrame', background = '#00868B')
        topMenuFont = font.Font(family='Roboto', size=52)
        bottomMenuFont = font.Font(family='Roboto', size=42)

    
        shortWidth = width*0.1
        longWidth = width*0.15
        shopUIHeight = height*0.1

        iconWidth = int(shortWidth*0.5)
        iconHeight = int(shopUIHeight*0.9)

        
        #COINS
        self.coinFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        self.coinFrame.grid(column=0, row=0, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))

        self.coinIcon = Image.open(getFilePath('img\\' + 'coin.jpg'))
        self.coinImg = resizeImage(self, self.coinIcon, iconWidth, iconHeight)

        self.coinText = Label(self.coinFrame, bg='white', font=topMenuFont)
        self.coinText.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.coinFrame.grid_columnconfigure(0, weight=1)
        self.coinLabel = Label(self.coinFrame, image=self.coinImg, bg='white')
        self.coinLabel.grid(column=1,row=0, padx=10, sticky=(N,S,E,W))


        #LIVES
        self.livesFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        self.livesFrame.grid(column=1, row=0, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))

        self.livesIcon = Image.open(getFilePath('img\\' + 'heart.jpg'))
        self.livesImg = resizeImage(self, self.livesIcon, iconWidth, iconHeight)

        self.livesText = Label(self.livesFrame, bg='white', font=topMenuFont)
        self.livesText.grid(column=0,row=0, padx=10)
        self.livesFrame.grid_columnconfigure(0, weight=1)
        self.livesLabel = Label(self.livesFrame, image=self.livesImg, bg='white')
        self.livesLabel.grid(column=1,row=0, padx=10)


        #WINS
        self.winsFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        self.winsFrame.grid(column=2, row=0, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))

        self.winsIcon = Image.open(getFilePath('img\\' + 'trophy.jpg'))
        self.winsImg = resizeImage(self, self.winsIcon, iconWidth, iconHeight)

        self.winsText = Label(self.winsFrame, bg='white', font=topMenuFont)
        self.winsFrame.grid_columnconfigure(0, weight=1)
        self.winsText.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.winsLabel = Label(self.winsFrame, image=self.winsImg, bg='white')
        self.winsLabel.grid(column=1,row=0, padx=10, sticky=(N,S,E,W))


        #SPACER (Invisible frame meant to act as a way of pushing the UI elements apart)
        spacerFrame = ttk.Frame(self, style='Spacer.TFrame', width=width*0.2, height=shopUIHeight)
        spacerFrame.grid(row=0, column=3, padx=5)

        #PIECES VALUE
        self.piecesValueFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        self.piecesValueFrame.grid(column=4, row=0, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))

        self.piecesValueIcon = Image.open(getFilePath('Chess Pieces\\' + 'blackPawn.png'))
        self.piecesValueImg = resizeImage(self, self.piecesValueIcon, iconWidth, iconHeight)

        self.piecesValueText = Label(self.piecesValueFrame, bg='white', font=topMenuFont)
        self.piecesValueFrame.grid_columnconfigure(0, weight=1)
        self.piecesValueText.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.piecesValueLabel = Label(self.piecesValueFrame, image=self.piecesValueImg, bg='white')
        self.piecesValueLabel.grid(column=1,row=0, padx=10, sticky=(N,S,E,W))

        #NUM ROWS
        self.numRowsFrame = ttk.Frame(self, style='shopUI.TFrame', width=longWidth, height=shopUIHeight)
        self.numRowsFrame.grid(column=5, row=0, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))

        self.numRowsIcon = Image.open(getFilePath('img\\' + 'row.png'))
        self.numRowsImg = resizeImage(self, self.numRowsIcon, iconWidth, iconHeight)

        self.numRowsText = Label(self.numRowsFrame, bg='white', font=topMenuFont)
        self.numRowsFrame.grid_columnconfigure(0, weight=1)
        self.numRowsText.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.numRowsLabel = Label(self.numRowsFrame, image=self.numRowsImg, bg='white')
        self.numRowsLabel.grid(column=1,row=0, padx=10, sticky=(N,S,E,W))


        self.updateUI()


        #~~~~~~~~~~~~~~~~~~
        #   MIDDLE UI
        #~~~~~~~~~~~~~~~~~~

        testWidth = int(width*0.35/4)
        testHeight = int(height*0.5/4)
        

        #ADD ROW
        self.buyRowFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        self.buyRowFrame.grid(column=5, row=1, padx = 5, pady = 50, rowspan=1, sticky=(S,W))

        self.buyRowIcon = Image.open(getFilePath('img\\' + 'addRow3.png'))
        self.buyRowImg = resizeImage(self, self.buyRowIcon, testWidth, testHeight)

        #self.numRowsText = Label(self.buyRowFrame, bg='white', font=topMenuFont)
        #self.numRowsFrame.grid_columnconfigure(0, weight=1)
        #self.numRowsText.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.buyRowButton = Button(self.buyRowFrame, image=self.buyRowImg, borderwidth=0, bg='#B58863') 
        self.buyRowButton.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.buyRowButton['command'] = lambda: self.unlockRow()

        #ADD PIECE VALUE
        self.addPieceFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        self.addPieceFrame.grid(column=5, row=2, padx = 5, pady = 50, rowspan=1, sticky=(N,W))

        self.addPieceIcon = Image.open(getFilePath('img\\' + 'addPiece.png'))
        self.addPieceImg = resizeImage(self, self.addPieceIcon, testWidth, testHeight)

        self.addPieceButton = Button(self.addPieceFrame, image=self.addPieceImg, borderwidth=0, bg='#F0D9B5') 
        self.addPieceButton.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.addPieceButton['command'] = lambda: self.addPieceValue()
        
        
        #~~~~~~~~~~~~~~~~~~~
        #    BOTTOM UI
        #~~~~~~~~~~~~~~~~~~~

        spacerFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        spacerFrame.grid(row=3, column=0, padx=5)

        spacerFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        spacerFrame.grid(row=3, column=1, padx=5)

        #REROLL
        rerollFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        rerollFrame.grid(column=0, row=3, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))
        rerollFrame.columnconfigure(0, weight=1)

        rerollButton = Button(rerollFrame, text="Reroll", borderwidth=0, bg='white', font=bottomMenuFont)
        rerollButton.grid(column=0,row=0, sticky=(N,S,E,W))
        rerollButton['command'] = lambda: rerollPieces(self, FALSE)


        #SELL
        sellFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        sellFrame.grid(column=1, row=3, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))
        sellFrame.columnconfigure(0, weight=1)
        sellButton = Button(sellFrame, text="$ Sell", borderwidth=0, bg='white', font=bottomMenuFont)
        sellButton.grid(column=0,row=0, sticky=(N,S,E,W))
        sellButton['command'] = lambda: sellPiece(self)


        spacerFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        spacerFrame.grid(row=3, column=2, padx=5)

        spacerFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        spacerFrame.grid(row=3, column=4, padx=5)
        

        def endTurn(self):
            pieceState = []
            for square in self.boardState:
                square.getPiece().setHomeSquare(square)
                pieceState.append(square.getPiece())

            controller.showFrame("Chess Screen", self.boardState, pieceState)
            
        #END TURN
        endTurnFrame = ttk.Frame(self, style='shopUI.TFrame', width=longWidth, height=shopUIHeight)
        endTurnFrame.grid(column=5, row=3, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))
        endTurnFrame.columnconfigure(0, weight=1)
        endTurnButton = Button(endTurnFrame, text="End Turn", borderwidth=0, bg='white', font=bottomMenuFont)
        endTurnButton.grid(column=0,row=0, sticky=(N,S,E,W))
        endTurnButton['command'] = lambda: endTurn(self)





        #locked light square: 807668
        #locked dark square: 564130
        #~~~~~~~~~~~~~~~~~~~
        #    SHOP BOARD
        #~~~~~~~~~~~~~~~~~~~
        boardWidth = width*0.4
        boardHeight = height*0.46
        style.configure('ChessBoard.TFrame', background ="brown")
        board = ttk.Frame(self, style='ChessBoard.TFrame', width = boardWidth, height = boardHeight)
        board.grid(column=0, row=1, padx = 20, pady = 50, sticky = (N,S), columnspan=5, rowspan=2)


        def resetSquares():
            for square in self.boardState:
                square['bg'] = square.setBackground(square.getIsActive())
            for child in shopItemFrame.winfo_children():
                child['bg'] = child.setBackground(child.getIsActive())

        def movePiece(start, end):
            if self.piecesValue > self.maxPiecesValue:
                print("CAN'T EXCEED PIECE VALUE")
            else:
                tempPiece = end.getPiece() #when a piece is moved ontop of another in the shop, they will just switch spots
                end.placePiece(start.getPiece())
                start.placePiece(tempPiece)

                
        def buttonPress(event): #event refers to the button being pressed
            pieceMoved = False # 
            resetSquares() 
            if event.getIsActive() == True: #Only lets you select squares in the active rows the user has unlocked
                if event.isSelected() == True:
                    event.deselectSquare()
                else:
                    if event not in shopItemFrame.winfo_children(): 

                        for square in self.boardState:
                            if square.isSelected() and square.getPiece().getPieceType() != 'Empty':
                                movePiece(square,event)
                                event.setSelected(False)
                                square.setSelected(False)
                                pieceMoved = True

                        for shopItem in shopItemFrame.winfo_children() : 
                            if shopItem.isSelected() and shopItem.getPiece().getPieceType() != 'Empty':
                                #Only lets you buy a piece if you have 3 or more coins and buying the piece wouldn't put you over the max value
                                if self.getNumCoins()-3 >= 0 and shopItem.getPiece().getPieceValue()+self.piecesValue <= self.maxPiecesValue :
                                   #Prevents an existing piece from being deleted if a shop piece is placed ontop of it
                                    if (shopItem in shopItemFrame.winfo_children() and event.getPiece().getPieceType() == 'Empty'):
                                        self.buyPiece(shopItem.getPiece())
                                        movePiece(shopItem,event)
                                        event.setSelected(False)
                                        shopItem.setSelected(False)
                                        pieceMoved = True


                    if pieceMoved == False: #if a button is pressed and no piece ends up getting moved, will instead select that square 
                        for square in self.boardState:
                            if square.isSelected():
                                square.setSelected(False)
                        for shopItem in shopItemFrame.winfo_children():
                            if shopItem.isSelected(): 
                                shopItem.setSelected(False)
                        
                        print(event.getPiece().getTimesMoved())
                        event.selectSquare() #changes the color of the selected square 
                        

                        #highlightSquares(event) #highlights all the squares that can be moved to from the selected Square
            return


        #READDS THE PIECES TO THE SHOP BOARD ON SUBSEQUENT VISITS TO THE SHOP
        index = 0
        if len(boardState) > 0:
            for row in range(8):
                for col in range(8):
                    isActive = FALSE
                    if row >= 8-self.numRows:
                        isActive = TRUE
                    details = boardState[index].getDetails()
                    details[0].updatePiece()

                    self.boardState.append(ChessSquare(board, self.pieceState[index],details[1],details[2],boardWidth*1.4,boardHeight*1.4,isActive, self.boardState))

                    if row < 4:
                        self.boardState[index].grid_remove()
                    index += 1
                                

        #THIS IS THE FIRST TIME SETUP CODE                    
        elif len(boardState) == 0:
            # Creates the squares/buttons on the chess board. Each square is automatically populated with the "empty" chess piece
            chessSquares = []
            index = 0
            #for index in range(64)
            for row in range(8):
                for col in range(8):
                    isActive = FALSE
                    piece = ChessPiece('empty', 'Empty', 0, 0, self.playerColor, 0)

                    if row >= 8-self.numRows:
                        isActive = TRUE
                    

                    self.boardState.append(ChessSquare(board, 
                        piece,
                        row, 
                        col,
                        boardWidth*1.4,
                        boardHeight*1.4,
                        isActive,
                        self.boardState
                    ))

                    if row < 4:
                        self.boardState[index].grid_remove()
                    #chessSquares.append(ChessSquare(board, 
                    #    piece,
                    #    row, 
                    #    col,
                    #    boardWidth*1.4,
                    #    boardHeight*1.4,
                    #    isActive
                    #    ))
                    index += 1

            # Sets all of the squares to perform the buttonPress function when clicked
            activeSquares = []
            for square in self.boardState:
                if square.getIsActive() == TRUE:
                    activeSquares.append(square)
                #square['command'] = lambda square=square: buttonPress(square)

            #The first time (Places the king on a random square to start)
            randIndex = random.randint(0,len(activeSquares)-1)
            activeSquares[randIndex].placePiece(ChessPiece(self.playerColor + 'King', 'King', 0, 0, self.playerColor, 0))

        for square in self.boardState:
            square['command'] = lambda square=square: buttonPress(square)


        #~~~~~~~~~~~~~~~~~~~
        #   SHOP ITEMS
        #~~~~~~~~~~~~~~~~~~~
        style.configure('ShopItems.TFrame', background = '#00868B') #00868B
        shopItemFrame = ttk.Frame(self, style='ShopItems.TFrame', width=longWidth, height=shopUIHeight)
        shopItemFrame.grid(column=2, row=3, padx = 25, pady = 5, columnspan=2, rowspan=1, sticky=(N,S,E,W))

     
        def rerollPieces(self, setup): #Rerolls cost 1 coin
            if self.numCoins > 0:
                pieceList = ['Pawn', 'Bishop', 'Knight', 'Rook', 'Queen'] #TEMPORARY, REPLACE!!
                for child in shopItemFrame.winfo_children():
                    randIndex = random.randint(0,len(pieceList)-1)
                    child.placePiece(ChessPiece('black' + pieceList[randIndex], pieceList[randIndex], 0, 0, self.playerColor,0))

                if setup == FALSE: #setup is used to prevent the initial setup reroll from costing money
                    self.makePurchase(-1)
                    self.updateUI()

        def sellPiece(self): #pieces sold are worth 1 coin
            for square in self.boardState:
                if square.isSelected() and square.getPiece().getPieceType() != 'Empty' and square.getPiece().getPieceType() != 'King':
                    self.makePurchase(1)
                    self.piecesValue = self.piecesValue - square.getPiece().getPieceValue()
                    self.updateUI()
                    square.removePiece()
                elif square.getPiece().getPieceType() == 'Empty' or square.getPiece().getPieceType() == 'King':
                    resetSquares()
                    square.deselectSquare()


        shopSquareWidth = width*0.4
        shopSquareHeight = height*0.46
        row = 0
        col = 0
        isActive = TRUE
        for i in range(4):
            piece = ChessPiece('empty', 'Empty', 0, 0, self.playerColor, 0)
            ChessSquare(shopItemFrame, 
                piece,
                row, 
                col,
                shopSquareWidth*1.4,
                shopSquareHeight*1.05,
                isActive,
                self.boardState
                )
            col = col + 1
        rerollPieces(self, TRUE)

        for child in shopItemFrame.winfo_children(): #Adds padding between the 4 squares in the shop
            child.grid_configure(padx=10)
            child['command'] = lambda child=child: buttonPress(child)
                

    def getBoardState(self):
        return self.boardState
    def setBoardState(self, newBoardState):
        self.boardState = newBoardState
