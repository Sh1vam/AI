
import turtle
from turtle import *
bgcolor("black")
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
pensize(5)
begin_fill()
i=0
while True:
    speed(0)
    pencolor(colors[i//2%6])
    circle(0.66+i,899,2)
    i+=1
    if abs(pos()) < 1:
        break
end_fill()
done()


