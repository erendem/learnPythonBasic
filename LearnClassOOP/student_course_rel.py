class Student:
    number_of_student = 0

    def __init__(self, name, age, grade):
        self.__name = name
        self.age = age
        self.grade = grade
        Student.number_of_student += 1

    @property
    def return_name_from_private(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def show_student_info(self):
        return self.__name + " - " + str(self.grade)


class Course:

    def __init__(self, name, student_capacity):
        self.name = name
        self.student_capacity = student_capacity
        self.student_list = []

    def add_student(self, student):
        if len(self.student_list) < self.student_capacity:
            self.student_list.append(student)
            print("{} Öğrenci eklendi".format(student.return_name_from_private))
        else:
            print("kontenjan dolduğu için {} eklenemedi".format(student.return_name_from_private))

    def delete_student(self, student):
        if student in self.student_list:
            print("{} öğrenci dersten silindi".format(student.return_name_from_private))
            self.student_list.remove(student)
        else:
            print("Silinecek Öğrenci bulunamadı")

    def show_all_students_name_of_course(self):
        for student in self.student_list:
            print(student.return_name_from_private) # return_name_from_private ismi private yaptığımız için property decoratörüyle erişiyoruz

    def calc_average_grade(self):

        total_grade = sum([i.grade for i in self.student_list])

        return total_grade / len(self.student_list)


s1 = Student("Eren", 25, 95)
s2 = Student("ahmet", 25, 75)
s3 = Student("mehmet", 25, 77)

c1 = Course("Python", 2)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

c1.delete_student(s2)
c1.add_student(s3)
c1.show_all_students_name_of_course()


#print(s1.__name) # error (private attr)
"""property decorator'u bir değişkene method gibi değil de attribute gibi direkt erişmemizi sağlar"""
print(s1.return_name_from_private)
print(s1.show_student_info())
print(c1.calc_average_grade())

print(Student.number_of_student)