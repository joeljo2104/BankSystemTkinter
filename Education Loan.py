from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class EducationLoanWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_EducationLoan()

    def Main_EducationLoan(self):
        self.master.title("Education Loan")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))
        self.ButtonMonthly = ImageTk.PhotoImage(Image.open("assets/Monthly.png"))
        self.ButtonQuarterly = ImageTk.PhotoImage(Image.open("assets/Quarterly.png"))    
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide23.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','16'))
        self.entry20.place(x = 815, y = 225, width = 250)

        self.entry21 = Entry(self, font=('Montserrat','16'))
        self.entry21.place(x = 815, y = 285, width = 250)

        self.entry22 = Entry(self, font=('Montserrat','16'))
        self.entry22.place(x = 815, y = 405, width = 250)

        self.entry23 = Entry(self, font=('Montserrat','16'))
        self.entry23.place(x = 815, y = 466, width = 250)

        ButtonMonthly = Button(self, bd = 0, height = 50, width = 174, command = self.MonthlyPayment)
        ButtonMonthly.config(image = self.ButtonMonthly)
        ButtonMonthly.place(x = 815, y = 518)

        ButtonQuarterly = Button(self, bd = 0, height = 50, width = 174, command = self.QuarterlyPayment)
        ButtonQuarterly.config(image = self.ButtonQuarterly)
        ButtonQuarterly.place(x = 1015, y = 518)

        self.Confirm = Button(self, bd = 0, state = DISABLED, height = 74, width = 330, command = self.End_EducationLoan)
        self.Confirm.config(image = self.ButtonConfirm)
        self.Confirm.place(x = 548, y = 595)

    def MonthlyPayment(self):
        self.EducationLoan_Payment = 'Monthly'
        self.Confirm.config(state="normal")

    def QuarterlyPayment(self):
        self.EducationLoan_Payment = 'Quarterly'
        self.Confirm.config(state="normal")

    def End_EducationLoan(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Education Loan Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = EducationLoanWin_End(root10)

class EducationLoanWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_EducationLoanWindow()

    def End_EducationLoanWindow(self):
        self.master.title("Education Loan Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGEducationLoanEnd = ImageTk.PhotoImage(Image.open("assets/Slide24.jpg"))
        tk.Label(self,image = self.BGEducationLoanEnd).pack()

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

app = EducationLoanWin(root)
root.mainloop()
