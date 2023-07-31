from tkinter import *
root=Tk()
root.title("classes")
root.geometry("600x600")

name=Label(root,text="Enter Name: ")
name.place(relx=0.4,rely=0.2,anchor=CENTER)
name_input=Entry(root)
name_input.place(relx=0.6,rely=0.2,anchor=CENTER)

age=Label(root,text="Enter Age: ")
age.place(relx=0.4,rely=0.3,anchor=CENTER)
age_input=Entry(root)
age_input.place(relx=0.6,rely=0.3,anchor=CENTER)

gender=Label(root,text="Select Gender")
gender.place(relx=0.4,rely=0.4,anchor=CENTER)

rb=StringVar(value="0")
r1=Radiobutton(root,text="Male",variable=rb,value="yes")
r1.place(relx=0.55,rely=0.4,anchor=CENTER)

r2=Radiobutton(root,text="Female",variable=rb,value="no")
r2.place(relx=0.65,rely=0.4,anchor=CENTER)

phone=Label(root,text="Enter Phone no : ")
phone.place(relx=0.4,rely=0.5,anchor=CENTER)
phone_input=Entry(root)
phone_input.place(relx=0.6,rely=0.5,anchor=CENTER)


name_get=""
age_get=""
gender_get=""
phone_get=""

class citizen:
    def __init__(self,name,age,gender,phone):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
        
    def addCitizen(self):
        global name_get
        global age_get
        global gender_get
        global phone_get
        
        name_get=name_input.get()
        age_get=age_input.get()
        gender_get=rb.get()
        phone_get=phone_input.get()
        
        
        print("name  ",self.name)
        print("age  ",str(self.age))
        print("gender  ",self.gender)
        print("phone  " ,str(self.phone))
        print("citizen added \n")
        
citizen1=citizen("avidan","15","male","8956021675")
citizen1.addCitizen()




root.mainloop()