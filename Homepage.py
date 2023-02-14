from tkinter import *
from tkinter import messagebox

from addstudent import addstudentClass
from change_password import changePasswordClass
from course_page import courseClass
from departmentpage import deptClass
from detail_page import *
from manageuser import userClass
from report1 import report1Class
from report2 import report2Class
from studentpage import studentClass

class HomepageClass:
    def __init__(self,usertype,username):
        self.window = Tk()
        w=self.window.winfo_screenwidth()
        h=self.window.winfo_screenheight()
        self.window.title(app_name)
        # self.window.config(background='#C9C8FF')
        #method 1
        self.window.minsize(600,400)
        #method 2
        self.window.geometry("%dx%d+%d+%d"%(600,400,400,200))
        #method3
        self.window.state("zoomed")


        #------------ background image---------------------

        from PIL import ImageTk, Image
        self.bimg1 = Image.open("myimages//bg1.jpg")
        self.bimg1 = self.bimg1.resize((w,h))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bglbl=Label(self.window,image=self.bimg2)
        self.bglbl.place(x=0,y=0)

        #-------------------------------------------------









        self.menubar=Menu(self.window)
        self.window.config(menu=self.menubar)
        self.window.option_add('*TearOff',False)
        self.menu1 = Menu(self.menubar)
        self.menu2 = Menu(self.menubar)
        self.menu3 = Menu(self.menubar)
        self.menu4 = Menu(self.menubar)
        self.menu5 = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu1,label='Student')
        self.menubar.add_cascade(menu=self.menu2,label='Teacher')
        self.menubar.add_cascade(menu=self.menu3,label='Department')
        self.menubar.add_cascade(menu=self.menu4,label='Record')
        self.menubar.add_cascade(menu=self.menu5,label='Account')

        # self.menu1.add_command(label='Add Student',command=lambda : addstudentClass())#create other independent window
        self.menu1.add_command(label='Add Student',command=lambda : addstudentClass(self.window))
        self.menu1.add_command(label='Update Student')
        self.menu1.add_command(label='Delete Student')
        self.menu1.add_command(label='Student',command=lambda :  studentClass(self.window))

        self.menu3.add_command(label='Department',command=lambda :  deptClass(self.window))
        self.menu3.add_command(label='Course',command=lambda :  courseClass(self.window))

        self.menu4.add_command(label='Student Record',command=lambda :  report1Class(self.window))
        self.menu4.add_command(label='Department Record',command=lambda :  report2Class(self.window))

        self.menu5.add_command(label='Manage User',command=lambda :  userClass(self.window))
        self.menu5.add_command(label='Change Password',command=lambda :  changePasswordClass(self.window,username))
        self.menu5.add_command(label='Logout',command=self.quitter)

        if usertype=='Employee':
            self.cust_window()

        self.window.mainloop()

    def cust_window(self):
        self.window.config(background='pink')
        self.menubar.entryconfig(2, state='disabled') #teacher
        self.menubar.delete(4)  #record


        self.menu1.entryconfig(1, state='disabled') #teacher
        self.menu1.delete(2)  #record

        self.menu5.entryconfig(0, state='disabled') #teacher

    def quitter(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to logout ? ")
        if ans=='yes':
            self.window.destroy()
            from loginpage import loginClass
            loginClass()


if __name__ == '__main__':
    HomepageClass("Employee","simran")