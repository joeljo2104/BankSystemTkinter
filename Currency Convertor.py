from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class CurrencyConvertorWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_CurrencyConvertor()

    def Main_CurrencyConvertor(self):
        self.master.title("Currency Convertor")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.ButtonUSD = ImageTk.PhotoImage(Image.open("assets/USD.png"))
        self.ButtonINR = ImageTk.PhotoImage(Image.open("assets/INR.png"))

        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide29.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','16'))
        self.entry20.place(x = 750, y = 282, width = 182)

        ButtonUSD1 = Button(self, bd = 0, height = 60, width = 182, command = self.InPut_USD)
        ButtonUSD1.config(image = self.ButtonUSD)
        ButtonUSD1.place(x = 855, y = 204)

        ButtonINR1 = Button(self, bd = 0, height = 60, width = 182, command = self.InPut_INR)
        ButtonINR1.config(image = self.ButtonINR)
        ButtonINR1.place(x = 1051, y = 204)

        ButtonUSD2 = Button(self, bd = 0, height = 60, width = 182, command = self.OutPut_USD)
        ButtonUSD2.config(image = self.ButtonUSD)
        ButtonUSD2.place(x = 885, y = 384)

        ButtonINR2 = Button(self, bd = 0, height = 60, width = 182, command = self.OutPut_INR)
        ButtonINR2.config(image = self.ButtonINR)
        ButtonINR2.place(x = 1081, y = 384)

        self.label1 = Label(self,text = "", font = ('Montserrat' , '24', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 693, y = 455)

        self.label2 = Label(self,text = "", font = ('Montserrat' , '24', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label2.place(x = 663, y = 275)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 548, y = 595)

    def InPut_USD(self):
        global Currency1
        Currency1 = 'USD'
        self.label2.config(text = "USD")

    def InPut_INR(self):
        global Currency1
        Currency1 = 'INR'
        self.label2.config(text = "INR")

    def OutPut_INR(self):
        if Currency1 == 'INR':
            Out = "INR",self.entry20.get(),"/-"
            self.label1.config(text = Out)
        elif Currency1 == 'USD':
            OutPut = float(self.entry20.get()) * 64.02
            Out = "INR",OutPut,"/-"
            self.label1.config(text = Out)

    def OutPut_USD(self):
        if Currency1 == 'USD':
            Out = "USD",self.entry20.get(),"/-"
            self.label1.config(text = Out)
        elif Currency1 == 'INR':
            OutPut = float(self.entry20.get()) * 0.016
            Out = "USD",OutPut,"/-"
            self.label1.config(text = Out)

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()

root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = CurrencyConvertorWin(root)
root.mainloop()
