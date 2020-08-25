import turtle as t
import random

t.title(" Exercise 1. Drawing Olympic Logo")
#t.pensize(5)
t.width(5)
colors = ['yellow', 'blue', 'red', 'black', 'green']

count = 0
first_row = 3
total_circle = 5
while count < first_row:
	for i in range(1):
		col = random.choice(colors)
		t.color(col)
		t.circle(55)
		t.penup()
		t.fd(100)
		t.pendown()
	count += 1

t.penup()
t.goto(50, 70)
t.pendown()

	
t.color("blue")
t.circle(55)

t.penup()
t.goto(140, 70)
t.pendown()

t.color("red")
t.circle(55)


t.done()