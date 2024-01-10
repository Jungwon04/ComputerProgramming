import math
import turtle

def draw_half_circle(x, y, radius, direction, size=1, p_color='black', f_color=None):
    pen = turtle.Turtle()
    pen.setheading(direction) # 펜의 방향을 설정
    pen.pensize(size)         # 펜의 굵기를 설정
    pen.pencolor(p_color)     # 펜의 색을 설정

    pen.penup()
    pen.goto(x, y)
    pen.pendown()             # 반원을 그릴 준비

    if f_color:               # 채우기 색이 있으면
        pen.fillcolor(f_color) # 반원의 채우기 색 설정
        pen.begin_fill()
        pen.circle(radius, extent=180)
        pen.end_fill()
    else:                     # 채우기 색이 없으면
        pen.circle(radius, extent=180)

    pen.hideturtle()


def draw_rectangle(x, y, w, h, direction, size=1, p_color='black', f_color=None):
    pen = turtle.Turtle()
    pen.setheading(direction)  # 펜의 방향을 설정
    pen.pensize(size)  # 펜의 굵기를 설정
    pen.pencolor(p_color)  # 펜의 색을 설정

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    if f_color:
        pen.fillcolor(f_color)
        pen.begin_fill()
        for side in [w/2, h, w, h, w/2]:
            pen.forward(side)
            pen.left(90)
        pen.end_fill()
    else:
        for side in [w/2, h, w, h, w/2]:
            pen.forward(side)
            pen.left(90)

    pen.hideturtle()


def draw_taegeuk(u, direction):
    pen = turtle.Turtle()
    pen.penup()
    pen.pendown()
    pen.hideturtle()

    x = 1/2*u*3/math.sqrt(13)
    y = 1/2*u*2/math.sqrt(13)

    draw_half_circle(x, -y, u//2, 90 - direction, 1, 'red', 'red')
    draw_half_circle(-x, y, u//2, 270 - direction, 1, 'blue', 'blue')
    draw_half_circle(x, -y, u//4, 90 - direction, 1, 'blue', 'blue')
    draw_half_circle(-x, y, u//4, 270 - direction, 1, 'red', 'red')

    pen.hideturtle()


def draw_guae(kinds_guae, u, direction):   # kind : 궤의 종류
    pen = turtle.Turtle()
    pen.penup()
    pen.pendown()
    pen.hideturtle()

    x = 3/4*u*3/math.sqrt(13)
    y = 3/4*u*2/math.sqrt(13)

    if kinds_guae == 'gun':
        draw_rectangle(-x, y, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(-x*7/6, y*7/6, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(-x*4/3, y*4/3,  u//2, u//12, direction, 1, 'black', 'black')
    elif kinds_guae == 'gon':
        draw_rectangle(x, -y, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(x*7/6, -y*7/6, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(x*4/3, -y*4/3, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(x, -y, u//24, u//12, direction, 1, 'white', 'white')
        draw_rectangle(x*7/6, -y*7/6, u//24, u//12, direction, 1, 'white', 'white')
        draw_rectangle(x*4/3, -y*4/3, u//24, u//12, direction, 1, 'white', 'white')
    elif kinds_guae == 'gam':
        draw_rectangle(x, y, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(x*7/6, y*7/6, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(x*4/3, y*4/3, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(x, y, u//24, u//12, direction, 1, 'white', 'white')
        draw_rectangle(x*4/3, y*4/3, u//24, u//12, direction, 1, 'white', 'white')
    else:
        draw_rectangle(-x, -y, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(-x*7/6, -y*7/6, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(-x*4/3, -y*4/3, u//2, u//12, direction, 1, 'black', 'black')
        draw_rectangle(-x*7/6, -y*7/6, u//24, u//12, direction, 1, 'white', 'white')

    pen.hideturtle()