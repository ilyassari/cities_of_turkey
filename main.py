import turtle
import pandas

# Turtle Ops
screen = turtle.Screen()
screen.title("Cities of Turkey")
screen.setup(width=1200, height=515)
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

# create turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed("fastest")


# Get data with pandas
data = pandas.read_csv("cities.csv")
cities = data.name.to_list()
found_cities = list()

while len(found_cities) < len(cities):
    answer = screen.textinput(title=f"{len(found_cities)}/{len(cities)} Şehir Bilindi",
                              prompt="Bir şehir adı yazınız?")

    if answer is None:
        missing_cities = list(city for city in cities if city not in found_cities)
        t.color("red")
        for city in missing_cities:
            city_data = data[data.name == city]
            t.goto(float(city_data.x), float(city_data.y))
            t.write(city_data.name.values[0])
        break

    answer = answer.title()

    # correct İ and double named cities
    if answer == "İçel" or answer == "Içel":
        answer = "Mersin"
    elif answer == "Istanbul":
        answer = "İstanbul"
    elif answer == "Izmir":
        answer = "İzmir"
    elif answer == "Urfa":
        answer = "Şanlıurfa"
    elif answer == "Antep":
        answer = "Gaziantep"
    elif answer == "Maraş":
        answer = "Kahramanmaraş"
    elif answer == "Afyon":
        answer = "Afyonkarahisar"
    elif answer == "Adapazarı":
        answer = "Sakarya"

    if answer in cities and answer not in found_cities:
        found_cities.append(answer)
        city_data = data[data.name == answer]
        t.goto(float(city_data.x), float(city_data.y))
        t.write(city_data.name.values[0])

screen.mainloop()

