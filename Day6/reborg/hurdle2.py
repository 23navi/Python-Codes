#similar to hurdle 1 but number of hurdle is different but is constant 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_by(n):
    for i in range(0,n):
        move()

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