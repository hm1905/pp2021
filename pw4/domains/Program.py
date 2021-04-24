import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate

screen = curses.initscr()
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
