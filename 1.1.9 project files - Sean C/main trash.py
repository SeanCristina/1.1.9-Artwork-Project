import turtle

screen = turtle.Screen()

# 1. Register all your GIF images
images = ["Tree 1.gif", "grass.gif", ]
for img in images:
    screen.addshape(img)

# 2. Create independent turtles for each image
tree_turtle = turtle.Turtle()
grass_turtle = turtle.Turtle()

# 3. Position them wherever you want
# Place the cat at the top-left
tree_turtle.penup()
tree_turtle.goto(-200, 150)
tree_turtle.shape("tree skib.gif")

# Place the dog in the center
grass_turtle.penup()
grass_turtle.goto(0, -200)
grass_turtle.shape("grass.gif")

turtle.done()