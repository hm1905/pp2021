import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate

# VARIABLES.
l_course = [{'id': '11', 'name':  'math', 'Credit': 3},
            {'id': '12', 'name':  'python', 'Credit': 4}]
l_student = [{'id': '1', 'name':  'joe', 'DoB': '12/12'},
             {'id': '2', 'name':  'beth', 'DoB': '11/12'}]
mark_list = [{'Subject': 'math', 'Name': 'joe', 'Mark': 19}, {'Subject': 'python',
                                                              'Name': 'joe', 'Mark': 20}, {'Subject': 'python', 'Name': 'beth', 'Mark': 12}]
l_student_gpa_included = []

# CLASS CREATION


class Program:
    def __init__(self):
        self.__id = None
        self.__name = None

    def _get_id(self):
        return self.__id

    def _get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def input_information(self):
        screen.addstr("Please enter ID: ")
        screen.refresh()
        self.__id = screen.getstr().decode('utf-8')
        while (self.validate_id(self.__id) == False):
            screen.addstr("Invalid ID, Please try again: ")
            screen.refresh()
            self.__id = screen.getstr().decode('utf-8')
        screen.addstr("Please enter Name: ")
        screen.refresh()
        self.__name = screen.getstr().decode('utf-8')
        while (self.validate_name(self.__name) == False):
            screen.addstr("Invalid Name, Please try again: ")
            screen.refresh()
            self.__Name = screen.getstr().decode('utf-8')

    def set_information(self, list):
        info = {'id': self.__id,
                'name': self.__name}
        list.append(info)
        return list

    def show_info(self, list):
        screen.addstr(tabulate.tabulate(list, headers="keys"))
        screen.refresh()
        time.sleep(2)

    def validate_name(self, name):
        if (len((self.__name)) == 0):
            return False
        else:
            return True

    def validate_id(self, id):
        if (len((self.__id)) == 0):
            return False
        else:
            return True


class Student(Program):
    def __init__(self):
        self.__DoB = None

    def _get_DoB(self):
        return self.__DoB

    def set_DoB(self, DoB):
        self.__DoB = DoB

    def input_information(self):
        super().input_information()
        screen.addstr("Please enter Date of Birth of student: ")
        screen.refresh()
        self.__DoB = screen.getstr().decode('utf-8')
        while (self.validate_DoB(self.__DoB) == False):
            screen.addstr("Invalid Date of Birth, Please try again: ")
            screen.refresh()
            self.__DoB = screen.getstr().decode('utf-8')

    def set_information(self, list):
        info = {'id': self._Program__id,
                'name': self._Program__name,
                'DoB': self.__DoB}
        list.append(info)
        return list

    def validate_DoB(self, DoB):
        if (len((self.__DoB)) == 0):
            return False
        else:
            return True


class Course(Program):
    def __init__(self):
        self.__Credit = 0

    def _get_Credit(self):
        return self.__Credit

    def input_information(self):
        super().input_information()
        screen.addstr("Please enter credit of course: ")
        screen.refresh()
        self.__Credit = screen.getstr().decode('utf-8')
        while (self.validate_Credit(self.__Credit) == False):
            screen.addstr("Invalid number of credit, Please try again: ")
            screen.refresh()
            self.__Credit = screen.getstr().decode('utf-8')

    def set_information(self, list):
        info = {'id': self._Program__id,
                'name': self._Program__name,
                'Credit': self.__Credit}
        list.append(info)
        return list

    def validate_Credit(self, Credit):
        if (self.__Credit) == 0:
            return False
        else:
            return True


