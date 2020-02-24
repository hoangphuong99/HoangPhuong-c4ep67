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

# import turtle
# dr= turtle.Turtle() 
# def draw_square(sz, cl):
#     for i in range(4):
#         dr.forward(sz)
#         dr.left(90)
#         dr.color(cl)

# draw_square(50,'red')

# mainloop()
# 4
# t= turtle.Turtle() 
# def draw_square1(sz,cl):
#     for ​i ​in ​range​(​30​):
#     ​t.draw_square1​(i * ​5​, ​cl​)
#     t.left(​17​)
#     t.penup()
#     t.forward(i * ​2​)
#     t.pendown()

# draw_square1(50,'red')

# mainloop()
# import turtle   #Outside_In 
 
# skk = turtle.Turtle() 

  
# def draw_star(size,colors): 
#     for i in range(5): 
#         skk.forward(size) 
#         skk.right(144) 
#        
#         skk.color(colors)
  
# draw_star(150,'red') 

# mainloop()
# 6
speed(0​)
color(​'blue'​)
for ​i ​in ​range​(​100​):
    ​import ​random
    x = random.randint(-​300​, ​300​)
    y = random.randint(-​300​, ​300​)
    length = random.randint(​3​, ​10​)
    draw_star(x​, ​y​, ​length)


# 7
