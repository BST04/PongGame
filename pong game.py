import turtle
import random as rand 


a = turtle.Turtle() #ball turtle
b = turtle.Turtle() #text turtle
t = turtle.Turtle() #player turtle
f = turtle.Turtle() #field turtle

#screen settings
screen = turtle.Screen()
screen.title("pong game") #title name 
screen.setworldcoordinates(-500, -500, 500, 500)
screen.setup(600, 600)
screen.tracer(False)
screen.bgcolor("black") #bg color
screen.update()

t.ht() 
a.ht()
b.ht()
f.ht()


size = 40 #size of the ball

pdirection = "R" #direction of the character

speed = 15 #speed of the character

x = 0 #ball position in x
y = 0 #ball position in y

speed_x = 10 #speed ball in x
speed_y = 10 #speed ball in y

border = 360 #border position

colors = ["old lace", "orange", "red", "sky blue","yellow", "cyan", "purple",] #list colors ball
colors2 = ["brown", "black", "dark blue","gold3", "blue", "pink", "green"] #list colors bg
color = "" #color ball
color2 = "" #color bg

bounces = 0 #puntuation

px = 0  #player position in x
py = -200 #player position in y
pt = 0 #player total



#generating colors with random
def generate_color():
    global color, colors, color2
    color = colors[rand.randint(0, len(colors)-1)]
    color2 = colors2[rand.randint(0, len(colors)-1)]

#drawing the field
def draw_field():
    global border
    f.pensize(2)
    f.pencolor("white")
    f.up()
    f.goto(-border,-border)
    f.down()
    f.fillcolor("white")
    #field.begin_fill()
    for i in range(0,360,90):
        f.seth(i)
        f.fd(2* border)
    #field.end_fill()
    screen.update()

#drawing all
def draw():
    global size, x, y, color

    #square
    a.clear()
    b.clear()
    t.clear()

    #ball
    a.pensize(2)
    a.up()
    a.goto(x,y)
    a.down()
    a.pencolor(color)
    a.dot(12)

    #puntuation text
    b.goto(-335,280)
    b.pencolor("white")
    b.write(bounces,font=("Calibri", 20, "bold"))

    #player
    t.up()
    t.goto(px,py)
    t.down()
    player()

    screen.update()

#drawing player
def player():
    t.pencolor("white")
    t.pensize(5)
    t.fd(50)
    t.left(180)
    t.fd(80)

#check border with the ball
def check_border():
    global px, py, x
        
    if bounces >= 10:
        if px > 300:
            px =-300
        if px < -300:
            px= 300
        
    elif bounces >= 20:
        if x > 300:
            x =-300
        if x < -300:
            x= 300
    else:
        if px == 300:
            px -= speed
        if px == -300:
            px += speed

#check player with walls and ball
def check():
    global x, y, speed_x, speed_y, size, border, bounces
    if x >= border or x <= -border:
        speed_x = -speed_x
        generate_color()
    
    if bounces > 5:
        turtle.bgcolor(color2)
    
    if bounces == 10:
        turtle.bgcolor(color2)
        
    if y >= border or y <= -border:
        generate_color()
        speed_y = -speed_y
        
    if abs(x - px) <= pt + size and abs(y - py) <= pt + size:
        speed_y = - speed_y
        bounces += 1
        speed_x += 3
        speed_y += 3
        
    
    if y < (py - 10):
        screen.bgcolor("Black")
        a.pencolor("black")
        t.pencolor("white")
        t.goto(-150,0)
        t.write("GAME OVER \n BOUNCES:" ,bounces , font=("Calibri", 20, "bold"))
        t.home()
        t.fd(120)
        t.write(bounces,font=("Calibri", 20, "bold"))
        
        turtle.done()

#moving the ball 
def move_ball():
    global x, y, size, speed_x, speed_y
    draw()
    x += speed_x
    y += speed_y
    check()

#when a turn left
def turn_left():
    global pdirection
    pdirection = "L"

#when d turn rigth
def turn_right():
    global pdirection
    pdirection = "R"

#animate all 
def animate():
    global px, pdirection, py
    if pdirection == "R":
        px += speed
    elif pdirection =="L":
        px -= speed
    draw()
    check_border()
    turtle.ontimer(move_ball(), 100)
    animate()


turtle.onkey(turn_left, "a")
turtle.onkey(turn_right, "d")
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")

turtle.listen()
    

draw_field()
generate_color()
animate()

turtle.done()