from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

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
            command=lambda: controller.showFrame("Login Screen"),
            image = self.continueButton,
            borderwidth= 0
        ).grid(row=0,column=0, sticky=S)