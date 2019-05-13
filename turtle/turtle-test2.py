import turtle
wn = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)


# for i in range(20):
# 	turtle.circle(5*i)
# 	turtle.circle(-5*i)
# 	turtle.left(i)
# 	turtle.color(2*i, 2*i, 2*i)

def shape(size, sides):
	for i in range(sides):
		turtle.forward(size)
		turtle.left(360.0/sides)

for i in range(20):
	shape(5*i, 5)
	turtle.left(30)

# shape(100,12)

turtle.exitonclick()