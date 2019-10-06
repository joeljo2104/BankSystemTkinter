from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class LoansWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_Loans()

    def Main_Loans(self):
        self.master.title("Loans")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonCarLoan = ImageTk.PhotoImage(Image.open("assets/Car Loan.png"))   
        self.ButtonGoldLoan = ImageTk.PhotoImage(Image.open("assets/Gold Loan.png"))  
        self.ButtonHomeLoan = ImageTk.PhotoImage(Image.open("assets/Home Loan.png"))  
        self.ButtonEducationLoan = ImageTk.PhotoImage(Image.open("assets/Education Loan.png")) 
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide33.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        ButtonCarLoan = Button(self, bd = 0, height = 78, width = 561, command = self.CarLoan)
        ButtonCarLoan.config(image = self.ButtonCarLoan)
        ButtonCarLoan.place(x = 451, y = 188)

        ButtonGoldLoan = Button(self, bd = 0, height = 78, width = 561, command = self.GoldLoan)
        ButtonGoldLoan.config(image = self.ButtonGoldLoan)
        ButtonGoldLoan.place(x = 451, y = 294)

        ButtonHomeLoan = Button(self, bd = 0, height = 78, width = 561, command = self.HomeLoan)
        ButtonHomeLoan.config(image = self.ButtonHomeLoan)
        ButtonHomeLoan.place(x = 451, y = 400)

        ButtonEducationLoan = Button(self, bd = 0, height = 78, width = 561, command = self.EducationLoan)
        ButtonEducationLoan.config(image = self.ButtonEducationLoan)
        ButtonEducationLoan.place(x = 451, y = 505)

    def CarLoan(self):
    	os.startfile("Car Loan.py")
    	self.quit()

    def GoldLoan(self):
    	os.startfile("Gold Loan.py")
    	self.quit()

    def HomeLoan(self):
    	os.startfile("Home Loan.py")
    	self.quit()

    def EducationLoan(self):
    	os.startfile("Education Loan.py")
    	self.quit()
    	   	
    def View(self):
    	os.startfile("View.py")
    	self.quit()

root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = LoansWin(root)
root.mainloop()
