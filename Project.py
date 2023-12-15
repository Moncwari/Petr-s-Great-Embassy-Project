from tkinter import *
from tkinter import messagebox
import time
import tkinter as tk
from tkinter.ttk import Radiobutton
from tkinter import ttk
# Заимствований кода из учебников или других проектов не было

root = Tk()
root.geometry("1920x1080")

global question_index
question_index = 0

frame_0 = Frame(root, height=1920, width=1080)
frame_0.place(x=0, y=0)
canvas = Canvas(frame_0, width=1920, height=1080)
python_image_0 = PhotoImage(file="Petr_I.png")
canvas.create_image(160, 0, anchor="nw", image=python_image_0)
canvas.pack(fill="both")
canvas.create_text(
    800,
    30,
    text="Великое посольство Петра I",
    fill="#e5404b",
    font=(
        "Times new Roman",
         40))
Button(frame_0, text="К карте", font=("Times new Roman", 20), bg="white",
       activebackground="white", borderwidth=1.5, relief="solid",
       command=lambda: frame_1.tkraise()).place(x=1200, y=700)
Button(
    frame_0,
    text="К вопросам",
    font=(
        "Times new Roman",
        20),
    bg="white",
    activebackground="white",
    borderwidth=1.5,
    relief="solid",
    command=lambda: frame_2.tkraise()).place(
    x=200,
    y=700)


frame_1 = Frame(root, height=1920, width=1080)
frame_1.place(x=0, y=0)
canvas = Canvas(frame_1, width=1920, height=1080)
python_image_1 = PhotoImage(file="Karta_pustaya.png")
Button(frame_1, text="На главную", font=("Times new Roman", 13),
       command=lambda: frame_0.tkraise()).place(x=80, y=730)
Button(frame_1, text="К вопросам", font=("Times new Roman", 13),
       command=lambda: frame_2.tkraise()).place(x=200, y=730)


def map_background():
    """Функция размещения на холсте изображения пустой карты без стрелок
    Верхний левый угол карты совпадает с верхним левым углом холста
    """
    canvas.create_image(0, 0, anchor="nw", image=python_image_1)
    canvas.pack(fill="both")

def show_info():
    return messagebox.showinfo(title=", ".join(text), message=self.story)


def animation_fwd(coords, obj, line):
    """Функция передвижения кареты на 1 стрелку вперёд

    :param coords: Список координат маршрута
    :type coords: list (matrix)
    :param obj: Передвигающийся объект
    :type obj: canvas figure
    :param line: Номер стрелки, по которой будет передвигаться объект
    :type line: int
    :raises WrongCoordinatsExceptionX: Если x-координата города вылетает за пределы холста
    :raises WrongCoordinatsExceptionY: Если y-координата города вылетает за пределы холста
    """
    if (any((coords[line][x] > 1920 or coords[line][x] < 0)
            for x in range(0, len(coords[line]) - 1, 2))):
        raise WrongCoordinatsExceptionX
    if (any((coords[line][y] > 1080 or coords[line][y] < 0)
            for y in range(1, len(coords[line]) - 1, 2))):
        raise WrongCoordinatsExceptionY
    for i in range(2, len(coords[line]) - 1, 2):
        canvas.move(obj,
                    coords[line][i] - coords[line][i - 2],
                    coords[line][i + 1] - coords[line][i - 1])
        frame_1.update()
        frame_1.after(50)


def animation_bwd(coords, obj, line):
    """Функция передвижения кареты на 1 стрелку назад

    :param coords: Список координат маршрута
    :type coords: list (matrix)
    :param obj: Передвигающийся объект
    :type obj: canvas figure
    :param line: Номер стрелки, по которой будет передвигаться объект
    :type line: int
    :raises WrongCoordinatsExceptionX: Если x-координата города вылетает за пределы холста
    :raises WrongCoordinatsExceptionY: Если y-координата города вылетает за пределы холста
    """
    if (any((coords[line][x] > 1920 or coords[line][x] < 0)
            for x in range(0, len(coords[line]), 2))):
        raise WrongCoordinatsExceptionX
    if (any((coords[line][y] > 1080 or coords[line][y] < 0)
            for y in range(1, len(coords[line]), 2))):
        raise WrongCoordinatsExceptionY
    for j in range(len(coords[line]) - 2, 1, -2):
        canvas.move(obj,
                    coords[line][j - 2] - coords[line][j],
                    coords[line][j - 1] - coords[line][j + 1])
        frame_1.update()
        frame_1.after(50)


