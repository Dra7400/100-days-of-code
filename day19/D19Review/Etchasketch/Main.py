from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)
def move_backward():
    tim.bk(10)
def move_right():
    tim.rt(10)
def move_left():
    tim.lt(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left" )
screen.onkey(clear, "c")

screen.exitonclick()
