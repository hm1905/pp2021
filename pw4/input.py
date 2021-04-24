from domains import *

class Input(Student, Course):
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
