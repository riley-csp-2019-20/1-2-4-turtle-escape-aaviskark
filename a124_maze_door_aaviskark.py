#imports turtle and random
import turtle as trtl 
import random 

# creates variables for the program
maze_painter= trtl.Turtle()
maze_player= trtl.Turtle(shape="turtle")
number_walls= 25
wall_width= 20
wall_color= "red"
distance = 20
door_width = 20

maze_painter.pencolor(wall_color)

count= 0 
maze_painter.ht()
maze_painter.speed(0)
maze_painter.pensize(4)
maze_player.pencolor("gray")
#function that creates barriers in the maze
def barrier_wall(): 
    maze_painter.left(90)
    maze_painter.forward(wall_width*2)
    maze_painter.backward(wall_width*2)
    maze_painter.right(90)

def drawDoor():
    maze_painter.penup()
    maze_painter.forward(door_width)
    maze_painter.pendown()

#loop that creates the maze and its doors
while count < number_walls:
    if count > 4:  
        door= random.randint(door_width, distance - door_width)
        barrier= random.randint(2*wall_width, distance-2*door_width)
        #Door First
        if door < barrier:
            maze_painter.forward(door)
            drawDoor()
            maze_painter.forward(barrier - door - door_width)
            barrier_wall()                   
            maze_painter.forward(distance-barrier)     
        #barrier first
        else:
            maze_painter.forward(barrier)
            barrier_wall()
            maze_painter.forward(door - barrier)
            drawDoor()
            maze_painter.forward(distance-door-door_width)
        maze_painter.left(90)
    distance += wall_width
    count +=1

def player_up():
    maze_player.setheading(90)
    maze_player.forward(10)
def player_down():
    maze_player.setheading(270)
    maze_player.forward(10)
def player_left():
    maze_player.setheading(180)
    maze_player.forward(10)
def player_right():
    maze_player.setheading(0)
    maze_player.forward(10)

wn= trtl.Screen() 
wn.bgcolor("gray")

wn.onkeypress(player_up, "Up")
wn.onkeypress(player_down, "Down")
wn.onkeypress(player_left, "Left")
wn.onkeypress(player_right, "Right")

wn.listen()

wn.mainloop()