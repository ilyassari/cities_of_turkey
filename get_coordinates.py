import turtle
import csv

with open("city_list.csv", mode="r+", encoding="UTF-8") as file:
    global city_list
    city_list = list(csv.reader(file))

# for plate, city in cities:
#     print(plate, city)
# # print(cities)

screen = turtle.Screen()
screen.title("Cities of Turkey")
screen.setup(width=1200, height=515)

image = "map.gif"
screen.addshape(image)
turtle.shape(image)

counter = 0

def get_mouse_click_coor(x, y):
    # print(x, y)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    # state_data = data[data.state == answer_state]
    t.goto(x, y)
    global counter
    t.write(city_list[counter][1])
    city_list[counter].append(x)
    city_list[counter].append(y)
    print(city_list[counter])
    with open("cities.csv", mode="a+", encoding="UTF-8") as cities:
        cities.write(f"{city_list[counter][1]}, {x}, {y}")
    counter += 1

turtle.onscreenclick(get_mouse_click_coor)



screen.mainloop()