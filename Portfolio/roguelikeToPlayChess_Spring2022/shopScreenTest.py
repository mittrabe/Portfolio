from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
import sqlalchemy as db

import random 
from chessSquareTest import ChessSquare
from chessPieceTest import ChessPiece
from tooltip import ToolTip
from moveset import Movesets


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
        self.piecesValue = self.piecesValue + piece.getValue()
        self.updateUI()

    
    def getPiecesValue(self):
        return self.piecesValue
    def setPiecesValue(self, newValue):
        self.piecesValue = newValue
    def getMaxPiecesValue(self):
        return self.maxPiecesValue

    def addPieceValue(self):
        upgradeCost = 4 #cost of buying a piece value upgrade is 4
        if self.numCoins >= upgradeCost:
            self.maxPiecesValue = self.maxPiecesValue + 5 #increases max piece value by 5
            self.makePurchase(-upgradeCost)
            self.updateUI()
        
    def getCpuUsername(self):
            return self.cpuUsername

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

    def getNumTurns(self):
        return self.numTurns
    def setNumTurns(self, turns):
        self.numTurns = turns

    def getNumLives(self):
        return self.numLives
    def getNumWins(self):
        return self.numWins

    def getFrozenPieces(self):
        return self.frozenPieces
    def setFrozenPieces(self, pieces):
        self.forzenPieces = pieces

    #Updates the values shown in the UI for number of coins, lives, wins, etc.
    def updateUI(self):
        if self.numCoins < 10:
            self.coinCount = "0" + str(self.numCoins)
        else: 
            self.coinCount = str(self.numCoins)
        self.coinText.configure(text = self.coinCount + "/" + str(self.maxNumCoins))
        self.livesText.configure(text = str(self.numLives) + "/5")
        self.winsText.configure(text = str(self.numWins) + "/5")

        if self.numTurns < 10:
            self.turnCount = "0" + str(self.numTurns)
        else: 
            self.turnCount = str(self.numTurns)
        self.turnsText.configure(text=str(self.turnCount))

        if self.piecesValue < 10:
            self.valueCount = "0" + str(self.piecesValue)
        else: 
            self.valueCount = str(self.piecesValue)
        self.piecesValueText.configure(text = str(self.valueCount) + "/" + str(self.maxPiecesValue))
        self.numRowsText.configure(text = str(self.numRows) + "/4")
    
    '''
    UPDATES THE SHOP POOL TO HAVE BETTER PIECES AS THE GAME PROGRESSES
    '''
    def updateShopPool(self):
        dummyPiece = ChessPiece('empty', 'Empty', 'Empty', 0, 0,'Empty', self.playerColor, 0)
        pieceList = dummyPiece.getValueList()
        self.shopPool = []
        if self.numTurns <= 2: #pieces with value 1 & 2 in Shop pool in round 1 and 2 
            self.shopPool = pieceList[1] + pieceList[2]
        elif self.numTurns <= 4: #value 3-4 added to shop pool on turn 3-4
            self.shopPool = pieceList[1] + pieceList[2] + pieceList[3] + pieceList[4]
        elif self.numTurns <= 6: #value 5-6 added to the shop pool on turn 5-6
            self.shopPool = pieceList[1] + pieceList[2] + pieceList[3] + pieceList[4] + pieceList[5] + pieceList[6]
        elif self.numTurns >= 7: #All pieces in shop pool
            self.shopPool = pieceList[1] + pieceList[2] + pieceList[3] + pieceList[4] + pieceList[5] + pieceList[6] + pieceList[7] + pieceList[8] + pieceList[9]
        self.shopPool = [x for x in self.shopPool if not isinstance(x, int)]


    '''
    CREATES TOOL TIPS THAT HOVER OVER EACH SQUARE
    '''
    def CreateToolTip(self, widget, text):
        self.toolTip = ToolTip(widget)
        def enter(event):
            self.toolTip.showtip(text)
        def leave(event):
            self.toolTip.hidetip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)
    

    '''
    CHANGES WHAT THE TOOL TIP SAYS WHEN PIECES ARE MOVED 
    '''
    def updateTooltip(self, square):
        squareDesc = Movesets().getDescription(square.getPiece())
        if square.getPiece().getType() != 'Empty':
            underline = ""
            for i in range(len(square.getPiece().getType())):
                underline += '\u2501'
            self.CreateToolTip(square, text = square.getPiece().getType() + ' [' + str(square.getPiece().getValue()) + ']\n' + underline + '\n' + squareDesc)
        else:
            self.CreateToolTip(square, text = '')
        

    def __init__(self, parent, controller, boardState, numCoins, maxNumCoins, numLives, numWins, numTurns, piecesValue, maxPiecesValue, numRows, playerColor, pieceState, frozenPieces, username): #NEED TO IMPLEMENT # OF GAMES PLAYED
        #self.boardState = boardState
        self.numCoins = numCoins #number of coins they have left to spend
        self.maxNumCoins = maxNumCoins
        self.numLives = numLives 
        self.numWins = numWins 
        self.numTurns = numTurns #number of turns that have passed
        self.piecesValue = piecesValue #the current combined value of the pieces on their board
        self.maxPiecesValue = maxPiecesValue #The current max combined piece value they can place on the board
        self.numRows = numRows #The number of rows they have unlocked for placing pieces
        self.playerColor = playerColor
        self.username = username
        print(username)
        if playerColor == "black":
            self.cpuColor = "white"
        else:
            self.cpuColor = "black"

        self.boardState = []
        self.pieceState = pieceState
        self.updateShopPool()

        self.frozenPieces = frozenPieces #Frozen pieces that are carried over from the last shop
    
        


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

        #Turns
        self.turnsFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        self.turnsFrame.grid(column=3, row=0, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))

        self.turnsIcon = Image.open(getFilePath('img\\' + 'turns.jpg'))
        self.turnsImg = resizeImage(self, self.turnsIcon, iconWidth, iconHeight)

        self.turnsText = Label(self.turnsFrame, bg='white', font=topMenuFont)
        self.turnsFrame.grid_columnconfigure(0, weight=1)
        self.turnsText.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.turnsLabel = Label(self.turnsFrame, image=self.turnsImg, bg='white')
        self.turnsLabel.grid(column=1,row=0, padx=10, sticky=(N,S,E,W))

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

        self.buyRowButton = Button(self.buyRowFrame, image=self.buyRowImg, borderwidth=0, bg='#B58863') 
        self.buyRowButton.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.buyRowButton['command'] = lambda: self.unlockRow()
        self.CreateToolTip(self.buyRowButton, text = 'Purchase Row (-$6)')

        #ADD PIECE VALUE
        self.addPieceFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        self.addPieceFrame.grid(column=5, row=2, padx = 5, pady = 50, rowspan=1, sticky=(N,W))

        self.addPieceIcon = Image.open(getFilePath('img\\' + 'addPiece.png'))
        self.addPieceImg = resizeImage(self, self.addPieceIcon, testWidth, testHeight)

        self.addPieceButton = Button(self.addPieceFrame, image=self.addPieceImg, borderwidth=0, bg='#F0D9B5') 
        self.addPieceButton.grid(column=0,row=0, padx=10, sticky=(N,S,E,W))
        self.addPieceButton['command'] = lambda: self.addPieceValue()

        self.CreateToolTip(self.addPieceButton, text = '+5 to max piece value (-$4)')
        
        
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

        rerollButton = Button(rerollFrame, text="Reroll (-1)", borderwidth=0, bg='white', font=bottomMenuFont)
        rerollButton.grid(column=0,row=0, sticky=(N,S,E,W))
        rerollButton['command'] = lambda: rerollPieces(self, FALSE)


        #SELL
        sellFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        sellFrame.grid(column=1, row=3, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))
        sellFrame.columnconfigure(0, weight=1)

        sellButton = Button(sellFrame, text="$ Sell (+1)", borderwidth=0, bg='white', font=bottomMenuFont)
        sellButton.grid(column=0,row=0, sticky=(N,S,E,W))
        sellButton['command'] = lambda: sellPiece(self)


        spacerFrame = ttk.Frame(self, style='Spacer.TFrame', width=longWidth, height=shopUIHeight)
        spacerFrame.grid(row=3, column=2, padx=5)


        #FREEZE 
        freezeFrame = ttk.Frame(self, style='ShopUI.TFrame', width=longWidth, height=shopUIHeight)
        freezeFrame.grid(column=4, row=3, padx = 5, pady = 5, rowspan=1, sticky=(N,S,E,W))
        freezeFrame.columnconfigure(0, weight=1)

        freezeButton = Button(freezeFrame, text="Freeze", borderwidth=0, bg='white', font=bottomMenuFont)
        freezeButton.grid(column=0,row=0, sticky=(N,S,E,W))
        freezeButton['command'] = lambda: freezePiece(self)

        '''
        Saves the locations of each piece in the shop and creates the CPU pieces
        '''
        def endTurn(self):
            pieceState = []
            self.frozenPieces = []
            for child in shopItemFrame.winfo_children():
                if child.getIsFrozen() == True:
                    self.frozenPieces.append(child.getPiece())

            for square in self.boardState:
                square.getPiece().setHomeSquare(square)
                pieceState.append(square.getPiece())

            placeCpuPieces()
            for square in self.boardState:
                if square.getRow() < 4:
                    square['command'] = lambda square=square: buttonPress(square)
                    #descText = Movesets().getDescription(square.getPiece())
                    self.updateTooltip(square)
                
            controller.showFrame("Chess Screen", self.boardState, pieceState,self.playerColor)
            
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

        '''
        RETURNS THE BACKGROUND COLOR OF SQUARES TO THEIR DEFAULT STATE
        '''
        def resetSquares():
            for square in self.boardState:
                square['bg'] = square.setBackground(square.getIsActive())
            for child in shopItemFrame.winfo_children():
                if child.getIsFrozen() == False:
                    child['bg'] = child.setBackground(child.getIsActive())

        '''
        SWAPS THE PIECES LOCATED ON START AND END
        '''
        def movePiece(start, end):
            if self.piecesValue > self.maxPiecesValue:
                print("CAN'T EXCEED PIECE VALUE")
            else:
                tempPiece = end.getPiece() #when a piece is moved ontop of another in the shop, they will just switch spots
                end.placePiece(start.getPiece())
                start.placePiece(tempPiece)
                self.updateTooltip(start)
                self.updateTooltip(end)
                self.toolTip.hidetip()

        
        def buttonPress(event): #event refers to the button being pressed
            pieceMoved = False # 
            resetSquares() 
            if event.getIsActive() == True: #Only lets you select squares in the active rows the user has unlocked
                if event.isSelected() == True:
                    event.deselectSquare()
                else:
                    if event not in shopItemFrame.winfo_children(): 

                        for square in self.boardState:
                            if square.isSelected() and square.getPiece().getType() != 'Empty':
                                movePiece(square,event)
                                event.setSelected(False)
                                square.setSelected(False)
                                pieceMoved = True

                        '''
                        IF THE PIECE SELECTED IS IN THE SHOP
                        '''
                        for shopItem in shopItemFrame.winfo_children() : 
                            if shopItem.isSelected() and shopItem.getPiece().getType() != 'Empty':
                                #Only lets you buy a piece if you have 3 or more coins and buying the piece wouldn't put you over the max value
                                if self.getNumCoins()-3 >= 0 and shopItem.getPiece().getValue()+self.piecesValue <= self.maxPiecesValue :
                                   #Prevents an existing piece from being deleted if a shop piece is placed ontop of it
                                    if (shopItem in shopItemFrame.winfo_children() and event.getPiece().getType() == 'Empty'):
                                        if shopItem.getIsFrozen():
                                            shopItem.unfreeze()
                                        self.buyPiece(shopItem.getPiece())
                                        movePiece(shopItem,event)
                                        event.setSelected(False)
                                        shopItem.setSelected(False)
                                        pieceMoved = True


                    '''
                    if a button is pressed and no piece ends up getting moved, will instead select that square 
                    '''
                    if pieceMoved == False: 
                        for square in self.boardState:
                            if square.isSelected():
                                square.setSelected(False)
                        for shopItem in shopItemFrame.winfo_children():
                            if shopItem.isSelected(): 
                                shopItem.setSelected(False)
                        
                        print(event.getPiece().getTimesMoved())
                        event.selectSquare() #changes the color of the selected square 
                        
            return


        '''
        POPULATES THE CPU's SIDE OF THE BOARD WITH TEAMS FROM OTHER PLAYERS
        '''
        def placeCpuPieces():
            engine = db.create_engine('sqlite:///C:\\Users\\1magi\\Desktop\\roguelikeToPlayChess\\chessDatabase.db')
            connection = engine.connect()
            metadata = db.MetaData()
            cpuBoard = db.Table('cpuBoard',metadata,autoload=True,autoload_with=engine)
            

            #SAVE THE PLAYER'S BOARD TO THE DATABASE TO BE USED BY THE CPU
            playerBoardStr = ''
            playerBoard = []
            validBoard = False
            for square in self.boardState:
                square.getPiece().setHomeSquare(square)
                pieceState.append(square.getPiece())
                
                if square.getRow() >= 4:
                    playerBoard.append(square.getPiece().getType())
                
                if square.getPiece().getType() != 'Empty' and square.getPiece().getType() != 'King':
                    validBoard = True
            
            
            if validBoard == True:
                #Add all pieces to the database in reverse 
                i = len(playerBoard)-1
                while i >= 0 :
                    playerBoardStr += playerBoard[i] + ','
                    i -= 1
                playerBoardStr = playerBoardStr[:-1] #drop the ',' at the end

                query = db.insert(cpuBoard).values(turn=self.numTurns,user=self.username,pieces=playerBoardStr)
                resultProxy = connection.execute(query)
                results = connection.execute(db.select([cpuBoard])).fetchall()
                #print(results)

                #Pull all the board for that turn and randomly select one
                cpuStates = connection.execute(db.select([cpuBoard]).where(db.and_(cpuBoard.columns.turn == self.numTurns, cpuBoard.columns.user != self.username))).fetchall()
                randIndex = random.randint(0,len(cpuStates)-1)
                cpuBoard = cpuStates[randIndex][2].split(',')

                self.cpuUsername = cpuStates[randIndex][1]

                #ADDS CPU PIECES TO THE BOARD
                index = 0
                for square in self.boardState:
                    if square.getRow() < 4:
                        if cpuBoard[index] == 'Empty':
                            square.placePiece(ChessPiece('empty', 'Empty','Empty', 0, 0,'Empty', self.playerColor, 0))
                        else:
                            square.placePiece(ChessPiece(self.cpuColor + cpuBoard[index],'CPU', cpuBoard[index], 0, 0, 'Empty', self.cpuColor, 0))
                        index += 1
                    else:
                        break
    

    
        #THIS IS THE FIRST TIME SETUP CODE                    
        if len(boardState) == 0:
            # Creates the squares/buttons on the chess board. Each square is automatically populated with the "empty" chess piece
            chessSquares = []
            index = 0
            #for index in range(64)
            for row in range(8):
                for col in range(8):
                    isActive = FALSE
                    piece = ChessPiece('empty', 'Empty','Empty', 0, 0,'Empty', self.playerColor, 0)

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
            activeSquares[randIndex].placePiece(ChessPiece(self.playerColor + 'King','Player','King', 0, 0,'Empty', self.playerColor, 0))
        

        #READDS THE PIECES TO THE SHOP BOARD ON SUBSEQUENT VISITS TO THE SHOP
        elif len(boardState) > 0:
            index = 0
            for row in range(8):
                for col in range(8):
                    isActive = FALSE
                    if row >= 8-self.numRows:
                        isActive = TRUE
                    details = boardState[index].getDetails()
                    details[0].updatePiece(row)

                    
                    
                    self.boardState.append(ChessSquare(board, self.pieceState[index],details[1],details[2],boardWidth*1.4,boardHeight*1.4,isActive, self.boardState))


                    if row < 4:
                        self.boardState[index].grid_remove() #Hides all but the last 4 rows in the chess board
                    index += 1
        
        #THIS CODE HAPPENS EVERY TIME REGARDLESS OF WHICH ROUND IT IS
        placeCpuPieces()
        for square in self.boardState:
            square['command'] = lambda square=square: buttonPress(square)
            #descText = Movesets().getDescription(square.getPiece())
            self.updateTooltip(square)
            #self.CreateToolTip(square, text = descText)


        #~~~~~~~~~~~~~~~~~~~
        #   SHOP ITEMS
        #~~~~~~~~~~~~~~~~~~~
        style.configure('ShopItems.TFrame', background = '#00868B') #00868B
        shopItemFrame = ttk.Frame(self, style='ShopItems.TFrame', width=longWidth, height=shopUIHeight)
        shopItemFrame.grid(column=2, row=3, padx = 25, pady = 5, columnspan=2, rowspan=1, sticky=(N,S,E,W))

        
        '''
        REROLLS THE PIECES IN THE SHOP
        '''
        def rerollPieces(self, setup): #Rerolls cost 1 coin
            if self.numCoins > 0:
                
                for child in shopItemFrame.winfo_children():
                    if child.getIsFrozen() != True: #only rerolls pieces that aren't frozen
                        randIndex = random.randint(0,len(self.shopPool)-1)
                        child.placePiece(ChessPiece(self.playerColor + self.shopPool[randIndex],'Player', self.shopPool[randIndex], 0, 0,'Empty', self.playerColor,0))
                        if child.getPiece().getType() == "Mimic":
                            child.getPiece().setMovesetType("King")
                        self.updateTooltip(child)


                if setup == FALSE: #setup is used to prevent the initial setup reroll from costing money
                    self.makePurchase(-1)
                    self.updateUI()


        '''
        SELLS AN OWNED PIECE FOR 1 GOLD
        '''
        def sellPiece(self): #pieces sold are worth 1 coin
            for square in self.boardState:
                if square.isSelected() and square.getPiece().getType() != 'Empty' and square.getPiece().getType() != 'King':
                    self.makePurchase(1)
                    self.piecesValue = self.piecesValue - square.getPiece().getValue()
                    self.updateUI()
                    square.removePiece()
                    self.updateTooltip(square)
                elif square.getPiece().getType() == 'Empty' or square.getPiece().getType() == 'King':
                    resetSquares()
                    square.deselectSquare()
        
        '''
        FREEZES A PIECE IN THE SHOP (frozen pieces remain in the shop when rerolling and between visits to the shop)
        '''
        def freezePiece(self):
            for child in shopItemFrame.winfo_children():
                if child.isSelected():
                    if child.getIsFrozen() == True:
                        child.unfreeze()
                    elif child.getIsFrozen() == False:
                        child.freeze()


        shopSquareWidth = width*0.4
        shopSquareHeight = height*0.46
        row = 0
        col = 0
        isActive = TRUE
        for i in range(4):
            piece = ChessPiece('empty', 'Empty','Empty', 0, 0,'Empty', self.playerColor, 0)
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

        if len(self.frozenPieces) > 0:
            shopItems = shopItemFrame.winfo_children()
            for i in range(len(self.frozenPieces)):
                shopItems[i].placePiece(self.frozenPieces[i])
                if shopItems[i].getPiece().getType() == "Mimic":
                    shopItems[i].getPiece().setMovesetType("King")
                self.updateTooltip(shopItems[i])
                shopItems[i].freeze()


        

        for child in shopItemFrame.winfo_children(): #Adds padding between the 4 squares in the shop

            #self.CreateToolTip(child, text = Movesets().getDescription(child.getPiece()))
            self.updateTooltip(child)
            child.grid_configure(padx=10)
            child['command'] = lambda child=child: buttonPress(child)
        
        
                

    def getBoardState(self):
        return self.boardState
    def setBoardState(self, newBoardState):
        self.boardState = newBoardState
