from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql as pymysql
from tkcalendar import DateEntry

from detail_page import *


class addstudentClass:
    def __init__(self,pwindow):
        # self.window = Tk()    # create independent window
        # self.window=pwindow  # self.window became homepage
        self.window=Toplevel(pwindow)  # self.window acts as child classs of homepage
        self.window.title(app_name + "//Add student")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (w-100, h-200, 50, 100))

        self.headlbl = Label(self.window,text='Add Student',font=('Century725 Cn BT',50,'bold'))

        self.myfont=('Book Antiqua',15)
        self.L1 = Label(self.window,text='Rollno',font=self.myfont)
        self.L2 = Label(self.window,text='Name',font=self.myfont)
        self.L3 = Label(self.window,text='Phone',font=self.myfont)
        self.L4 = Label(self.window,text='Gender',font=self.myfont)
        self.L5 = Label(self.window,text='DOB',font=self.myfont)
        self.L6 = Label(self.window,text='Address',font=self.myfont)
        self.L7 = Label(self.window,text='Department',font=self.myfont)
        self.L8 = Label(self.window,text='Course',font=self.myfont)

        self.t1=Entry(self.window,width=20,font=self.myfont)
        self.t2=Entry(self.window,font=self.myfont)
        self.t3=Entry(self.window,font=self.myfont)

        self.v1 = StringVar()
        self.r1=Radiobutton(self.window,text='Female',value='f',variable=self.v1,font=self.myfont)
        self.r2=Radiobutton(self.window,text='Male',value='m',variable=self.v1,font=self.myfont)
        self.v1.set(" ")


        self.t5=DateEntry(self.window, width=20, background='darkblue', foreground='white', borderwidth=2, year=2010,
                          font=self.myfont,date_pattern='y-mm-dd')
        self.t6=Text(self.window,width=20,height=3,font=self.myfont)

        self.v2=StringVar()
        self.c1=Combobox(self.window,values=('IT','Commerce'),textvariable=self.v2,state='readonly',font=self.myfont)


        self.v3=StringVar()
        self.c2=Combobox(self.window,values=('BCA','Bcom','MCA'),textvariable=self.v3,state='readonly',font=self.myfont)


        self.b1 = Button(self.window,text="Save",font=self.myfont,command=self.save_data)

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
        self.t3.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L4.place(x=x1,y=y1)
        self.r1.place(x=x1+x_diff,y=y1)
        self.r2.place(x=x1+x_diff+x_diff,y=y1)

        y1+=y_diff
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L6.place(x=x1,y=y1)
        self.t6.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        y1+=y_diff
        self.L7.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L8.place(x=x1,y=y1)
        self.c2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.b1.place(x=x1,y=y1)

        self.clearpage()
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
            #rollno	name	phone	gender	dob	address	dept	course
            qry="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)"
            row_count = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.t3.get(),self.v1.get(),
                        self.t5.get_date(),self.t6.get('1.0',END).strip() , self.v2.get(),self.v3.get()))
            self.conn.commit()
            if row_count==1:
                messagebox.showinfo("Success","Student Record saved successfully",parent=self.window)
                self.clearpage()
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)

    def clearpage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.v1.set(None)
        self.t5.delete(0,END)
        self.t6.delete('1.0',END)
        self.c1.set("Choose Department")
        self.c2.set("Choose Course")





if __name__ == '__main__':
    dummy_homepage = Tk()
    addstudentClass(dummy_homepage)
    dummy_homepage.mainloop()