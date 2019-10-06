from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image
import time

class AirTicketWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_AirTicket()

    def Main_AirTicket(self):
        self.master.title("Air Ticket")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonFirst = ImageTk.PhotoImage(Image.open("assets/First.png"))
        self.ButtonBusiness = ImageTk.PhotoImage(Image.open("assets/Business.png"))
        self.ButtonEconomy = ImageTk.PhotoImage(Image.open("assets/Economy.png"))
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))    
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide15.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','16'))
        self.entry20.place(x = 800, y = 470, width = 250)

        ButtonFirst = Button(self, bd = 0, height = 45, width = 203, command = self.AmountingFirst)
        ButtonFirst.config(image = self.ButtonFirst)
        ButtonFirst.place(x = 295, y = 525)

        ButtonBusiness = Button(self, bd = 0, height = 45, width = 203, command = self.AmountingBusiness)
        ButtonBusiness.config(image = self.ButtonBusiness)
        ButtonBusiness.place(x = 626, y = 525)

        ButtonEconomy = Button(self, bd = 0, height = 45, width = 203, command = self.AmountingEconomy)
        ButtonEconomy.config(image = self.ButtonEconomy)
        ButtonEconomy.place(x = 958, y = 525)

        self.label1 = Label(self,text = "", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 890, y = 265)

        self.Confirm = Button(self, bd = 0, state = DISABLED, height = 74, width = 330, command = self.Confirm)
        self.Confirm.config(image = self.ButtonConfirm)
        self.Confirm.place(x = 548, y = 595)

    def AmountingFirst(self):
        Price = 60000
        Amount = int(self.entry20.get())*Price
        DisplayAmount = "INR",Amount,"/-"
        self.label1.config(text = DisplayAmount)
        self.Confirm.config(state="normal")

    def AmountingBusiness(self):
        Price = 40000
        Amount = int(self.entry20.get())*Price
        DisplayAmount = "INR",Amount,"/-"
        self.label1.config(text = DisplayAmount)
        self.Confirm.config(state="normal")

    def AmountingEconomy(self):
        Price = 20000
        Amount = int(self.entry20.get())*Price
        DisplayAmount = "INR",Amount,"/-"
        self.label1.config(text = DisplayAmount)
        self.Confirm.config(state="normal")

    def Confirm(self):
        self.End_AirTicket()

    def End_AirTicket(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Air Ticket Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = AirTicketWin_End(root10)

class AirTicketWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_AirTicketWindow()

    def End_AirTicketWindow(self):
        self.master.title("Air Ticket Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGAirTicketEnd = ImageTk.PhotoImage(Image.open("assets/Slide16.jpg"))
        tk.Label(self,image = self.BGAirTicketEnd).pack()

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

app = AirTicketWin(root)
root.mainloop()