def click_1(event):
    """Функция клика на кнопку "вперёд"
    Вызывет функцию animation_fwd продвижения кареты на 1 стрелку вперёд
    """
    global arrows
    global cities
    global ball
    global line
    if line < len(arrows) - 1:
        line += 1
        animation_fwd(arrows, ball, line)
        messagebox.showinfo(title=", ".join(cities[line+1][4:]), message=cities[line+1][3])


def click_2(event):
    """Функция клика на кнопку "назад"
    Вызывет функцию animation_bwd продвижения кареты на 1 стрелку назад
    """
    global arrows
    global cities
    global ball
    global line
    if line > -1:
        animation_bwd(arrows, ball, line)
        line -= 1
        messagebox.showinfo(title=", ".join(cities[line+1][4:]), message=cities[line+1][3])


class WrongCoordinatsExceptionX(Exception):
    ...


class WrongCoordinatsExceptionY(Exception):
    ...


class City:
    """Класс городов маршрута

    :param x: x-координата города
    :type x: int
    :param y: y-координата города
    :type y: int
    :param size: Размер кружка, обозначающего город
    :type size: str
    :param story: Информация, появляющаяся при нажатии на название города
    :type story: str
    :param args: Название города и дата прибытия (если имеется)
    :type args: str
    """

    def __init__(self, x, y, size, story, *args):
        self.x = x
        self.y = y
        self.size = size
        self.story = story
        self.info = args[0]

    def draw(self):
        """Функция отрисовки кружочка города
        """
        if self.size == "small":
            canvas.create_oval(self.x - 3, self.y - 3, self.x + 3, self.y + 3,
                               fill="white")
        else:
            canvas.create_oval(self.x - 6, self.y - 6, self.x + 6, self.y + 6,
                               fill="white")

    def button(self):
        """Функция создания кнопки с названием города
        Для предоставления информации по нему
        """
        text = self.info

        def show_info():
            return messagebox.showinfo(
                title=", ".join(text), message=self.story)

        btn = Button(
            frame_1,
            command=show_info,
            text=text[0],
            font=(
                "Times new Roman",
                8))
        btn.config(
            bg="white",
            bd=0,
            activebackground="white",
            borderwidth=1.5,
            relief="solid")
        if text[0] in [
            "Псков",
            "Рига",
            "Саардам",
            "Лондон",
            "Портсмут",
                "Краков"]:
            btn.place(anchor="se", height=15, width=75, x=self.x, y=self.y - 5)
        else:
            btn.place(
                anchor="nw",
                height=15,
                width=75,
                x=self.x + 10,
                y=self.y - 7)


class Arrow:
    """Класс стрелок, формирующих маршрут

    :param coords: Список координат, через которые проходит стрелка
    :type coords: str
    """

    def __init__(self, coords):
        self.coords = coords

    def draw(self):
        """Функция отрисовки стрелки
        """
        canvas.create_line(
            *self.coords,
            fill="#d94ec2",
            width=2,
            arrow="last",
            arrowshape=[
                9,
                9,
                4])


map_background()

cities = []
with open("cities.txt", "r", encoding="utf-8") as f:
    for line in f:
        cities.append(line[:-1].split("; "))

for i in cities:
    city = City(int(i[0]), int(i[1]), i[2], i[3], i[4:])
    City.draw(city)
    City.button(city)


arrows = []
with open("arrows.txt", "r") as f:
    for line in f:
        line = [int(coord) for coord in line.split()]
        arrows.append(line)

for i in arrows:
    arrow = Arrow(i)
    Arrow.draw(arrow)


ball = canvas.create_oval(
    arrows[0][0] - 7,
    arrows[0][1] - 7,
    arrows[0][0] + 7,
    arrows[0][1] + 7,
    fill="#d6d00f")
