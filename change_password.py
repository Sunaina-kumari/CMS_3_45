from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql as pymysql
from detail_page import *

class  changePasswordClass:
    def __init__(self,pwindow,username):
        self.username = username
        self.window=Toplevel(pwindow)  # self.window acts as child class of homepage
        self.window.title(app_name+"//change Password")
        self.window.config(background='#C9C8FF')

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (w-100, h-200, 50, 100))

        self.headlbl = Label(self.window,text='change Password ',font=('Century725 Cn BT',50,'bold'))

        self.myfont=('Book Antiqua',15)
        self.L1 = Label(self.window,text='Current  Password',font=self.myfont)
        self.L2 = Label(self.window,text='New Password',font=self.myfont)
        self.L3 = Label(self.window,text='Confirm Password',font=self.myfont)

        self.t1=Entry(self.window,font=self.myfont,width=20,show='*')
        self.t2=Entry(self.window,font=self.myfont,width=20,show='*')
        self.t3=Entry(self.window,font=self.myfont,width=20,show='*')


        self.b1 = Button(self.window,text="Change Password ",font=self.myfont,command=self.save_data)


        #---------- placement------------------------
        self.headlbl.place(x=100,y=10)

        x1=100
        y1=100
        y_diff=50
        x_diff=200

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1+x_diff,y=y1)

        self.clearpage()
        self.window.mainloop()

    def database_connection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db="CMS_3_45_db", user="root", password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", "Error in database Connection\n"+str(e),parent=self.window)

    def save_data(self):

        if self.t2.get()==self.t3.get():
            self.database_connection()
            try:


                qry="update usertable set password=%s where username=%s and password=%s"
                row_count = self.curr.execute(qry,(self.t2.get(),self.username,self.t1.get()))
                self.conn.commit()
                if row_count==1:
                    messagebox.showinfo("Success","Password changed successfully",parent=self.window)
                    self.clearpage()
                else:
                    messagebox.showinfo("UnSuccessfull", "Password is incorrect", parent=self.window)

            except Exception as e:
                messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)
        else:

            messagebox.showwarning("Warning", "Confirm password carefully", parent=self.window)

    def clearpage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
if __name__ == '__main__':
    dummy_homepage = Tk()
    changePasswordClass(dummy_homepage,"simran")
    dummy_homepage.mainloop()