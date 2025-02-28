
#range(start, finish)
# for i in range(10):
#     print(i)

fruit = 'apple'

# for i in fruit:
#     print(i)


import turtle

t = turtle.Turtle()
wn = turtle.Screen()

t.speed(1)

# for _ in range(360):
#     t.forward(0.1)
#     t.left(1)

sides = 10
length = 70

# for _ in range(sides):
#     t.forward(length)
#     t.left(360 / sides)


# while True:
#     speed = input('Enter speed (l, m, h, e): ')

#     if speed == 'l':
#         t.speed(1)
#     elif speed == 'm':
#         t.speed(5)
#     elif speed == 'h':
#         t.speed(10)
#     elif speed == 'e':
#         break

#     t.forward(100)
#     t.right(90)

import random

for _ in range(25):
    t.forward(random.randint(10, 70))
    t.left(random.randint(0, 360))

wn.mainloop()




