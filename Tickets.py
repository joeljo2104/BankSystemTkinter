from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class TicketWin(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.Main_Ticket()

    def Main_Ticket(self):
        self.master.title("Ticket")
        self.pack( fill = BOTH, expand = 1)
         
        self.ButtonMovieTicket = ImageTk.PhotoImage(Image.open("assets/Movie Ticket.png"))   
        self.ButtonAirTicket = ImageTk.PhotoImage(Image.open("assets/Air Ticket.png")) 
        self.BGMainPage = ImageTk.PhotoImage(Image.open("assets/Slide32.jpg"))
        tk.Label(self,image = self.BGMainPage).pack()

        ButtonMovieTicket = Button(self, bd = 0, height = 78, width = 561, command = self.MovieTicket)
        ButtonMovieTicket.config(image = self.ButtonMovieTicket)
        ButtonMovieTicket.place(x = 451, y = 294)

        ButtonAirTicket = Button(self, bd = 0, height = 78, width = 561, command = self.AirTicket)
        ButtonAirTicket.config(image = self.ButtonAirTicket)
        ButtonAirTicket.place(x = 451, y = 505)

    def MovieTicket(self):
    	os.startfile("Movie Ticket.py")
    	self.quit()

    def AirTicket(self):
    	os.startfile("Air Ticket.py")
    	self.quit()
    	   	
root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = TicketWin(root)
root.mainloop()
