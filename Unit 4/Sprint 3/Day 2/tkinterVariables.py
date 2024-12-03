from tkinter import *

root = Tk()


width = 800
height = 500

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth/2-width/2))
y = int((screenHeight/2-height/2))
root.geometry(f"{width}x{height}+{x}+{y}")


#tkinter variables: StringVar(), IntVar(), DoubleVar(), BooleanVar()

# name = StringVar(value = "Rakesh")
# print(name.get())
# name.set("Pawan")
# print(name.get())


# age = IntVar(value = 45.56)
# print(age.get())
# age.set(46)
# print(age.get())


# salary = DoubleVar(value = 45000.56)
# print(salary.get())
# salary.set(46000.10)
# print(salary.get())

# isMarried = BooleanVar(value = True)
# print(isMarried.get())
# isMarried.set(False)
# print(isMarried.get())

root.mainloop()