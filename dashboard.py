from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from result import resultClass
from report import reportClass
class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1450x700+0+0")
        self.root.config(bg = "white")
##ICON (Image Upload)
        self.logo_dash = ImageTk.PhotoImage(file = "download.jpg")
##TITLE
        title = Label(self.root, text = "Student Result Managemnet System", padx = 10, compound = LEFT, image = self.logo_dash, font = ("goudy old style", 20, "bold"), bg = "#033054", fg = "white").place(x = 0, y = 0, relwidth = 1, height = 50)
##Menu
        M_Frame = LabelFrame(self.root, text = "Menus", font = ("times new roman", 15), bg = "white")
        M_Frame.place(x = 10, y = 70, width = 1400, height = 80)
##Buttons
        btn_Course = Button(M_Frame, text = "Course", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2", command = self.add_course).place(x = 20, y = 5, width = 200, height = 40)
        btn_Student = Button(M_Frame, text = "Student", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2",command=self.add_student).place(x = 240, y = 5, width = 200, height = 40)
        btn_Result = Button(M_Frame, text = "Result", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2",command=self.add_result).place(x = 460, y = 5, width = 200, height = 40)
        btn_View = Button(M_Frame, text = "View Student's Result", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2",command=self.add_report).place(x = 680, y = 5, width = 250, height = 40)
        btn_Logout = Button(M_Frame, text = "Logout", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x = 950, y = 5, width = 200, height = 40)
        btn_Exit = Button(M_Frame, text = "Exit", font = ("goudy old style", 15, "bold"), bg = "#0b5377", fg = "white", cursor = "hand2").place(x = 1170, y = 5, width = 200, height = 40)

##Content Window
        self.bg_img = Image.open("images.jpg")
        self.bg_img = self.bg_img.resize((920, 350), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image = self.bg_img).place(x = 450, y = 180, width = 920, height = 350)

##Update Details
        self.lbl_course = Label(self.root, text = "Total Courses\n[0]", font = ("goudy old style", 20), bd = 10, relief = RIDGE, bg = "#556B2F", fg = "white" )
        self.lbl_course.place(x = 450, y = 530, width = 300, height = 100)
        
        self.lbl_student = Label(self.root, text = "Total Students\n[0]", font = ("goudy old style", 20), bd = 10, relief = RIDGE, bg = "#DAA520", fg = "white" )
        self.lbl_student.place(x = 760, y = 530, width = 300, height = 100)
        
        self.lbl_result = Label(self.root, text = "Total Result\n[0]", font = ("goudy old style", 20), bd = 10, relief = RIDGE, bg = "#8A3324", fg = "white" )
        self.lbl_result.place(x = 1070, y = 530, width = 300, height = 100)
##Footer
        footer = Label(self.root, text = "SRMS - Student Result Managemnet System\n Contact us for any Technical Issue: 970xxxxx21", font = ("goudy old style", 12,), bg = "#262626", fg = "white").pack(side = BOTTOM, fill = X)

    def add_course(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = studentClass(self.new_win)
    
    def add_result(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = reportClass(self.new_win)
    

 
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
