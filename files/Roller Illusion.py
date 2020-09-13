import turtle
import math

screen = turtle.Screen()
screen.setup(1100,1000)
screen.setworldcoordinates(-620,-550,680,550)
screen.tracer(0,0)
screen.title('Roller Illusion - PythonTurtle.Academy')
turtle.hideturtle()
turtle.speed(0)
n=100
# parametric equation to draw ellipses
def ellipse(cx,cy,a,b,c1,c2,c3):
    t = -math.pi/2
    x = cx+a*math.cos(t)
    y = cy+b*math.sin(t)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pencolor(c1)
    turtle.fillcolor(c3)
    turtle.begin_fill()
    for i in range(n//2):
        x = cx+a*math.cos(t)
        y = cy+b*math.sin(t)
        turtle.goto(x,y)    
        t += 2*math.pi/n
    turtle.pencolor(c2)
    for i in range(n//2):
        x = cx+a*math.cos(t)
        y = cy+b*math.sin(t)
        turtle.goto(x,y)    
        t += 2*math.pi/n
    turtle.end_fill()

def rolling_column(x,size):
    for y in range(-400,500,100):
        ellipse(x,y,size,35,'white','black','dark orange')
        
def rolling_column2(x,size):
    for y in range(-400,500,100):
        ellipse(x,y,size,35,'black','white','dark orange')

def rolling():
    rolling_column(-450,10)
    rolling_column(-410,13)
    rolling_column(-360,16)
    rolling_column(-300,19)
    rolling_column(-240,16)
    rolling_column(-190,13)
    rolling_column(-150,10)

    rolling_column2(-130,10)
    rolling_column2(-90,13)
    rolling_column2(-40,16)
    rolling_column2(20,19)
    rolling_column2(80,16)
    rolling_column2(130,13)
    rolling_column2(170,10)

    rolling_column(190,10)
    rolling_column(230,13)
    rolling_column(280,16)
    rolling_column(340,19)
    rolling_column(400,16)
    rolling_column(450,13)
    rolling_column(490,10)
    
turtle.color('steel blue')
turtle.up()
turtle.goto(-1000,-1000)
turtle.down()
turtle.begin_fill()
turtle.seth(0)
for _ in range(4):
    turtle.fd(2000)
    turtle.left(90)
turtle.end_fill()
turtle.pensize(3)
rolling()
screen.update()
# the following generates high quality image
filename="rolling_illusion.eps" 
ts = turtle.getscreen()
ts.getcanvas().postscript(file=filename)
