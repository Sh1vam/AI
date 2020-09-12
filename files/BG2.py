
import turtle
from turtle import *
bgcolor("black")
color('white','grey')
begin_fill()
i=0
while True:
    speed(0)
    circle(0.66+i,899,3)
    i+=1
    if abs(pos()) < 1:
        break
end_fill()
done()

