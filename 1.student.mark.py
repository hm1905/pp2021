#Function

def no_student():
    student_no = int(input("Please enter number of student: "))
    return student_no

def no_course():
    course_no = int(input("Please enter number of courses: "))
    return course_no

  #Student info include : id, name, DoB
def student_info(l_student, number_s):
    for i in range(1, number_s+1):
        info_s = {'id': input("Please enter student id: "),
                  'name': input("Please enter student name: "),
                  'DoB' : input("please enter student's date of birth: ")}
        l_student.append(info_s)
    return l_student

  #Course info include : id, name
def course_info(l_course, number_c):
    for i in range(1, number_c+1):
        info_c = {'id': input("Please enter courese id: "),
                  'name': input("Please enter course name: ")}
        l_course.append(info_c)
    return l_course

def student_mark(l_student, l_course, mark_list):
    print("Available Courses: ")
    print(l_course)
    c_name = input("Please select one to enter mark<by name>: ")
    while not any(i['name'] == c_name for i in l_course):
        print("Please try again: ")
        c_name = input("Please select one to enter mark<by name>: ")
    i = str(1)
    count = 0
    while i == str(1):
        print("Student list: ")
        print(l_student)
        s_name = input("Please select which student to mark<by name>: ")
        while not any(i['name'] == s_name for i in l_student):
            print("Please try again: ")
            s_name = input("Please select which student to mark<by name>: ")
        mk = input("The mark: ")
        mark_list.append({'Subject': c_name,'Name': s_name,'Mark': mk})
        count += 1
        if count >= number_s:
            print("You have entered mark for every students for " + c_name)
        i = input("Do you wish to continue marking the student<1:Yes, 0:No>: ")
        while not (i == str(1) or i == str(0)):
            print("Please enter only 1 or 0")
            i = input("Do you wish to continue marking the student<1:Yes, 0:No>: ")
    return mark_list


def list_courses(l_course):
    print("Available course: ")
    print(" ")
    for i in  l_course:
        print(i)

def list_students(l_student):
    print("Students list: ")
    print(" ")
    for i in  l_student:
        print(i)

def sh_student_mark(x):
    show=[]
    print("Marked subject")
    mk_s = []
    for i in x:
        if i['Subject'] not in mk_s:
            mk_s.append(i['Subject'])
    print(mk_s)
    name = input("Please select which subject you want to see: ")
    print(" ")
    while not any(i['Subject'] == name for i in x):
        print("Please try again. You might havent marked "+ name +" yet")
        name = input("Please select which subject you want to see: ")
        print(" ")
    for i in x:
        if i['Subject'] == name:
            show.append({'Name': i['Name'], 'Mark': i['Mark']})
    for i in show:
        print(i)


#Variable
 #List of Students
l_student = []
 #List of Courses
l_course = []
 #List of mark
mark_list = []

#UI

if __name__ == '__main__':
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
        7. Show list of students
        8. Show mark of students in a given course
        9.Exit""")
        i = int(input("Choose your action: "))
        print(" ")
        while i not in range(1, 10):
            print("Please try again")
            i = int(input("Choose your action: "))

        if i==1:
            number_s=no_student()
            if i not in op:
                op.append(i)
        if i==2:
            try:
                student_info(l_student, number_s)
                if i not in op:
                    op.append(i)
            except:
                print("No number of student was given. Please insert it before try again.")
        if i==3:
            number_c=no_course()
            if i not in op:
                op.append(i)
        if i==4:
            try:
                course_info(l_course, number_c)
                if i not in op:
                    op.append(i)
            except:
                print("No number of courses was given. Please insert it before try again.")
        if i==5:
            if l_course == [] or l_student == []:
                print("Not enough information about students or courses was given please try again")
            else:
                x=student_mark(l_student, l_course, mark_list)
                if i not in op:
                    op.append(i)
        if i==6:
            if l_course == []:
                print("No information about course was given")
            else:
                list_courses(l_course)
                if i not in op:
                    op.append(i)
        if i==7:
            if l_student == []:
                print("No information about students was given")
            else:
                list_students(l_student)
                if i not in op:
                    op.append(i)
        if i==8:
            try:
                sh_student_mark(x)
                if i not in op:
                    op.append(i)
            except:
                print("You havent mark anyone")
