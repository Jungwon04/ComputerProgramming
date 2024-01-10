import turtle as t
import math

u = 200

# 태극기 크기 설정
w = 3*u
h = 2*u

# 화면의 크기 설정
width = int(1.5*w)
height = int(1.5*h)
angle = math.degrees(math.acos(3/math.sqrt(9+4)))
print(f'각도: {angle}')

t.setup(width, height)
pen = t.Turtle()

# 태극기 테두리
pen.up()
pen.goto(int(-1.5*u), -u)

pen.down()
pen.pensize(3)
for side in 2*[3*u, 2*u]:
    pen.forward(side)
    pen.left(90)

pen.penup()
pen.home()

# 태극 큰 원 안의 빨간 반원
pen.setheading(90-angle)
pen.color('red')

pen.pendown()
pen.color('red')
c1 = int(u/2 * 3/math.sqrt(9+4))
c2 = -int(u/2 * 2/math.sqrt(9+4))

pen.goto(c1,c2)
pen.pendown()
pen.begin_fill()
pen.circle(u//2, extent=180)
pen.end_fill()

# 태극 큰 원 안의 파란 반원
pen.color('blue')
pen.begin_fill()
pen.circle(u//2, extent=180)
pen.end_fill()

# 파란색 작은 반원 그리기
pen.begin_fill()
pen.circle(u//4, extent=180)
pen.end_fill()

# 빨간색 작은 반원 그리기
pen.color('red')
pen.right(90)
pen.forward(u//2)
pen.left(90)

pen.begin_fill()
pen.circle(u//4, extent=180)
pen.end_fill()

# 궤의 길이와 색 지정
rext_l = u//2
rect_s = u//24
rect_h = u//12
rect_gap = u//24
pen.color('black')

# 건괘
pen.penup()
pen.setheading(180-angle)
pen.forward(3*u//4)
pen.right(90)

pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()
pen.penup()
pen.home()

# 곤 궤
pen.penup()
pen.setheading(180+angle)
pen.forward(3*u//4)
pen.right(90)
pen.pendown()

pen.color('black')
pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(90+angle)
pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.setheading(180+angle)
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.color('black')
pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()
pen.penup()
pen.home()

# 감 궤
pen.setheading(360+angle)
pen.forward(3*u//4)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(270+angle)
pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(-90)
pen.end_fill()

pen.penup()
pen.setheading(360+angle)
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.color('black')
pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(270+angle)
pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(-90)
pen.end_fill()

pen.penup()
pen.home()

# 리 궤
pen.setheading(360-angle)
pen.forward(3*u//4)
pen.right(90)
pen.pendown()

pen.color('black')
pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(270-angle)
pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(-90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.color('black')
pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(270-angle)
pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(-90)
pen.end_fill()

pen.penup()
pen.forward(3*u//24)
pen.right(90)
pen.pendown()

pen.color('black')
pen.begin_fill()
for side in [u//4, u//12, u//2, u//12, u//4]:
    pen.forward(side)
    pen.left(90)
pen.end_fill()

pen.color('white')
pen.setheading(270-angle)
pen.begin_fill()
for side in [u//48, u//12, u//24, u//12, u//48]:
    pen.forward(side)
    pen.right(-90)
pen.end_fill()

pen.penup()
pen.home()
pen.hideturtle()

t.done()