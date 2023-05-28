'''Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
"Человек". Каждый класс должен иметь метод, который выводит информацию о
поле объекта'''

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_sex(self):
        print("Пол:", self.sex)


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Мужчина")


class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Женщина")

man = Man("Анатолий", 30)
woman = Woman("Мария", 25)

man.print_sex()
woman.print_sex()