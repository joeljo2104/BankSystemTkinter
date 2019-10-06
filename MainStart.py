from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class StartWindow(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_Window()

    def Main_Window(self):
        self.master.title("AJD BANK")
        self.pack( fill = BOTH, expand = 1)
        
        self.ButtonNewCustomer = ImageTk.PhotoImage(Image.open("assets/NewCustomer.png"))
        self.ButtonExistingCustomer = ImageTk.PhotoImage(Image.open("assets/ExistingCustomer.png"))
        self.ButtonAdmin = ImageTk.PhotoImage(Image.open("assets/Admin.png"))
        
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide1.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        NewAccountButton = Button(self, bd = 0, height = 80, width = 570, command = self.NewAccountWin)
        NewAccountButton.config(image = self.ButtonNewCustomer)
        NewAccountButton.place(x = 450, y = 335)

        ExAccountButton = Button(self, bd = 0, height = 80, width = 570, command = self.ExistingAccountWin)
        ExAccountButton.config(image = self.ButtonExistingCustomer)
        ExAccountButton.place(x = 450, y = 465)

        AdminButton = Button(self,text = "", bd = 0, height = 80, width = 570, command = self.AdminWin)
        AdminButton.config(image = self.ButtonAdmin)
        AdminButton.place(x = 450, y = 595)

    def NewAccountWin(self):
        global root1
        root1 = Toplevel(self.master)
        root1.title("New Account")
        root1.geometry("1366x768")
        root1.state('zoomed')
        a1 = NewAccountWindow(root1)

    def ExistingAccountWin(self):
        global root2
        root2 = Toplevel(self.master)
        root2.title("Existing Account")
        root2.geometry("1366x768")
        root2.state('zoomed')
        a2 = ExistingAccountWindow(root2)

    def AdminWin(self):
        global root3
        root3 = Toplevel(self.master)
        root3.title("Admin")
        root3.geometry("1366x768")
        root3.state('zoomed')
        a3 = AdminWindow(root3)

class NewAccountWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.Main_NewAccountWindow()

    def Main_NewAccountWindow(self):
        self.master.title("New Account")
        self.pack(fill = BOTH, expand = 1)

        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm.png"))
        self.ButtonUserPass = ImageTk.PhotoImage(Image.open("assets/User.png"))
        self.BGNewAccount = ImageTk.PhotoImage(Image.open("assets/Slide2.jpg"))
        tk.Label(self,image = self.BGNewAccount).pack()
                    
        self.entry1 = Entry(self, font=('Montserrat','16'))
        self.entry1.place(x = 600,y = 225, width = 250)

        self.entry2 = Entry(self, font=('Montserrat','16'))
        self.entry2.place(x = 600,y = 285, width = 250)

        self.entry3 = Entry(self, font=('Montserrat','16'))
        self.entry3.place(x = 600,y = 345, width = 250)

        self.entry4 = Entry(self, font=('Montserrat','16'))
        self.entry4.place(x = 600,y = 410, width = 250)

        self.entry5 = Entry(self, font=('Montserrat','16'))
        self.entry5.place(x = 600,y = 470, width = 250)

        self.entry6 = Entry(self, font=('Montserrat','16'))
        self.entry6.place(x = 600,y = 530, width = 250)

        self.entry7 = Entry(self, font=('Montserrat','16'))
        self.entry7.place(x = 600,y = 590, width = 250)

        self.entry8 = Entry(self, font=('Montserrat','16'))
        self.entry8.place(x = 600,y = 650, width = 250)

        self.Confirm1 = Button(self, bd = 0, height = 72, width = 330, command = self.GetData1)
        self.Confirm1.config(image = self.ButtonConfirm)
        self.Confirm1.place(x = 963, y = 257)

        self.UserPass = Button(self, bd = 0, state = DISABLED, height = 80, width = 331, command = self.UserName_PasswordWin)
        self.UserPass.config(image = self.ButtonUserPass)
        self.UserPass.place(x = 963, y = 375)

    def GetData1(self):

        c=Customer()
        c.__init__()
        self.Customer_Name=self.entry1.get()
        self.Customer_Gender=self.entry2.get()
        self.Customer_EmailID=self.entry3.get()
        self.Customer_DateOfBirth=self.entry4.get()
        self.Customer_PhoneNumber=self.entry5.get()
        self.Customer_PhoneNumber2=self.entry6.get()
        self.Customer_POBox=self.entry7.get()
        self.Customer_Address=self.entry8.get()
        Bank=open("Account1.dat","ab")
        pickle.dump(c,Bank)
        Bank.close()
        self.UserPass.config(state="normal")
        
    def Exception1(self):
    	EmptyCheckList = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get(), self.entry7.get(), self.entry8.get()]


    def Empty_Field(list):

        self.message = "<{0}> field cannot be empty.".format(field_name)
        if EmptyCheckList[value] == '':
            tkinter.messagebox.showinfo("Empty Field", message = self.message)

        if len(EmptyCheckList[0]) == 0:
            Empty_Field(0,'Customer Name')
                
        elif len(EmptyCheckList[1]) == 0:
            Empty_Field(1,'Gender')

        elif len(EmptyCheckList[3]) == 0:
            Empty_Field(3,'Date of Birth')

        elif len(EmptyCheckList[4]) == 0:
            Empty_Field(4,'Phone Number')

        elif len(EmptyCheckList[5]) == 0:
            Empty_Field(5,"Alt Phone Number")

        elif len(EmptyCheckList[6]) == 0:
            Empty_Field(6,"PO Box")

        elif len(EmptyCheckList[7]) == 0:
            Empty_Field(7,'Address')

        else:
            self.GetData1()
            self.UserPass.config(state="normal")
            
    def UserName_PasswordWin(self):
        root4 = Toplevel(self.master)
        root4.title("UserName & Password Creation")
        root4.geometry("1366x768")
        root4.state('zoomed')
        a4 = UserName_PasswordWindow(root4)

