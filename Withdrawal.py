from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class WithdrawalWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_Withdrawal()

    def Main_Withdrawal(self):
        self.master.title("Withdrawal")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))    
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide27.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','22') )
        self.entry20.place(x = 548, y = 285, width = 250)

        self.label1 = Label(self,text = "BALANCE", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 900, y = 385)

        ButtonConfirm = Button(self, bd = 0, height = 74, width = 330, command = self.End_Withdrawal)
        ButtonConfirm.config(image = self.ButtonConfirm)
        ButtonConfirm.place(x = 548, y = 595)

    def End_Withdrawal(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Withdrawal Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = WithdrawalWin_End(root10)

class WithdrawalWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_WithdrawalWindow()

    def End_WithdrawalWindow(self):
        self.master.title("Withdrawal Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGWithdrawalEnd = ImageTk.PhotoImage(Image.open("assets/Slide28.jpg"))
        tk.Label(self,image = self.BGWithdrawalEnd).pack()

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

app = WithdrawalWin(root)
root.mainloop()
