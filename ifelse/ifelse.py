# if 7 > 10:
#     print('7 > 3')
# else:
#     print('7 ne bilshe 10')


age = 19

if age < 18:
    print('nepovnolitni')
elif age >= 18:
    print('povnolitnii')
else:
    print('ne vine chislo')


# and or not

prava = True
age = 19

if age >= 18 and prava:
    print('mozhna yihaty')
else:
    print('ne mozhna')


import turtle

t = turtle.Turtle()
wn = turtle.Screen()


# direction = input('Enter some direction: ')

# if direction == 'вперед':
#     t.forward(100)
# elif direction == 'назад':
#     t.backward(100)
# elif direction == 'вправо':
#     t.right(90)
#     t.forward(100)
# elif direction == 'вліво':
#     t.left(90)
#     t.forward(100)
# else:
#     print('nevirni dani. sprobuite sche raz')



# Написати програму, яка запитує у користувача число та переміщує черепашку на 
# відповідну відстань вперед, якщо число додатнє, або назад, якщо число від'ємне.

number = int(input('enter number: '))

if number > 0:
    t.forward(number)
elif number < 0:
    t.forward(number)
else:
    print('wrong number')


wn.mainloop()