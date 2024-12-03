from tkinter import *

root = Tk()

#to make root window center:
width = 800
height = 500

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth/2-width/2))
y = int((screenHeight/2-height/2))
root.geometry(f"{width}x{height}+{x}+{y}")

#Label: to show the text related data.
lb1 = Label(root, text="Welcome to TKINTER class", font=("Arial", 30, "bold"), fg="red", bg="yellow")

#pack - to align the widget at specific place.
# lb1.pack(side=TOP)
#margin - padx - x axis, pady - y axis
# lb1.pack(side=TOP, pady=30, padx=20)
#padding - ipadx - x axis, ipady - y axis
lb1.pack(side=TOP, pady=20, ipadx=50, ipady=20)
#fill and expand

#grid()
#place()


root.mainloop()