think(100)
move()
def move_till_home():
    while at_goal()!=True:
        while front_is_clear():
            if object_here():
               take() 
            move()    
        else:
            turn_left()

move_till_home()