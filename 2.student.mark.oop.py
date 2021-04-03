# VARIABLES.
l_course = []
l_student = []

# CLASS CREATION


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
        self.__id = input("Please enter ID: ")
        while (self.validate_id(self.__id) == False):
            self.__id = input("Invalid ID, Please try again: ")
        self.__name = input("Please enter Name: ")
        while (self.validate_name(self.__name) == False):
            self.__name = input("Invalid Name, Please try again: ")

    def set_information(self, list):
        info = {'id': self.__id,
                'name': self.__name}
        list.append(info)
        return list

    def show_info(self, list):
        if list == []:
            print("No information was given")
        else:
            for i in list:
                print(i)

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


class Student(Program):
    def __init__(self):
        self.__DoB = None

    def _get_DoB(self):
        return self.__DoB

    def set_DoB(self, DoB):
        self.__DoB = DoB

    def input_information(self):
        super().input_information()
        self.__DoB = input("Please enter Date of Birth of student: ")
        while (self.validate_DoB(self.__DoB) == False):
            self.__DoB = input("Invalid Date of Birth, Please try again: ")

    def set_information(self, list):
        info = {'id': self._Program__id,
                'name': self._Program__name,
                'DoB': self.__DoB}
        list.append(info)
        return list

    def validate_DoB(self, DoB):
        if (len((self.__DoB)) == 0):
            return False
        else:
            return True


class Course(Program):
    pass


class Mark:
    mark_list = []
    show = []

    def __init__(self, l_student, l_course, number_s, number_c):
        self.l_student = l_student
        self.l_course = l_course
        self.number_s = number_s
        self.number_c = number_c

    def student_mark(self):
        if self.l_course == [] or self.l_student == []:
            print(
                "Not enough information about students or courses was given please try again")
        else:
            print("Available Courses: ")
            print(self.l_course)
            c_name = input("Please select one to enter mark<by name>: ")
            while not any(i['name'] == c_name for i in self.l_course):
                print("Please try again: ")
                c_name = input("Please select one to enter mark<by name>: ")
            i = str(1)
            count = 0
            while i == str(1):
                print("Student list: ")
                print(self.l_student)
                s_name = input(
                    "Please select which student to mark<by name>: ")
                while not any(i['name'] == s_name for i in self.l_student):
                    print("Please try again: ")
                    s_name = input(
                        "Please select which student to mark<by name>: ")
                mk = input("The mark: ")
                self.mark_list.append(
                    {'Subject': c_name, 'Name': s_name, 'Mark': mk})
                count += 1
                if count >= self.number_s:
                    print("You have entered mark for every students for " + c_name)
                i = input(
                    "Do you wish to continue marking the student<1:Yes, 0:No>: ")
                while not (i == str(1) or i == str(0)):
                    print("Please enter only 1 or 0")
                    i = input(
                        "Do you wish to continue marking the student<1:Yes, 0:No>: ")
            return self.mark_list

    def sh_student_mark(self):
        print("Marked subject")
        mk_s = []
        for i in self.mark_list:
            if i['Subject'] not in mk_s:
                mk_s.append(i['Subject'])
        print(mk_s)
        name = input("Please select which subject you want to see: ")
        print(" ")
        while not any(i['Subject'] == name for i in self.mark_list):
            print("Please try again. You might havent marked " + name + " yet")
            name = input("Please select which subject you want to see: ")
            print(" ")
        for i in self.mark_list:
            if i['Subject'] == name:
                self.show.append({'Name': i['Name'], 'Mark': i['Mark']})
        for i in self.show:
            print(i)


# MAIN
def no_student():
    student_no = int(input("Please enter number of student: "))
    return student_no


def no_course():
    course_no = int(input("Please enter number of courses: "))
    return course_no


def main():
    i = None
    op = []
    while i != 9:
        print(" ")
        print("Finished option: ")
        op.sort()
        print(op)
        print("Recommend order from 1 to 8")
        print("""
        Availabe option:
        1. Define number of student in a class
        2. Create new student information
        3. Make number of availabe Courses
        4. Define course information
        5. Input mark of students for a given coursess
        6. Show list of Courses
        7. Show list of students
        8. Show mark of students in a given course
        9.Exit""")
        i = int(input("Choose your action: "))
        print(" ")
        while i not in range(1, 10):
            print("Please try again")
            i = int(input("Choose your action: "))

        if i == 1:
            number_s = no_student()
            students = Student()
            op.append(i)
        if i == 2:
            try:
                for i in range(1, number_s + 1):
                    students.input_information()
                    students.set_information(l_student)
                op.append(i)
            except:
                print("No number of students was given. Please insert it before try again.")
        if i == 3:
            number_c = no_course()
            courses = Course()
            op.append(i)
        if i == 4:
            try:
                for i in range(1, number_c + 1):
                    courses.input_information()
                    courses.set_information(l_course)
                op.append(i)
            except:
                print("No number of courses was given. Please insert it before try again.")
        if i == 5:
            if l_course == [] or l_student == []:
                print("Not enough information about students or courses was given please try again")
            else:
                marked = Mark(l_student, l_course, number_s, number_c)
                marked.student_mark()
                op.append(i)
        if i == 6:
            try:
                courses.show_info(l_course)
                op.append(i)
            except:
                print("No information about course was given")
        if i == 7:
            try:
                students.show_info(l_student)
                op.append(i)
            except:
                print("No information about student was given")
        if i == 8:
            try:
                marked.sh_student_mark()
                op.append(i)
            except:
                print("You havent marked anyone")
        if i == 9:
            print("Goodbye")


# UI
if __name__ == '__main__':
    main()
