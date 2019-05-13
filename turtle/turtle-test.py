import turtle
import math
import random
import os


#Set up screen
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.bgpic('bgimage.gif')
wn.tracer(3)

#Draw border
mypen = turtle.Turtle()
mypen.color('white')
mypen.penup()
mypen.setposition(-300, -300)
mypen.down()
mypen.pensize(3)
for side in range(4):
	mypen.forward(600)
	mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()

#Create goals
maxGoals = 6
goals = []
for i in range(maxGoals):
	goals.append(turtle.Turtle())
	goals[i].color("red")
	goals[i].shape("circle")
	goals[i].penup()
	goals[i].speed(0)
	goals[i].setposition(random.randint(-300, 300), 
		random.randint(-300, 300))


#Create player score
score = 0

#Set speed variable'
speed = 1

# Define functions
def turnleft():
	player.left(30)

def turnright():
	player.right(30)

def increasespeed():
	global speed
	speed += 1

def decreasespeed():
	global speed
	speed -= 1

def isCollision(t1,t2):
	return math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+
		math.pow(t1.ycor()-t2.ycor(),2)) < 15


#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

for i in range(2000):
	player.forward(speed)

	# os.system("sound.mp3")

	# Boundary Checking
	if player.xcor() > 300 or player.xcor() < -300:
		player.right(180)
	if player.ycor() > 300 or player.ycor() < -300:
		player.right(180)

	for count in range(maxGoals):
		goals[count].forward(2)
		if goals[count].xcor() > 300 or goals[count].xcor() < -300:
			goals[count].right(180)
		if goals[count].ycor() > 300 or goals[count].ycor() < -300:
			goals[count].right(180)

		# Collision checking
		if isCollision(player, goals[count]):
			# goal.hideturtle()
			goals[count].setposition(random.randint(-300, 300), 
				random.randint(-300, 300))
			goals[count].right(random.randint(0, 360))
			score += 1
			
			#Draw the score on the screen
			mypen.undo()
			mypen.penup()
			mypen.hideturtle()
			mypen.setposition(-290, 310)
			scorestring = "Score: %s" %score
			mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

