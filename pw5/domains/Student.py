import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate
import datetime
date_format = '%d-%m-%Y'


class Student:
    def __init__(self):
        self.__DoB = None
        self.__id = None
        self.__name = None

    def _get_id(self):
        return self.__id

    def _get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def _get_DoB(self):
        return self.__DoB

    def set_DoB(self, DoB):
        self.__DoB = DoB

    def validate_DoB(self, DoB):
        try:
            datetime.datetime.strptime(self.__DoB, date_format)
            return True
        except:
            return False

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
