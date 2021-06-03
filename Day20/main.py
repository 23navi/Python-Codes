import turtle as t
import time
from snake import Snake
screen=t.Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

snake=Snake()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")


game_on=True

while game_on:
    time.sleep(.1)
    screen.update()
    snake.move()




screen.exitonclick()
