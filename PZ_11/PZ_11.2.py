'''Из предложенного текстового файла (text18-26.txt) вывести на экран его содержимое, количество знаков препинания.
Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив все знаки пунктуации
на знак «/».'''

# чтение файла, вывод его содержимого
f1 = open("text18-26.txt", "r", encoding="UTF-8")
f2 = f1.read()
for k in f2:
    print(k, end='')

score = 0 # счетчик
# цикл подсчитывающий знаки препинаний
for i in range(len(f2)):
    if f2[i] in ",.;:/?!..--":
        score += 1
f1.close()

print(f"\nКоличество знаков препинаний: {score}")  # вывод количества знаков препинаний

list_2 = list()  # создание пустого списка

# создание второго файла
f2 = open("text_2.txt", "r", encoding="UTF-8")
for i in f2.readlines():
    list_2.append(i)
f2.close()

# замена знаков пунктуация на "/"
f3 = open("text_2.txt", "w", encoding="UTF-8")
for k in range(len(list_2)):
    for n in range(len(list_2[k])):
        if list_2[k][n] in ",.!?'>>:;-":
            f3.write("/")
        else:
            f3.write(list_2[k][n])