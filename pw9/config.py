from tkinter import *

root = Tk()
frame1 = LabelFrame(root, text="Function", width=200, height=600)
frame2 = LabelFrame(root, text="Initialization", width=200, height=600)

# VARIABLES.
l_course = []
l_student = []
mark_list = []
l_student_gpa_included = []

def clear_frame():
    for widget in frame2.winfo_children():
        widget.destroy()