class Mark:

    def __init__(self, l_student, l_course, number_s, number_c, mark_list, l_student_gpa_included):
        self.l_student = l_student
        self.l_course = l_course
        self.number_s = number_s
        self.number_c = number_c
        self.mark_list = mark_list
        self.l_student_gpa_included = l_student_gpa_included

    def student_mark(self):
        if self.l_course == [] or self.l_student == []:
            screen.addstr(
                "Not enough information about students or courses was given please try again")
            screeb.refresh()
        else:
            screen.addstr("Available Courses: " + '\n')
            screen.addstr(str(self.l_course) + '\n')
            screen.addstr("Please select one to enter mark<by name>: ")
            c_name = screen.getstr().decode('utf-8')
            while not any(i['name'] == c_name for i in self.l_course):
                screen.addstr("Please try again: " + '\n')
                screen.addstr("Please select one to enter mark<by name>: ")
                c_name = screen.getstr()
            i = str(1)
            count = 0
            while i == str(1):
                screen.addstr("Student list: " + '\n')
                screen.addstr(str(self.l_student) + '\n')
                screen.addstr("Please select which student to mark<by name>: ")
                s_name = screen.getstr().decode('utf-8')
                while not any(i['name'] == s_name for i in self.l_student):
                    screen.addstr("Please try again: ")
                    s_name = screen.getstr().decode('utf-8')
                screen.addstr("The mark: ")
                mk = float(screen.getstr().decode('utf-8'))
                mk = math.floor(mk)
                self.mark_list.append(
                    {'Subject': c_name, 'Name': s_name, 'Mark': mk})
                count += 1
                if count >= self.number_s:
                    screen.addstr(
                        "You have entered mark for every students for " + str(c_name) + '\n')
                screen.addstr(
                    "Do you wish to continue marking the student<1:Yes, 0:No>: " + '\n')
                i = screen.getstr().decode('utf-8')
                while not (i == str(1) or i == str(0)):
                    screen.addstr("Please enter only 1 or 0" + '\n')
                    screen.addstr(
                        "Do you wish to continue marking the student<1:Yes, 0:No>: " + '\n')
                    i = screen.getstr().decode('utf-8')
            return self.mark_list

    def sh_student_mark(self):
        show = []
        screen.addstr("Marked subject:" + '\n')
        mk_s = []
        for i in self.mark_list:
            if i['Subject'] not in mk_s:
                mk_s.append(i['Subject'])
        screen.addstr(str(mk_s) + '\n')
        screen.addstr("Please select which subject you want to see: ")
        name = screen.getstr().decode('utf-8')
        while not any(i['Subject'] == name for i in self.mark_list):
            screen.addstr(
                "Please try again. You might havent marked " + str(name) + " yet" + '\n')
            screen.addstr("Please select which subject you want to see: ")
            name = screen.getstr().decode('utf-8')
        for i in self.mark_list:
            if i['Subject'] == name:
                show.append({'Name': i['Name'], 'Mark': i['Mark']})
        for i in show:
            for keys, values in i.items():
                screen.addstr(str(keys) + ': ' + str(values))
                screen.refresh()
            time.sleep(1)

    def average_gpa(self):
        total_mark = numpy.array([])
        total_credit = numpy.array([])
        screen.addstr("Marked student" + '\n')
        mk_n = []
        for i in self.mark_list:
            if i['Name'] not in mk_n:
                mk_n.append(i['Name'])
        screen.addstr(str(mk_n) + '\n')
        screen.addstr("Please select which student's GPA you want: ")
        name = screen.getstr().decode('utf-8')
        while not any(i['Name'] == name for i in self.mark_list):
            screen.addstr("Please try again" + '\n')
            screen.addstr("Please select which student's GPA you want: ")
            name = screen.getstr().decode('utf-8')

        for i in self.mark_list:
            if i['Name'] == name:
                total_mark = numpy.append(total_mark, i['Mark'])
                for y in l_course:
                    if (y['name'] == i['Subject']):
                        total_credit = numpy.append(total_credit, y['Credit'])
        gpa = numpy.dot(total_mark, total_credit) / numpy.sum(total_credit)
        gpa = math.floor(gpa)
        screen.addstr(str(gpa))
        screen.refresh()
        time.sleep(2)

    def all_student_gpa(self):
        for z in self.l_student:
            total_mark = numpy.array([])
            total_credit = numpy.array([])
            for i in self.mark_list:
                if i['Name'] == z['name']:
                    total_mark = numpy.append(total_mark, i['Mark'])
                    for y in l_course:
                        if (y['name'] == i['Subject']):
                            total_credit = numpy.append(
                                total_credit, y['Credit'])
            gpa = numpy.dot(total_mark, total_credit) / numpy.sum(total_credit)
            gpa = math.floor(gpa)
            info = {'id': z['id'],
                    'name': z['name'],
                    'DoB': z['DoB'],
                    'GPA': gpa}
            l_student_gpa_included.append(info)
        screen.addstr("GPA updated")
        screen.refresh()
        time.sleep(2)

    def show_info(self):
        if l_student_gpa_included == []:
            screen.addstr('You havent calculate all of students GPA')
            screen.refresh()
            time.sleep(2)
        else:
            l_student_gpa_included_sorted = []
            l_student_gpa_included_sorted = sorted(
                l_student_gpa_included, key=itemgetter('GPA'), reverse=True)
            screen.addstr(tabulate.tabulate(
                l_student_gpa_included_sorted, headers="keys"))
            screen.refresh()
            time.sleep(2)


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
    marked = Mark(l_student, l_course, number_s, number_c,
                  mark_list, l_student_gpa_included)
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
