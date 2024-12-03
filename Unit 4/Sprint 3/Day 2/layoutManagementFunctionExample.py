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


#Label: to show the text
lb1 = Label(root, text ="Python", font=(25), bg="red", fg="white")

#there are three types of layout function to show any widget inside window:
#pack() - 
#grid()
#place()

# lb.pack() #bydefault pack side is Top
# lb1.pack(side=LEFT, fill=Y)

# lb2 = Label(root, text ="Java", font=(25), bg="red", fg="white")

# lb2.pack(side=TOP, padx=20, pady=20, ipadx=20, ipady=10)


#grid() - to show the widget in rows and columns
# name = Label(root, text ="Name", font=(25), bg="red", fg="white")
# name.grid(row=0, column=0, pady=10, padx=10)

# city = Label(root, text ="City", font=(25), bg="red", fg="white")
# city.grid(row=0, column=1, pady=10, padx=10)

# nameValue = Label(root, text ="Pankaj", font=(25), bg="red", fg="white")
# nameValue.grid(row=1, column=0)

# cityValue = Label(root, text ="Delhi", font=(25), bg="red", fg="white")
# cityValue.grid(row=1, column=1)


#place() - to align the widgets at specific cordinates

# lb1 = Label(root, text ="Chitkara", font=(25), bg="red", fg="white")
# lb1.place(x=10, y=10, width=200,height=200)

# lb1 = Label(root, text ="Chitkara", font=(25), bg="red", fg="white")
# lb1.place(relx=.5, rely=.5, anchor="center") #anchor - n, e s w, ne, se, sw, sn, center




root.mainloop()