from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
import pymysql as pymysql
from tkcalendar import DateEntry

from PIL import ImageTk,Image

from detail_page import *

class  studentClass:
    default_name="default_user.png"
    def __init__(self,pwindow):
        # self.window = Tk()    # create independent window
        # self.window=pwindow  # self.window became homepage
        self.window=Toplevel(pwindow)  # self.window acts as child class of homepage
        self.window.title(app_name+"//student")
        self.window.config(background='#C9C8FF')

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        # method 1
        self.window.minsize(600, 400)

        # method 2
        self.window.geometry("%dx%d+%d+%d" % (w-100, h-200, 50, 100))



        #------------ background image---------------------

        from PIL import ImageTk, Image
        self.bimg1 = Image.open("myimages//bg1.jpg")
        self.bimg1 = self.bimg1.resize((w,h))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bglbl=Label(self.window,image=self.bimg2)
        self.bglbl.place(x=0,y=0)

        #-------------------------------------------------






        self.headlbl = Label(self.window,text='Student',font=('Century725 Cn BT',50,'bold'),background='pink')

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
        self.c1=Combobox(self.window ,textvariable=self.v2,state='readonly',font=self.myfont)
        self.c1.bind("<<ComboboxSelected>>",lambda e: self.fetch_all_courses())

        self.v3=StringVar()
        self.c2=Combobox(self.window ,textvariable=self.v3,state='readonly',font=self.myfont)

        self.imglbl=Label(self.window,borderwidth=10,relief='groove')

        self.b1 = Button(self.window,text="Save",font=self.myfont,command=self.save_data)
        self.b2 = Button(self.window,text="Update",font=self.myfont,command=self.update_data)
        self.b3 = Button(self.window,text="Delete",font=self.myfont,command=self.delete_data )
        self.b4 = Button(self.window,text="Fetch",font=self.myfont ,command=self.fetch_data)
        self.b5 = Button(self.window,text="Search",font=self.myfont,command=self.fetch_all_stu_data)

        self.b6 = Button(self.window,text="Upload",font=self.myfont ,command=self.open_image_option)

        #-------------------- table------------------------------
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea, columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'), height=10)

        self.mytable.heading('c1', text='Rollno')
        self.mytable.heading('c2', text='Name')
        self.mytable.heading('c3', text='Phone')
        self.mytable.heading('c4', text='Gender')
        self.mytable.heading('c5', text='DOB')
        self.mytable.heading('c6', text='Address')
        self.mytable.heading('c7', text='Department')
        self.mytable.heading('c8', text='Course')

        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=80, anchor='e')  # n, ne, e, se, s, sw, w, nw, or center
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=100, anchor='center')
        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=100, anchor='center')
        self.mytable.column("#7", width=100, anchor='center')
        self.mytable.column("#8", width=100, anchor='center')
        self.mytable.bind("<ButtonRelease-1>",lambda e: self.fetch_pk())

        self.mytable.pack()
        #---------- placement------------------------
        self.headlbl.place(x=100,y=10)

        x1=100
        y1=100
        y_diff=50
        x_diff=150

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
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
        self.r1.place(x=x1+x_diff,y=y1)
        self.r2.place(x=x1+x_diff+x_diff,y=y1)

        y1+=y_diff
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L6.place(x=x1,y=y1)
        self.t6.place(x=x1+x_diff,y=y1)


        y1+=y_diff

        self.imglbl.place(x=x1+500,y=y1,height=150,width=150)
        self.b6.place(x=x1+500,y=y1+150,width=150)
        y1+=y_diff
        self.L7.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L8.place(x=x1,y=y1)
        self.c2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.b1.place(x=x1,y=y1)
        self.b2.place(x=x1+x_diff,y=y1)
        self.b3.place(x=x1+x_diff+x_diff,y=y1)

        self.clearpage()
        self.fetch_all_dept()
        self.window.mainloop()

    def open_image_option(self):
        self.filename = askopenfilename(file = ( ("All Images","*.jpg;*.png;*.jpeg" ),("PNG images","*.png"),("JPG Images","*.jpg")))
        print("filename = ",self.filename)
        if self.filename!="":
            self.img1 = Image.open(self.filename)
            self.img1 = self.img1.resize((150,150))

            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)


            path = self.filename.split("/")
            name = path[-1]
            import time
            uniqueness = str(round(time.time()))
            self.actual_name = uniqueness+name


    def database_connection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db="CMS_3_45_db", user="root", password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", "Error in database Connection\n"+str(e),parent=self.window)

    def save_data(self):
        if self.validate_check()==False:
            return

        if self.actual_name==self.default_name: # no image is selected
            # nothoing to save in folder
            pass
        else: # new image is selected
            self.img1.save("stu_images//"+self.actual_name)

        self.database_connection()
        try:
            #rollno	name	phone	gender	dob	address	dept	course
            qry="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            row_count = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.t3.get(),self.v1.get(),
                        self.t5.get_date(),self.t6.get('1.0',END).strip() , self.v2.get(),self.v3.get(),
                        self.actual_name))
            self.conn.commit()
            if row_count==1:
                messagebox.showinfo("Success","Student Record saved successfully",parent=self.window)
                self.clearpage()
            else:
                messagebox.showinfo("UnSuccessfull", "Student Record not inserted successfully\n check all fields", parent=self.window)

        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)

    def update_data(self):
        if self.validate_check()==False:
            return
        self.database_connection()

        if self.actual_name==self.old_name: # no new image is selected
                #nothing to delete or save in folder
                pass
        else: #some new image is selected
            self.img1.save("stu_images//" + self.actual_name)
            if self.old_name==self.default_name: #no old image was given
                #nothing to delete
                pass
            else: #some image was given in past
                import os
                os.remove("stu_images//"+self.old_name)




        try:
            #rollno	name	phone	gender	dob	address	dept	course
            qry="update student set name=%s, phone=%s, gender=%s, dob=%s, address=%s, dept=%s, course=%s ,pic=%swhere rollno=%s"
            row_count = self.curr.execute(qry,(self.t2.get(),self.t3.get(),self.v1.get(),
                        self.t5.get_date(),self.t6.get('1.0',END).strip() , self.v2.get(),self.v3.get(),self.actual_name,self.t1.get()))
            self.conn.commit()
            if row_count==1:
                messagebox.showinfo("Success","Student Record updated successfully",parent=self.window)
                self.clearpage()
            else:
                messagebox.showinfo("UnSuccessfull", "Student Record not updated successfully\n update some fields first", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)

    def delete_data(self):
        self.database_connection()
        if self.old_name == self.default_name:  # no old image was given
            # nothing to delete
            pass
        else:  # some image was given in past
            import os
            os.remove("stu_images//" + self.old_name)
        ans = messagebox.askquestion("Confirmation","Are you sure to delete??",parent=self.window)
        if ans=='yes':
            try:
                #rollno	name	phone	gender	dob	address	dept	course
                qry="delete from student where rollno=%s"
                row_count = self.curr.execute(qry,( self.t1.get()))
                self.conn.commit()
                if row_count==1:
                    messagebox.showinfo("Success","Student Record deleted successfully",parent=self.window)
                    self.clearpage()
                else:
                    messagebox.showinfo("UnSuccessfull", "Student Record not deleted successfully\n check all fields", parent=self.window)
            except Exception as e:
                messagebox.showerror("Error", "Error in insertion query \n"+str(e),parent=self.window)

    def fetch_pk(self):
        row_id =  self.mytable.focus()
        # print("row - id = ",row_id)
        content = self.mytable.item(row_id)
        # print("content = ",content)
        myvalues = content['values']
        # print("myvalues = ",myvalues)
        pk_col = myvalues[0]
        # print("rollno = ",pk_col)
        self.fetch_data(pk_col)

    def fetch_data(self,rollno=None):

        if rollno==None:
            r = self.t1.get()
        else:
            r=rollno

        self.database_connection()
        try:
            # rollno	name	phone	gender	dob	address	dept	course
            qry = "select * from student where rollno =%s"
            row_count = self.curr.execute(qry, (r ))
            data = self.curr.fetchone()
            # print("data = ",data)
            self.clearpage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.v1.set(data[3])
                self.t5.set_date(data[4])
                self.t6.insert('1.0',data[5])
                self.c1.set(data[6])
                self.c2.set(data[7])

                self.actual_name=data[8]
                self.old_name=self.actual_name

                self.img1 = Image.open("stu_images//" + self.actual_name)
                self.img1 = self.img1.resize((150, 150))

                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)


                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'
            else:
                messagebox.showinfo("Empty!!", "No Stduent Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)

    def fetch_all_stu_data(self):
        self.database_connection()
        self.mytable.delete(*self.mytable.get_children())
        try:
            qry = "select * from student where name like %s"
            row_count = self.curr.execute(qry ,(self.t2.get()+"%"))
            data = self.curr.fetchall()

            if data:
                for row in data:
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showinfo("Empty!!", "No Stduent Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)

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

    def fetch_all_courses(self):
        self.database_connection()
        try:
            qry = "select * from course where dname = %s "
            row_count = self.curr.execute(qry,(self.v2.get()))
            data = self.curr.fetchall()
            mycombobox_list=[]
            if data:
                for row in data:
                    mycombobox_list.append(row[1])
                self.c2.set("Choose Course")

            else:
                self.c2.set("No Course")

            self.c2.config(values=mycombobox_list)
        except Exception as e:
            messagebox.showerror("Error", "Error in insertion query \n" + str(e), parent=self.window)

    def clearpage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.v1.set(None)
        self.t5.delete(0,END)
        self.t6.delete('1.0',END)
        self.c1.set("Choose Department")
        self.c2.set("No Course")
        self.b2['state']='disabled'
        self.b3['state']='disabled'
        self.fetch_all_stu_data()

        self.actual_name=self.default_name
        self.img1 = Image.open("stu_images//"+self.default_name)
        self.img1 = self.img1.resize((150, 150))

        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

    def validate_check(self):
        if not(self.t1.get().isdigit()):
            messagebox.showwarning("Validation Check", "Invalid Roll no", parent=self.window)
            return False
        elif (self.t2.get().isdigit())   or  len(self.t2.get())<3:
            messagebox.showwarning("Validation Check", "Enter proper name (atleast 3 chracters) ", parent=self.window)
            return False

        elif not(self.t3.get().isdigit())   or  len(self.t3.get())!=10:
            messagebox.showwarning("Validation Check", "Enter valid phone no \n10 digits only", parent=self.window)
            return False
        elif self.v1.get() != 'm' and self.v1.get() != 'f':
            messagebox.showwarning("Input Error", "Please Select gender ", parent=self.window)
            return False
        elif (self.t5.get() == ""):
            messagebox.showwarning("Input Error", "Please Select DOB ", parent=self.window)
            return False
        elif len(self.t6.get('1.0', END)) < 3:
            messagebox.showwarning("Input Error", "Please Enter Address ", parent=self.window)
            return False
        elif (self.v2.get() == "Choose Department")or (self.v2.get() == "No Department"):
            messagebox.showwarning("Input Error", "Please Select Department ", parent=self.window)
            return False

        elif (self.v3.get() == "Choose Course") or (self.v3.get() == "No Course"):
            messagebox.showwarning("Input Error", "Please Select Course ", parent=self.window)
            return False

        return True

if __name__ == '__main__':
    dummy_homepage = Tk()
    studentClass(dummy_homepage)
    dummy_homepage.mainloop()