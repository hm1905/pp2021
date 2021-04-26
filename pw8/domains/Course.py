import math
import numpy
import curses
import time
from operator import itemgetter
import tabulate


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
