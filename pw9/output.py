from domains import *
from tkinter import *
from tkinter import messagebox
from config import *

def show_info(list):
    if list == []:
        messagebox.showwarning("Warning", "No information was given")
    else:
        clear_frame()
        if any('GPA' in i for i in list):
            l_student_gpa_included_sorted = []
            l_student_gpa_included_sorted = sorted(
                list, key=itemgetter('GPA'), reverse=True)
            show=Label(frame2, text=tabulate.tabulate(
                l_student_gpa_included_sorted, headers="keys")).pack()
        else:
            show=Label(frame2, text=tabulate.tabulate(list, headers="keys")).pack()

def show_student_mark(list):
    clear_frame()
    def display():
        for i in list:
            if i['Subject'] == pick.get():
                show.append({'ID': i['ID'], 'Mark': i['Mark']})
        display=Label(frame2, text=tabulate.tabulate(show ,headers = "keys")).pack()
    show = []
    mk_s = []

    for i in list:
        if i['Subject'] not in mk_s:
            mk_s.append(i['Subject'])

    pick = StringVar()
    pick.set("Choose a course")
    option = OptionMenu(frame2, pick, *mk_s)
    option.pack()

    selection = Button(frame2, text="Select", command=display)
    selection.pack()
