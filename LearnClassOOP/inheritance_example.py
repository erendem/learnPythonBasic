class Employee:

    employee_main_value = 15

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def show_info_who_i_am(self):
        return "Sadece Employee, spesifik sınıf değil"


class Engineer(Employee):

    def __init__(self, name, age, gender, marital):
        super().__init__(name, age, gender)
        self.marital = marital

    def show_info_who_i_am(self):
        return "Mühendis !!"


class Expert(Employee):
    employee_main_value = 400

    def show_info_who_i_am(self):
        return "Uzmanım !!"



employee_1 = Employee("Eren", 28, 'male')
engineer_1 = Engineer("Ahmet", 30, 'male', 'Married')
expert_1 = Expert("Ahmet", 30, 'male')

print(employee_1.show_info_who_i_am())
print(engineer_1.show_info_who_i_am())
print(expert_1.show_info_who_i_am())

print(employee_1.employee_main_value)
print(engineer_1.employee_main_value)
print(expert_1.employee_main_value)