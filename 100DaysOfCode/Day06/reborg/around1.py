def move_till_wall(n):
    for i in range(0,n):
        while front_is_clear():
            move()
        else:
            turn_left()
think(10) #Think will reduce or increase the robo speed
move_till_wall(4)