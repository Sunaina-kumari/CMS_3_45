import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql as pymysql
from tkcalendar import DateEntry
from detail_page import *
from printout import my_cust_PDF


class report1Class:
    def __init__(self,pwindow):
        self.window=Toplevel(pwindow)  # self.window acts as child classs of homepage
        self.window.title(app_name + "//Student Record")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (w-100, h-200, 50, 100))

        self.headlbl = Label(self.window,text='All Student Record',font=('Century725 Cn BT',50,'bold'))

        self.myfont=('Book Antiqua',15)

        self.tablearea = Frame(self.window)
        self.mytable=Treeview(self.tablearea,columns=('c1','c2','c3','c4','c5','c6','c7','c8'),height=20)

        self.mytable.heading('c1',text='Rollno')
        self.mytable.heading('c2',text='Name')
        self.mytable.heading('c3',text='Phone')
        self.mytable.heading('c4',text='Gender')
        self.mytable.heading('c5',text='DOB')
        self.mytable.heading('c6',text='Address')
        self.mytable.heading('c7',text='Department')
        self.mytable.heading('c8',text='Course')

        self.mytable['show']='headings'

        self.mytable.column("#1",width=100,anchor='e')  #n, ne, e, se, s, sw, w, nw, or center
        self.mytable.column("#2",width=200,anchor='center')
        self.mytable.column("#3",width=200,anchor='center')
        self.mytable.column("#4",width=130,anchor='center')
        self.mytable.column("#5",width=130,anchor='center')
        self.mytable.column("#6",width=200,anchor='center')
        self.mytable.column("#7",width=200,anchor='center')
        self.mytable.column("#8",width=200,anchor='center')

        self.mytable.pack()

        self.b1=Button(self.window,text='Print',command=self.get_printout,font=('Book Antiqua',15))

        #---------- placement------------------------
        self.headlbl.place(x=500,y=10)

        x1=70
        y1=100
        y_diff=50
        x_diff=150

        self.tablearea.place(x=x1,y=y1)
        self.b1.place(x=x1+500,y=y1+500)
        self.fetch_all_stu_data()
        self.window.mainloop()

    def get_printout(self):
        pdf = my_cust_PDF()


        pdf.print_chapter(self.print_data)
        os.remove('pdf_file1.pdf')
        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')


    def database_connection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db="CMS_3_45_db", user="root", password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", "Error in database Connection\n"+str(e),parent=self.window)

    def fetch_all_stu_data(self):
        self.database_connection()
        try:
            # rollno	name	phone	gender	dob	address	dept	course
            qry = "select * from student"
            row_count = self.curr.execute(qry )
            data = self.curr.fetchall()
            self.print_data=[]

            if data:
                for row in data:
                    self.print_data.append(row[:-1])
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showinfo("Empty!!", "No Stduent Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)

if __name__ == '__main__':
    dummy_homepage = Tk()
    report1Class(dummy_homepage)
    dummy_homepage.mainloop()