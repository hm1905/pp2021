import curses
from domains import *
from input import *
import output
import json
import zipfile
import os

# VARIABLES.
l_course = []
l_student = []
mark_list = []
l_student_gpa_included = []


# MAIN
def no_student():
    screen.addstr("Please enter number of student: ")
    screen.refresh()
    student_no = int(screen.getstr())
    return student_no


def no_course():
    screen.addstr("Please enter number of course: ")
    screen.refresh()
    course_no = int(screen.getstr())
    return course_no

def main(stdscr):
    if os.path.isfile('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zip:
            zip.extractall()
            if os.path.isfile('students.txt'):
                global l_student
                l_student = json.load(open('students.txt'))
            if os.path.isfile('courses.txt'):
                global l_course
                l_course = json.load(open('courses.txt'))
            if os.path.isfile('marks.txt'):
                global mark_list
                mark_list = json.load(open('marks.txt'))
        os.remove('students.dat')


    number_c = 0
    number_s = 0
    input = Input()
    global screen
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    output.print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(output.menu) - 1:
            current_row += 1
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 0:
            stdscr.refresh()
            curses.echo()
            number_s = no_student()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 1:
            stdscr.refresh()
            curses.echo()
            for i in range(1, number_s + 1):
                input.input_information_student()
                input.set_information_student(l_student)
            with open('students.txt', 'w') as f:
                f.write(json.dumps(l_student))
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 2:
            stdscr.refresh()
            curses.echo()
            number_c = no_course()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 3:
            stdscr.refresh()
            curses.echo()
            for i in range(1, number_c + 1):
                input.input_information_course()
                input.set_information_course(l_course)
            with open('courses.txt', 'w') as f:
                f.write(json.dumps(l_course))
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 4:
            stdscr.refresh()
            marked = Mark(l_student, l_course, number_s, number_c,
                          mark_list, l_student_gpa_included)
            marked.student_mark()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 5:
            stdscr.refresh()
            output.show_info(l_course)
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 6:
            stdscr.refresh()
            output.show_info(l_student)
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 7:
            stdscr.refresh()
            output.show_student_mark(mark_list)
            with open('marks.txt', 'w') as f:
                f.write(json.dumps(mark_list))
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 8:
            stdscr.refresh()
            marked.average_gpa()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 9:
            stdscr.refresh()
            marked.all_student_gpa()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 10:
            output.show_info(l_student_gpa_included)
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 11:
            if os.path.isfile('students.txt'):
                with zipfile.ZipFile('students.dat', 'a') as zip:
                    zip.write('students.txt')
                    os.remove('students.txt')
            if os.path.isfile('courses.txt'):
                with zipfile.ZipFile('students.dat', 'a') as zip:
                    zip.write('courses.txt')
                    os.remove('courses.txt')
            if os.path.isfile('marks.txt'):
                with zipfile.ZipFile('students.dat', 'a') as zip:
                    zip.write('marks.txt')
                    os.remove('marks.txt')
            break
        output.print_menu(stdscr, current_row)
        stdscr.refresh()


# UI
if __name__ == '__main__':
    screen = curses.initscr()
    curses.wrapper(main)