from tkinter import *
from tkinter import messagebox
import pymysql as pymysql

from detail_page import *
class  loginClass:
    def __init__(self ):
        self.window=Tk()
        self.window.title(app_name+"//Login")
        self.window.config(background='#C9C8FF')

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)
        self.window.maxsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (600, 400, 400, 200))


        #------------ background image---------------------

        from PIL import ImageTk, Image
        self.bimg1 = Image.open("myimages//bg1.jpg")
        self.bimg1 = self.bimg1.resize((600,400))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bglbl=Label(self.window,image=self.bimg2)
        self.bglbl.place(x=0,y=0)

        #-------------------------------------------------












        self.headlbl = Label(self.window,text=' Login  to '+app_name,font=('Century725 Cn BT',50,'bold'))

        self.myfont=('Book Antiqua',15)
        self.L1 = Label(self.window,text='Username',font=self.myfont)
        self.L2 = Label(self.window,text='Password',font=self.myfont)

        self.t1=Entry(self.window,font=self.myfont,width=20)
        self.t2=Entry(self.window,font=self.myfont,width=20,show='*')

        self.b1 = Button(self.window,text="Let me in!!",font=self.myfont,command=self.check_data)


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
        self.b1.place(x=x1,y=y1)

        self.window.mainloop()

    def database_connection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db="CMS_3_45_db", user="root", password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", "Error in database Connection\n"+str(e),parent=self.window)

    def check_data(self):
        self.database_connection()
        try:
            qry = "select * from usertable where username= %s and password=%s"
            row_count = self.curr.execute(qry ,(self.t1.get(),self.t2.get()))
            data = self.curr.fetchone()

            if data:
                ut=data[2]
                un=data[0]
                self.window.destroy()
                from Homepage import HomepageClass
                HomepageClass(ut,un)
            else:

                messagebox.showwarning("Login Failed", " Wrong Username or password ", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)


if __name__ == '__main__':
    loginClass( )