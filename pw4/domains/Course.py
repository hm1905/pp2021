import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate
from .Program import Program

screen = curses.initscr()

class Course(Program):
    def __init__(self):
        self.__Credit = 0

    def _get_Credit(self):
        return self.__Credit

    def input_information(self):
        super().input_information()
        screen.addstr("Please enter credit of course: ")
        screen.refresh()
        self.__Credit = int(screen.getstr().decode('utf-8'))
        while (self.validate_Credit(self.__Credit) == False):
            screen.addstr("Invalid number of credit, Please try again: ")
            screen.refresh()
            self.__Credit = int(screen.getstr().decode('utf-8'))

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
