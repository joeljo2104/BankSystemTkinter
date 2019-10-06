from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image
import time

class MovieTicketWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_MovieTicket()

    def Main_MovieTicket(self):
        self.master.title("Movie Ticket")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonStandard = ImageTk.PhotoImage(Image.open("assets/Standard.png"))
        self.ButtonVIP = ImageTk.PhotoImage(Image.open("assets/VIP.png"))
        self.ButtonEconomy = ImageTk.PhotoImage(Image.open("assets/Economy.png"))
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))    
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide13.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','16'))
        self.entry20.place(x = 800, y = 470, width = 250)

        ButtonStandard = Button(self, bd = 0, height = 45, width = 203, command = self.AmountingStandard)
        ButtonStandard.config(image = self.ButtonStandard)
        ButtonStandard.place(x = 437, y = 523)

        ButtonVIP = Button(self, bd = 0, height = 45, width = 203, command = self.AmountingVIP)
        ButtonVIP.config(image = self.ButtonVIP)
        ButtonVIP.place(x = 788, y = 523)

        self.label1 = Label(self,text = "", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 890, y = 265)

        self.Confirm = Button(self, bd = 0, state = DISABLED, height = 74, width = 330, command = self.Confirm)
        self.Confirm.config(image = self.ButtonConfirm)
        self.Confirm.place(x = 548, y = 595)

    def AmountingStandard(self):
        Price = 120
        Amount = (float(self.entry20.get()))*Price
        DisplayAmount = "INR",Amount,"/-"
        self.label1.config(text = DisplayAmount)
        self.Confirm.config(state="normal")

    def AmountingVIP(self):
        Price = 150
        Amount = (float(self.entry20.get()))*Price
        DisplayAmount = "INR",Amount,"/-"
        self.label1.config(text = DisplayAmount)
        self.Confirm.config(state="normal")

    def Confirm(self):
        self.End_MovieTicket()

    def End_MovieTicket(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Movie Ticket Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = MovieTicketWin_End(root10)

class MovieTicketWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_MovieTicketWindow()

    def End_MovieTicketWindow(self):
        self.master.title("Movie Ticket Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGMovieTicketEnd = ImageTk.PhotoImage(Image.open("assets/Slide14.jpg"))
        tk.Label(self,image = self.BGMovieTicketEnd).pack()

        self.label1 = Label(self,text = random.randint(1000,9000), font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 618, y = 275)

        self.label2 = Label(self,text = "Reward Points", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label2.place(x = 645, y = 480)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 548, y = 595)

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()

root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = MovieTicketWin(root)
root.mainloop()
