import turtle
import random

def quadrado(posx, posy, angulo, lado, cor):
    # Prepara
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.setheading(angulo)
    turtle.pencolor(cor)

    # Desenha

    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.hideturtle()

def quad_concent(num, lado, incremento, posx, posy, angulo):
    # Prepara
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.setheading(angulo)

    # Cores
    cores = ('red', 'green', 'blue', 'yellow', 'pink', 'orange', 'black')

    for i in range(num):
        cor = cores[i % len(cores)]  # <-- Percebe para que serve?
        quadrado(posx, posy, angulo, lado, cor)
        posx = posx - incremento / 2
        posy = posy - incremento / 2
        lado = lado + incremento

def quad_concent_b(num, lado, incremento, posx, posy, angulo):
    # Prepara
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.setheading(angulo)

    # Cores
    cores = ('red', 'green', 'blue', 'yellow', 'pink', 'orange', 'black')

    for i in range(num):
        indice = random.randint(0, len(cores) - 1)
        cor = cores[indice]
        quadrado(posx, posy, angulo, lado, cor)
        posx = posx - incremento / 2
        posy = posy - incremento / 2
        lado = lado + incremento

if __name__ == '__main__':
    # quad_concent(10,30,15,0,0,0)
    quad_concent_b(10, 30, 15, 0, 0, 0)
    turtle.exitonclick()