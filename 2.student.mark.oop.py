# CLASS CREATION

class Student:
    l_student = []

    def __init__(self, number_s):
        self.number_s = number_s

    def information(self):
        for i in range(1, self.number_s + 1):
            info_s = {'id': input("Please enter student id: "),
                      'name': input("Please enter student name: "),
                      'DoB': input("please enter student's date of birth: ")}
            self.l_student.append(info_s)
        return self.l_student

    def show_info(self):
        if self.l_student == []:
            print("No information about students was given")
        else:
            print("Students list: ")
            print(" ")
            for i in self.l_student:
                print(i)


class Course:
    l_course = []

    def __init__(self, number_c):
        self.number_c = number_c

    def information(self):
        for i in range(1, number_c + 1):
            info_c = {'id': input("Please enter courese id: "),
                      'name': input("Please enter course name: ")}
            self.l_course.append(info_c)
        return self.l_course

    def show_info(self):
        if self.l_course == []:
            print("No information about course was given")
        else:
            print("Available course: ")
            print(" ")
            for i in self.l_course:
                print(i)


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
        7. Show list of Students
        8. Show mark of students in a given course
        9.Exit""")
        i = int(input("Choose your action: "))
        print(" ")
        while i not in range(1, 10):
            print("Please try again")
            i = int(input("Choose your action: "))

        if i == 1:
            number_s = no_student()
            students = Student(number_s)
            op.append(i)
        if i == 2:
            try:
                students.information()
                op.append(i)
            except:
                print(
                    "No number of student was given. Please insert it before try again.")
        if i == 3:
            number_c = no_course()
            courses = Course(number_c)
            op.append(i)
        if i == 4:
            try:
                courses.information()
                op.append(i)
            except:
                print(
                    "No number of courses was given. Please insert it before try again.")
        if i == 5:
            marked = Mark(students.l_student,
                          courses.l_course, number_s, number_c)
            marked.student_mark()
            op.append(i)
        if i == 6:
            try:
                courses.show_info()
                op.append(i)
            except:
                print("No information about course was given")
        if i == 7:
            try:
                students.show_info()
                op.append(i)
            except:
                print("No information about students was given")
        if i == 8:
            try:
                marked.sh_student_mark()
                op.append(i)
            except:
                print("You havent marked anyone!")

        if i == 9:
            print("Goodbye")


if __name__ == '__main__':
    main()
