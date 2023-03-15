from tkinter import *
class oopsie:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry('1525x780+0+0')



if __name__=="__main__":
    root=Tk()
    obj=oopsie(root)
    root.mainloop()
