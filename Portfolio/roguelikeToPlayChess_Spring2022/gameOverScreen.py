from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import numpy as np


###########################################
#               MAIN MENU
###########################################
class GameOverScreen(tk.Frame):
    def __init__(self, parent, controller, winner):

#=====================
# FRAME CONFIGURATION
#=====================

        style = ttk.Style()
        style.configure('Menu.TFrame', background="#00868B")
        ttk.Frame.__init__(self, parent, style="Menu.TFrame")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

        def setStyle(element):
            style.configure(element + '.TButton', font=('Helvetica',24),background='#00868B', padding=15)
            return element + '.TButton'



#=====================
#   FRAME CONTENT
#=====================
        winnerText = ""
        if winner == "Player":
            winnerText = "Victory!"
        elif winner == 'CPU':
            winnerText = "Defeat"
        else: 
            winnerText = ""
        winnerFont = font.Font(family='Roboto', size=80)
        winnerLabel = Label(self, text=winnerText, font=winnerFont, bg='#00868B', fg = 'white')
        winnerLabel.grid(column=1,row=0)

        menuButton = ttk.Button(
            self, 
            text="Return to Menu",
            style=setStyle('newGameButton'), 
            command=lambda: controller.showFrame("Menu Screen"))
        menuButton.grid(column=1,row=1)

        

        for child in self.winfo_children(): 
            child.grid_configure(padx=10, pady=10)