import turtle as t

class Snake():
    def __init__(self):
        self.snakes=[]
        self.create_start()

    def create_start(self):
        for i in range(3):
            tur=t.Turtle("square")
            tur.penup()
            tur.color("white")
            tur.goto(-i*20,0)
            self.snakes.append(tur)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].xcor(), self.snakes[i - 1].ycor())
        self.snakes[0].fd(20)


    def up(self):
        if (self.snakes[0].heading()==0.0):
            self.snakes[0].lt(90)
        elif (self.snakes[0].heading()==180.0):
            self.snakes[0].rt(90)
        else:
            pass

    def down(self):
        if (self.snakes[0].heading()==0.0):
            self.snakes[0].rt(90)
        elif (self.snakes[0].heading()==180.0):
            self.snakes[0].lt(90)
        else:
            pass

    def left(self):
        if (self.snakes[0].heading()==90.0):
            self.snakes[0].lt(90)
        elif (self.snakes[0].heading()==270.0):
            self.snakes[0].rt(90)
        else:
            pass

    def right(self):
        if (self.snakes[0].heading()==90.0):
            self.snakes[0].rt(90)
        elif (self.snakes[0].heading()==270.0):
            self.snakes[0].lt(90)
        else:
            pass
