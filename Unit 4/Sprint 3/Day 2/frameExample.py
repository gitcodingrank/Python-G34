from tkinter import *
from tkinter.messagebox import showerror, showinfo, showwarning
import uuid
import json
import os

def getStudents():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as file:
            file.write(json.dumps({"students":[]}))
    else:
        with open('data.json', 'r') as file:
            return json.loads(file.read())


def registerStudent():
    student = {}
    student["id"] = str(uuid.uuid4().int)[:15:]
    student["name"] = name.get()
    student["email"] = email.get()
    student["city"] = city.get()

    if not all([student["name"], student["email"], student["city"]]):
        showerror(title="Fields Required", message="Kindly fill the all the fields")
    else:
        data = getStudents()
        studentsData = list(filter(lambda stu: stu["email"]==student["email"], data["students"]))
        
        if len(studentsData) > 0:
            showwarning(title="Student Already Exists", message="Can't add students")
            return 
        
        data["students"].append(student)

        with open('data.json', 'w') as file:
            # file.write(json.dumps(data))
            json.dump(data, file, indent=4)
            showinfo(title="Registred Successfully", message="Student has registered successfully")


root = Tk()


width = 800
height = 500

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth/2-width/2))
y = int((screenHeight/2-height/2))
root.geometry(f"{width}x{height}+{x}+{y}")

lb = Label(root, text = "Student Registration System", bg="red", fg="white", relief="groove", font=(30))
lb.pack(side=TOP, fill=X, ipadx=20)

#frame is like box/div
registrationFrame = Frame(root, bg="teal")
registrationFrame.place(relx=.5, rely=.5, anchor="center", width=500, height=300)

name = StringVar()
email = StringVar()
city = StringVar()

nameLabel = Label(registrationFrame, text = "Enter Name:", bg="teal", font=(25), fg="white")
nameLabel.place(x=30, y=30)
nameEntry = Entry(registrationFrame, textvariable=name, font=(20))
nameEntry.place(x=150, y=30, width=300, height=30)

emailLabel = Label(registrationFrame, text = "Enter Email:", bg="teal", font=(25), fg="white")
emailLabel.place(x=30, y=80)
emailEntry = Entry(registrationFrame, textvariable=email, font=(20))
emailEntry.place(x=150, y=80, width=300, height=30)


cityLabel = Label(registrationFrame, text = "Enter City:", bg="teal", font=(25), fg="white")
cityLabel.place(x=30, y=130)
cityEntry = Entry(registrationFrame, textvariable=city, font=(20))
cityEntry.place(x=150, y=130, width=300, height=30)


btn = Button(registrationFrame, text = "Register Student", command=registerStudent, font=(25), bg="yellow")
btn.place(x=30, y=190, width=200, height=30)

root.mainloop()