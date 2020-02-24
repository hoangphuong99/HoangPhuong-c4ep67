from turtle import *
# 1
def greeting(name):
   print(f'hello {name}')
greeting('Phượng')
# 2
def sum(a,b):
    print("sum = " + str(a + b))
sum(4,7)
# 3

import turtle
def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        t.color('red')
alex = turtle.Turtle() # Create alex
draw_square(alex, 50)

mainloop()
# 4
def draw_square1(t,sz):
    for ​j ​in ​range​(​30​):
    ​t.draw_square1​(j * ​5​, ​'red'​)
    t.left(​17​)
    t.penup()
    t.forward(j * ​2​)
    t.pendown()
alex = turtle.Turtle() 
draw_square1(alex, 50)

mainloop()