from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class Main_Menu(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_MainMenu()

    def Main_MainMenu(self):
        self.master.title("Main Menu")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonBankServices = ImageTk.PhotoImage(Image.open("assets/BankServices.png"))
        self.ButtonBillPayment = ImageTk.PhotoImage(Image.open("assets/BillPayment.png"))
        self.ButtonTickets = ImageTk.PhotoImage(Image.open("assets/Tickets.png"))
        self.ButtonLoans = ImageTk.PhotoImage(Image.open("assets/Loans.png"))
        self.ButtonFundsTransfer = ImageTk.PhotoImage(Image.open("assets/FundsTransfer.png"))
        self.ButtonCurrencyConvertor = ImageTk.PhotoImage(Image.open("assets/CurrencyConvertor.png"))
        self.ButtonQuit = ImageTk.PhotoImage(Image.open("assets/Quit.png"))
        
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide6.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        BankServicesButton = Button(self, bd = 0, height = 75, width = 450, command = self.Bank_Services)
        BankServicesButton.config(image = self.ButtonBankServices)
        BankServicesButton.place(x = 290, y = 202)

        BillPaymentButton = Button(self, bd = 0, height = 75, width = 450, command = self.Bill_Payment)
        BillPaymentButton.config(image = self.ButtonBillPayment)
        BillPaymentButton.place(x = 760, y = 202)

        TicketsButton = Button(self,text = "", bd = 0, height = 75, width = 450, command = self.Tickets)
        TicketsButton.config(image = self.ButtonTickets)
        TicketsButton.place(x = 289, y = 335)

        LoansButton = Button(self, bd = 0, height = 75, width = 450, command = self.Loans)
        LoansButton.config(image = self.ButtonLoans)
        LoansButton.place(x = 759, y = 335)

        FundsTransferButton = Button(self, bd = 0, height = 75, width = 450, command = self.Funds_Transfer)
        FundsTransferButton.config(image = self.ButtonFundsTransfer)
        FundsTransferButton.place(x = 290, y = 466)

        CurrencyConvertorButton = Button(self,text = "", bd = 0, height = 75, width = 450, command = self.Currency_Convertor)
        CurrencyConvertorButton.config(image = self.ButtonCurrencyConvertor)
        CurrencyConvertorButton.place(x = 761, y = 466)

        QuitButton = Button(self,text = "", bd = 0, height = 75, width = 514, command = self.quit)
        QuitButton.config(image = self.ButtonQuit)
        QuitButton.place(x = 484, y = 605)

    def Bank_Services(self):
    	os.startfile("Bank Services.py")
    	root.quit()

    def Bill_Payment(self):
    	os.startfile("Bill Payment.py")
    	root.quit()

    def Tickets(self):
    	os.startfile("Tickets.py")
    	root.quit()

    def Loans(self):
    	os.startfile("Loans.py")
    	root.quit()

    def Funds_Transfer(self):
    	os.startfile("Funds Transfer.py")
    	root.quit()

    def Currency_Convertor(self):
    	os.startfile("Currency Convertor.py")
    	root.quit()

    def quit(self):
    	root.quit()


root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = Main_Menu(root)
root.mainloop()
