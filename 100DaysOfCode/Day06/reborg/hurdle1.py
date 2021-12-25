#number of hurdles are fix and height and distance of two hurdle is also constant
def turn_right():
    turn_left()
    turn_left()
    turn_left()

think(10)
while at_goal()!=True:
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()