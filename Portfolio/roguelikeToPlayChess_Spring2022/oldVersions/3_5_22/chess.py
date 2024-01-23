from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

from chessSquareTest import ChessSquare


###########################################
#             RESOURCES USED
###########################################
#https://www.journaldev.com/48165/tkinter-working-with-classes
#https://stackoverflow.com/questions/31360480/tkinter-label-image-without-border/49857791 

#tk vs ttk
# highlightthickness is only tk
# styles are only ttk
class windows(tk.Tk):

###########################################
#             PROGRAM WINDOW
###########################################
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Would You Roguelike To Play Chess?")
 
        self.attributes("-fullscreen", 1)
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        # creating a frame and assigning it to container
        window = ttk.Frame(self)
        # specifying the region where the frame is packed in root
        window.grid(column=0, row=0, sticky=(N, W, E, S))
 
        # configuring the location of the container using grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        def close_win(e):
            self.destroy()

        self.bind('<Escape>', lambda e: close_win(e))
 
        # Dictionary of Frames
        self.frames = {}

        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (TitleScreen, LoginScreen, MenuScreen, ShopScreen, ChessGame):
            frame = F(window, self)
 
            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(column=0, row=0, sticky=(N, W, E, S))
 
        # Using a method to switch frames
        self.showFrame(TitleScreen)

    def showFrame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    


###########################################
#              TITLE SCREEN
###########################################
class TitleScreen(ttk.Frame):
    def __init__(self, parent, controller):

#=====================
# FRAME CONFIGURATION
#=====================
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="Menu.TFrame")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

#=====================
#   FRAME CONTENT
#=====================
        titleCanvas = Canvas(self, background="red")
        titleCanvas.grid(column=0, row=0, sticky=(N, W, E, S))
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.titleScreenImg = ImageTk.PhotoImage(Image.open(getFilePath('img\\titleScreen2.png')).resize((width, height), Image.ANTIALIAS))
        titleBackground = titleCanvas.create_image(0, 0, anchor=NW, image=self.titleScreenImg)

        self.continueButton = ImageTk.PhotoImage(Image.open(getFilePath('img\\clickToContinue.png')).resize((400, 50), Image.ANTIALIAS))
        
        continueBtn = tk.Button(
            self, 
            command=lambda: controller.showFrame(LoginScreen),
            image = self.continueButton,
            borderwidth= 0
        ).grid(row=0,column=0, sticky=S)
 


###########################################
#              LOGIN SCREEN
###########################################
class LoginScreen(ttk.Frame):
    def __init__(self, parent, controller):

#=====================
# FRAME CONFIGURATION
#=====================
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="Menu.TFrame")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

#=====================
#   FRAME CONTENT
#=====================
        titleCanvas = Canvas(self, background="red")
        titleCanvas.grid(column=0, row=0, sticky=(N, W, E, S))
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.titleScreenImg = ImageTk.PhotoImage(Image.open(getFilePath('img\\loginScreen.png')).resize((width, height), Image.ANTIALIAS))
        titleBackground = titleCanvas.create_image(0, 0, anchor=NW, image=self.titleScreenImg)

        self.continueButton = ImageTk.PhotoImage(Image.open(getFilePath('img\\clickToContinue.png')).resize((400, 50), Image.ANTIALIAS))
        
        continueBtn = tk.Button(
            self, 
            command=lambda: controller.showFrame(MenuScreen),
            image = self.continueButton,
            borderwidth= 0
        ).grid(row=0,column=0, sticky=S)



###########################################
#               MAIN MENU
###########################################
class MenuScreen(tk.Frame):
    def __init__(self, parent, controller):

#=====================
# FRAME CONFIGURATION
#=====================
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="Menu.TFrame")
        self.columnconfigure(1, weight=1)
        
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

        def setStyle(element):
            style.configure(element + '.TButton', font=('Helvetica',24),background='#00868B', padding=15)
            return element + '.TButton'

        def changeStyle(element):
            style.configure(element + '.TButton', background='red')

        self.titleBanner = PhotoImage(file= getFilePath('img\\titleBanner.png'))
        titleLabel = tk.Label(self, image = self.titleBanner, borderwidth=0, highlightthickness=0).grid(column=0, row=0, columnspan=3)

#=====================
#   FRAME CONTENT
#=====================
        newGameButton = ttk.Button(
            self, 
            text="New Game",
            style=setStyle('newGameButton'), 
            command=lambda: controller.showFrame(ShopScreen))
        newGameButton.grid(column=1,row=1)

        loadGameButton = ttk.Button(
            self, 
            text="Load Game", 
            style=setStyle('loadGameButton'), 
            command= lambda: changeStyle('loadGameButton'))
        loadGameButton.grid(column=1,row=2)

        howToPlayButton = ttk.Button(
            self, 
            text="How To Play",
            style=setStyle('howToPlayButton'), 
            command= lambda: changeStyle('howToPlayButton'))
        howToPlayButton.grid(column=1,row=3)

        settingsButton = ttk.Button(
            self, 
            text="Settings", 
            style=setStyle('settingsButton'), 
            command= lambda: changeStyle('settingsButton'))
        settingsButton.grid(column=1,row=4)

        quitButton = ttk.Button(
            self, 
            text="Quit",
            style=setStyle('quitButton'), 
            command= 'exit')
        quitButton.grid(column=1,row=5)

        for child in self.winfo_children(): 
            child.grid_configure(padx=10, pady=10)
 


