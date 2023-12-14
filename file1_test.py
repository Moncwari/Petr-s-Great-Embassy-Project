from tkinter import *
from tkinter import messagebox
import time
import tkinter as tk
from tkinter.ttk import Radiobutton
from tkinter import ttk
import pytest
from Project import  *


def test_animation_fwd():
    with pytest.raises(WrongCoordinatsExceptionX):
        animation_fwd([[20000, 261, 1050, 200, 923, 216]], 1, 0)
    with pytest.raises(WrongCoordinatsExceptionY):
        animation_fwd([[1200, 20000, 1050, 200, 923, 216]], 1, 0)
    


def test_animation_bwd():
    with pytest.raises(WrongCoordinatsExceptionX):
        animation_bwd([[20000, 261, 1050, 200, 923, 216]], 1, 0)
    with pytest.raises(WrongCoordinatsExceptionY):
        animation_bwd([[1200, 20000, 1050, 200, 923, 216]], 1, 0)

'''
win = tk.Tk()
win.title('Тестирование по Великому посольтву Петра')
win.geometry('1920x1080')
win.mainloop()

question1 = ['Вопрос номер один', 'Вариант номер 1', 'Вариант номер 2', 'Вариант номер 3', 'Вариант номер 4', 'Вариант номер 5', 1, -1, -2, -3, -4, 1]
question2 = ['Вопрос номер два', 'Вариант номер 1', 'Вариант номер 2', 'Вариант номер 3', 'Вариант номер 4', 'Вариант номер 5', 1, 1, -1, -1, -1, 2]
question3 = ['Вопрос номер три', 'Вариант номер 1', 'Вариант номер 2', 'Вариант номер 3', 'Вариант номер 4', 'Вариант номер 5']
All_question = [question1,question2,question3]
global question_index
question_index = 0
def test_one_answer():
    global question_index
    question_index = 0
    answer_var = Mock()
    answer_var.get = 1
    answer = Mock()
    only_one_answer()
    answer.assert_called_with(tk.Label(win, text = 'Это правильный ответ, молодец!',font=('Times new Roman', 13)))


def test_one_answer_check():
    ...

def test_many_answer():
    ...

def test_many_answer_check():
    ...

def test_comparison_answer():
    ...

def test_comparison_answer_check():
    ...

def test_show_results():
    ...

'''