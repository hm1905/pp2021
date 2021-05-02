from domains import *
import curses

screen = curses.initscr()

class Input(Student, Course):
    def input_information_student(self):
        screen.addstr("Please enter ID: ")
        screen.refresh()
        self._Student__id = screen.getstr().decode('utf-8')
        while (self.validate_id(self._Student__id) == False):
            screen.addstr("Invalid ID, Please try again: ")
            screen.refresh()
            self._Student__id = screen.getstr().decode('utf-8')
        screen.addstr("Please enter Name: ")
        screen.refresh()
        self._Student__name = screen.getstr().decode('utf-8')
        while (self.validate_name(self._Student__name) == False):
            screen.addstr("Invalid Name, Please try again: ")
            screen.refresh()
            self._Student__name = screen.getstr().decode('utf-8')
        screen.addstr("Please enter Date of Birth of student<format:d-m-Y>: ")
        screen.refresh()
        self._Student__DoB = screen.getstr().decode('utf-8')
        while (self.validate_DoB(self._Student__DoB) == False):
            screen.addstr("Invalid Date of Birth, Please try again: ")
            screen.refresh()
            self._Student__DoB = screen.getstr().decode('utf-8')
        screen.clear()

    def input_information_course(self):
        screen.addstr("Please enter ID: ")
        screen.refresh()
        self._Course__id = screen.getstr().decode('utf-8')
        while (self.validate_id(self._Course__id) == False):
            screen.addstr("Invalid ID, Please try again: ")
            screen.refresh()
            self._Course__id = screen.getstr().decode('utf-8')
        screen.addstr("Please enter Name: ")
        screen.refresh()
        self._Course__name = screen.getstr().decode('utf-8')
        while (self.validate_name(self._Course__name) == False):
            screen.addstr("Invalid Name, Please try again: ")
            screen.refresh()
            self._Course__name = screen.getstr().decode('utf-8')
        screen.addstr("Please enter credit of course: ")
        screen.refresh()
        self._Course__Credit = int(screen.getstr().decode('utf-8'))
        while (self.validate_Credit(self._Course__Credit) == False):
            screen.addstr("Invalid number of credit, Please try again: ")
            screen.refresh()
            self._Course__Credit = int(screen.getstr().decode('utf-8'))
        screen.clear()

    def set_information_student(self, list):
        info = {'id': self._Student__id,
                'name': self._Student__name,
                'DoB': self._Student__DoB}
        list.append(info)
        return list

    def set_information_course(self, list):
        info = {'id': self._Course__id,
                'name': self._Course__name,
                'Credit': self._Course__Credit}
        list.append(info)
        return list
