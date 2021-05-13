import math
import numpy
import time
from operator import itemgetter
import tabulate
from tkinter import *
from tkinter import messagebox
from config import *

class Mark:

    def __init__(self, l_student, l_course, mark_list, l_student_gpa_included):
        self.l_student = l_student
        self.l_course = l_course
        self.mark_list = mark_list
        self.l_student_gpa_included = l_student_gpa_included

    def validate_mark(self, mark):
        try:
            if (mark != None and float(mark) in numpy.arange(0, 21, 0.1)):
                return True
        except:
            return False

    def student_mark(self):
        if self.l_course == [] or self.l_student == []:
            messagebox.showwarning("Warning", "Not enough information")
        else:
            def Submit():
                if self.validate_mark(mark.get()) == False:
                    messagebox.showerror("Error","Invalid mark")
                else:
                    self.mark_list.append(
                        {'Subject': pick.get(), 'ID': id.get(), 'Mark': float(mark.get())})
                    messagebox.showinfo("Update", "Update SUCCESSFUL")

            def open():
                list = Label(frame3, text=tabulate.tabulate(self.l_student, headers="keys")).pack()

            clear_frame()
            course_op=[]
            for i in l_course:
                if i['name'] not in course_op:
                    course_op.append(i['name'])

            pick = StringVar()
            pick.set("Choose a course")
            option = OptionMenu(frame2, pick, *course_op)
            option.pack()

            selection = Button(frame2, text="Select", command=open)
            selection.pack()

            id_t = Label(frame2, text="ID")
            id_t.pack(side='left')
            id = Entry(frame2)
            id.pack(side='left')


            mark_t = Label(frame2, text="Mark")
            mark_t.pack(side='left')
            mark = Entry(frame2)
            mark.pack(side='left')

            submit = Button(frame2, text="Submit", command=Submit)
            submit.pack(side='left')

    #NEED TO MAKE VALIDATE ID


    def average_gpa(self):
        clear_frame()
        def gpa_process():
            total_mark = numpy.array([])
            total_credit = numpy.array([])
            for i in self.mark_list:
                if i['ID'] == pick.get():
                    total_mark = numpy.append(total_mark, i['Mark'])
                    for y in self.l_course:
                        if (y['name'] == i['Subject']):
                            total_credit = numpy.append(total_credit, y['Credit'])
            gpa = numpy.dot(total_mark, total_credit) // numpy.sum(total_credit)
            print = Label(frame2, text=gpa).pack()

        mk_n = []
        for i in self.mark_list:
            if i['ID'] not in mk_n:
                mk_n.append(i['ID'])

        pick = StringVar()
        pick.set("Choose a student")
        option = OptionMenu(frame2, pick, *mk_n)
        option.pack()

        selection = Button(frame2, text="Select", command=gpa_process)
        selection.pack()


    def all_student_gpa(self):
        for z in self.l_student:
            total_mark = numpy.array([])
            total_credit = numpy.array([])
            for i in self.mark_list:
                if i['ID'] == z['ID']:
                    total_mark = numpy.append(total_mark, float(i['Mark']))
                    for y in self.l_course:
                        if (y['name'] == i['Subject']):
                            total_credit = numpy.append(
                                total_credit, float(y['Credit']))
            gpa = numpy.dot(
                total_mark, total_credit) // numpy.sum(total_credit)
            info = {'id': z['ID'],
                    'name': z['name'],
                    'DoB': z['DoB'],
                    'GPA': gpa}
            self.l_student_gpa_included.append(info)

        messagebox.showinfo("Status", "Update GPA SUCCESSFUL")
