def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_by(n):
    for i in range(0,n):
        move()
def block(n):
    for i in range(0,n):
        move_by(3)
        turn_left()
        move_by(3)
        if(at_goal()):
            break
        turn_right()
        move()
        turn_right()
     
block(4)