class UserName_PasswordWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.Main_UserName_PasswordWindow()

    def Main_UserName_PasswordWindow(self):

        self.master.title("UserName & Password Creation")
        self.pack( fill = BOTH, expand = 1)

        self.ButtonConfirm = ImageTk.PhotoImage(Image.open("assets/Confirm.png"))
        self.ButtonProceed = ImageTk.PhotoImage(Image.open("assets/Proceed.png"))
        self.BGUserPass = ImageTk.PhotoImage(Image.open("assets/Slide3.jpg"))
        tk.Label(self,image = self.BGUserPass).pack()

        self.Customer_AccountNumber=random.randint(1001,9998)
        self.label1 = Label(self,text = self.Customer_AccountNumber, font = ('Montserrat' , '24', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 600, y = 210)

        self.entry10 = Entry(self, font=('Montserrat','16'))
        self.entry10.place(x = 600, y = 305, width = 250)

        self.entry11 = Entry(self, font=('Montserrat','16'), show = '*')
        self.entry11.place(x = 755, y = 425, width = 250)

        self.entry12 = Entry(self, font=('Montserrat','16'), show = '*')
        self.entry12.place(x = 755, y = 485, width = 250)

        self.Confirm2 = Button(self, bd = 0, height = 72, width = 330, command = self.Exception2)
        self.Confirm2.config(image = self.ButtonConfirm)
        self.Confirm2.place(x = 356, y = 596)

        self.Proceed = Button(self, state = DISABLED, bd = 0, height = 72, width = 315, command = self.ExistingAccountWin)
        self.Proceed.config(image = self.ButtonProceed)
        self.Proceed.place(x = 796, y = 596)

    def GetData2(self):

        c=Customer()
        self.Customer_UserName = self.entry10.get()
        self.Customer_Password = self.entry11.get()
        Bank=open("Account1.dat","ab")
        pickle.dump(c,Bank)
        Bank.close()
        
    def Exception2(self):

        EmptyCheckList = [self.entry10.get(), self.entry11.get(), self.entry12.get()]

        def Empty_Field(value, field_name):

            self.message = "<{0}> field cannot be empty.".format(field_name)
            if EmptyCheck[value] == '':
                tkinter.messagebox.showinfo("Empty Field", message = self.message)

        if len(EmptyCheckList[0]) == 0:
            Empty_Field(0,'UserName')
            
        elif len(EmptyCheckList[1]) == 0:
            Empty_Field(1,'Password')
                        
        elif len(EmptyCheckList[2]) == 0:
            Empty_Field(2,'Reentered Password')

        elif EmptyCheckList[1]!=EmptyCheckList[2]:
            tkinter.messagebox.showerror('Input Error' , "Passwords do not match")

        else:
            self.GetData2()
            self.Proceed.config(state="normal")
            
    def ExistingAccountWin(self):
        root2 = Toplevel(self.master)
        root2.title("Existing Account")
        root2.geometry("1366x768")
        root2.state('zoomed')
        a2 = ExistingAccountWindow(root2)

class ExistingAccountWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.Main_ExistingAccountWindow()

    def Main_ExistingAccountWindow(self):

        self.master.title("Existing Customer")
        self.pack( fill = BOTH, expand = 1)

        self.ButtonLogin = ImageTk.PhotoImage(Image.open("assets/Login.png"))
        self.BGExistingAccount = ImageTk.PhotoImage(Image.open("assets/Slide4.jpg"))
        tk.Label(self,image = self.BGExistingAccount).pack()

        self.entry15 = Entry(self, font=('Montserrat','20'))
        self.entry15.place(x = 660, y = 262, width = 250)

        self.entry16 = Entry(self, font=('Montserrat','20'))
        self.entry16.place(x = 660, y = 388, width = 250)

        self.entry17 = Entry(self, font=('Montserrat','20'), show = '*')
        self.entry17.place(x = 660, y = 503, width = 250)

        self.Login = Button(self, bd = 0, height = 75, width = 330, command = self.Main_Menu)
        self.Login.config(image = self.ButtonLogin)
        self.Login.place(x = 548, y = 595)	

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()

class AdminWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.Main_Admin()

    def Main_Admin(self):

        self.master.title("Admin")
        self.pack( fill = BOTH, expand = 1)

        self.ButtonLogin = ImageTk.PhotoImage(Image.open("assets/Login.png"))
        self.BGAdmin = ImageTk.PhotoImage(Image.open("assets/Slide5.jpg"))
        tk.Label(self,image = self.BGAdmin).pack()

        self.entry19 = Entry(self, font=('Montserrat','20'), show = '*')
        self.entry19.place(x = 750, y = 365, width = 250)

        self.Login = Button(self, bd = 0, height = 75, width = 330, command = self.AdminLogged)
        self.Login.config(image = self.ButtonLogin)
        self.Login.place(x = 548, y = 595)

    def AdminLogged(self):
        if self.entry19.get()=='Admin@AJD':
            print('Hi')
        else:
        	tkinter.messagebox.showinfo("Incorrect Password", message = "Incorrect Password. Redirected to Main Menu!")
        	root3.destroy()

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



root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = StartWindow(root)
root.mainloop()
