import turtle
from tkinter import *

janela = Tk() 

def write_f(i, j):
    tt = turtle.Turtle()
    tt.shape("turtle")
    tt.color("pink")
    tt.pen(fillcolor="white", pensize=10)
    tt.speed(6)

    tt.home()
    tt.right(90)
    tt.forward(150)
    tt.backward(150)
    tt.left(90)
    tt.forward(50)
    tt.backward(50)
    tt.right(90)
    tt.forward(75)
    tt.left(90)
    tt.forward(50)

def write_k(i, j):
    tt = turtle.Turtle()
    tt.shape("turtle")
    tt.color("cyan")
    tt.pen(fillcolor="white", pensize=10)
    tt.speed(2)

    tt.home()
    tt.right(90)
    tt.forward(150)
    tt.backward(75)
    tt.left(130)
    tt.forward(100)
    tt.backward(80)
    tt.right(95)
    tt.forward(100)

def first_name():
    turtle.Screen().bgcolor("black")
    screen = turtle.Screen()
    turtle.title("First")
    screen.onclick(write_f)

def second_name():
    turtle.Screen().bgcolor("black")
    screen = turtle.Screen()
    turtle.title("second")
    screen.onclick(write_k)


janela.title('Atividade-CG ')
botao1 = Button(janela, text='first name', width=20, command=first_name)
botao1.place(x=0, y=10)
botao2 = Button(janela, text='second name', width=20, command=second_name)
botao2.place(x=0, y=40)

janela.mainloop()
