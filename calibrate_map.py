import turtle
import pandas

# All 28 states in order to click
states_to_click = [
    "andhra pradesh", "arunachal pradesh", "assam", "bihar",
    "chhattisgarh", "goa", "gujarat", "haryana",
    "himachal pradesh", "jharkhand", "karnataka", "kerala",
    "madhya pradesh", "maharashtra", "manipur", "meghalaya",
    "mizoram", "nagaland", "odisha", "punjab",
    "rajasthan", "sikkim", "tamil nadu", "telangana",
    "tripura", "uttar pradesh", "uttarakhand", "west bengal"
]

clicks = []
current_index = [0]  # use list so it's mutable inside nested function

screen = turtle.Screen()
screen.title(f"Click on: {states_to_click[0].title()}")
img = "IndiaMap.gif"
# Use bgpic to set background image
screen.bgpic(img)
# Set screen size to match image dimensions (564x661)
screen.setup(width=564, height=661)

# Turtle to show click marker
marker = turtle.Turtle()
marker.hideturtle()
marker.penup()
marker.color("red")

def on_click(x, y):
    idx = current_index[0]
    state = states_to_click[idx]
    clicks.append({"state": state, "x": round(x), "y": round(y)})
    print(f"[{idx+1}/28] {state.title()} -> ({round(x)}, {round(y)})")

    # Draw a small dot at click position
    marker.goto(x, y)
    marker.dot(8, "red")
    marker.write(f" {state[:4]}", font=("Arial", 7, "normal"))

    current_index[0] += 1

    if current_index[0] < len(states_to_click):
        # Prompt next state
        screen.title(f"[{current_index[0]+1}/28] Click on: {states_to_click[current_index[0]].title()}")
    else:
        # All done — save to CSV
        screen.title("Done! Saving CSV...")
        df = pandas.DataFrame(clicks)
        df.to_csv("28_states.csv", index=False)
        print("\n✅ 28_states.csv updated successfully!")
        screen.bye()

screen.onscreenclick(on_click)
print(f"[1/28] Click on: {states_to_click[0].title()}")
turtle.mainloop()
