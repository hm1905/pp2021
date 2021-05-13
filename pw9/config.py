from tkinter import *

root = Tk()
frame1 = LabelFrame(root, text="Function", width=300, height=400, bd=20)
frame2 = LabelFrame(root, text="Initialization", width=600, height=400)
frame3 = LabelFrame(root, text="Status", width=300, height=400)

root.resizable(width=False, height=False)
# VARIABLES.
l_course = []
l_student = []
mark_list = []
l_student_gpa_included = []

def clear_frame():
    for widget in frame2.winfo_children():
        widget.destroy()

def clear_status():
    for widget in frame3.winfo_children():
        widget.destroy()
