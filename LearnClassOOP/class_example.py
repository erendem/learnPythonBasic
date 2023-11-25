class Employee:

    inflation_amount = 1.25

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + "." + last_name + "@bilmemne.com"


    def __repr__(self):
        """ Yazılımlara çağrıldığında neyin/nasıl temsil ediliği hakkında detay bilgi verir """
        return f"Employee('{self.first_name}','{self.last_name}','{self.salary}')"

    def __str__(self):
        """Son kullanıcıya ilgili class'ın nasıl gözüktüğünü nasıl temsil edildiğini ifade eder."""
        return f"{self.last_name} - {self.email}"

    def __add__(self, other):
        """ magic methodu toplama işlemini söyler normalde employee sınıfında toplama methodu yokken yazılıp dekore edilebilir.
            bununla beraber + operatörüyle beraber kullanıldığında çalışır +'nın sol tarafı self kısmını sağ tarafı da other kısmına denk gelir.
        """
        return self.salary + other.salary

    def apply_inflation(self):
        self.salary *= self.inflation_amount


    @classmethod
    def change_inflation_amount_all_class(cls, new_value):
        """ Class methodları tüm sınıfın değerini değiştirir, instance olarak çağrılsa da tüm sınıf etkilenir. """
        cls.inflation_amount = new_value

    @staticmethod
    def some_calculations(value_1, value_2):
        """ static methodlar self ve cls özelliği olmadan hesaplanan veya bazı bilgileri döndürmek amacıyla yazılan methodlardır."""
        return value_1 + value_2


e1 = Employee('eren', 'demir', 5000)
e2 = Employee('test', 'somename', 5500)

print(e1.email)

print(e1.inflation_amount)
print(e2.inflation_amount)
Employee.inflation_amount = 1.35  # class attribute (tüm class'ın enflasyon oranını değiştirir.)
print(e1.inflation_amount)
print(e2.inflation_amount)

e1.inflation_amount = 1.45  # instance attribute(sadece e1 instance'ını yani class örneğinin değerini değiştirir)
print(e1.inflation_amount)
print(e2.inflation_amount)

print("REPR-->", e1.__repr__())
print("Default __str__ varsa onu çağırır ---> ", e1)

print(e1.salary)
e1.apply_inflation()
print(e1.salary)

print(e1 + e2)