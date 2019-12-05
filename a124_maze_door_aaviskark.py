import turtle as trtl 
import random 

maze_painter= trtl.Turtle(shape= "turtle")
number_walls= 25
wall_width= 15
wall_color= "red"
distance = 15
door_width = 20

maze_painter.pencolor(wall_color)

count= 0 
maze_painter.ht()
maze_painter.speed(0)

def barrier_wall(): 
    maze_painter.left(90)
    maze_painter.forward(distance*2)
    maze_painter.backward(distance*2)
    maze_painter.right(90)

while count < number_walls:
    maze_painter.forward(distance/2)
    maze_painter.penup()
    maze_painter.forward(door_width)
    maze_painter.pendown()
    maze_painter.forward(door_width*2)
    if count > 4:
        barrier_wall()
    maze_painter.forward(distance/2 + count*15)
    maze_painter.left(90)
    count +=1

wn= trtl.Screen() 
wn.mainloop()