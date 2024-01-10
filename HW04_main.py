import math
import turtle
from HW04 import *

unit = 300
kinds_guae = ['gun', 'gon', 'gam', 'yee']

width = 3 * unit
height = 2 * unit
theta = round(math.degrees(math.asin(2/math.hypot(3, 2))))

turtle.setup(int(1.2 * width), int(1.2 * height))
draw_rectangle(0, -height / 2, width, height, 0, 3)
draw_taegeuk(unit, theta)

direction = [90 - theta, 270 - theta, -90 + theta, 90 + theta]

for n in range(4):
    draw_guae(kinds_guae[n], unit, direction[n])

turtle.done()
