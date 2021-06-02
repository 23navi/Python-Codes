def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
think(10)

while at_goal()!=True:
    if wall_in_front():
        jump_wall()
    else:
        move()