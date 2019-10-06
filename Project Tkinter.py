from tkinter import *
import tkinter as tk
import tkMessageBox
import pickle , os , string , random , ttk , tkFont
from PIL import ImageTk, Image

class StartWindow(Frame):

	def __init__(self,master = None):
		Frame.__init__(self,master)
		self.master = master
		self.main_window()

	def main_window(self):
		self.master.title("AJD BANK")
		self.pack( fill = BOTH, expand = 1)
		self.photo = ImageTk.PhotoImage(Image.open("assets/1.png"))
		self.Background = ImageTk.PhotoImage(Image.open("assets/Best.jpg"))
		tk.Label(self,image = self.Background).pack()

		NewAccountButton = Button(self,text = "", bd = 0, height = 100, width = 300, command = self.NewAccountWin)
		NewAccountButton.config(image = self.photo)
		NewAccountButton.place(x = 500, y = 250)

		ExAccountButton = Button(self,text = "", bd = 0, height = 100, width = 300, command = self.ExisitingAccountWin)
		ExAccountButton.config(image = self.photo)
		ExAccountButton.place(x = 500, y = 300)

		AdminButton = Button(self,text = "", bd = 0, height = 100, width = 300, command = self.AdminWin)
		AdminButton.config(image = self.photo)
		AdminButton.place(x = 500, y = 250)

	def NewAccountWin(self):
		root1 = Toplevel(self.master)
		root1.title("New Account")
		root1.geometry("1366x768")
		a1 = NewAccountWindow(root1)

	def ExisitingAccountWin(self):
		root2 = Toplevel(self.master)
		root2.title("Exisiting Account")
		root2.geometry("1366x768")
		a2 = ExisitingAccountWindow(root2)

	def AdminWin(self):
		root3 = Toplevel(self.master)
		root3.title("Admin")
		root3.geometry("1366x768")
		a3 = AdminWindow(root3)

class NewAccountWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.Main_NewAccountWindow()

    def Main_NewAccountWindow():
		self.master.title("New Account")
		self.pack(fill = BOTH, expand = 1)
		
		self.photo = ImageTk.PhotoImage(Image.open("assets/1.png"))
		self.Background = ImageTk.PhotoImage(Image.open("assets/Best.jpg"))
		tk.Label(self,image = self.Background).pack()

		self.entry1 = Entry(self, font=('Montserrat','12'))
		self.entry1.place(x = 500,y = 100, width = 160)

		self.entry2 = Entry(self, font=('Montserrat','12'))
		self.entry2.place(x = 500,y = 200, width = 160)

		self.entry3 = Entry(self, font=('Montserrat','12'))
		self.entry3.place(x = 500,y = 300, width = 160)

		self.entry4 = Entry(self, font=('Montserrat','12'))
		self.entry4.place(x = 500,y = 400, width = 160)

		self.entry5 = Entry(self, font=('Montserrat','12'))
		self.entry5.place(x = 500,y = 500, width = 160)

		self.entry6 = Entry(self, font=('Montserrat','12'))
		self.entry6.place(x = 500,y = 600, width = 160)

		self.entry7 = Entry(self, font=('Montserrat','12'))
		self.entry7.place(x = 500,y = 700, width = 160)

		self.entry8 = Entry(self, font=('Montserrat','12'))
		self.entry8.place(x = 500,y = 800, width = 160)

		self.Confirm1 = Button(self,text = "", bd = 0, height = 100, width = 300, command = self.Exception1)
		self.Confirm1.config(image = self.photo)
		self.Confirm1.place(x = 800, y = 800)

		self.UserPass = Button(self,text = "", state = DISABLED, bd = 0, height = 100, width = 300, command = self.UserName_Password)
		self.UserPass.config(image = self.photo)
		self.UserPass.place(x = 800, y = 900)

	def GetData1(self):
        self.Customer_Name=self.entry1.get()
		self.Customer_Gender=self.entry2.get()
		self.Customer_EmailID=self.entry3.get()
        self.Customer_DateOfBirth=self.entry4.get()
        self.Customer_PhoneNumber=self.entry5.get()
        self.Customer_PhoneNumber2=self.entry6.get()
        self.Customer_POBox=self.entry7.get()
        self.Customer_Address=self.entry8.get()

        EmptyCheck1 = [self.Customer_Name, self.Customer_Gender, self.Customer_EmailID, self.Customer_DateOfBirth, self.Customer_PhoneNumber, self.Customer_PhoneNumber2, self.Customer_POBox, self.Customer_Address]
        return EmptyCheck

	def Exception1(self):
		EmptyCheckList = self.GetData1()

    def Empty_Field(value, field_name):

    	self.message = "<{0}> field cannot be empty.".format(field_name)
    	if EmptyCheck[value] == '':
    		tkMessageBox.showinfo("Empty Field", message = self.message)

		if len(EmptyCheckList[0]) == 0:
			empty_field_checker(0,'Customer Name')
            
		elif not EmptyCheckList[0].isalpha():
			tkMessageBox.showerror('Invalid Input',"<First Name> field you've entered is not valid.")
                
		elif len(EmptyCheckList[1]) == 0:
			empty_field_checker(1,'Gender')
        
		elif "Male" not in EmptyCheckList[1] or "Female" not in EmptyCheckList[1] or "male" not in EmptyCheckList[1] or "female" not in EmptyCheckList[1]:
			tkMessageBox.showerror("Invalid Input ", "Enter only Male or Female")
                
		elif "@" not in EmptyCheckList[2] or ".com" not in EmptyCheckList[2]:
			tkMessageBox.showerror("Invalid Input ", "The Email ID you entered is not valid")

		elif len(EmptyCheckList[3]) == 0:
			empty_field_checker(3,'Date of Birth')

		elif len(EmptyCheckList[4]) == 0:
			empty_field_checker(4,'Phone Number')

		elif len(EmptyCheckList[5]) == 0:
			empty_field_checker(5,"Alt Phone Number")

		elif len(EmptyCheckList[6]) == 0:
			empty_field_checker(6,"PO Box")

		elif len(EmptyCheckList[7]) == 0:
			empty_field_checker(7,'Address')

		else:
			self.UserPass.config(state="normal")

	def UserName_PasswordWin(self):
		root4 = Toplevel(self.master)
		root4.title("Admin")
		root4.geometry("1366x768")
		a4 = UserName_PasswordWindow(root4)

