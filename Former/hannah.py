import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Lovely Hannah")

# Create turtle for the heart
heart = turtle.Turtle()
heart.pensize(3)
heart.color("purple")            # outline in purple
heart.speed(1)

# Function to draw heart shape
def draw_heart(fill_shade):
    heart.begin_fill()
    heart.fillcolor(fill_shade)  # dynamic fill shade
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.hideturtle()
    heart.end_fill()

# Draw a pulsing purple heart
shades = ["#9b30ff", "#800080"]   # lighter and deeper purple
for i in range(4):
    shade = shades[i % 2]
    heart.clear()
    heart.color(shade)
    draw_heart(shade)
    time.sleep(0.4)

# Final heart in a rich purple
heart.clear()
heart.color("purple")
draw_heart("purple")

# Create another turtle for the text
text_writer = turtle.Turtle()
text_writer.hideturtle()
# Set the text color to a shimmering gradient effect

def shimmer_text(turtle_obj, text, pos, font):
    colors = ["#da70d6", "#e066ff", "#ba55d3", "#dda0dd", "#c71585", "#ffb6c1"]
    for i in range(10):
        turtle_obj.clear()
        turtle_obj.color(random.choice(colors))
        turtle_obj.penup()
        turtle_obj.goto(pos)
        turtle_obj.write(text, align="center", font=font)
        time.sleep(0.15)
    turtle_obj.color("purple")
    turtle_obj.clear()
    turtle_obj.penup()
    turtle_obj.goto(pos)
    turtle_obj.write(text, align="center", font=font)

# Use shimmer effect for the text
shimmer_text(text_writer, "Lovely Hannah", (0, -20), ("Lucida Handwriting", 32, "bold"))
text_writer.penup()
text_writer.goto(0, -20)
text_writer.write("Lovely Hannah",
                  align="center",
                  font=("Lucida Handwriting", 32, "bold"))

# Optional: add a little purple sparkle animation
sparkle = turtle.Turtle()
sparkle.hideturtle()
sparkle.speed(0)
sparkle.pensize(2)
sparkle.shape("circle")
sparkle.color("#da70d6")   # orchid sparkle
sparkle.penup()

positions = [(-70, 100), (50, 130), (0, 160), (80, 80), (-90, 80)]
for pos in positions:
    sparkle.goto(pos)
    sparkle.dot(10)

# Keep the window open until clicked
screen.exitonclick()