line = -1

btn_fwd = Button(frame_1, text="Вперёд", font=("Times new Roman", 15),
                 bg="#2fba2d", bd=0, activebackground="#5efc5b")
btn_fwd.place(anchor="nw", height=30, width=100, x=1100, y=700)
btn_fwd.bind("<Button-1>", click_1)

btn_bwd = Button(
    frame_1,
    text="Назад",
    font=(
        "Times new Roman",
        15),
    bg="#cc2135",
    bd=0,
    activebackground="#fa5757")
btn_bwd.place(anchor="nw", height=30, width=100, x=1100, y=750)
btn_bwd.bind("<Button-1>", click_2)


frame_2 = Frame(root, height=1080, width=1920)
frame_2.place(x=0, y=0)
Button(frame_2, text="На главную", font=("Times new Roman", 13),
       command=lambda: frame_0.tkraise()).place(x=80, y=730)
Button(frame_2, text="К карте", font=("Times new Roman", 13),
       command=lambda: frame_1.tkraise()).place(x=200, y=730)

Counter = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
question1 = ['Губернатор какой страны был в Риге во время посольства?',
             'Швеция', 'Франция', 'Испания', 'Пруссия', 'Голландия', 1, -1, -2, -3, -4, 1]
question2 = ['На каких языках написали овации Петру в Минтаве?', 'На немецком',
             'На французском', 'На латинском', 'На русском', 'На греческом', 1, -1, 1, -1, 1, 3]
question3 = ['Под каким именем Пётр участвовал в посольстве?', 'Григорий Меньшиков',
             'Иван Потёмкин', 'Пётр Михайлов', 'Фёдор Разумовский', 'Александр Трубецкой', -1, -2, 1, -3, -4, 1]
question4 = ['Когда был заключён тайный договор между Петром и Августом 2?', '25 августва 1698',
             '21 ноября 1699', '25 октября 1699', '14 февраля 1698', '3 сентября 1700', -1, 1, -2, -3, -4, 1]
question5 = ['Сколько дней Пётр провёл в Зандаме?', '40 дней',
             '7 дней', '13 дней', '8 дней', '21 день', -1, -2, -3, 1, -4, 1]
question6 = ['Где Пётр начал изучать артиллерийское дело?', 'В Пиллау',
             'В Стальгорне', 'В Эреборе', 'В Перу', 'В Браге', 1, -1, -2, -3, -4, 1]
question7 = ['Где Пётр познакомился с двумя Софиями?', 'В таверне', 'В публичном доме',
             'В Коппенбрюгге', 'В Курфюршестве', 'В Лондоне', -1, -2, 1, -3, -4, 1]
question8 = ['На какой Пётр жил в Зандаме?', 'На улице Кринж', 'На улице Крид',
             'На улице Крит', 'На улице Кримп', 'На улице Крип', -1, -2, -3, 1, -4, 1]
question9 = ['Сколько Пётр вручил в Лондоне актрисе Летиции Кросс в качестве подарка?',
             '500 фунтов', '300 долларов', 'чеканную монету', '1000 рублей', '350 крон', 1, -1, -2, -3, -4, 1]
question10 = [
    'Расставьте посещённые города в хронологическом порядке:',
    'Рига',
    'Смоленск',
    'Псков',
    'Лондон',
    'Псков',
    'Рига',
    'Лондон',
    'Смоленск']
question11 = ['Название корабля, заложенного и построенного Волонтёрами в Голландии?', 'Павел и Пётр',
              'Пётр и Павел', 'Пётр Великий', 'Павел Петрович', 'Пётр Павлович', -1, 1, -2, -3, -4, 1]
question12 = [
    'Расставьте посещённые города в хронологическом порядке:',
    'Рига',
    'Рава Русская',
    'Кёнигсберг',
    'Портсмунд',
    'Рига',
    'Кёнигсберг',
    'Портсмунд',
    'Рава Русская']
question13 = ['Дата приезда в Минтаву:', '8 августа 1697', '8 марта 1697',
              '8 апреля 1697', '8 июня 1697', '8 февраля 1697', -1, -2, 1, -3, -4, 1]
