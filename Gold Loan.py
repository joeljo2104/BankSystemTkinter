from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class GoldLoanWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_GoldLoan()

    def Main_GoldLoan(self):
        self.master.title("Gold Loan")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))
        self.ButtonMonthly = ImageTk.PhotoImage(Image.open("assets/Monthly.png"))
        self.ButtonQuarterly = ImageTk.PhotoImage(Image.open("assets/Quarterly.png"))
        self.Button22 = ImageTk.PhotoImage(Image.open("assets/22 Carat.png"))
        self.Button24 = ImageTk.PhotoImage(Image.open("assets/24 Carat.png"))       
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide19.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','16'))
        self.entry20.place(x = 815, y = 225, width = 250)

        self.entry21 = Entry(self, font=('Montserrat','16'))
        self.entry21.place(x = 815, y = 285, width = 250)

        self.entry22 = Entry(self, font=('Montserrat','16'))
        self.entry22.place(x = 815, y = 405, width = 250)

        self.entry23 = Entry(self, font=('Montserrat','16'))
        self.entry23.place(x = 815, y = 466, width = 250)

        Button22 = Button(self, bd = 0, height = 50, width = 174, command = self.Carat22)
        Button22.config(image = self.Button22)
        Button22.place(x = 815, y = 140)

        Button24 = Button(self, bd = 0, height = 50, width = 174, command = self.Carat24)
        Button24.config(image = self.Button24)
        Button24.place(x = 1015, y = 140)

        self.Monthly = Button(self, bd = 0, state = DISABLED, height = 50, width = 174, command = self.MonthlyPayment)
        self.Monthly.config(image = self.ButtonMonthly)
        self.Monthly.place(x = 815, y = 518)

        self.Quarterly = Button(self, bd = 0, state = DISABLED, height = 50, width = 174, command = self.QuarterlyPayment)
        self.Quarterly.config(image = self.ButtonQuarterly)
        self.Quarterly.place(x = 1015, y = 518)

        self.Confirm = Button(self, bd = 0, state = DISABLED, height = 74, width = 330, command = self.End_GoldLoan)
        self.Confirm.config(image = self.ButtonConfirm)
        self.Confirm.place(x = 548, y = 595)

    def Carat22(self):
        self.GoldLoan_GoldType = '22 Carat'
        self.Quarterly.config(state="normal")
        self.Monthly.config(state="normal")

    def Carat24(self):
        self.GoldLoan_GoldType = '24 Carat'
        self.Quarterly.config(state="normal")
        self.Monthly.config(state="normal")

    def MonthlyPayment(self):
        self.GoldLoan_Payment = 'Monthly'
        self.Confirm.config(state="normal")

    def QuarterlyPayment(self):
        self.GoldLoan_Payment = 'Quarterly'
        self.Confirm.config(state="normal")

    def End_GoldLoan(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Gold Loan Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = GoldLoanWin_End(root10)

class GoldLoanWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_GoldLoanWindow()

    def End_GoldLoanWindow(self):
        self.master.title("Gold Loan Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGGoldLoanEnd = ImageTk.PhotoImage(Image.open("assets/Slide20.jpg"))
        tk.Label(self,image = self.BGGoldLoanEnd).pack()

        self.label1 = Label(self,text = random.randint(1000,9000), font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 775, y = 390)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 548, y = 595)

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()

root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = GoldLoanWin(root)
root.mainloop()
