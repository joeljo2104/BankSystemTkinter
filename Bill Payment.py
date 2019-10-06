from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class BillPaymentWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_BillPayment()

    def Main_BillPayment(self):
        self.master.title("Bill Payment")
        self.pack( fill = BOTH, expand = 1)
         
        self.ButtonMobileBill = ImageTk.PhotoImage(Image.open("assets/MobileBill.png"))   
        self.ButtonUtilityBill = ImageTk.PhotoImage(Image.open("assets/UtilityBill.png")) 
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide31.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        ButtonMobileBill = Button(self, bd = 0, height = 78, width = 561, command = self.MobileBill)
        ButtonMobileBill.config(image = self.ButtonMobileBill)
        ButtonMobileBill.place(x = 451, y = 294)

        ButtonUtilityBill = Button(self, bd = 0, height = 78, width = 561, command = self.UtilityBill)
        ButtonUtilityBill.config(image = self.ButtonUtilityBill)
        ButtonUtilityBill.place(x = 451, y = 505)

    def MobileBill(self):
    	os.startfile("Mobile Bill.py")
    	self.quit()

    def UtilityBill(self):
    	os.startfile("Utility Bill.py")
    	self.quit()
    	   	
root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = BillPaymentWin(root)
root.mainloop()
