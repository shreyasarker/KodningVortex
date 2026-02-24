import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color
screen.title("Polygon Drawing Program")

# Create the turtle object
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)

def draw_polygon(sides, length, border_color, fill_color, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    pen.color(border_color)
    pen.fillcolor(fill_color)
    
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(length)
        pen.left(360 / sides)  # The logic for the exterior angle
    pen.end_fill()

# 1. Draw Equilateral Triangle (3 sides)
draw_polygon(3, 100, "cyan", "blue", -200, 0)

# 2. Draw Rectangle (Special case: 4 sides, but 2 different lengths)
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("yellow")
pen.fillcolor("orange")
pen.begin_fill()
for _ in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()

# 3. Draw Hexagon (6 sides)
draw_polygon(6, 70, "lime", "green", 200, 0)

# Hide the turtle and keep window open
pen.hideturtle()
screen.mainloop()