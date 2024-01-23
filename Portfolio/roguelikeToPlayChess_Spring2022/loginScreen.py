from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
import tkinter.font as font
import sqlalchemy as db
import bcrypt

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
        self.columnconfigure(1, weight=1)
        
        def getFilePath(filename):
            return os.path.realpath(__file__)+f'\\..\\{filename}'

        self.titleBanner = PhotoImage(file= getFilePath('img\\titleBanner.png'))
        titleLabel = tk.Label(self, image = self.titleBanner, borderwidth=0, highlightthickness=0).grid(column=0, row=0, columnspan=3)

#=====================
#   FRAME CONTENT
#=====================
        textBoxFont = font.Font(family='Roboto', size=40)
        labelFont = font.Font(family='Roboto',size=24)

        usernameLabel = Label(self, text='Username',font=labelFont, bg='#00868B', fg='white').grid(column=1,row=1)
        self.usernameEntry = Entry(self,
            font = textBoxFont,
            width = 20)
        self.usernameEntry.grid(column=1,row=2)

        emailLabel = Label(self, text='Email',font=labelFont, bg='#00868B', fg='white').grid(column=1,row=3)
        self.emailEntry = Entry(self,
            font = textBoxFont,
            width = 20)
        self.emailEntry.grid(column=1,row=4)  
        

        style.configure('Buttons.TFrame', background = '#00868B') 
        self.buttonFrame = ttk.Frame(self, style='Buttons.TFrame', width=500, height=100)
        self.buttonFrame.grid(column=1,row=7)
        self.buttonFrame.columnconfigure(0, weight=1)

        def setStyle(element):
            style.configure(element + '.TButton', font=('Helvetica',24),background='#00868B', padding=15)
            return element + '.TButton'

        self.loginButton = ttk.Button(
            self.buttonFrame, 
            text="Login",
            style=setStyle('loginButton'), 
            command=lambda: self.login(controller))
        self.loginButton.grid(row=0, column=0, sticky=(N,S,E,W), padx=25, pady=10)

        self.signupButton = ttk.Button(
            self.buttonFrame, 
            text="Create Account",
            style=setStyle('loginButton'), 
            command=lambda: self.createAccount(controller))
        self.signupButton.grid(column=1,row=0, sticky=(N,S,E,W), padx=25, pady=10)

        errorFont = font.Font(family='Roboto',size=18) 
        self.errorLabel = Label(self.buttonFrame, text='',font=errorFont, bg='#00868B', fg='#e03a53')
        self.errorLabel.grid(column=0,row=1,columnspan=2)

        


        for child in self.winfo_children(): 
            child.grid_configure(padx=10, pady=5)
        
    

    def getUsername(self):
        return self.username


    def validateInputs(self, username, email):
        allowedCharacters = 'abcdefghijklmnopqrstuvwxyz1234567890@.'

        for char in username:
            if char not in allowedCharacters:
                return False

        for char in email:
            if char not in allowedCharacters:
                return False
        
        return True
        
    
    def login(self, controller):
        self.username = self.usernameEntry.get()
        self.email = self.emailEntry.get()
        loginInput = [self.username,self.email]

        engine = db.create_engine('sqlite:///C:\\Users\\1magi\\Desktop\\roguelikeToPlayChess\\chessDatabase.db')
        connection = engine.connect()
        metadata = db.MetaData()
        users = db.Table('users',metadata,autoload=True,autoload_with=engine)

        query = db.select([users])
        results = connection.execute(query).fetchall()


        if self.username == "" or self.email == "":
            self.displayError("Missing Fields")
        elif self.validateInputs(self.username,self.email) == False:
            self.displayError("Invalid Characters")
        else:
            recordExists = False
            #CHECKING IF ACCOUNT EXISTS WITH ENTERED CREDENTIALS
            for record in results:
                recordList = list(record[1:])
                if loginInput == recordList:
                    recordExists = True
            
            if recordExists == False:
                self.displayError("No Account Exists With Those Credentials")
            else:
                controller.showFrame("Menu Screen")

        

    #https://compucademy.net/user-login-with-python-and-sqlite/
    def createAccount(self, controller):
        self.username = self.usernameEntry.get()
        self.email = self.emailEntry.get()


        engine = db.create_engine('sqlite:///C:\\Users\\1magi\\Desktop\\roguelikeToPlayChess\\chessDatabase.db')
        connection = engine.connect()
        metadata = db.MetaData()
        users = db.Table('users',metadata,autoload=True,autoload_with=engine)

        usernameQuery = db.select([users.c.username])
        emailQuery = db.select([users.c.email])
        

        usernameData = connection.execute(usernameQuery).fetchall()
        emailData = connection.execute(emailQuery).fetchall()
        usernameResults = []
        emailResults = []
        for usernameRecord, emailRecord in zip(usernameData, emailData):
            newUserRecord = str(usernameRecord).strip('()').replace(',', '')
            newUserRecord = newUserRecord.replace("\'","")

            newEmailRecord = str(emailRecord).strip('()').replace(',', '')
            newEmailRecord = newEmailRecord.replace("\'","")

            usernameResults.append(newUserRecord)
            emailResults.append(newEmailRecord)
        

      

        #============================
        #   CHECK ENTRY FOR ERRORS
        #============================
        if self.username == "" or self.email == "":
            self.displayError("Missing Fields")
        else:
            if self.username in usernameResults:
                self.displayError("Username Already Taken")
            else:
                if self.email in emailResults:
                    self.displayError("Email Already Taken")
                else:
                    query = db.insert(users).values(username=self.username,email=self.email)
                    resultProxy = connection.execute(query)
                
                    controller.showFrame("Menu Screen")

    def displayError(self, errorMsg):
        self.errorLabel.configure(text="[ERROR] - " + errorMsg)