question14 = ['На каком корабле Пётр плыл из Минтавы в Кёнигсберг?', 'Святой Брут',
              'Святой Пётр', 'Святой Иуда', 'Святой Патрик', 'Святой Георгий', -1, -2, -3, -4, 1, 1]
question15 = ['С кем якобы встречался Пётр на монетном дворе Англии?', 'С Джеймсом Куком',
              'С Гаем Юлием Цезарем', 'С Наполеоном', 'C Исааком Ньютоном', 'С Суворовым', -1, -2, -3, 1, -4, 1]
question16 = ['Где Пётр встретился с Августом 2?', 'В Раве Прусской',
              'В Кёнигсберге', 'В Минтаме', 'В Пиллау', 'В Раве Русской', -1, -2, -3, -4, 1, 1]
question17 = ['Когда Пётр вернулся в Москву?', '25 августа 1698', '27 августа 1698',
              '23 августа 1699', '25 августа 1699', '23 августа 1698', 1, -1, -2, -3, -4, 1]
All_question = [
    question1,
    question2,
    question3,
    question4,
    question5,
    question6,
    question7,
    question8,
    question9,
    question10,
    question11,
    question12,
    question13,
    question14,
    question15,
    question16,
    question17]


def only_one_answer():
    """Returns question with only one answer
    """
    def only_one_answer_check():
        """Returns the correctness of the response

        :returns: ans
        :rtype: int
        """
        if answer_var.get() == All_question[question_index][-1]:
            answer = tk.Label(
                frame_2, text='Это правильный ответ, молодец!', font=(
                    'Times new Roman', 13))
            answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
            ans = 1
            Counter[question_index] = ans
        else:
            answer = tk.Label(
                frame_2, text='Лучше подумай ещё раз.', font=(
                    'Times new Roman', 13))
            answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
            ans = 0
            Counter[question_index] = ans
        return ans

    Title = tk.Label(
        frame_2,
        text=All_question[question_index][0],
        font=(
            'Times new Roman',
            15))
    Title.place(relx=0.25, y=216, relwidth=0.5, height=54)

    answer_var = tk.IntVar()
    variant1 = tk.Radiobutton(
        frame_2,
        text=All_question[question_index][1],
        font=(
            'Times new Roman',
            13),
        variable=answer_var,
        value=All_question[question_index][6])
    variant2 = tk.Radiobutton(
        frame_2,
        text=All_question[question_index][2],
        font=(
            'Times new Roman',
            13),
        variable=answer_var,
        value=All_question[question_index][7])
    variant3 = tk.Radiobutton(
        frame_2,
        text=All_question[question_index][3],
        font=(
            'Times new Roman',
            13),
        variable=answer_var,
        value=All_question[question_index][8])
    variant4 = tk.Radiobutton(
        frame_2,
        text=All_question[question_index][4],
        font=(
            'Times new Roman',
            13),
        variable=answer_var,
        value=All_question[question_index][9])
    variant5 = tk.Radiobutton(
        frame_2,
        text=All_question[question_index][5],
        font=(
            'Times new Roman',
            13),
        variable=answer_var,
        value=All_question[question_index][10])
    variant1.place(relx=0.25, y=270, relwidth=0.5, height=54)
    variant2.place(relx=0.25, y=324, relwidth=0.5, height=54)
    variant3.place(relx=0.25, y=378, relwidth=0.5, height=54)
    variant4.place(relx=0.25, y=432, relwidth=0.5, height=54)
    variant5.place(relx=0.25, y=486, relwidth=0.5, height=54)

    get_answer = tk.Button(frame_2, text='Проверить ответ', font=(
        'Times new Roman', 13), command=only_one_answer_check)
    get_answer.place(relx=0.4, y=540, relwidth=0.2, height=54)


