import random
import turtle as t
my_screen=t.Screen()
my_screen.setup(1000,200)
names=["red","green","black","blue","pink","orange","purple"]
user_winner=my_screen.textinput("Winner Number","1:red \n2:green \n3:black \n4:blue \n5:pink \n6:orange \n7:purple")
racers=[]
my_turtle=t.Turtle()
my_turtle.penup()
my_turtle.goto(480,-100)
my_turtle.pensize(5)
my_turtle.pendown()
my_turtle.goto(480,100)

race_on=True

# red=t.Turtle()
# green=t.Turtle()
# black=t.Turtle()
# blue=t.Turtle()
# pink=t.Turtle()
# orange=t.Turtle()
# purple=t.Turtle()
# my_racers=[red,green,black,blue,pink,orange,purple]

# for i in range(7):
#     my_racers[i].shape("turtle")
#     my_racers[i].color(names[i])
#     my_racers[i].penup()
#     if i<4:
#         my_racers[i].goto(-480,0+i*20)
#     else:
#         my_racers[i].goto(-480,0-((i-3)*20))
actual_winner=0


for i in range(7):
    new_turtle=t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(names[i])
    if i < 4:
        new_turtle.goto(-480,0+i*20)
    else:
        new_turtle.goto(-480,0-((i-3)*20))
    racers.append(new_turtle)


while(race_on):
    for i in range(7):
        racers[i].fd(random.randint(1,20))
        if racers[i].xcor()>460:
            actual_winner=i+1
            race_on=False
            break


if(actual_winner==user_winner):
    print("You won!")
else:
    print(f"you lost! {names[actual_winner-1]} is the winner")

my_screen.exitonclick()