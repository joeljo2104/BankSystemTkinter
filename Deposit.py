from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class DepositWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_Deposit()

    def Main_Deposit(self):
        self.master.title("Deposit")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))    
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide25.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','22') )
        self.entry20.place(x = 548, y = 285, width = 250)

        self.label1 = Label(self,text = "BALANCE", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 900, y = 385)

        ButtonConfirm = Button(self, bd = 0, height = 74, width = 330, command = self.End_Deposit)
        ButtonConfirm.config(image = self.ButtonConfirm)
        ButtonConfirm.place(x = 548, y = 595)

    def End_Deposit(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Deposit Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = DepositWin_End(root10)

class DepositWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_DepositWindow()

    def End_DepositWindow(self):
        self.master.title("Deposit Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGDepositEnd = ImageTk.PhotoImage(Image.open("assets/Slide26.jpg"))
        tk.Label(self,image = self.BGDepositEnd).pack()

        self.label1 = Label(self,text = "Balance", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 900, y = 325)

        self.label2 = Label(self,text = random.randint(1000,9000), font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label2.place(x = 630, y = 445)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 548, y = 595)

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()
        
root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = DepositWin(root)
root.mainloop()
