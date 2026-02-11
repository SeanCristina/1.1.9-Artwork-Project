import turtle
import time

# --- SETUP SCREEN ---
screen = turtle.Screen()
screen.title("1.1.9 Art Project - SEAN C. P2")
screen.bgcolor("light blue")
screen.setup(width=800, height=600) # Set a specific window size

# --- REGISTER IMAGES ---
# IMPORTANT: These files must be in the same folder as your python script.
# IMPORTANT: Turtle only accepts .GIF files. Convert your PNGs to GIFs.
image_list = ["Tree 1.gif", "grass.gif", "white car.gif", "gray car.gif"] 




# --- DRAW SCENE ---

# 1. Place Grass (Background items first)
# You can call this multiple times to make a field
grass_1 = create_object("grass.gif", 0, -200)
grass_2 = create_object("grass.gif", 200, -200) # Another grass patch

# 2. Place Trees
tree_1 = create_object("Tree 1.gif", 50, 100)
tree_2 = create_object("Tree 1.gif", -150, 50) # A second tree

# 3. Create the Car (For animation)
white_car = create_object("white car.gif", -350, -150)
gray_car = create_object("gray car.gif", 350, -150)
# --- ANIMATION LOOP ---
# This makes the car drive across the screen
while True:
    white_car.forward(100) # Move car forward by 5 pixels
    gray_car.back(100)
    # If car goes off the right side of screen, reset to left side
    if white_car.xcor() > 400:
        white_car.goto(-400, -150)
    
    # Update screen is usually automatic, but this keeps it smooth
    screen.update() 
    time.sleep(0.01) # Control animation speed

# Note: The while loop replaces screen.exitonclick()