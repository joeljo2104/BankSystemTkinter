from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class Customer():
    def __init__(self):
        self.Customer_Name=""
        self.Customer_Gender=""
        self.Customer_EmailID=""
        self.Customer_DateOfBirth="00/00/0000"
        self.Customer_PhoneNumber=0
        self.Customer_PhoneNumber2=0
        self.Customer_POBox=0
        self.Customer_Address=""
        self.Customer_AccountNumber=0
        self.Customer_UserName=""
        self.Customer_Password=""
        self.Customer_Balance=0
        self.Customer_RewardPoints=0
        self.CarLoanApplication="Not Applied"
        self.GoldLoanApplication="Not Applied"
        self.HomeLoanApplication="Not Applied"
        self.EducationLoanApplication="Not Applied"
        self.TransactionMobileBill=[]
        self.TransactionUtilityBill=[]
        self.TransactionFundsTransfer=[]
        self.TransactionMovieTicket=[]
        self.TransactionAirTicket=[]
        self.TransactionDeposit=[]
        self.TransactionWithdraw=[]

class Account(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_Window()

    def Main_Window(self):
        self.master.title("Generate List")
        self.pack( fill = BOTH, expand = 1)
        
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide37.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()
        self.ButtonGenerate = ImageTk.PhotoImage(Image.open("assets/Generate.png"))

        self.entry19 = Entry(self, font=('Montserrat','20'))
        self.entry19.place(x = 750, y = 365, width = 250)


        
        GenerateButton = Button(self,text = "", bd = 0, height = 80, width = 354, command = self.TransactionList)
        GenerateButton.config(image = self.ButtonGenerate)
        GenerateButton.place(x = 550, y = 595)

    def TransactionList(self):
        global AccountNo
        AccountNo=int(self.entry19.get())
        global root3
        root3 = Toplevel(self.master)
        root3.title("Transaction List")
        root3.geometry("1366x768")
        root3.state('zoomed')
        a3 = TransactionListWindow(root3)

class TransactionListWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.Transactions()
        self.Main_TransactionListWindow(c)

    def Transactions(self):
        Bank=open("Account.dat","rb")
        global c
        c=Customer()
        

        try:
            while True:
                c=pickle.load(Bank)

                if AccountNo==c.Customer_AccountNumber:
                	break
                    
        except EOFError:
            pass

    def Main_TransactionListWindow(self,c):

        self.master.title("View Account Details")
        self.pack( fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BG = ImageTk.PhotoImage(Image.open("assets/Slide35.jpg"))
        tk.Label(self,image = self.BG).pack()

        self.Transaction = Label(self,text = 'Trans. Type', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.Transaction.place(x = 200, y = 180)

        self.TransNo = Label(self,text = 'Trans#', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.TransNo.place(x = 380, y = 180)

        self.TransTime = Label(self,text = '         Time of Transaction', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.TransTime.place(x = 480, y = 180)

        self.TransPayTo = Label(self,text = '     To', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.TransPayTo.place(x = 825, y = 180)

        self.TransAmount = Label(self,text = '  Amount', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.TransAmount.place(x = 980, y = 180)

        self.TransPoints = Label(self,text = 'Reward Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.TransPoints.place(x = 1130, y = 180)        

        self.MB = Label(self,text = 'Mobile Bill', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MB.place(x = 200, y = 252)

        self.MBNo = Label(self,text = c.TransactionMobileBill[0], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MBNo.place(x = 380, y = 252)

        self.MBTime = Label(self,text = c.TransactionMobileBill[1], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MBTime.place(x = 480, y = 252)

        self.MBPayTo = Label(self,text = c.TransactionMobileBill[2], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MBPayTo.place(x = 825, y = 252)

        self.MBAmount = Label(self,text = 'INR '+str(c.TransactionMobileBill[3]), font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MBAmount.place(x = 980, y = 252)

        self.MBPoints = Label(self,text = str(c.TransactionMobileBill[4])+' Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MBPoints.place(x = 1130, y = 252)

        self.UB = Label(self,text = 'Utility Bill', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.UB.place(x = 200, y = 315)

        self.UBNo = Label(self,text = c.TransactionUtilityBill[0], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.UBNo.place(x = 380, y = 315)

        self.UBTime = Label(self,text = c.TransactionUtilityBill[1], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.UBTime.place(x = 480, y = 315)

        self.UBPayTo = Label(self,text = c.TransactionUtilityBill[2], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.UBPayTo.place(x = 825, y = 315)

        self.UBAmount = Label(self,text = 'INR '+str(c.TransactionUtilityBill[3]), font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.UBAmount.place(x = 980, y = 315)

        self.UBPoints = Label(self,text = str(c.TransactionUtilityBill[4])+' Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.UBPoints.place(x = 1130, y = 315)

        self.FT = Label(self,text = 'Fund Transfer', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.FT.place(x = 200, y = 377)

        self.FTNo = Label(self,text = c.TransactionFundsTransfer[0], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.FTNo.place(x = 380, y = 377)

        self.FTTime = Label(self,text = c.TransactionFundsTransfer[1], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.FTTime.place(x = 480, y = 377)

        self.FTPayTo = Label(self,text = c.TransactionFundsTransfer[2], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.FTPayTo.place(x = 825, y = 377)

        self.FTAmount = Label(self,text = 'INR '+str(c.TransactionFundsTransfer[4]), font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.FTAmount.place(x = 980, y = 377)

        self.FTPoints = Label(self,text = '0 Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.FTPoints.place(x = 1130, y = 377)

        self.MT = Label(self,text = 'Movie Ticket', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MT.place(x = 200, y = 440)

        self.MTNo = Label(self,text = c.TransactionMovieTicket[0], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MTNo.place(x = 380, y = 440)

        self.MTTime = Label(self,text = c.TransactionMovieTicket[1], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MTTime.place(x = 480, y = 440)

        self.MTPayTo = Label(self,text = c.TransactionMovieTicket[2], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MTPayTo.place(x = 825, y = 440)

        self.MTAmount = Label(self,text = 'INR '+str(c.TransactionMovieTicket[3]), font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MTAmount.place(x = 980, y = 440)

        self.MTPoints = Label(self,text = str(c.TransactionMovieTicket[4])+' Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.MTPoints.place(x = 1130, y = 440)

        self.AT = Label(self,text = 'Air Ticket', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.AT.place(x = 200, y = 502)

        self.ATNo = Label(self,text = c.TransactionAirTicket[0], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.ATNo.place(x = 380, y = 502)

        self.ATTime = Label(self,text = c.TransactionAirTicket[1], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.ATTime.place(x = 480, y = 502)

        self.ATPayTo = Label(self,text = c.TransactionAirTicket[2], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.ATPayTo.place(x = 825, y = 502)

        self.ATAmount = Label(self,text = 'INR '+str(c.TransactionAirTicket[3]), font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.ATAmount.place(x = 980, y = 502)

        self.ATPoints = Label(self,text = str(c.TransactionAirTicket[4])+' Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.ATPoints.place(x = 1130, y = 502)

        self.WD = Label(self,text = 'Withdrawal', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.WD.place(x = 200, y = 565)

        self.WDNo = Label(self,text = c.TransactionWithdraw[0], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.WDNo.place(x = 380, y = 565)

        self.WDTime = Label(self,text = c.TransactionWithdraw[1], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.WDTime.place(x = 480, y = 565)

        self.WDPayTo = Label(self,text = c.TransactionWithdraw[2], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.WDPayTo.place(x = 825, y = 565)

        self.WDAmount = Label(self,text = 'INR '+str(c.TransactionWithdraw[3]), font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.WDAmount.place(x = 980, y = 565)

        self.WDPoints = Label(self,text = str(c.TransactionWithdraw[4])+' Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.WDPoints.place(x = 1130, y = 565)

        self.DP = Label(self,text = 'Deposit', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.DP.place(x = 200, y = 627)

        self.DPNo = Label(self,text = c.TransactionDeposit[0], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.DPNo.place(x = 380, y = 627)

        self.DPTime = Label(self,text = c.TransactionDeposit[1], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.DPTime.place(x = 480, y = 627)

        self.DPPayTo = Label(self,text = c.TransactionDeposit[2], font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.DPPayTo.place(x = 825, y = 627)

        self.DPAmount = Label(self,text = 'INR '+str(c.TransactionDeposit[3]), font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.DPAmount.place(x = 980, y = 627)

        self.DPPoints = Label(self,text = str(c.TransactionDeposit[4])+' Points', font = ('Montserrat' , '18', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.DPPoints.place(x = 1130, y = 627)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 750, y = 50)

    def Main_Menu(self):
        self.quit()


root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = Account(root)

root.mainloop()
