from tkinter import *

def showGender():
    print(gender.get())

root = Tk()


width = 800
height = 500

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth/2-width/2))
y = int((screenHeight/2-height/2))
root.geometry(f"{width}x{height}+{x}+{y}")

gender = StringVar()

maleRadio = Radiobutton(root, text="Male", variable=gender, value="Male", command=showGender)
maleRadio.pack()

femaleRadio = Radiobutton(root, text="Female", variable=gender, value="Female", command=showGender)
femaleRadio.pack()



root.mainloop()