import turtle

t = turtle.Turtle()
wn = turtle.Screen()

t.speed(0)

# size = 20

# for x in range(-100, 100, size):
#     t.color('green')
#     for y in range(-100, 100, size):
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#         if x % 60 == 0:
#             t.color('red')
#         if x % 50 == 0:
#             t.color('yellow')
#         if x % 40 == 0:
#             t.color('blue')
        
#         for _ in range(4):
#             t.forward(size)
#             t.right(90)


t.shape('square')
t.up()

colors = ['black', 'white']

for y in range(8):
    for x in range(8):
        t.goto(x * 20 - 80, y * 20 - 80)
        if (x + y) % 2 == 0:
            t.color('black')
        if (x + y) % 2 == 1:
            t.color('white')
        t.stamp()

wn.mainloop()