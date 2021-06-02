def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_by(n):
    for i in range(0,n):
        move()

def reach_bottom():
    turn_right()
    move()
    turn_right()
    while wall_in_front()!=True:
        move()
    else:
        turn_left()
def jump_wall():
    turn_left()
    while right_is_clear()!=True:
        move()
    else:
        reach_bottom()
    
think(10)
while at_goal()!=True:
    if wall_in_front():
        jump_wall()
    else:
        move()