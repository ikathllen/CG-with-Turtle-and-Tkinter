import turtle
from tkinter import *

window = Tk() 

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

def write_n(i, j):
    tt = turtle.Turtle()
    tt.shape("turtle")
    tt.color("yellow")
    tt.pen(fillcolor="white", pensize=10)
    tt.speed(6)

    tt.home()
    tt.left(90)
    tt.forward(150)
    tt.right(160)
    tt.forward(150)
    tt.left(160)
    tt.forward(150)
    tt.right(175)

def write_d(i, j):
    tt = turtle.Turtle()
    tt.shape("turtle")
    tt.color("green")
    tt.pen(fillcolor="white", pensize=10)
    tt.speed(6)

    tt.home()
    tt.left(90)
    tt.backward(150)
    tt.right(90)
    tt.circle(80, 180)

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

def third_name():
    turtle.Screen().bgcolor("black")
    screen = turtle.Screen()
    turtle.title("third")
    screen.onclick(write_n)

def fourth_name():
    turtle.Screen().bgcolor("black")
    screen = turtle.Screen()
    turtle.title("fourth")
    screen.onclick(write_d)

window.title('CG-with-Turtle-and-Tkinter')
botao1 = Button(window, text='first name', width=20, bg = '#ffb6c1', command=first_name)
botao1.place(x=0, y=10)
botao2 = Button(window, text='second name', width=20, bg = '#ffb6c1', command=second_name)
botao2.place(x=0, y=40)
botao3 = Button(window, text='third name', width=20, bg = '#ffb6c1', command=third_name)
botao3.place(x=0, y=70)
botao4 = Button(window, text='fourth name', width=20, bg = '#ffb6c1', command=fourth_name)
botao4.place(x=0, y=100)

window.mainloop()
