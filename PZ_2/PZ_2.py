#С начала суток прошло N секунд (N-целое). Найти количество секунд, прошедших с начала последней минуты.
try:
    N=int(input("Введите количество секунд"))
    print("секунд с последней минуты", N%3600)
except ValueError:
   print("Неверно введены данные")