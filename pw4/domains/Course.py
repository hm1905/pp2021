import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate

screen = curses.initscr()

class Course:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__Credit = 0

    def _get_id(self):
        return self.__id

    def _get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def _get_Credit(self):
        return self.__Credit

    def input_information_course(self):
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
        screen.addstr("Please enter credit of course: ")
        screen.refresh()
        self.__Credit = int(screen.getstr().decode('utf-8'))
        while (self.validate_Credit(self.__Credit) == False):
            screen.addstr("Invalid number of credit, Please try again: ")
            screen.refresh()
            self.__Credit = int(screen.getstr().decode('utf-8'))

    def validate_Credit(self, Credit):
        if (self.__Credit) == 0:
            return False
        else:
            return True

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