def only_one_answer_check(answer_var_get, question_index):
    """Returns the correctness of the response

    :param answer_var: sinonimous to answer_var.get()
    :type answer_var: int
    :param question_index: index of question
    :type question_index: int
    :returns: ans
    :rtype: int
    """
    if answer_var_get == All_question[question_index][-1]:
        answer = tk.Label(
            frame_2, text='Это правильный ответ, молодец!', font=(
                'Times new Roman', 13))
        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
        ans = 1
        Counter[question_index] = ans
    else:
        answer = tk.Label(
            frame_2, text='Лучше подумай ещё раз.', font=(
                'Times new Roman', 13))
        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
        ans = 0
    Counter[question_index] = ans
    return ans


def many_answers():
    """Returns question with many answers
    """
    def answer_check():
        """Returns the correctness of the response

        :returns: ans
        :rtype: int
        """
        count_of_answer = answer1.get() + answer2.get() + answer3.get() + \
            answer4.get() + answer5.get()
        if count_of_answer == All_question[question_index][-1]:
            answer = tk.Label(
                frame_2, text='Это правильный ответ, молодец!', font=(
                    'Times new Roman', 13))
            answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
            ans = 1
            Counter[question_index] = ans
        else:
            answer = tk.Label(
                frame_2, text='Лучше подумай ещё раз.', font=(
                    'Times new Roman', 13))
            answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
            ans = 0
            Counter[question_index] = ans
        return ans

    answer1 = tk.IntVar()
    answer2 = tk.IntVar()
    answer3 = tk.IntVar()
    answer4 = tk.IntVar()
    answer5 = tk.IntVar()
    Title = tk.Label(
        frame_2, text=str(
            All_question[question_index][0]), font=(
            'Times new Roman', 15))
    Title.place(relx=0.25, y=216, relwidth=0.5, height=54)
    variant1 = tk.Checkbutton(
        frame_2,
        text=All_question[question_index][1],
        font=(
            'Times new Roman',
            13),
        variable=answer1,
        onvalue=All_question[question_index][6])
    variant2 = tk.Checkbutton(
        frame_2,
        text=All_question[question_index][2],
        font=(
            'Times new Roman',
            13),
        variable=answer2,
        onvalue=All_question[question_index][7])
    variant3 = tk.Checkbutton(
        frame_2,
        text=All_question[question_index][3],
        font=(
            'Times new Roman',
            13),
        variable=answer3,
        onvalue=All_question[question_index][8])
    variant4 = tk.Checkbutton(
        frame_2,
        text=All_question[question_index][4],
        font=(
            'Times new Roman',
            13),
        variable=answer4,
        onvalue=All_question[question_index][9])
    variant5 = tk.Checkbutton(
        frame_2,
        text=All_question[question_index][5],
        font=(
            'Times new Roman',
            13),
        variable=answer5,
        onvalue=All_question[question_index][10])
    variant1.place(relx=0.25, y=270, relwidth=0.5, height=54)
    variant2.place(relx=0.25, y=324, relwidth=0.5, height=54)
    variant3.place(relx=0.25, y=378, relwidth=0.5, height=54)
    variant4.place(relx=0.25, y=432, relwidth=0.5, height=54)
    variant5.place(relx=0.25, y=486, relwidth=0.5, height=54)
    get_answer = tk.Button(
        frame_2, text='Проверить ответ', font=(
            'Times new Roman', 13), command=answer_check)
    get_answer.place(relx=0.4, y=540, relwidth=0.2, height=54)


def many_answer_check(answer_var, question_index):
    """Returns the correctness of the response

    :param answer_var: sinonimous to count_of_answer in answer.check()
    :type answer_var: int
    :param question_index: index of question
    :type question_index: int
    :returns: ans
    :rtype: int
    """
    if answer_var == All_question[question_index][-1]:
        ans = 1
        answer = tk.Label(
            frame_2, text='Это правильный ответ, молодец!', font=(
                'Times new Roman', 13))
        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
        Counter[question_index] = ans
    else:
        answer = tk.Label(
            frame_2, text='Лучше подумай ещё раз.', font=(
                'Times new Roman', 13))
        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
        ans = 0
        Counter[question_index] = ans
    return ans


