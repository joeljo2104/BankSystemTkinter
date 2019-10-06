from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle , os , string , random , tkinter.ttk , tkinter.font
from PIL import ImageTk, Image

class ViewAccountDetailsWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.Main_ViewAccountDetailsWindow()

    def Main_ViewAccountDetailsWindow(self):

        self.master.title("View Account Details")
        self.pack( fill = BOTH, expand = 1)

        self.ButtonMainMenu = ImageTk.PhotoImage(Image.open("assets/Main Menu.png"))
        self.BG = ImageTk.PhotoImage(Image.open("assets/Slide34.jpg"))
        tk.Label(self,image = self.BG).pack()

        self.label1 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label1.place(x = 600,y = 207)

        self.label2 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label2.place(x = 600,y = 270)

        self.label3 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label3.place(x = 600,y = 330)

        self.label4 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label4.place(x = 600,y = 390)

        self.label5 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label5.place(x = 600,y = 452)

        self.label6 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label6.place(x = 600,y = 514)

        self.label7 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label7.place(x = 600,y = 575)

        self.label8 = Label(self,text = 'Text', font = ('Montserrat' , '28', 'bold'), bg = '#06357a', fg ='white', anchor = W)
        self.label8.place(x = 600,y = 636)

        ButtonMainMenu = Button(self, bd = 0, height = 74, width = 330, command = self.Main_Menu)
        ButtonMainMenu.config(image = self.ButtonMainMenu)
        ButtonMainMenu.place(x = 963, y = 257)

    def Main_Menu(self):
        os.startfile("Main Menu.py")
        self.quit()


root = Tk()

root.geometry("1366x768+0+0")
root.state('zoomed')

app = ViewAccountDetailsWindow(root)
root.mainloop()