class UserName_PasswordWindow(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.Main_UserName_PasswordWindow()

	def Main_UserName_PasswordWindow(self):

		self.Customer_AccountNumber=random.randint(1001,9998)
		self.label1 = Label(self,text = self.Customer_AccountNumber, font = ('Montserrat' , '12'), fg ='white', anchor = W)
		self.label1.place(x=50,y=160)

		self.entry10 = Entry(self, font=('Montserrat','12'))
		self.entry10.place(x = 500,y = 400, width = 160)

		self.entry11 = Entry(self, font=('Montserrat','12'))
		self.entry11.place(x = 500,y = 500, width = 160)

		self.entry12 = Entry(self, font=('Montserrat','12'))
		self.entry12.place(x = 500,y = 600, width = 160)

		self.Confirm2 = Button(self,text = "", bd = 0, height = 100, width = 300, command = self.Exception2)
		self.Confirm2.config(image = self.photo)
		self.Confirm2.place(x = 800, y = 800)

		self.Proceed = Button(self,text = "", state = DISABLED, bd = 0, height = 100, width = 300, command = self.ExisitingAccountWin)
		self.Proceed.config(image = self.photo)
		self.Proceed.place(x = 800, y = 900)

	def GetData2(self):
		
		UserName=self.entry10.get()
        Password=self.entry11.get()
        RePassword=self.entry12.get()
        EmptyCheck2 = [UserName, Password, RePassword]
        return EmptyCheck

	def Exception2(self):
		EmptyCheckList = self.GetData2()

	def Empty_Field(value, field_name):
		self.message = "<{0}> field cannot be empty.".format(field_name)
		if EmptyCheck[value] == '':
			tkMessageBox.showinfo("Empty Field", message = self.message)

		if len(EmptyCheckList[0]) == 0:
			empty_field_checker(0,'UserName')
            
		elif len(EmptyCheckList[1]) == 0:
			empty_field_checker(1,'Password')
                        
		elif len(EmptyCheckList[2]) == 0:
			empty_field_checker(2,'Reentered Password')

		elif EmptyCheckList[1]!=EmptyCheckList[2]:
			tkMessageBox.showerror('Input Error' , "Passwords do not match")

		else:
			self.Customer_UserName=UserName
			self.Customer_Password=Password
			self.Proceed.config(state="normal")

#class ExisitingAccountWindow(Frame):
	#

#class AdminWindow(Frame):
	#
	
root = Tk()
root.geometry("1366x768")

app = window(root)
root.mainloop()