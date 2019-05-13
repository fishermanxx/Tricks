import sys
from Tkinter import *
import time

def tick():
	time_s = time.strftime("%H:%M:%S")
	clock.config(text=time_s)
	clock.after(200, tick)

root = Tk()
clock = Label(root, font=("times", 50, "bold"), bg="white")
clock.grid(row=0, column=1)
tick()
root.mainloop()