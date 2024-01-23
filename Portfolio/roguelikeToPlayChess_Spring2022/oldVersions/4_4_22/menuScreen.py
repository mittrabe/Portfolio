from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np


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
        boardState = []
        newGameButton = ttk.Button(
            self, 
            text="New Game",
            style=setStyle('newGameButton'), 
            command=lambda: controller.showFrame("Shop Screen", boardState))
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