'''Составить генератор (yield), который выводит из строки только буквы.'''

a = str(input("Задайте содержимое строки: "))

def vvod(n):  # генератор yield
    for i in n:
        if i.isalpha():
            yield i

b = [i for i in vvod(a)]
print("Буквы из строки: ", *b)
