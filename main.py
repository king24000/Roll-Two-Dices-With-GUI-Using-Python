from tkinter import *
import random 

fs = Tk()
fs.geometry("500x300") #500 is width and 300 is height
fs.title("Roll Two Dices")
fs.resizable(False,False)
fs.config(bg="orange")
label = Label(fs,text="",font=("times",100) ,bg="black",fg="white",height=20,width=20 )
def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack(padx=10,pady=110,)
button = Button(fs,text="Rolling",font=("The New Roman",21),bg="red",fg="white",command=roll)
button.place(x=120, height=80,width=250)
fs.mainloop()