from tkinter import *
# from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class studentClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "white")
        self.root.focus_force()

##TITLE
        title = Label(self.root, text = "Manage Course Details", font = ("goudy old style", 20, "bold"), bg = "#033054", fg = "white").place(x = 10, y = 15, width = 1180, height = 35)

##Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        
##Widgets  
#column1
        lbl_rollno = Label(self.root, text = "Roll no", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 60)
        lbl_name = Label(self.root, text = "Name", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 100)
        lbl_email = Label(self.root, text = "Email", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 140)
        lbl_gender = Label(self.root, text = "Gender", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 180)
        lbl_state = Label(self.root, text = "State", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 220)
        lbl_address = Label(self.root, text = "Address", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 260)

##Entry Fields
        self.txt_roll = Entry(self.root, textvariable = self.var_roll, font = ("goudy old style", 15, "bold"), bg = "lightyellow")
        self.txt_roll.place(x = 200, y = 60, width = 200)
        txt_name = Entry(self.root, textvariable = self.var_name, font = ("goudy old style", 15, "bold"), bg = "lightyellow").place(x = 150, y = 100, width = 200)
        txt_email = Entry(self.root, textvariable = self.var_email, font = ("goudy old style", 15, "bold"), bg = "lightyellow").place(x = 150, y = 140, width = 200)
        self.txt_gender = ttk.Combobox(self.root, textvariable = self.var_gender, font = ("goudy old style", 15, "bold"),state='readonly',justify=CENTER,values=("select","male","female","other"))
        self.txt_gender.place(x = 150, y = 180, width = 200)
        self.txt_gender.current(0)
        self.txt_address = Text(self.root, font = ("goudy old style", 15, "bold"), bg = "lightyellow")
        self.txt_address.place(x = 150, y = 250, width = 500, height = 100)

#column2
        lbl_rollno = Label(self.root, text = "Roll no", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 60)
        lbl_name = Label(self.root, text = "Name", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 100)
        lbl_email = Label(self.root, text = "Email", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 140)
        lbl_gender = Label(self.root, text = "Gender", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 180)

##Entry Fields
        self.txt_roll = Entry(self.root, textvariable = self.var_roll, font = ("goudy old style", 15, "bold"), bg = "lightyellow")
        self.txt_roll.place(x = 200, y = 60, width = 200)
        txt_name = Entry(self.root, textvariable = self.var_name, font = ("goudy old style", 15, "bold"), bg = "lightyellow").place(x = 150, y = 100, width = 200)
        txt_email = Entry(self.root, textvariable = self.var_email, font = ("goudy old style", 15, "bold"), bg = "lightyellow").place(x = 150, y = 140, width = 200)
        self.txt_gender = ttk.Combobox(self.root, textvariable = self.var_gender, font = ("goudy old style", 15, "bold"),state='readonly',justify=CENTER,values=("select","male","female","other"))
        self.txt_gender.place(x = 150, y = 180, width = 200)
        self.txt_gender.current(0)


##Buttons
        self.btn_add = Button(self.root, text = "Save", font = ("goudy old style", 15, "bold"), bg = "#2196f3", fg = "white", cursor = "hand2",command=self.add)
        self.btn_add.place(x = 200, y = 400, width = 110, height = 40)
        self.btn_update = Button(self.root, text = "Update", font = ("goudy old style", 15, "bold"), bg = "#4caf50", fg = "white", cursor = "hand2",command=self.update)
        self.btn_update.place(x = 320, y = 400, width = 110, height = 40)
        self.btn_delete = Button(self.root, text = "Delete", font = ("goudy old style", 15, "bold"), bg = "#f44336", fg = "white", cursor = "hand2",command=self.delete)
        self.btn_delete.place(x = 440, y = 400, width = 110, height = 40)
        self.btn_clear = Button(self.root, text = "Clear", font = ("goudy old style", 15, "bold"), bg = "#607d8b", fg = "white", cursor = "hand2",command=self.clear)
        self.btn_clear.place(x = 560, y = 400, width = 110, height = 40)

##Search Panel
        self.var_search = StringVar()
        lbl_search_courseName = Label(self.root, text = "Course Name", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 720, y = 60)
        txt_search_courseName = Entry(self.root, textvariable = self.var_search, font = ("goudy old style", 15, "bold"), bg = "lightyellow").place(x = 870, y = 60, width = 180)
        btn_search = Button(self.root, text = "Search", font = ("goudy old style", 15, "bold"), bg = "#2196f3", fg = "white", cursor = "hand2",command=self.search).place(x = 1070, y = 60, width = 120, height = 28)

