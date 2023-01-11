import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Thailand Province's Game")
image = "blank_province_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("provinces_thailand.csv")
all_provinces = data.province.to_list()
guessed_province = []
num_province = len(all_provinces)

while len(guessed_province) < num_province:
    answer_province = turtle.textinput(title="Guess the Province", prompt="What's another province?").title()
    
    if answer_province == "Exit":
        missing_province = []
        for province in all_provinces:
            if province not in guessed_province:
                missing_province.append(province)
        new_data = pd.DataFrame(missing_province)
        new_data.to_csv("provinces_to_learn")
        break


    if answer_province in all_provinces:
        guessed_province.append(answer_province)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinate = data[data.province == answer_province]
        t.goto(x=int(coordinate.x), y=int(coordinate.y))
        t.write(answer_province,align="left")
