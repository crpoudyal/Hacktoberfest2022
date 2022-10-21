#Turtle program to repoduce two symmetrical diamonds side by side
import turtle
tscreen=turtle.Screen()
#setting the screen size for the turtle program to run in
tscreen.setup(700,500)
#rgb colour of light blue found with google search set as backround
turtle.Screen().bgcolor('#CCE5FF')
#turtle shape as the classic turtle
turtle.shape('turtle')
#good speed to catch errors, not to fast so that you dont see the shape being drawn
turtle.speed(3)
#starts the drawing process with the pen down on the screen
turtle.pendown()
#set position to middle of screen to start the shape
turtle.setposition(0,0)
#pen colour black for the line
turtle.pencolor('black')
#fill colour for the shape is white
turtle.fillcolor('white')
#starts the fill process
turtle.begin_fill()
#pensize set appropriately for a thicker line
turtle.pensize(2)
#degree angle left
turtle.left(45)
#move turtle forward 155pixels
turtle.forward(155)
turtle.left(90)
turtle.forward(155)
turtle.left(90)
turtle.forward(155)
turtle.left(90)
turtle.forward(155)
#the end of the fill process, all lines in shape meet
turtle.end_fill()
#penup/stop leaving a trail behind
turtle.penup()
turtle.left(90)
turtle.forward(155)
#second diamond start
turtle.pencolor('black')
turtle.pendown()
turtle.begin_fill()
turtle.forward(155)
turtle.right(90)
turtle.forward(155)
turtle.right(90)
turtle.forward(155)
turtle.right(90)
turtle.forward(155)
turtle.end_fill()
turtle.penup()
#hide the turtle from being visible
turtle.hideturtle()
#keep screen open
turtle.mainloop()