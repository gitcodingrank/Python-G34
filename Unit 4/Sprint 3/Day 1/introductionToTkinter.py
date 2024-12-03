#
# import tkinter
from tkinter import *

win = Tk()
win.title("CHitkara University")
# win.geometry("800x400+100+50")

# win.config(bg="yellow")
win["bg"] = "red"
# win.resizable(False, False)

# win.attributes('-alpha', .5) # for changing the opacity

#How to show above window on center.
width = 800
height = 500

screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()

x = int((screenWidth/2-width/2))
y = int((screenHeight/2-height/2))
win.geometry(f"{width}x{height}+{x}+{y}")



win.mainloop()