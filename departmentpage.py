from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql as pymysql
from tkcalendar import DateEntry
from detail_page import *
class  deptClass:
    def __init__(self,pwindow):
        self.window=Toplevel(pwindow)  # self.window acts as child class of homepage
        self.window.title(app_name+"//Department")
        self.window.config(background='#C9C8FF')

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (w-100, h-200, 50, 100))

        self.headlbl = Label(self.window,text='Department',font=('Century725 Cn BT',50,'bold'))

        self.myfont=('Book Antiqua',15)
        self.L1 = Label(self.window,text='Department Name',font=self.myfont)
        self.L2 = Label(self.window,text='Head of Department',font=self.myfont)

        self.t1=Entry(self.window,font=self.myfont)
        self.t2=Entry(self.window,font=self.myfont)

        self.b1 = Button(self.window,text="Save",font=self.myfont,command=self.save_data)
        self.b2 = Button(self.window,text="Update",font=self.myfont,command=self.update_data)
        self.b3 = Button(self.window,text="Delete",font=self.myfont,command=self.delete_data )
        self.b4 = Button(self.window,text="Fetch",font=self.myfont ,command=self.fetch_data)
        self.b5 = Button(self.window,text="Search",font=self.myfont,command=self.fetch_all_stu_data)

        #-------------------- table------------------------------
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea, columns=('c1', 'c2' ), height=20)

        self.mytable.heading('c1', text='Department Name')
        self.mytable.heading('c2', text='Head of Department')

        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=200, anchor='center')  # n, ne, e, se, s, sw, w, nw, or center
        self.mytable.column("#2", width=200, anchor='center')
        self.mytable.bind("<ButtonRelease-1>",lambda e: self.fetch_pk())

        self.mytable.pack()
        #---------- placement------------------------
        self.headlbl.place(x=100,y=10)

        x1=100
        y1=100
        y_diff=50
        x_diff=300

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        self.b4.place(x=x1+x_diff+x_diff+60,y=y1,height=30)
        self.tablearea.place(x=x1+x_diff+x_diff+x_diff ,y=y1 )

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff+x_diff+60,y=y1,height=30)

        y1+=y_diff
        self.b1.place(x=x1,y=y1)
        self.b2.place(x=x1+x_diff,y=y1)
        self.b3.place(x=x1+x_diff+x_diff,y=y1)

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
            qry="insert into department values(%s,%s)"
            row_count = self.curr.execute(qry,(self.t1.get(),self.t2.get()))
            self.conn.commit()
            if row_count==1:
                messagebox.showinfo("Success","Department Record saved successfully",parent=self.window)
                self.clearpage()
            else:
                messagebox.showinfo("UnSuccessfull", "Department Record not inserted successfully\n check all fields", parent=self.window)

        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)

    def update_data(self):
        self.database_connection()
        try:
            #dname	head_of_dept

            qry="update department set head_of_dept=%s where dname=%s"
            row_count = self.curr.execute(qry,(self.t2.get(),self.t1.get()))
            self.conn.commit()
            if row_count==1:
                messagebox.showinfo("Success","Department Record updated successfully",parent=self.window)
                self.clearpage()
            else:
                messagebox.showinfo("UnSuccessfull", "Department Record not updated successfully\n update some fields first", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)

    def delete_data(self):
        self.database_connection()
        ans = messagebox.askquestion("Confirmation","Are you sure to delete??",parent=self.window)
        if ans=='yes':
            try:
                #rollno	name	phone	gender	dob	address	dept	course
                qry="delete from Department where dname=%s"
                row_count = self.curr.execute(qry,( self.t1.get()))
                self.conn.commit()
                if row_count==1:
                    messagebox.showinfo("Success","Department Record deleted successfully",parent=self.window)
                    self.clearpage()
                else:
                    messagebox.showinfo("UnSuccessfull", "Department Record not deleted successfully\n check all fields", parent=self.window)
            except Exception as e:
                messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)

    def fetch_pk(self):
        row_id =  self.mytable.focus()
        content = self.mytable.item(row_id)
        myvalues = content['values']
        pk_col = myvalues[0]
        self.fetch_data(pk_col)

    def fetch_data(self,pk=None):

        if pk==None:
            r = self.t1.get()
        else:
            r=pk

        self.database_connection()
        try:
            # rollno	name	phone	gender	dob	address	dept	course
            qry = "select * from department where dname =%s"
            row_count = self.curr.execute(qry, (r ))
            data = self.curr.fetchone()
            # print("data = ",data)
            self.clearpage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])

                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'
            else:
                messagebox.showinfo("Empty!!", "No Department Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)

    def fetch_all_stu_data(self):
        self.database_connection()
        self.mytable.delete(*self.mytable.get_children())
        try:
            qry = "select * from Department where head_of_dept like %s"
            row_count = self.curr.execute(qry ,(self.t2.get()+"%"))
            data = self.curr.fetchall()

            if data:
                for row in data:
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showinfo("Empty!!", "No Department Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)
    def clearpage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.b2['state']='disabled'
        self.b3['state']='disabled'
        self.fetch_all_stu_data()
if __name__ == '__main__':
    dummy_homepage = Tk()
    deptClass(dummy_homepage)
    dummy_homepage.mainloop()