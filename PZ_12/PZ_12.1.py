'''В последовательности их N чисел (N –четное) во второй ее половине найти сумму
элементов больших 10.'''

from random import *

a = int(input("Введите размер списка: "))

while True:  # цикл с условием
    if a % 2 == 0:
        break

spisok = [randint(0, 20) for n in range(a)]
spisok = [f for f in spisok[a//2:] if f > 10]
print("Сумма элементов второй половины списка, больших 10 равна:", sum(spisok))