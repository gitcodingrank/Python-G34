from tkinter import *

def showFun():
    lb.config(text=boxText.get())

root = Tk()


width = 800
height = 500

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth/2-width/2))
y = int((screenHeight/2-height/2))
root.geometry(f"{width}x{height}+{x}+{y}")

boxText = StringVar()

box = Entry(root, font=(30), textvariable=boxText)
box.place(x=20, y=20, width=300, height=30)

btn = Button(root, text = "Show Text", command=showFun)
btn.place(x=20, y=60)

lb = Label(root, text = "", font=(25))
lb.place(x=20, y=100)




root.mainloop()