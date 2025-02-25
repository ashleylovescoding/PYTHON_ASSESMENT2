class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        return f"{self.name}, {self.age}, {self.salary}"

    def display_info2(self):
        return f" {self.name}, a {self.age}-year-old earning {self.salary} a month"

person1 = Person("Ashley", "21", "1.7 million")
print(person1.display_info())
print(person1.display_info2())
