import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate
import datetime
from .Program import Program
date_format = '%d-%m-%Y'

screen = curses.initscr()

class Student(Program):
    def __init__(self):
        self.__DoB = None

    def _get_DoB(self):
        return self.__DoB

    def set_DoB(self, DoB):
        self.__DoB = DoB

    def input_information(self):
        super().input_information()
        screen.addstr("Please enter Date of Birth of student<format:d-m-Y>: ")
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
        try:
            datetime.datetime.strptime(self.__DoB, date_format)
            return True
        except:
            return False