def comparison_answer():
    """Returns question with comparison
    """
    def comparison_answer_check():
        """Returns the correctness of the response

        :returns: ans
        :rtype: int
        """
        if combo1.get() == right_answer1:
            if combo2.get() == right_answer2:
                if combo3.get() == right_answer3:
                    if combo4.get() == right_answer4:
                        answer = tk.Label(
                            frame_2, text='Это правильный ответ, молодец!', font=(
                                'Times new Roman', 13))
                        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
                        ans = 1
                        Counter[question_index] = ans
                    else:
                        answer = tk.Label(
                            frame_2, text='Лучше подумай ещё раз.', font=(
                                'Times new Roman', 13))
                        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
                        ans = 0
                        Counter[question_index] = ans
                else:
                    answer = tk.Label(
                        frame_2, text='Лучше подумай ещё раз.', font=(
                            'Times new Roman', 13))
                    answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
                    ans = 0
                    Counter[question_index] = ans
            else:
                answer = tk.Label(
                    frame_2, text='Лучше подумай ещё раз.', font=(
                        'Times new Roman', 13))
                answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
                ans = 0
                Counter[question_index] = ans
        else:
            answer = tk.Label(
                frame_2, text='Лучше подумай ещё раз.', font=(
                    'Times new Roman', 13))
            answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
            ans = 0
            Counter[question_index] = ans
        return ans

    variants = (
        All_question[question_index][1],
        All_question[question_index][2],
        All_question[question_index][3],
        All_question[question_index][4])

    Title = tk.Label(
        frame_2,
        text=All_question[question_index][0],
        font=(
            'Times new Roman',
            15))
    Title.place(x=481, y=216, widt=960, height=54)

    combo1 = ttk.Combobox(frame_2, state="readonly", values=variants)
    right_answer1 = All_question[question_index][5]
    combo1.place(relx=0.25, y=270, relwidth=0.5, height=54)
    combo2 = ttk.Combobox(frame_2, state="readonly", values=variants)
    right_answer2 = All_question[question_index][6]
    combo2.place(relx=0.25, y=324, relwidth=0.5, height=54)
    combo3 = ttk.Combobox(frame_2, state="readonly", values=variants)
    right_answer3 = All_question[question_index][7]
    combo3.place(relx=0.25, y=378, relwidth=0.5, height=54)
    combo4 = ttk.Combobox(frame_2, state="readonly", values=variants)
    right_answer4 = All_question[question_index][8]
    combo4.place(relx=0.25, y=432, relwidth=0.5, height=54)

    get_answer = tk.Button(frame_2, text='Проверить ответ', font=(
        'Times new Roman', 13), command=comparison_answer_check)
    get_answer.place(relx=0.4, y=486, relwidth=0.2, height=108)


def comp_answer_check(answer_var, question_index):
    """Returns the correctness of the response

    :param answer_var: sinonimous to list of combos.get() in comparison_answer_check()
    :type answer_var: list
    :param question_index: index of question
    :type question_index: int
    :returns: ans
    :rtype: int
    """
    right_answer1 = All_question[question_index][5]
    right_answer2 = All_question[question_index][6]
    right_answer3 = All_question[question_index][7]
    right_answer4 = All_question[question_index][8]
    if answer_var == [
            right_answer1,
            right_answer2,
            right_answer3,
            right_answer4]:
        answer = tk.Label(
            frame_2,
            text='Это правильный ответ, молодец!',
            font=(
                'Times new Roman',
                13))
        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
        ans = 1
        Counter[question_index] = ans
    else:
        answer = tk.Label(
            frame_2, text='Лучше подумай ещё раз.', font=(
                'Times new Roman', 13))
        answer.place(relx=0.4, y=594, relwidth=0.2, height=54)
        ans = 0
        Counter[question_index] = ans
    return ans


All_right_answer = 0
All_false_answer = 0
not_made = 17


