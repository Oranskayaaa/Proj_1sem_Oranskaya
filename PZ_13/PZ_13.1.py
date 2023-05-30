'''В матрице найти среднее арифметическое положительных элементов.'''

matrix = [[1, -2, 3], [4, -5, 6], [-7, 8, -9]]

positive_numbers = []
for row in matrix:
    for number in row:
        if number > 0:
            positive_numbers.append(number)

if len(positive_numbers) > 0:
    average = sum(positive_numbers) / len(positive_numbers)
    print("Среднее арифметическое положительных элементов:", average)
else:
    print("Положительные элементы отсутствуют")


