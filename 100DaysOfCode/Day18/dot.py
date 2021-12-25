import turtle as t
from turtle import Turtle, Screen
import random
t.colormode(255) # to set turtle to use rgb color too! by default it is string only
my_turtle=Turtle()
my_turtle.penup()
my_turtle.speed(0)
rgb_colors=[(239, 246, 243), (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

for i in range(-300,301,30):
    my_turtle.sety(i)
    for j in range(-300,301,30):
        my_turtle.setx(j)
        my_turtle.dot(20,random.choice(rgb_colors))

my_turtle.goto(500,500)
my_screen=Screen()
my_screen.exitonclick()