def show_result():
    """Returns result
    """
    All_right_answer = 0
    All_false_answer = 0
    not_made = 17
    for k in Counter:
        if k == 0:
            All_false_answer += 1
            not_made -= 1
        if k == 1:
            All_right_answer += 1
            not_made -= 1
    if All_right_answer == 0 and All_false_answer == 0:
        result = tk.Label(
            frame_2, text='Вы ещё не ответили ни на один вопрос', font=(
                'Times new Roman', 15))  # 756
        result.place(relx=0.25, y=756, relwidth=0.5)
    else:
        if All_right_answer == 0:
            result = tk.Label(
                frame_2,
                text=f'Вы неправильно сделали {All_false_answer}. \n Вы не сделали {not_made}.',
                font=(
                    'Times new Roman',
                    13))
            result.place(relx=0.25, y=756, relwidth=0.5)
        elif All_false_answer == 0:
            result = tk.Label(
                frame_2,
                text=f'Вы правильно сделали {All_right_answer}! \n Вы не сделали {not_made}.',
                font=(
                    'Times new Roman',
                    13))
            result.place(relx=0.25, y=756, relwidth=0.5)
        else:
            result = tk.Label(
                frame_2,
                text=f'Вы правильно сделали {All_right_answer}! \n Вы неправильно сделали {All_false_answer}. \n Вы не сделали {not_made}.',
                font=(
                    'Times new Roman',
                    13))
            result.place(relx=0.25, y=756, relwidth=0.5)


def question_choise():
    global question_index
    """Returns question
    """

    if question_combo.get() == 'Вопрос №1':
        question_index = 0
        only_one_answer()

    elif question_combo.get() == 'Вопрос №2':
        question_index = 1
        many_answers()

    elif question_combo.get() == 'Вопрос №3':
        question_index = 2
        only_one_answer()

    elif question_combo.get() == 'Вопрос №4':
        question_index = 3
        only_one_answer()

    elif question_combo.get() == 'Вопрос №5':
        question_index = 4
        only_one_answer()

    elif question_combo.get() == 'Вопрос №6':
        question_index = 5
        only_one_answer()

    elif question_combo.get() == 'Вопрос №7':
        question_index = 6
        only_one_answer()

    elif question_combo.get() == 'Вопрос №8':
        question_index = 7
        only_one_answer()

    elif question_combo.get() == 'Вопрос №9':
        question_index = 8
        only_one_answer()

    elif question_combo.get() == 'Вопрос №10':
        question_index = 9
        comparison_answer()

    elif question_combo.get() == 'Вопрос №11':
        question_index = 10
        only_one_answer()

    elif question_combo.get() == 'Вопрос №12':
        question_index = 11
        comparison_answer()

    elif question_combo.get() == 'Вопрос №13':
        question_index = 12
        only_one_answer()

    elif question_combo.get() == 'Вопрос №14':
        question_index = 13
        only_one_answer()

    elif question_combo.get() == 'Вопрос №15':
        question_index = 14
        only_one_answer()

    elif question_combo.get() == 'Вопрос №16':
        question_index = 15
        only_one_answer()

    elif question_combo.get() == 'Вопрос №17':
        question_index = 16
        only_one_answer()
    return question_index


number_of_question = (
    'Вопрос №1',
    'Вопрос №2',
    'Вопрос №3',
    'Вопрос №4',
    'Вопрос №5',
    'Вопрос №6',
    'Вопрос №7',
    'Вопрос №8',
    'Вопрос №9',
    'Вопрос №10',
    'Вопрос №11',
    'Вопрос №12',
    'Вопрос №13',
    'Вопрос №14',
    'Вопрос №15',
    'Вопрос №16',
    'Вопрос №17')

question_combo = ttk.Combobox(
    frame_2,
    state="readonly",
    values=number_of_question)
question_combo.place(relx=0.4, y=54, relwidth=0.2)

Title = tk.Label(
    frame_2,
    text='Выберите номер вопроса',
    font=(
        'Times new Roman',
        15))
Title.place(relx=0.25, relwidth=0.5)

get_question = tk.Button(
    frame_2,
    text='Получить вопрос',
    font=(
        'Times new Roman',
        13),
    command=question_choise)
get_question.place(relx=0.4, y=108, relwidth=0.2)

get_last_answer = tk.Button(
    frame_2, text='Посмотреть статистику по вопросам', font=(
        'Times new Roman', 13), command=show_result)
get_last_answer.place(relx=0.4, y=702, relwidth=0.2)


frame_0.tkraise()

root.mainloop()
