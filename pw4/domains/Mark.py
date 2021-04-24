import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate

screen = curses.initscr()

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
            screen.refresh()
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

                screen.addstr("Mark<out of 20>: ")
                mk = None
                while mk == None:
                    try:
                        mk = float(screen.getstr().decode('utf-8'))
                        if mk not in numpy.arange(0, 21, 0.1):
                            screen.addstr("Invalid mark. Please try again: " + '\n')
                            screen.addstr("Mark<out of 20>: ")
                            mk = float(screen.getstr().decode('utf-8'))
                    except:
                        screen.addstr("Invalid input. Please try again: ")

                mk = math.floor(mk)
                self.mark_list.append(
                    {'Subject': c_name, 'Name': s_name, 'Mark': mk})
                count += 1
                if count >= self.number_s:
                    screen.addstr(
                        "You have entered mark for every students for " + str(c_name) + '\n')
                screen.addstr(
                    "Do you wish to continue marking the student<1:Yes, 0:No>: ")
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
            screen.addstr("Please select which subject you want to see: " + '\n')
            name = screen.getstr().decode('utf-8')
        for i in self.mark_list:
            if i['Subject'] == name:
                show.append({'Name': i['Name'], 'Mark': i['Mark']})
        screen.addstr(tabulate.tabulate(show ,headers = "keys"))
        screen.refresh()
        time.sleep(2)

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
        gpa = numpy.dot(total_mark, total_credit) // numpy.sum(total_credit)
        screen.addstr(str(gpa))
        screen.refresh()
        time.sleep(2)

    def all_student_gpa(self):
        for z in self.l_student:
            total_mark = numpy.array([])
            total_credit = numpy.array([])
            for i in self.mark_list:
                if i['Name'] == z['name']:
                    total_mark = numpy.append(total_mark, float(i['Mark']))
                    for y in l_course:
                        if (y['name'] == i['Subject']):
                            total_credit = numpy.append(
                                total_credit, float(y['Credit']))
            gpa = numpy.dot(
                total_mark, total_credit) // numpy.sum(total_credit)
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
