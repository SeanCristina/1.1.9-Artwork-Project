import turtle

# Create screen object
screen = turtle.Screen()

screen.title("1.1.9 Art Project - SEAN C. P2") # titling our artwork

screen.bgcolor("DeepSkyBlue2") # set initial background
screen.setup(width=650, height=820)

# Register all our images
images = ["Tree 1.gif", "Tree 2.gif", "grass.gif", "cloud.gif", "gray car.gif", "white car.gif", "dashed lines.gif", "sun.gif"]
for img in images:
    screen.addshape(img)


# Assigning independent turtles for each image/element
tree1_turtle = turtle.Turtle()
tree2_turtle = turtle.Turtle()
grass_turtle = turtle.Turtle()
cloud_turtle = turtle.Turtle()
whitecar_turtle = turtle.Turtle()
graycar_turtle = turtle.Turtle()
dirt_turtle = turtle.Turtle()
street_turtle = turtle.Turtle()
dashedlines_turtle = turtle.Turtle()
sun_turtle = turtle.Turtle()

#placing the sun image as a shape
sun_turtle.speed("fastest")
sun_turtle.turtlesize(.1)
sun_turtle.penup() #preventing the turtle from drawing a line each time it moves
sun_turtle.goto(-210, 300)
sun_turtle.shape("sun.gif")


#placing the cloud image as a shape
cloud_turtle.speed("fastest")
cloud_turtle.turtlesize(.1)
cloud_turtle.penup() #preventing the turtle from drawing a line each time it moves
cloud_turtle.goto(90, 275)
cloud_turtle.shape("cloud.gif")


# placing the grass image as a shape
grass_turtle.speed("fastest")
grass_turtle.turtlesize(.1)
grass_turtle.penup() #preventing the turtle from drawing a line each time it moves
grass_turtle.goto(0, -275)
grass_turtle.shape("grass.gif")

#drawing the dirt by hand
dirt_turtle.speed("fastest")
dirt_turtle.penup()
dirt_turtle.goto(-350, 20)
dirt_turtle.pendown()
dirt_turtle.turtlesize(.1)
dirt_turtle.fillcolor("LightSalmon4") # giving the dirt rectangle a brown fill color
dirt_turtle.begin_fill()
dirt_turtle.forward(700)
dirt_turtle.right(-90)
dirt_turtle.forward(50)
dirt_turtle.right(-90)
dirt_turtle.forward(700)
dirt_turtle.right(-90)
dirt_turtle.forward(50)
dirt_turtle.end_fill()

# setting up turtle for 1st tree
tree1_turtle.speed("fastest")
tree1_turtle.penup() #preventing the turtle from drawing a line each time it moves 
tree1_turtle.turtlesize(.1)
# placing the first tree
tree1_turtle.goto(50, 100)
tree1_turtle.shape("Tree 1.gif")

# setting up turtle for 2nd tree
tree2_turtle.speed("fastest")
tree2_turtle.penup() #preventing the turtle from drawing a line each time it moves
tree2_turtle.turtlesize(.1)
# placing the 2nd tree
tree2_turtle.goto(-200, 100)
tree2_turtle.shape("Tree 2.gif")

#drawing the street by hand
street_turtle.speed("fastest")
street_turtle.penup()
street_turtle.goto(-350, 20)
street_turtle.pendown()
street_turtle.turtlesize(.1)
street_turtle.fillcolor("gray20") # giving the street rectangle a gray fill color
street_turtle.begin_fill()
street_turtle.forward(700)
street_turtle.right(90)
street_turtle.forward(120)
street_turtle.right(90)
street_turtle.forward(700)
street_turtle.right(90)
street_turtle.forward(120)
street_turtle.end_fill()

# placing the yellow dash image as a shape
dashedlines_turtle.speed("fastest")
dashedlines_turtle.turtlesize(.1)
dashedlines_turtle.penup() #preventing the turtle from drawing a line each time it moves
dashedlines_turtle.goto(0, -30)
dashedlines_turtle.shape("dashed lines.gif")

# setting up turtle for white car
whitecar_turtle.speed(3) # making the car slower
whitecar_turtle.turtlesize(.1)
whitecar_turtle.penup() # preventing the turtle from drawing a line each time it moves

whitecar_turtle.goto(-650, -30) # setting the car's start position that it moves to
whitecar_turtle.shape("white car.gif")
whitecar_turtle.goto(650, -30) # setting the car's end position that it moves to

# setting up turtle for gray car
graycar_turtle.speed(3) # making the car slower
graycar_turtle.turtlesize(.1)
graycar_turtle.penup() # preventing the turtle from drawing a line each time it moves

graycar_turtle.goto(650, 20) # setting the car's start position that it moves to
graycar_turtle.shape("gray car.gif")
graycar_turtle.goto(-650, 20) # setting the car's end position that it moves to


# Keep the screen open until clicked
screen.exitonclick()
