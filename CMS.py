from tkinter import messagebox

import pymysql

from loginpage import loginClass
from manageradmin import adminClass
class  mainpageClass:
    def __init__(self ):
        self.database_connection()
        try:
            myqry = "select * from usertable "
            row_count = self.curr.execute(myqry)
            data = self.curr.fetchall()

            if data:
                #some already opened this
                loginClass()
            else:
                adminClass()

        except Exception as e:
            messagebox.showerror("Error", "Error in fetch query \n" + str(e) )



    def database_connection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db="CMS_3_45_db", user="root", password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", "Error in database Connection\n"+str(e) )


if __name__ == '__main__':
    mainpageClass( )