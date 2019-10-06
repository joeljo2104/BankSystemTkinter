from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class FundsTransferWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_FundsTransfer()

    def Main_FundsTransfer(self):
        self.master.title("Funds Transfer")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))    
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide11.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','16'), show = '*')
        self.entry20.place(x = 845, y = 285, width = 250)

        self.entry21 = Entry(self, font=('Montserrat','16'), show = '*')
        self.entry21.place(x = 1050, y = 405, width = 250)

        self.entry22 = Entry(self, font=('Montserrat','16'), show = '*')
        self.entry22.place(x = 700, y = 525, width = 150)

        ButtonConfirm = Button(self, bd = 0, height = 74, width = 330, command = self.End_FundsTransfer)
        ButtonConfirm.config(image = self.ButtonConfirm)
        ButtonConfirm.place(x = 548, y = 595)

    def End_FundsTransfer(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Funds Transfer Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = FundsTransferWin_End(root10)

class FundsTransferWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_FundsTransferWindow()

    def End_FundsTransferWindow(self):
        self.master.title("Funds Transfer Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGFundsTransferEnd = ImageTk.PhotoImage(Image.open("assets/Slide12.jpg"))
        tk.Label(self,image = self.BGFundsTransferEnd).pack()

        self.label1 = Label(self,text = random.randint(1000,9000), font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 625, y = 340)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 548, y = 595)

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()

root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = FundsTransferWin(root)
root.mainloop()
