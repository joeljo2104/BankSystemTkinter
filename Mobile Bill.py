from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class MobileBillingWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_MobileBilling()

    def Main_MobileBilling(self):
        self.master.title("Mobile Bill")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm2.png"))    
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide7.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        self.entry20 = Entry(self, font=('Montserrat','16'))
        self.entry20.place(x = 950, y = 225, width = 250)

        self.entry21 = Entry(self, font=('Montserrat','16'))
        self.entry21.place(x = 845, y = 360, width = 250)

        self.entry22 = Entry(self, font=('Montserrat','16'))
        self.entry22.place(x = 1075, y = 500, width = 150)

        ButtonConfirm = Button(self, bd = 0, height = 74, width = 330, command = self.MobileBillingWin)
        ButtonConfirm.config(image = self.ButtonConfirm)
        ButtonConfirm.place(x = 548, y = 595)

    def MobileBillingWin(self):
        global root10
        root10 = Toplevel(self.master)
        root10.title("Mobile Billing Confirmation")
        root10.geometry("1366x768")
        root10.state('zoomed')
        a1 = MobileBillingWin_End(root10)

class MobileBillingWin_End(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.End_MobileBillingWindow()

    def End_MobileBillingWindow(self):
        self.master.title("Mobile Billing Confirmation")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BGMobileBillingEnd = ImageTk.PhotoImage(Image.open("assets/Slide8.jpg"))
        tk.Label(self,image = self.BGMobileBillingEnd).pack()

        self.label1 = Label(self,text = random.randint(1000,9000), font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 620, y = 340)

        self.label2 = Label(self,text = "Left", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label2.place(x = 832, y = 410)

        self.label3 = Label(self,text = "Reward Points", font = ('Montserrat' , '30', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label3.place(x = 647, y = 480)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 548, y = 595)

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()

root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = MobileBillingWin(root)
root.mainloop()