###########################################
#              SHOP SCREEN
###########################################
class ShopScreen(ttk.Frame):
    def __init__(self, parent, controller):

#=====================
# FRAME CONFIGURATION
#=====================
        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="Menu.TFrame")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

#=====================
#   FRAME CONTENT
#=====================
        titleCanvas = Canvas(self, background="red")
        titleCanvas.grid(column=0, row=0, sticky=(N, W, E, S))
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.titleScreenImg = ImageTk.PhotoImage(Image.open(getFilePath('img\\shopScreen.png')).resize((width, height), Image.ANTIALIAS))
        titleBackground = titleCanvas.create_image(0, 0, anchor=NW, image=self.titleScreenImg)

        self.continueButton = ImageTk.PhotoImage(Image.open(getFilePath('img\\clickToContinue.png')).resize((400, 50), Image.ANTIALIAS))
        
        continueBtn = tk.Button(
            self, 
            command=lambda: controller.showFrame(ChessGame),
            image = self.continueButton,
            borderwidth= 0
        ).grid(row=0,column=0, sticky=S)


###########################################
#               CHESS BOARD
###########################################

class ChessGame(tk.Frame):
    def __init__(self, parent, controller):

        #=====================
        # FRAME CONFIGURATION
        #=====================
        width = parent.winfo_screenwidth()
        height = parent.winfo_screenheight()

        style = ttk.Style()
        style.configure('ChessFrame.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="ChessFrame.TFrame")
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=2)


        #=====================
        #   FRAME CONTENT
        #=====================


        #-------------------
        #  PIECE GRAVEYARD
        #-------------------
        style.configure('Graveyard.TFrame', background ="#44BEB7")
        graveyard = ttk.Frame(self, style='Graveyard.TFrame', width=width*0.15, height=height*0.95)
        graveyard.grid(column=0, row=0, padx = 20, pady = 20, rowspan=2)

        #graveyard.grid_rowconfigure(0, weight=1)
        #graveyard.grid_columnconfigure(0, weight=1)
        #my_button = ChessSquare(graveyard, text='test button').grid(column=0, row = 0)

        #FFCB67
        #-------------------
        #    CHESS BOARD
        #-------------------
        boardWidth = width*0.4
        boardHeight = height*0.46
        style.configure('ChessBoard.TFrame', background ="brown")
        board = ttk.Frame(self, style='ChessBoard.TFrame', width = boardWidth, height = boardHeight) #height = 1026, width = 960
        board.grid(column=1, row=0, padx = 20, pady = 20, rowspan=2)

        
        

        #def squareCommand():
            #print(ChessSquare.getCoordinates())

        
        chessSquares = []
        for row in range(8):
            for col in range(8):
                #numSquares = len(chessSquares)
                chessSquares.append(ChessSquare(board, 
                    row, 
                    col,
                    boardWidth,
                    boardHeight,
                    ))
                #numSquares += 1


        for square in chessSquares:
            square['command'] = lambda square=square: buttonPress(square)
            if square.getCoordinates() == 'E1':
                square['command'] = lambda square=square: controller.showFrame(ShopScreen) 
            if square.getCoordinates() == 'E8':
                square.placePiece('blackPawn')

        #Start == the square the piece is starting on
        #End == the square the piece is being moved to
        def movePiece(start, end):
            end.placePiece('blackPawn')
            #end.placePiece(start.getCurrentPieceType())
            start.removePiece() 
            

        #This resets all the squares to their original color before highlighting squares again.
        def resetSquares():
            for square in chessSquares:
                square['bg'] = square.setBackground()

        def highlightSquares(selection):
            for square in chessSquares:
                #Highlights all the squares that the selected pawn can move to
                if selection.getCurrentPieceType() == 'pawn':
                    if selection.getCoordinates()[-1] != 1:
                        if square.getCoordinates()[0] == selection.getCoordinates()[0] and square.getRow() == selection.getRow()-1:
                            #print(square.getCoordinates())
                            square.highlightSquare(selection)
                #if square.getCoordinates() == selection.getCoordinates():
                    #pass
                #elif (square.getCoordinates()[1] == selection.getCoordinates()[1]) or square.getCoordinates()[0] == selection.getCoordinates()[0]:
                    #square.highlightSquare() 


        def buttonPress(event):
            pieceMoved = False
            resetSquares() 
            if event.isSelected() == True:
                event.deselectSquare()
            else:
                #Marks whatever the previously clicked square is as deslected
                for square in chessSquares:
                    if square.isSelected():
                        print(square.getCoordinates())
                        if event.isHighlighted() == True and event.getHighlightedBy() == square.getCoordinates():
                            movePiece(square, event)
                            pieceMoved = True
                        square.setSelected(False)
                        event.setHighlighted(False)

                if pieceMoved == False:
                    event.selectSquare() #changes the color of the selected square 
                    highlightSquares(event) #highlights all the squares that can be moved to from the selected Square
            return
            #print(' the pressed button is: ' + str(event))
        

                

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

###########################################
#               RUNNER
###########################################
if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()