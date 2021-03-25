import turtle

# turtle.screen() allows you to define your screen size
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("#C09FFC")

# dictionary of colors
colors = {
  "purple" : "#C48AFE",
  "green" : "#9EFF8F",
  "light blue" : "#8FEEFF",
  "pink" : "#FF8FC7",
  "orange" : "#FFD599",
  "blue" : "#1BA9FF"
}

artist = turtle.Turtle()
artist.shape("turtle")
artist.color(colors["light blue"])

artist.penup()
artist.goto(0, 50)

userinput = input("What is your name?")

#(font-family, font size, font-style)
style = ("Snell Roundhand", 30, "italic")
artist.write("--------------------", font = style, align = "center")
artist.color(colors["light blue"])

artist.goto(0, 0)
artist.color(colors["pink"])
style = ("cursive", 30, "italic")
artist.write("Hello, how are you" + userinput + "!!" , font = style, align = "center")

artist.goto(0, -50)
artist.color(colors["light blue"])
style = ("Snell Roundhand", 30, "italic")
artist.write("--------------------", font = style, align = "center")

artist.goto(100, -200)
artist.color(colors["light blue"])
style = ("fantasy", 30, "italic")
artist.write("- Debanshi M", font = style, align = "center")
artist.hideturtle()

