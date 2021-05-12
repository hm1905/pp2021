from domains import *
from input import *
import output
import pickle
import zipfile
import os
import threading
from tkinter import *
from config import *



# MAIN
def start_up():
    if os.path.isfile('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zip:
            zip.extractall()
            if os.path.isfile('students.txt'):
                global l_student
                l_student = pickle.load(open('students.txt','rb'))
            if os.path.isfile('courses.txt'):
                global l_course
                l_course = pickle.load(open('courses.txt','rb'))
            if os.path.isfile('marks.txt'):
                global mark_list
                mark_list = pickle.load(open('marks.txt','rb'))
        os.remove('students.dat')


def main():
    input = Input()
    marked = Mark(l_student, l_course, mark_list, l_student_gpa_included)

    input_information_student_b = Button(frame1, text="Input student information", command=lambda: input.input_information_student())
    input_information_course_b = Button(frame1, text="Input course information", command=lambda: input.input_information_course())
    input_mark_b = Button(frame1, text="Input mark of students", command=lambda: marked.student_mark())
    input_show_course_b = Button(frame1, text="Show list of Courses", command=lambda: output.show_info(l_course))
    input_show_student_b = Button(frame1, text="Show list of Students", command=lambda: output.show_info(l_student))
    input_show_mark_by_course_b = Button(frame1, text="Show mark of students by course", command=lambda: output.show_student_mark(mark_list))
    input_show_student_gpa_b = Button(frame1, text="Show selected student GPA", command=lambda: marked.average_gpa())
    input_calculate_all_gpa = Button(frame1, text="Calculate all student GPA", command=lambda: marked.all_student_gpa())
    input_show_student_bygpa_b = Button(frame1, text="Show list of Students with GPA", command=lambda: output.show_info(l_student_gpa_included))
    input_exit_b = Button(frame1, text="Exit", command=root.quit)

    input_information_student_b.pack()
    input_information_course_b.pack()
    input_mark_b.pack()
    input_show_course_b.pack()
    input_show_student_b.pack()
    input_show_mark_by_course_b.pack()
    input_show_student_gpa_b.pack()
    input_calculate_all_gpa.pack()
    input_show_student_bygpa_b.pack()
    input_exit_b.pack()




# UI
if __name__ == '__main__':

    frame1.pack(fill=BOTH, side="left")
    frame2.pack(side="right")
    main()
    root.mainloop()

    #start = threading.Thread(target=main)
    #start1 = threading.Thread(target=start_up)
    #start.start()
    #start1.start()
    #start.join()
    #start1.join()
