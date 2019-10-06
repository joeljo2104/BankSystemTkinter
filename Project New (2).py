import pickle
import os
import random
import time
import string
import tkinter.ttk
import tkinter.font
from tkinter import *
import tkinter as tk
import tkinter.messagebox
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
        self.TransactionMobileBill=['N/A','N/A','N/A','N/A','N/A']
        self.TransactionUtilityBill=['N/A','N/A','N/A','N/A','N/A']
        self.TransactionFundsTransfer=['N/A','N/A','N/A','N/A','N/A']
        self.TransactionMovieTicket=['N/A','N/A','N/A','N/A','N/A']
        self.TransactionAirTicket=['N/A','N/A','N/A','N/A','N/A']
        self.TransactionDeposit=['N/A','N/A','N/A','N/A','N/A']
        self.TransactionWithdraw=['N/A','N/A','N/A','N/A','N/A']

    def UserName_Password(self):
        c=1
        UserName=input("Enter your desired UserName: ")
        
        while c==1:
            print()
            print("Password should have a maximum length of 8 characters and a minimum length of 4 characters.")
            Password=input("Enter your Password: ")
            print("Loading...Please Wait.")
            time.sleep(1)

            if len(Password)>8 or len(Password)<4:
                print("Try Again!", end=' ')

            elif len(Password)<=8 or len(Password)>=4:
                while c==1:
                    Password1=input("Reenter your Password: ")
                    print("Loading...Please Wait.")
                    time.sleep(1)

                    if Password==Password1:
                        self.Customer_UserName=UserName
                        print()
                        print("Welcome!")
                        print("You have Successfully Logged In!")

                        self.Customer_Password=Password
                        c=0

                    else:
                        print("Password does not match.")

    def GetData(self):
        
        self.Customer_Name=input("Enter your Name: ")
        self.Customer_Gender=input("Enter your Gender (Male/Female): ")
        self.Customer_EmailID=input("Enter your Email ID: ")
        self.Customer_DateOfBirth=input("Enter your Date of Birth in 'DD/MM/YYYY': ")
        self.Customer_PhoneNumber=input("Enter your Phone Number: ")
        self.Customer_PhoneNumber2=input("Enter your Alternate Phone Number: ")
        self.Customer_POBox=input("Enter your PO Box Number: ")
        self.Customer_Address=input("Enter your Mailing Address: ")
        self.Customer_RewardPoints=0
        time.sleep(1)
        print()
        print("Your Account Number is being Generated, Please Wait...")
        self.Customer_AccountNumber=random.randint(1001,9998)
        print("Your Account Number is",self.Customer_AccountNumber)
        print("Loading...Please Wait.")
        time.sleep(4)
        time.sleep(1)
        print()
        print("Dear",self.Customer_Name, end=' ')
        print()
        print("UserName and Password Creation")
        self.UserName_Password()
        
    def UpdateData(self):
        print()
        print("1. Name: ",self.Customer_Name)
        print("2. Gender: ",self.Customer_Gender)
        print("3. Email ID: ",self.Customer_EmailID)
        print("4. Date of Birth: ",self.Customer_DateOfBirth)
        print("5. Phone Number: ",self.Customer_PhoneNumber)
        print("6. Alternate Phone Number: ",self.Customer_PhoneNumber2)
        print("7. PO Box: ",self.Customer_POBox)
        print("8. Address: ",self.Customer_Address)
        print("9. UserName: ",self.Customer_UserName)
        print("10. Password: ", end=' ')
        for i in self.Customer_Password:
            print("*", end=' ')
        print()
        print("Loading...Please Wait.")
        time.sleep(1)
        Option=eval(input("Enter the Number of the Detail you wish to change: "))

        if Option==1:
            self.Customer_Name=input("Enter your Name: ")
        elif Option==2:
            self.Customer_Gender=input("Enter your Gender (Male/Female): ")
        elif Option==3:
            self.Customer_EmailID=input("Enter your Email ID: ")
        elif Option==4:
            self.Customer_DateOfBirth=input("Enter your Date of Birth in 'DD/MM/YYYY': ")
        elif Option==5:
            self.Customer_PhoneNumber=input("Enter your Phone Number: ")
        elif Option==6:
            self.Customer_PhoneNumber2=input("Enter your Alternate Phone Number: ")
        elif Option==7:
            self.Customer_POBox=input("Enter your PO Box Number: ")
        elif Option==8:
            self.Customer_Address=input("Enter your Mailing Address: ")

        elif Option==9:
            c=1
            while c==1:
                UserName1=input("Please Enter your Current UserName: ")

                if self.Customer_UserName==UserName1:
                    self.Customer_UserName=input("Enter your New UserName: ")
                    c=0

                else:
                    print("Incorrect Current UserName!")

        elif Option==10:
            c=1
            while c==1:
                Password1=input("Please Enter your Current Password: ")

                if self.Customer_Password==Password1:
                    while c==1:
                        print("Password should have a maximum length of 8 characters and a minimum length of 4 characters.")
                        Password=input("Enter your Password: ")
                        print("Loading...Please Wait.")
                        time.sleep(1)

                        if len(Password)>8 or len(Password)<4:
                            print("Try Again!", end=' ')

                        elif len(Password)<=8 or len(Password)>=4:
                            while c==1:
                                Password1=input("Reenter your Password: ")

                                if Password==Password1:
                                    print()
                                    print("Welcome!")
                                    print("You have Successfully Logged In!")
                                    print("Loading...Please Wait.")
                                    time.sleep(1)
                                    self.Customer_Password=Password
                                    c=0

                else:
                    print("Password does not match.")

    def DisplayData(self):
        time.sleep(1)
        print()
        print("Account Number:",self.Customer_AccountNumber)
        print("Name: ",self.Customer_Name)
        print("Gender: ",self.Customer_Gender)
        print("Email ID: ",self.Customer_EmailID)
        print("Date of Birth: ",self.Customer_DateOfBirth)
        print("Phone Number: ",self.Customer_PhoneNumber)
        print("Alternate Phone Number: ",self.Customer_PhoneNumber2)
        print("PO Box: ",self.Customer_POBox)
        print("Address: ",self.Customer_Address)
        print("UserName: ",self.Customer_UserName)
        print("Password: ", end=' ')
        for i in self.Customer_Password:
            print("*", end=' ')
        print()
        print("Account Balance: INR",self.Customer_Balance)
        print("Reward Points: ",self.Customer_RewardPoints)
        print("Car Loan: ",self.CarLoanApplication)
        print("Gold Loan: ",self.GoldLoanApplication)
        print("Home Loan: ",self.HomeLoanApplication)
        print("Education Loan: ",self.EducationLoanApplication)
        
    def MobileBill(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Mobile Bill Payment Service!")
        Service_Provider=input("Enter your Service Provider: (Etisalat/du)")
        print()
        BillAmount=eval(input("Enter your Mobile Bill Amount: INR "))

        print()
        s=1
        while s==1:
                Pay=eval(input("Enter the Amount you wish to pay: INR "))
                print("Loading...Please Wait.")
                time.sleep(1)
                if Pay>self.Customer_Balance:
                    print("You do not have Sufficient Account Balance to proceed this transaction.")

                elif Pay>BillAmount:
                    print("You cannot pay more than the Bill Amount")

                else:
                    self.Customer_Balance=self.Customer_Balance-Pay
                    print()
                    print("Payment Successfully Received! Thank You for using AJD Bank Fast Payment.")
                    print("Your Mobile Bill is now: INR", BillAmount-Pay)

                    TransactionNo=random.randint(100001,999998)
                    print("Your Transaction Number is",TransactionNo)

                    RewardPoints=Pay*0.10
                    self.Customer_RewardPoints+=RewardPoints
                    print("You have received",RewardPoints,"for this Transaction!")
                    print("Total Reward Points:",self.Customer_RewardPoints)

                    TransactionTime=time.ctime()
                    self.TransactionMobileBill=[TransactionNo,TransactionTime,Service_Provider,Pay,RewardPoints]
                    s=0

    def UtilityBill(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Utility Bill Payment Service!")
        Utility_Provider=input("Enter your Utility Provider: (FEWA/DEWA/SEWA)")
        print()
        BillAmount=eval(input("Enter your Utility Bill Amount: INR "))

        print()
        s=1
        while s==1:
                Pay=eval(input("Enter the Amount you wish to pay: INR "))
                print("Loading...Please Wait.")
                time.sleep(1)
                if Pay>self.Customer_Balance:
                    print("You do not have Sufficient Account Balance to proceed this transaction.")

                elif Pay>BillAmount:
                    print("You cannot pay more than the Bill Amount")

                else:
                    self.Customer_Balance=self.Customer_Balance-Pay
                    print()
                    print("Payment Successfully Received! Thank You for using AJD Bank Fast Payment.")
                    print("Your Utility Bill is now: INR", BillAmount-Pay)

                    TransactionNo=random.randint(100001,999998)
                    print("Your Transaction Number is",TransactionNo)

                    RewardPoints=Pay*0.10
                    self.Customer_RewardPoints+=RewardPoints
                    print("You have received",RewardPoints,"for this Transaction!")
                    print("Total Reward Points:",self.Customer_RewardPoints)

                    TransactionTime=time.ctime()
                    self.TransactionUtilityBill=[TransactionNo,TransactionTime,Utility_Provider,Pay,RewardPoints]
                    s=0

    def FundsTransfer(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Funds Transfer Service!")
        AccNo=eval(input("Enter the Account Number of the Account you wish to transfer to: "))
        AccName=input("Enter the Name of the Account Holder of the Account you wish to transfer to: ")

        s=1
        while s==1:
            PasswordVerification=input("Enter your Password for Verification: ")
            print("Loading...Please Wait.")
            time.sleep(1)
            if PasswordVerification==self.Customer_Password:
                Pay=eval(input("Enter the Amount you wish to transfer: INR "))
                if Pay>self.Customer_Balance:
                    print("You do not have Sufficient Account Balance to proceed this transaction.")

                else:
                    self.Customer_Balance=self.Customer_Balance-Pay
                    print("Loading...Please Wait.")
                    time.sleep(1)
                    print()
                    print("Amount Successfully Transferred! Thank You for using AJD Bank's Funds Transfer Service!")

                    TransactionNo=random.randint(100001,999998)
                    print("Your Transaction Number is",TransactionNo)

                    TransactionTime=time.ctime()
                    self.TransactionFundsTransfer=[TransactionNo,TransactionTime,AccNo,AccName,Pay,'0']
                    s=0
            else:
                print("Incorrect Password. Please Try Again!")
                
    def MovieTicket(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Movie Ticket Booking Service!")
        print("  Movie Ticket Pricing")
        print("     Seat       |      Price ")
        print(" -----------------------")
        print(" Standard  |   INR 35")
        print("      VIP         |   INR 45")

        print()
        NoOfSeats=eval(input("Enter the Number of Seats: "))
        TypeOfSeat=input("Enter the Type of Seats (S - Standard, V - VIP): ")

        if TypeOfSeat.lower()=="s":
            TotalAmount=35*NoOfSeats

        elif TypeOfSeat.lower()=="v":
            TotalAmount=45*NoOfSeats

        else:
            print("Invalid Option!")

    
        print("Total Amount: INR", TotalAmount)
        print("Loading...Please Wait.")
        time.sleep(1)
        print()
        PayConfirm=input("Confirm Payment for Movie Tickets? (Yes/No): ")
        if PayConfirm.lower()=="yes":
            s=1
            while s==1:
                Pay=TotalAmount
                if Pay>self.Customer_Balance:
                    print("You do not have Sufficient Account Balance to proceed this transaction.")
                    s=0

                else:
                    self.Customer_Balance=self.Customer_Balance-Pay
                    print()
                    print("Payment Successfully Received! Thank You for using AJD Bank Fast Payment.")

                    TransactionNo=random.randint(100001,999998)
                    print("Your Transaction Number is",TransactionNo)

                    RewardPoints=Pay*0.10
                    self.Customer_RewardPoints+=RewardPoints
                    print("You have received",RewardPoints,"for this Transaction!")
                    print("Total Reward Points:",self.Customer_RewardPoints)
                    print("Your Tickets have been sent to",self.Customer_EmailID)

                    TransactionTime=time.ctime()
                    self.TransactionMovieTicket=[TransactionNo,TransactionTime,"VOX",Pay,RewardPoints]
                    s=0
                    
    def AirTicket(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        
        print("Welcome to AJD Bank's Air Ticket Booking Service!")
        print("  Air Ticket Pricing")
        print("       Class     |         Price ")
        print(" -----------------------")
        print("   Economy  |   INR 2000")
        print("   Business  |   INR 5000")
        print(" First Class  |   INR 10000")

        print()
        NoOfSeats=eval(input("Enter the number of Seats: "))
        TypeOfSeat=input("Enter the Class (E - Economy, B - Business, F - First): ")

        if TypeOfSeat.lower()=="e":
            TotalAmount=2000*NoOfSeats

        elif TypeOfSeat.lower()=="b":
            TotalAmount=5000*NoOfSeats

        elif TypeOfSeat.lower()=="f":
            TotalAmount=10000*NoOfSeats

        else:
            print("Invalid Option!")

        print("Total Amount: INR", TotalAmount)
        print("Loading...Please Wait.")
        time.sleep(1)
        
        print()
        PayConfirm=input("Confirm Payment for Air Tickets? (Yes/No): ")
        if PayConfirm.lower()=="yes":
            s=1
            while s==1:
                Pay=TotalAmount
                if Pay>self.Customer_Balance:
                    print("You do not have Sufficient Account Balance to proceed this transaction.")
                    s=0

                else:
                    self.Customer_Balance=self.Customer_Balance-Pay
                    print()
                    print("Payment Successfully Received! Thank You for using AJD Bank Fast Payment.")

                    TransactionNo=random.randint(100001,999998)
                    print("Your Transaction Number is",TransactionNo)

                    RewardPoints=Pay*0.10
                    self.Customer_RewardPoints+=RewardPoints
                    print("You have received",RewardPoints,"for this Transaction!")
                    print("Total Reward Points:",self.Customer_RewardPoints)
                    print("Your Tickets have been sent to",self.Customer_EmailID)

                    TransactionTime=time.ctime()
                    self.TransactionAirTicket=[TransactionNo,TransactionTime,"AirLine",Pay,RewardPoints]
                    s=0
                    
    def CarLoan(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Car Loan Application Service!")
        self.CarLoanAmount=eval(input("Enter the Amount you want to Loan: INR "))
        self.CarLoanTime=eval(input("Enter the Number of Years: "))
        print("Loading...Please Wait.")
        time.sleep(1)
        print()
        print("The Interest Rate for Car Loan is 0.08% Per Annum.")
        self.CarLoanInterest=self.CarLoanAmount*0.08*self.CarLoanTime
        self.CarLoan=self.CarLoanInterest+self.CarLoanAmount
        print("You will have to repay INR",self.CarLoan,"in", self.CarLoanTime,"years.")
        print("Loading...Please Wait.")
        time.sleep(1)

        print()
        Payment=input("Do you wish to pay Monthly, or Quarterly? Enter M for Monthly, Q for Quarterly: ")
        if Payment.lower()=="m":
            self.CarLoanPayType="Monthly"
            self.CarLoanPayAmount=self.CarLoan/(12*self.CarLoanTime)
            print("You will have to pay INR",self.CarLoanPayAmount,"every month.")

        elif Payment.lower()=="q":
            self.CarLoanPayType="Quarterly"
            self.CarLoanPayAmount=self.CarLoan*3/(12*self.CarLoanTime)
            print("You will have to pay INR",self.CarLoanPayAmount,"every 3 months.")

        print("Loading...Please Wait.")
        time.sleep(1)
        self.CarLoanApplication="Applied"
        print()
        print("Your Application for Car Loan has been successfully received.")
        ApplicationNo=random.randint(10001,99998)
        print("Your Application Number is",ApplicationNo)
        print("Please head over to the AJD Bank for Document Verification.")
        print()
        
    def GoldLoan(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Car Loan Application Service!")
        self.GoldAmount=eval(input("Enter Amount of Gold in Grams: "))
        self.GoldCarat=eval(input("Enter Gold Carat (22/24): "))
        self.GoldLoanTime=eval(input("Enter the Number of Years: "))

        print()
        if self.GoldCarat==22:
            self.GoldLoanAmount=self.GoldAmount*30000
            print("The Interest Rate for Gold Loan is 0.02% Per Annum.")
            self.GoldLoanInterest=self.GoldLoanAmount*0.02*self.GoldLoanTime
            self.GoldLoan=self.GoldLoanInterest+self.GoldLoanAmount

        elif self.GoldCarat==24:
            self.GoldLoanAmount=self.GoldAmount*32000
            print("The Interest Rate for Gold Loan is 0.02% Per Annum.")
            self.GoldLoanInterest=self.GoldLoanAmount*0.02*self.GoldLoanTime
            self.GoldLoan=self.GoldLoanInterest+self.GoldLoanAmount
            
        print("You will have to repay INR",self.GoldLoan,"in", self.GoldLoanTime,"years.")
        print("Loading...Please Wait.")
        time.sleep(1)

        print()
        Payment=input("Do you wish to pay Monthly, or Quarterly? Enter M for Monthly, Q for Quarterly: ")

        if Payment.lower()=="m":
            self.GoldLoanPayType="Monthly"
            self.GoldLoanPayAmount=self.GoldLoan/(12*self.GoldLoanTime)
            print("You will have to pay INR",self.GoldLoanPayAmount,"every month.")

        elif Payment.lower()=="q":
            self.GoldLoanPayType="Quarterly"
            self.GoldLoanPayAmount=self.GoldLoan*3/(12*self.GoldLoanTime)
            print("You will have to pay INR",self.GoldLoanPayAmount,"every 3 months.")
            
        print("Loading...Please Wait.")
        time.sleep(1)
        self.GoldLoanApplication="Applied"
        print()
        print("Your Application for Gold Loan has been successfully received.")
        ApplicationNo=random.randint(10001,99998)
        print("Your Application Number is",ApplicationNo)
        print("Please head over to the AJD Bank for Document Verification.")
        print()
        
    def HomeLoan(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Car Loan Application Service!")
        self.HomeLoanAmount=eval(input("Enter the Amount you want to Loan: INR "))
        self.HomeLoanTime=eval(input("Enter the Number of Years: "))

        print()
        print("The Interest Rate for Home Loan is 1.5% Per Annum.")
        self.HomeLoanInterest=self.HomeLoanAmount*1.5*self.HomeLoanTime
        self.HomeLoan=self.HomeLoanInterest+self.HomeLoanAmount
        print("You will have to repay INR",self.HomeLoan,"in", self.HomeLoanTime,"years.")
        print("Loading...Please Wait.")
        time.sleep(1)

        print()
        Payment=input("Do you wish to pay Monthly, or Quarterly? Enter M for Monthly, Q for Quarterly: ")

        if Payment.lower()=="m":
            self.HomeLoanPayType="Monthly"
            self.HomeLoanPayAmount=self.HomeLoan/(12*self.HomeLoanTime)
            print("You will have to pay INR",self.HomeLoanPayAmount,"every month.")

        elif Payment.lower()=="q":
            self.HomeLoanPayType="Quarterly"
            self.HomeLoanPayAmount=self.HomeLoan*3/(12*self.HomeLoanTime)
            print("You will have to pay INR",self.HomeLoanPayAmount,"every 3 months.")

        print("Loading...Please Wait.")
        time.sleep(1)
        self.HomeLoanApplication="Applied"
        print()
        print("Your Application for Home Loan has been successfully received.")
        ApplicationNo=random.randint(10001,99998)
        print("Your Application Number is",ApplicationNo)
        print("Please head over to the AJD Bank for Document Verification.")
        print()

    def EducationLoan(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Welcome to AJD Bank's Car Loan Application Service!")
        self.EducationLoanAmount=eval(input("Enter the Amount you want to Loan: INR "))
        self.EducationLoanTime=eval(input("Enter the Number of Years: "))

        print()
        print("The Interest Rate for Education Loan is 1.5% Per Annum.")
        self.EducationLoanInterest=self.EducationLoanAmount*1.5*self.EducationLoanTime
        self.EducationLoan=self.EducationLoanInterest+self.EducationLoanAmount
        print("You will have to repay INR",self.EducationLoan,"in", self.EducationLoanTime,"years.")
        print("Loading...Please Wait.")
        time.sleep(1)

        print()
        Payment=input("Do you wish to pay Monthly, or Quarterly? Enter M for Monthly, Q for Quarterly: ")

        if Payment.lower()=="m":
            self.EducationLoanPayType="Monthly"
            self.EducationLoanPayAmount=self.EducationLoan/(12*self.EducationLoanTime)
            print("You will have to pay INR",self.EducationLoanPayAmount,"every month.")

        elif Payment.lower()=="q":
            self.EducationLoanPayType="Quarterly"
            self.EducationLoanPayAmount=self.EducationLoan*3/(12*self.EducationLoanTime)
            print("You will have to pay INR",self.EducationLoanPayAmount,"every 3 months.")

        print("Loading...Please Wait.")
        time.sleep(1)
        self.EducationLoanApplication="Applied"
        print()
        print("Your Application for Education Loan has been successfully received.")
        ApplicationNo=random.randint(10001,99998)
        print("Your Application Number is",ApplicationNo)
        print("Please head over to the AJD Bank for Document Verification.")
        print()

    def Deposit(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        Deposit=eval(input("Enter Amount to Deposit: INR "))
        c.Customer_Balance=c.Customer_Balance+Deposit
        print("Loading...Please Wait.")
        time.sleep(1)
        print("Deposited Successful!")
        print("Your Current Account Balance is INR",c.Customer_Balance)

        TransactionNo=random.randint(100001,999998)
        print("Your Transaction Number is",TransactionNo)

        RewardPoints=0
        TransactionTime=time.ctime()
        self.TransactionDeposit=[TransactionNo,TransactionTime,"Deposit",Deposit,RewardPoints]

    def Withdraw(self):
        print("Loading...Please Wait.")
        time.sleep(1)
        Withdraw=eval(input("Enter Amount to Withdraw: INR "))
        print("Loading...Please Wait.")
        time.sleep(1)
        if Withdraw>c.Customer_Balance:
            print("Sorry, your Account Balance is INR",c.Customer_Balance,", you have an Amount greater than your Account Balance. Please Try Again")
        else:
            c.Customer_Balance=c.Customer_Balance-Withdraw
            print("Withdraw Successful!")
            print("Your Current Account Balance is INR",c.Customer_Balance)

            TransactionNo=random.randint(100001,999998)
            print("Your Transaction Number is",TransactionNo)

            RewardPoints=0
            TransactionTime=time.ctime()
            self.TransactionWithdraw=[TransactionNo,TransactionTime,"Withdraw",Withdraw,RewardPoints]

    def TransactionList(self):
        print("Loading...Please Wait.")
        os.startfile("Transaction List.py")

def CurrencyConvertor():
    os.startfile("Currency Convertor.py")

nx=0
def NewAccount():
    print("You have chosen to make a New Account")
    Continue=input("Do you wish to continue?:")
    if Continue.lower()=="yes":
        c=Customer()
        c.__init__()
        c.GetData()

        Bank=open("Account.dat","ab")
        pickle.dump(c,Bank)
        Bank.close()

        global nx
        nx=3
    elif Continue.lower()=="no":
        Main()
    
def ExistingAccount():
    print("You have chosen to access your Account")
    Continue=input("Do you wish to continue?:")
    if Continue.lower()=="yes":

        Bank=open("Account.dat","rb")
        global nx
    
        c=Customer()

        try:
            AccountNumber=eval(input("Enter your Account Number: "))
            while True:
                c=pickle.load(Bank)
                if AccountNumber==c.Customer_AccountNumber:
                    nx=1
                    while nx==1:
                        UserName=input("Enter your UserName: ")
                        if UserName==c.Customer_UserName:
                            nx=2
                            while nx==2:
                                Password=input("Enter your Password: ")
                                if Password==c.Customer_Password:
                                    print("You have Successfully Logged In!")
                                    print("Welcome",c.Customer_Name,"!")
                                    nx=3
                                    break

                                else:
                                    print("Wrong Password!")

                        else:
                            print("Wrong UserName!")

        except EOFError:
            if nx==0:
                print("Wrong Account Number!")

        Bank.close()
    elif Continue.lower()=="no":
        Main()

    else:
        print("Invalid Option! You are being redirected to the Main Menu!")
        Main()

def Admin():
    AdminPassword="Admin@AJD"
    Password=input("Enter Admin Password: ")

    if Password==AdminPassword:
        c=Customer()
        Bank=open("Account.dat","rb")
        a=1

        print("1. View Details of All Accounts")
        print("2. Delete an Account")
        Choice=eval(input("Enter Choice: "))

        if Choice==1:
            try:
                while True:
                    c=pickle.load(Bank)
                    print("---------Account",a,"----------------")
                    c.DisplayData()
                    a+=1

            except EOFError:
                pass

        elif Choice==2:
            PasswordVerify=input("Enter Admin Password for Verification: ")

            if PasswordVerify==AdminPassword:
                AccountNo=eval(input("Enter Account Number: "))
                Bank=open("Account.dat","rb")
                Bank1=open("Temp.dat","wb")
                c=Customer()

                try:
                    while True:
                        c=pickle.load(Bank)

                        if AccountNo!=c.Customer_AccountNumber:
                            print("Account Deleted!")

                        else:
                            pickle.dump(c,Bank1)

                except EOFError:
                    pass

                Bank.close()
                Bank1.close()
                os.remove("Account.dat")
                os.rename("Temp.dat","Account.dat")

        LogOut=input("Do you wish to Log Out?")

        if LogOut.lower()=="y" or LogOut.lower()=="yes":
            Bank.close()
            print("You have Successfully Logged Out!")
        

    else:
        print("Wrong Password!")
        print("You are being redirected to the Main Menu for security reasons.")
        Main()


def Main():
    while nx==0:
        print("========================================")
        print("          Welcome to AJD Bank           ")
        print("========================================")
        print() 
        print("   Options:")
        print("----------------------------------------")
        print("      1. Existing Customer ")
        print("      2. New Customer ")
        print("----------------------------------------")
        print()

        Option=input("Enter your Option: ")
        if Option=="1":
            ExistingAccount()
        elif Option=="2":
            NewAccount()
        elif Option.lower()=="admin":
            Admin()

Main()
while nx==3:
    print() 
    print("========================================")
    print("      1. Bank Services")
    print("      2. Bill Payment")
    print("      3. Tickets")
    print("      4. Loans")
    print("      5. Funds Transfer")
    print("      6. Currency Convertor")
    print("      7. Quit")
    print("========================================")
    print()

    Option1=eval(input("Enter your Option: "))
    print()

    if Option1==1:
        print()
        print("========================================")
        print("              Bank Services")
        print("----------------------------------------")
        print("   1. Deposit Money")
        print("   2. Withdraw Money")
        print("   3. Transaction Summary")
        print("   4. Update Bank Account Information")
        print("   5. Display Bank Account Information")
        print("========================================")
        print()

        Option2=eval(input("Enter your Option: "))
        print("----------------------------------------")

        if Option2==1:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.Deposit()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==2:
            AccountNo=eval(input("Enter Account Number: "))
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")
            c=Customer()

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.Withdraw()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==3:
            c=Customer()
            c.TransactionList()
            
        elif Option2==4:
            AccountNo=eval(input("Enter Account Number: "))
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")
            c=Customer()

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.UpdateData()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==5:
            AccountNo=eval(input("Enter Account Number: "))
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")
            c=Customer()

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.DisplayData()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

    elif Option1==2:
        print("Bill Payment")
        print()
        print("1. Mobile Payment")
        print("2. Utility Payment")
        print()
        Option2=eval(input("Enter your Option: "))

        if Option2==1:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.MobileBill()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==2:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.UtilityBill()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

    elif Option1==3:
        print("Tickets")
        print()
        print("1. Movie Ticket")
        print("2. Air Ticket")
        print()
        Option2=eval(input("Enter your Option: "))

        if Option2==1:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.MovieTicket()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==2:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.AirTicket()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

    elif Option1==4:
        print()
        print("Loans")
        print("1. Car Loan")
        print("2. Gold Loan")
        print("3. Home Loan")
        print("4. Education Loan")
        print()
        Option2=eval(input("Enter your Option: "))
        
        if Option2==1:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.CarLoan()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==2:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.GoldLoan()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==3:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.HomeLoan()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

        elif Option2==4:
            AccountNo=eval(input("Enter Account Number: "))
            c=Customer()
            Bank=open("Account.dat","rb")
            Bank1=open("Temp.dat","wb")

            try:
                while True:
                    c=pickle.load(Bank)

                    if AccountNo!=c.Customer_AccountNumber:
                        pickle.dump(c,Bank1)

                    else:
                        c.EducationLoan()
                        pickle.dump(c,Bank1)

            except EOFError:
                pass

            Bank.close()
            Bank1.close()
            os.remove("Account.dat")
            os.rename("Temp.dat","Account.dat")

    elif Option1==5:
        AccountNo=eval(input("Enter Account Number: "))
        c=Customer()
        Bank=open("Account.dat","rb")
        Bank1=open("Temp.dat","wb")

        try:
            while True:
                c=pickle.load(Bank)
                if AccountNo!=c.Customer_AccountNumber:
                    pickle.dump(c,Bank1)

                else:
                    c.FundsTransfer()
                    pickle.dump(c,Bank1)

        except EOFError:
            pass

        Bank.close()
        Bank1.close()
        os.remove("Account.dat")
        os.rename("Temp.dat","Account.dat")

    elif Option1==6:
        CurrencyConvertor()

    elif Option1==7:
        quit()
    
