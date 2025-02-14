txt = 'Python'

print(txt[0])
print(txt[2])
print(txt[-1])

t1 = 'Hello'
t2 = 'World!'

#конкатенація склеювання
print(t1 + ' ' + t2)

#реплікація - повторенння
print('-' * 10)


# t.upper() - робить всі букви великими
t = 'lorEm ipSUM'
print(t.upper())

# .lower() - робить усі букви маленькими
print(t.lower())


#title() - робить кожну першу букву слова великою
print(t.title())


import turtle

t = turtle.Turtle()
wn = turtle.Screen()

t.color('red')
# t.write('Hello world', font=('Courier', 30, 'bold'))

user_text = wn.textinput('Enter text', 'Enter some text: ')

t.up()
t.goto(-200, 100)

t.write(user_text.upper(), font=('Courier', 30, 'bold'))


wn.mainloop()