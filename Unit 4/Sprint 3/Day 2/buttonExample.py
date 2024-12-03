from tkinter import *

def btnFun():
    lb.config(text="Somebody has clicked on button")

root = Tk()


width = 800
height = 500

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth/2-width/2))
y = int((screenHeight/2-height/2))
root.geometry(f"{width}x{height}+{x}+{y}")

btn = Button(root, text = "Click Me", font=(25), command=btnFun, relief="solid")
btn.place(x=100, y=100, width=100, height=30)

lb = Label(root, text="", font=(30))
lb.place(x=100, y=160)


root.mainloop()