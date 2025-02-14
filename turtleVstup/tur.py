import turtle

t = turtle.Turtle()

wn = turtle.Screen()

# title - назва вікна
wn.title('Вікно для малювання')

# bgcolor - задає фоновий колір для вікна
wn.bgcolor('orange')

# setup - розміри: ширина і висота вікна
wn.setup(width=800, height=800)


# рух черепахи вперед
# t.forward(200)


#поворот 
# t.left(90)
# t.forward(200)


# t.penup()
# t.up()
# t.forward(50)

# t.pendown()
# t.down()
# t.forward(50)


# t.clear()

# coord_x = 200
# coord_y = 300

# t.up()
# t.goto(178, 245)
# t.down()
# t.goto(coord_x, coord_y)

t.pensize(10)
#малюємо квадрат
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)



# нескінченна робота екрану
wn.mainloop()