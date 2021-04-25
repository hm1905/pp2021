import curses
from domains import *

screen = curses.initscr()

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

def show_info(list):
    if list == []:
        screen.addstr('No information was given')
        screen.refresh()
        time.sleep(2)
    else:
        if any('GPA' in i for i in list):
            l_student_gpa_included_sorted = []
            l_student_gpa_included_sorted = sorted(
                list, key=itemgetter('GPA'), reverse=True)
            screen.addstr(tabulate.tabulate(
                l_student_gpa_included_sorted, headers="keys"))
            screen.refresh()
            time.sleep(2)
        else:
            screen.addstr(tabulate.tabulate(list, headers="keys"))
            screen.refresh()
            time.sleep(2)


def show_student_mark(list):
    show = []
    screen.addstr("Marked subject:" + '\n')
    mk_s = []
    for i in list:
        if i['Subject'] not in mk_s:
            mk_s.append(i['Subject'])
    screen.addstr(str(mk_s) + '\n')
    screen.addstr("Please select which subject you want to see: ")
    name = screen.getstr().decode('utf-8')
    while not any(i['Subject'] == name for i in list):
        screen.addstr(
            "Please try again. You might havent marked " + str(name) + " yet" + '\n')
        screen.addstr("Please select which subject you want to see: " + '\n')
        name = screen.getstr().decode('utf-8')
    for i in list:
        if i['Subject'] == name:
            show.append({'Name': i['Name'], 'Mark': i['Mark']})
    screen.addstr(tabulate.tabulate(show ,headers = "keys"))
    screen.refresh()
    time.sleep(2)
