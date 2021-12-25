import turtle
import pandas as pd

screen= turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score=0
inp=""
data = pd.read_csv("50_states.csv")
arrayofstates=data.state.tolist()

while (score!=50 and inp!="Q"):
    inp=(screen.textinput(title=f"{score}/50. Guess the state name", prompt="What are the state names?")).title()
    if inp in arrayofstates:
        x=(data[data.state==inp])["x"].tolist()
        y=(data[data.state==inp])["y"].tolist()
        arrayofstates.remove(inp)
        tur=turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(x[0],y[0])
        tur.write(inp,font=("Arial", 12, "normal"))
        score+=1
        print(len(arrayofstates))

    else:
        continue

if score==50:
    print("Congo! You got everything right")

csvdata=pd.DataFrame(arrayofstates)
csvdata.to_csv("missed_state.csv")

