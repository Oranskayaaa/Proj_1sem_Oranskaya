# Составить программу, в которой функцию построит изображение, в котором в первой строке 1 звездочка, во второй-2, в
# третьей-3, ..., в строке с номером m-m звездочек.

def zvezda():  # функция
    m = int(input("Введите номер строки: "))  # ввод m
    i = 0
    while i <= m:  # цикл с шагом +1
        print((m + i) * '' + i * '*')
        i += 1
zvezda() # вызов функции