import turtle
import colorsys

def draw_one_color_arc(x,y,r,pensize,color):
    turtle.up()
    turtle.goto(x+r,y)
    turtle.down()
    turtle.seth(90)
    turtle.pensize(pensize)
    turtle.pencolor(color)
    turtle.circle(r,180)
    

turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.title('49-Color Rainbow')
turtle.setup(700,700)
num_colors = 49

radius = 300
penwidth = 20*7/num_colors
hue = 0
for i in range(num_colors):
    (r,g,b) = colorsys.hsv_to_rgb(hue,1,1)
    draw_one_color_arc(0,-100,radius,penwidth,(r,g,b))
    radius -= (penwidth-1) #overlapping a little removes the gaps
    hue += 0.9/num_colors
