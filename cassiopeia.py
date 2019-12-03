import turtle
import time

# Create a new turtle object
jo = turtle.Turtle()

# Set turtle screen to full size
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

# Function to clear screen every 10 seconds
def turtleClear():
    time.sleep(10)
    turtle.clearscreen()

# Function to create title page
def titlePage():
    jo.hideturtle()
    turtle.bgcolor('black')
    jo.color('white')
    style = ('Verdana', 42, 'normal')
    jo.write('Midterm Project' + '\n' + '   Cassiopeia' +  '\n' + ' By Jomir Uddin', font='style', align='center')
    
# Function call to title page
titlePage()

# Function call to turtleClear
turtleClear()

# Image of constellation
def bgImage():
    screen.bgpic('cass.png')
    screen.update()

# Invoke sexy Cassiopeia as background image
bgImage()

turtleClear()

# Draw stars and illuminate
def drawStars():
    turtle.hideturtle()
    turtle.bgcolor('black')
    turtle.pencolor('white')
    turtle.penup()
    turtle.goto(-90,70)
    turtle.pendown()
    turtle.shape('circle')
    turtle.stamp()
    turtle.goto(-50,-10)
    turtle.stamp()
    turtle.goto(0,0)
    turtle.stamp()
    turtle.goto(40,-50)
    turtle.stamp()
    turtle.goto(100,0)
    turtle.stamp()
    turtle.goto(100, 0)
    
drawStars()

turtleClear()

screen.update()

def plotStars():
    turtle.hideturtle()
    turtle.pencolor('black')
    turtle.penup()
    turtle.goto(-90,70)
    turtle.pendown()
    turtle.write('Segin 3.37')
    turtle.goto(-50,-10)
    turtle.write('Ruchbah 2.68')
    turtle.goto(0,0)
    turtle.write('Tsih 2.47')
    turtle.goto(40,-50)
    turtle.write('Shedir 2.24')
    turtle.goto(100,0)
    turtle.write('Caph 2.28')
    
plotStars()
