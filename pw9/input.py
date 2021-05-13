from domains import *
from tkinter import *
from tkinter import messagebox
from config import *

class Input(Student, Course):
    def input_information_student(self):
        clear_frame()
        def Submit_student():
            self._Student__id = id.get()
            self._Student__name = name.get()
            self._Student__DoB = DoB.get()
            if (self.validate_id(self._Student__id) == False or self.validate_name(self._Student__name) == False or self.validate_DoB(self._Student__DoB) == False):
                messagebox.showerror("Error", "Invalid input")
            else:
                clear_status()
                self.set_information_student(l_student)
                messagebox.showinfo("Update", "Update SUCCESSFUL")
                status = Label(frame3, text=tabulate.tabulate(l_student)).pack(expand=True)

        id_t = Label(frame2, text = "ID")
        id_t.pack(side = 'left')
        id = Entry(frame2)
        id.pack(side = 'left')

        name_t = Label(frame2, text = "Name")
        name_t.pack(side = 'left')
        name = Entry(frame2)
        name.pack(side = 'left')

        DoB_t = Label(frame2, text = "Date of Birth")
        DoB_t.pack(side = 'left')
        DoB = Entry(frame2)
        DoB.pack(side = 'left')

        submit = Button(frame2, text="Submit", command= lambda: Submit_student())
        submit.pack(side = 'left')

    def input_information_course(self):
        clear_frame()
        def Submit_course():
            self._Course__id = id.get()
            self._Course__name = name.get()
            self._Course__Credit = credit.get()

            if (self.validate_id(self._Course__id) == False or self.validate_name(self._Course__name) == False or self.validate_Credit(self._Course__Credit) == False):
                messagebox.showerror("Error", "Invalid input")
            else:
                clear_status()
                self.set_information_course(l_course)
                messagebox.showinfo("Update", "Update SUCCESSFUL")
                status = Label(frame3, text=tabulate.tabulate(l_student, headers="keys")).pack()

        id_t = Label(frame2, text = "ID")
        id_t.pack(side='left')
        id = Entry(frame2)
        id.pack(side = 'left')

        name_t = Label(frame2, text = "Name")
        name_t.pack(side='left')
        name = Entry(frame2)
        name.pack(side='left')

        credit_t = Label(frame2, text = "Credit")
        credit_t.pack(side='left')
        credit = Entry(frame2)
        credit.pack(side='left')

        submit = Button(frame2, text="Submit", command= lambda: Submit_course())
        submit.pack(side='left')

    def set_information_student(self, list):
        info = {'ID': self._Student__id,
                'name': self._Student__name,
                'DoB': self._Student__DoB}
        list.append(info)

    def set_information_course(self, list):
        info = {'ID': self._Course__id,
                'name': self._Course__name,
                'Credit': int(self._Course__Credit)}
        list.append(info)
        return list
