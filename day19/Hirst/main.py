import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(237, 34, 109), (155, 22, 65), (240, 72, 33), (7, 147, 92), (216, 170, 47), (180, 160, 41), (25, 123, 191), (44, 191, 233), (82, 21, 79), (244, 220, 49), (252, 224, 0), (125, 192, 86), (184, 38, 102), (213, 63, 21), (47, 171, 107), (172, 23, 17), (206, 133, 165), (22, 181, 216), (2, 108, 44), (237, 163, 192), (240, 167, 157), (162, 212, 180), (107, 0, 0), (138, 214, 231), (0, 81, 24), (250, 10, 20)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







screen = turtle_module.Screen()
screen.exitonclick()
