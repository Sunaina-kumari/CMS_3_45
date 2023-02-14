from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql as pymysql
from detail_page import *
class  adminClass:
    def __init__(self ):
        self.window=Tk()
        self.window.title(app_name+"//Create User")
        self.window.config(background='#C9C8FF')

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (600,400,300,200))

        self.headlbl = Label(self.window,text='Welcome to '+app_name,font=('Century725 Cn BT',50,'bold'))

        self.myfont=('Book Antiqua',15)
        self.L1 = Label(self.window,text='Username',font=self.myfont)
        self.L2 = Label(self.window,text='Password',font=self.myfont)
        self.L3 = Label(self.window,text='User Type',font=self.myfont)

        self.t1=Entry(self.window,font=self.myfont,width=20)
        self.t2=Entry(self.window,font=self.myfont,width=20,show='*')
        self.v1=StringVar()
        self.c1=Combobox(self.window ,textvariable=self.v1,state='disabled',font=self.myfont,values=("Admin","Employee"),width=18)
        self.c1.current(0)

        self.b1 = Button(self.window,text="Create Admin",font=self.myfont,command=self.save_data)


        #---------- placement------------------------
        self.headlbl.place(x=100,y=10)

        x1=100
        y1=100
        y_diff=50
        x_diff=150

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1)

        self.window.mainloop()

    def database_connection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db="CMS_3_45_db", user="root", password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", "Error in database Connection\n"+str(e),parent=self.window)


    def save_data(self):
        self.database_connection()
        try:
            #username	password	usertype

            qry="insert into usertable values(%s,%s,%s)"
            row_count = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.v1.get()))
            self.conn.commit()
            if row_count==1:
                messagebox.showinfo("Success","Admin Created successfully",parent=self.window)
                self.window.destroy()
                from loginpage import loginClass
                loginClass()

            else:
                messagebox.showinfo("UnSuccessfull", "  Record not inserted successfully\n check all fields", parent=self.window)

        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)


if __name__ == '__main__':
    adminClass( )