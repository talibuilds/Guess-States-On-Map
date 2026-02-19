import turtle
import pandas
screen = turtle.Screen()
screen.title("Guess States Name - By TALIB")
# [FIX]: Set screen size to image dimensions (564x661) for correct mapping
screen.setup(width=564, height=661)
# Font used for writing state names (change the size here)
FONT = ("Arial", 10, "bold")
img = "IndiaMap.gif"
turtle.addshape(img)
turtle.shape(img)

data = pandas.read_csv("28_states.csv")
states = data.state.to_list()
guessed_states = []


while len(guessed_states) <28:
    user_input = screen.textinput(title=f"{len(guessed_states)}/28 Correct Guess", prompt="Enter Any States Name").lower()
    if user_input in states :
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        state_data = data[data.state ==user_input]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_input.title(), align="center", font=FONT)
        guessed_states.append(user_input)



screen.exitonclick()