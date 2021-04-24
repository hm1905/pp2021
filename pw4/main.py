import curses
from domains.Student import *
from domains.Course import *
from domains.Program import *
from domains.Mark import *
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


menu = ['Define number of student in a class',
        'Create new student information',
        'Define number of availabe Courses',
        'Create course information',
        'Input mark of students for a given coursess',
        'Show list of Courses',
        'Show list of Students',
        'Show mark of students in a given course',
        'Show selected student GPA',
        'Calculate GPA of all students',
        'Show list of Students with GPA',
        'Exit']


def print_menu(stdscr, selected):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main(stdscr):
    number_c = 0
    number_s = 0
    students = Student()
    courses = Course()
    global screen
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 0:
            stdscr.refresh()
            curses.echo()
            number_s = no_student()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 1:
            stdscr.refresh()
            curses.echo()
            for i in range(1, number_s + 1):
                students.input_information()
                students.set_information(l_student)
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 2:
            stdscr.refresh()
            curses.echo()
            number_c = no_course()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 3:
            stdscr.refresh()
            curses.echo()
            for i in range(1, number_c + 1):
                courses.input_information()
                courses.set_information(l_course)
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 4:
            stdscr.refresh()
            marked = Mark(l_student, l_course, number_s, number_c,
                          mark_list, l_student_gpa_included)
            marked.student_mark()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 5:
            stdscr.refresh()
            students.show_info(l_course)
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 6:
            stdscr.refresh()
            students.show_info(l_student)
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 7:
            stdscr.refresh()
            marked.sh_student_mark()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 8:
            stdscr.refresh()
            marked.average_gpa()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 9:
            stdscr.refresh()
            marked.all_student_gpa()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 10:
            marked.show_info()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row == 11:
            break
        print_menu(stdscr, current_row)
        stdscr.refresh()


# UI
if __name__ == '__main__':
    screen = curses.initscr()
    curses.wrapper(main)