##Content
        self.C_Frame = Frame(self.root, bd = 2, relief = RIDGE)
        self.C_Frame.place(x = 720, y = 100, width = 470, height = 340)    

        scrolly = Scrollbar(self.C_Frame, orient = VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient = HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns = ("cid", "name", "duration", "charges", "description"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.CourseTable.xview)
        scrolly.config(command = self.CourseTable.yview)

        self.CourseTable.heading("cid", text = "Course ID")
        self.CourseTable.heading("name", text = "Name")        
        self.CourseTable.heading("duration", text = "Duration")
        self.CourseTable.heading("charges", text = "Charges")
        self.CourseTable.heading("description", text = "Description")   
        self.CourseTable["show"] = "headings"   
        self.CourseTable.column("cid", width = 100)
        self.CourseTable.column("name", width = 100)        
        self.CourseTable.column("duration", width = 100)
        self.CourseTable.column("charges", width = 100)
        self.CourseTable.column("description", width = 150)   
 
        self.CourseTable.pack(fill = BOTH, expand = 1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

def search(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute("select * from course where roll=?",(self.var_search.get(),))
        row=cur.fetchone()
        if row!=None:
            self.CourseTable.delete(*self.CourseTable.get_children())
            self.CourseTable.insert('',END,values=row)
        else:
            messagebox.showerror("Error","No record found",parent=self.root)
    except Exception as ex:
        messagebox. showerror ("Error",f"Error due to {str(ex)}")


def clear(self):
    self.show()
    self.var_roll.set("")
    self.var_name.set("")
    self.var_email.set("")
    self.var_gender.set("")
    self.var_dob.set("")
    self.var_contact.set("")
    self.var_a_date.set("")
    self.var_course.set("")
    self.var_state.set("")
    self.var_city.set("")
    self.var_pin.set("")
    self.txt_address.delete("1.0",END)
    self.txt_roll.config(state=NORMAL)
    self.var_search.set("")

def delete(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if self.var_roll.get()=="":
            messagebox.showerror("Error", "Roll number is required",parent=self.root)
        else:
            cur.execute("select * from course where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","please select student from the list",parent=self.root)
            else:
                op=messagebox.askyesno("confirm","Do you really want to delete the course",parent=self.root)
                if op==True:
                    cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                    cur.commit()
                    messagebox.showinfo("Delete","student deleted successfully")
                    self.clear()
    except Exception as ex:
        messagebox. showerror ("Error",f"Error due to {str(ex)}")

def get_data(self,ev):
    self.txt_roll.config(state="readonly")
    self.txt_roll
    r=self.CourseTable.focus()
    content=self.CourseTable.item(r)
    row=content["values"]
    self.var_roll.set(row[0])
    self.var_name.set(row[1])
    self.var_email.set(row[2])
    self.var_gender.set(row[3])
    self.var_dob.set(row[4])
    self.var_contact.set(row[5])
    self.var_a_date.set(row[6])
    self.var_course.set(row[7])
    self.var_state.set(row[8])
    self.var_city.set(row[9])
    self.var_pin.set(row[10])
    self.txt_address.delete('1',END)
    self.txt.address.insert(END,row[11])


def add(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if self.var_roll.get()=="":
            messagebox.showerror("Error", "Course Name should be required",parent=self.root)
        else:
            cur.execute("select * from course where name=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Course Name already present",parent=self.root)
            else:
                cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                    self.var_roll.get(),
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0",END)
                ))
                con.commit()
                messagebox.showinfo("Success","course added successfully",parent=self.root)
    except Exception as ex:
        messagebox. showerror ("Error",f"Error due to {str(ex)}")

def update(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if self.var_roll.get()=="":
            messagebox.showerror("Error", "Course Name should be required",parent=self.root)
        else:
            cur.execute("select * from course where name=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","select course from list",parent=self.root)
            else:
                cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0",END),
                    self.var_roll.get()
                ))
                con.commit()
                messagebox.showinfo("Success","course updated successfully",parent=self.root)
    except Exception as ex:
        messagebox. showerror ("Error",f"Error due to {str(ex)}")

def show(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute("select * from course")
        rows=cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
            self.CourseTable.insert('',END,values=row)
    except Exception as ex:
        messagebox. showerror ("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
