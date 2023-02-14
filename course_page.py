from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql as pymysql
from tkcalendar import DateEntry

from detail_page import *

class  courseClass:
    def __init__(self,pwindow):
        # self.window = Tk()    # create independent window
        # self.window=pwindow  # self.window became homepage
        self.window=Toplevel(pwindow)  # self.window acts as child class of homepage
        self.window.title(app_name+"//Course")
        self.window.config(background='#C9C8FF')

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (w-100, h-200, 50, 100))

        self.headlbl = Label(self.window,text='Course',font=('Century725 Cn BT',50,'bold'))

        self.myfont=('Book Antiqua',15)
        self.L1 = Label(self.window,text='Department Name',font=self.myfont)
        self.L2 = Label(self.window,text='Course Name',font=self.myfont)
        self.L3 = Label(self.window,text='Fee',font=self.myfont)
        self.L4 = Label(self.window,text='Duaration',font=self.myfont)


        self.v2 = StringVar()
        self.c1 = Combobox(self.window, values=('IT', 'Commerce'), textvariable=self.v2,
                           state='readonly', font=self.myfont)
        self.t2=Entry(self.window,font=self.myfont)
        self.t3=Entry(self.window,font=self.myfont)
        self.t4=Entry(self.window,font=self.myfont)




        self.b1 = Button(self.window,text="Save",font=self.myfont,command=self.save_data)
        self.b2 = Button(self.window,text="Update",font=self.myfont )
        self.b3 = Button(self.window,text="Delete",font=self.myfont )
        self.b4 = Button(self.window,text="Fetch",font=self.myfont  )
        self.b5 = Button(self.window,text="Search",font=self.myfont)

        #-------------------- table------------------------------
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea, columns=('c1', 'c2', 'c3', 'c4'), height=20)

        self.mytable.heading('c1', text='Department')
        self.mytable.heading('c2', text='Course Name')
        self.mytable.heading('c3', text='Fee')
        self.mytable.heading('c4', text='Duration')

        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=100, anchor='center')  # n, ne, e, se, s, sw, w, nw, or center
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=100, anchor='center')

        self.mytable.pack()
        #---------- placement------------------------
        self.headlbl.place(x=100,y=10)

        x1=100
        y1=100
        y_diff=50
        x_diff=200

        self.L1.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        self.b4.place(x=x1+x_diff+x_diff+60,y=y1,height=30)
        self.tablearea.place(x=x1+x_diff+x_diff+x_diff ,y=y1 )

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff+x_diff+60,y=y1,height=30)

        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L4.place(x=x1,y=y1)
        self.t4.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1)
        self.b2.place(x=x1+x_diff,y=y1)
        self.b3.place(x=x1+x_diff+x_diff,y=y1)

        self.clearpage()
        self.fetch_all_dept()
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
            #dname	cname	fee	duration

            qry="insert into course values(%s,%s,%s,%s)"
            row_count = self.curr.execute(qry,(self.v2.get(),self.t2.get(),self.t3.get(),self.t4.get() ))
            self.conn.commit()
            if row_count==1:
                messagebox.showinfo("Success","Course Record saved successfully",parent=self.window)
                self.clearpage()
            else:
                messagebox.showinfo("UnSuccessfull", "Course Record not inserted successfully\n check all fields", parent=self.window)

        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)


    def fetch_all_dept(self):
        self.database_connection()
        try:
            qry = "select * from department "
            row_count = self.curr.execute(qry)
            data = self.curr.fetchall()
            mycombobox_list=[]
            if data:
                for row in data:
                    mycombobox_list.append(row[0])
                self.c1.set("Choose Department")
                self.c1.config(values=mycombobox_list)

            else:
                self.c1.set("No Department")
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)

    def clearpage(self):
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.t4.delete(0,END)
        self.c1.set("Choose Department")
        self.b2['state']='disabled'
        self.b3['state']='disabled'
        # self.fetch_all_stu_data()





if __name__ == '__main__':
    dummy_homepage = Tk()
    courseClass(dummy_homepage)
    dummy_homepage.mainloop()