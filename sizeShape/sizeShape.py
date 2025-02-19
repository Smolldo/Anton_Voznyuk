import turtle 

t = turtle.Turtle()
wn = turtle.Screen()

# Напишіть програму, яка виводить рядок "Hello, World!" у трьох різних шрифтах та кольорах за допомогою Turtle.

# t.up()
# t.goto(-100, 200)

# t.color('red')
# t.write('Hello world', font=('Arial', 14, 'normal'))

# t.goto(-100, 0)

# t.color('blue')
# t.write('Hello world', font=('Colibri', 14, 'normal'))

# t.goto(-100, -200)

# t.color('green')
# t.write('Hello world', font=('Tahoma', 14, 'normal'))
t.speed(1)

# t.shape('turtle')
# t.forward(100)

# t.shape('circle')
# t.forward(100)


t.color('red', 'yellow')

# t.begin_fill()

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# t.end_fill()


# t.circle(50)
# t.circle(100)
# t.circle(150)
# t.circle(200)

# t.shape('turtle')

# t.stamp()
# t.forward(40)
# t.stamp()
# t.forward(40)
# t.stamp()
# t.forward(40)
# t.stamp()
# t.forward(40)
# t.stamp()
# t.forward(40)

# Створити просту анімацію, де черепашка малює квадрат, але змінює свою швидкість (speed()) після кожної сторони.

form = wn.textinput('Enter shape', 'enter some shape')
color = wn.textinput('Enter color', 'enter some color')

t.shape(form)
t.color(color)

t.forward(100)


wn.mainloop()