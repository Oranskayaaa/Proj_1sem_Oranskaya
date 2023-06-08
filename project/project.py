from tkinter import *
import random

# константы
window_width = 800  #окно
window_heigh = 500
margin = 60  # отступ
fon_color = "white"
button_color = "white"
text_color = "black"
human_color = "black"
label_word = []  # список подчеркиваний
button_alf = []  # список кнопок

def start_pos():  # строим виселицу
    line_1 = canvas.create_line(margin, window_heigh - margin, margin, margin, width=4)
    line_2 = canvas.create_line(margin, margin, window_width // 3, margin, width=4)
    line_3 = canvas.create_line(window_width // 3, margin, window_width // 3, margin * 2, width=4)

def start_alf():  # создаем и выстраиваем кнопки
    shift_x = shift_y = 0
    count = 0

    for c in range(ord("А"), ord("Я") + 1):
        button = Button(text=chr(c), background=button_color, foreground=text_color,
                        font="Arial 12", relief=SOLID)
        button.place(x=window_heigh - margin * 2 + shift_x, y=margin * 4.5 - shift_y)
        button.bind("<Button-1>", lambda event:check_alf(event, word))
        button_alf.append(button)
        shift_x += 45
        count += 1

        if (count == 8):
            shift_x = count = 0
            shift_y -= 45

def start_word():  # считываем файл и заносим слова
    f = open("words.txt")
    count = 0

    for s in f:
        count += 1

    num_word = random.randint(1, count)
    word = ""
    count = 0

    f = open("words.txt", encoding="utf-8")

    for s in f:
        count += 1

        if (count == num_word):
            word = s[:len(s) - 1:]

    word = word.upper()
    return word

def start_dash(word):  # ставим черточки
    shift = 0

    for i in range(len(word)):
        label_under = Label(window, text="_", font="Arial 12", background=fon_color)
        label_under.place(x=window_heigh - margin * 2 + shift, y=margin * 3.5)
        shift += 20
        label_word.append((label_under))

def human(lifes):  # строим человечка
    if (lifes == 6):
        head = canvas.create_oval(window_width // 3 - 40, margin * 1.5,
                                   window_width // 3 + 40, margin * 2.5, fill=human_color)
    elif (lifes == 5):
        body = canvas.create_oval(window_width // 3 - 25, margin * 2.5,
                                   window_width // 3 + 25, margin * 5, fill=human_color)
    elif (lifes == 4):
        l_hand = canvas.create_line(window_width // 3 - 15, margin * 3.5,
                                   window_width // 3 - 105, margin * 2.4, width=5, fill=human_color)
    elif (lifes == 3):
        r_hand = canvas.create_line(window_width // 3 + 15, margin * 3.5,
                                   window_width // 3 + 105, margin * 2.4, width=5, fill=human_color)
    elif (lifes == 2):
        l_foot = canvas.create_line(window_width // 3 - 15, margin * 4.5,
                                   window_width // 3 - 110, margin * 7, width=7, fill=human_color)
    elif (lifes == 1):
        r_foot = canvas.create_line(window_width // 3 + 15, margin * 4.5,
                                   window_width // 3 + 110, margin * 7, width=7, fill=human_color)
    elif (lifes == 0):
        game_over("lose")
        
def check_alf(event, word):  # функция, передающая слово и происходящее событие
    alf = event.widget["text"]
    pos = []

    for i in range(len(word)):
        if (word[i] == alf):
            pos.append(i)

    if (pos):
        for i in pos:
            label_word[i].config(text="{}".format(word[i]))

        count_alpha = 0

        for i in label_word:
            if (i["text"].isalpha()):
                count_alpha += 1

        if (count_alpha == len(word)):
            game_over("win")
    else:
        lifes = int(label_life.cget("text")) - 1

        if (lifes != -1):
             label_life.config(text=" {}".format(lifes))
        human(lifes)

def game_over(status):  # присваеваем статус итогу игры
    for button in button_alf:
        button.destroy()

    if(status == "win"):
        canvas.create_text(canvas.winfo_width()/1.5, canvas.winfo_height()/2, font="Arial 30", text="Поздравляю!\nТы победил!")
    else:
        canvas.create_text(canvas.winfo_width()/1.5, canvas.winfo_height()/2, font="Arial 30", text=" Увы,\n попробуй ещё раз")

window = Tk()  # присваеваем имя окну
window.title("Виселица")
window.resizable(False, False)

lifes = 7  # строим окно с жизнями
label_text = Label(window, text="Попыток:", font="Arial 25")
label_text.place(x=600, y=10)
label_life = Label(window, text="{}".format(lifes), font="Arial 25")
label_life.place(x=750, y=10)

canvas = Canvas(window, bg=fon_color, height=window_heigh, width=window_width)
canvas.place(x=0, y=70)

window.geometry("800x580")  # размер окна
# вызываем функции
start_pos()
start_alf()
word = start_word()
start_dash(word)
human(lifes)

window.mainloop()  # запуск игры