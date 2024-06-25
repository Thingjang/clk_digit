from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("Digit Clk")
def clock():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)   
    label.after(1000, clock)

label=Label(root, font =("Digital-7", 75), background='brown', foreground='blue')
label.pack(anchor='center')
clock()
root.mainloop()