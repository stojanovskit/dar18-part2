# import colorgram
import turtle
from turtle import Turtle, Screen
import random
#
# colors = colorgram.extract('1.jpg', 30)
# print(colors)
# list = []
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_collor=(r,g,b)
#     list.append(rgb_collor)
# print(list)
from typing import List, Union, Tuple, Any

color_list: list[Union[tuple[int, int, int], Any]] = [(195, 162, 115), (149, 86, 42), (184, 163, 22), (220, 206, 119),
                                                      (69, 32, 20), (139, 160, 188),
                                                      (70, 92, 130), (183, 145, 159), (139, 28, 15), (32, 36, 55),
                                                      (129, 77, 100), (57, 29, 39),
                                                      (141, 176, 151), (185, 101, 84), (174, 99, 117), (126, 26, 36),
                                                      (77, 109, 84), (86, 89, 13),
                                                      (106, 119, 170), (43, 58, 106), (170, 206, 180), (182, 186, 211),
                                                      (216, 181, 174), (210, 180, 192),
                                                      (220, 206, 17), (99, 146, 110)]


def rancol(list):
    col = random.choice(list)
    return col


tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.setheading(-225)
tim.forward(500)
tim.setheading(0)


def draw():
    for number in range(20):
        tim.dot(20, rancol(color_list))
        tim.penup()
        tim.fd(50)
    tim.penup()
    tim.right(90)
    tim.fd(50)
    tim.right(90)
    tim.forward(1000)
    tim.setheading(0)
    draw()


draw()
Screen().exitonclick()
