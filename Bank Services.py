from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class BankServicesWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_BankServices()

    def Main_BankServices(self):
        self.master.title("Bank Services")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonDeposit = ImageTk.PhotoImage(Image.open("assets/Deposit.png"))   
        self.ButtonWithdraw = ImageTk.PhotoImage(Image.open("assets/Withdrawal.png"))  
        self.ButtonTransSummary = ImageTk.PhotoImage(Image.open("assets/TransSummary.png"))  
        self.ButtonUpdate = ImageTk.PhotoImage(Image.open("assets/Update.png")) 
        self.ButtonView = ImageTk.PhotoImage(Image.open("assets/View.png"))  
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide30.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        ButtonDeposit = Button(self, bd = 0, height = 78, width = 561, command = self.Deposit)
        ButtonDeposit.config(image = self.ButtonDeposit)
        ButtonDeposit.place(x = 451, y = 188)

        ButtonWithdraw = Button(self, bd = 0, height = 78, width = 561, command = self.Withdrawal)
        ButtonWithdraw.config(image = self.ButtonWithdraw)
        ButtonWithdraw.place(x = 451, y = 294)

        ButtonTransSummary = Button(self, bd = 0, height = 78, width = 561)#, command = self.NewAccountWin)
        ButtonTransSummary.config(image = self.ButtonTransSummary)
        ButtonTransSummary.place(x = 451, y = 400)

        ButtonUpdate = Button(self, bd = 0, height = 78, width = 561)#, command = self.NewAccountWin)
        ButtonUpdate.config(image = self.ButtonUpdate)
        ButtonUpdate.place(x = 451, y = 505)

        ButtonView = Button(self, bd = 0, height = 78, width = 561, command = self.View)
        ButtonView.config(image = self.ButtonView)
        ButtonView.place(x = 451, y = 611)

    def Deposit(self):
    	os.startfile("Deposit.py")
    	self.quit()

    def Withdrawal(self):
    	os.startfile("Withdrawal.py")
    	self.quit()

    def TransSummary(self):
    	os.startfile("TransSummary.py")
    	self.quit()

    def Update(self):
    	os.startfile("Update.py")
    	self.quit()
    	   	
    def View(self):
    	os.startfile("View Details.py")
    	self.quit()

root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = BankServicesWin(root)
root.mainloop()
