import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (34, 177, 76)
light_green = (0, 255, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
blue = (0, 0, 255)


display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')
# icon = pygame.image.load('apple.png')
# pygame.display.set_icon(icon)
gameDisplay.fill(blue)


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

clock = pygame.time.Clock()
FPS = 15


tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5


# Pix = pygame.PixelArray(gameDisplay)
# Pix[10][10] = red
# pygame.draw.line(gameDisplay, red, (200, 300), (500, 500), 5)
# pygame.draw.circle(gameDisplay, red, (200, 200), 100)
# pygame.draw.rect(gameDisplay, green, (150, 150, 200, 100))
# pygame.draw.polygon(gameDisplay, white, ((140, 5),(200,16),(88, 333)))


def barrier(xlocation, randomHeight, barrier_width):
	pygame.draw.rect(gameDisplay, black, [xlocation, display_height - randomHeight, barrier_width, randomHeight])

def fireShell(xy, tankx, tanky, turPos):
	fire = True
	turPos = 2*turPos
	startingShell = list(xy)
	print("FIRE!")

	while fire:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		print (startingShell[0], startingShell[1])
		pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
		
		startingShell[0] -= (12 - turPos)*2
		startingShell[1] += int(((startingShell[0] - xy[0])*0.01)**2 - (turPos+turPos/(12-turPos)))

		if startingShell[1] > display_height:
			fire = False

		pygame.display.update()
		clock.tick(60)
		# fire = False

def tank(x, y, turPos):
	x, y = int(x), int(y)

	possibleTurrets = [
		(x-27, y-2),
		(x-20, y-14),
		(x-11, y-21),
		(x-2, y-27)
	]	
	pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight/2))
	pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))
	pygame.draw.line(gameDisplay, black, (x, y), possibleTurrets[turPos], turretWidth)


	startX = 15
	for i in range(7):
		pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth)
		startX -= 5

	return possibleTurrets[turPos]

def score(score):
	text = smallfont.render("Score: "+str(score), True, black)
	gameDisplay.blit(text, [0, 0])

def text_objects(text, color, size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	if size == "medium":
		textSurface = medfont.render(text, True, color)
	if size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displayce = 0, size = "small"):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (display_width/2), (display_height/2)+y_displayce
	gameDisplay.blit(textSurf, textRect)

def text_to_button(msg, color, x, y, width, height, size="small"):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = ((x+width/2), y+height/2)
	gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action=None):
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# print(click)
	

	if x < cur[0] < x+width and y < cur[1] < y+height:
		pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
		if click[0] == 1 and action != None:
			if action == "quit":
				pygame.quit()
			if action == "control":
				game_control()
			if action == "play":
				gameLoop()
			if action == "back":
				game_intro()

	else:
		pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
	text_to_button(text, black, x, y, width, height)

def game_control():
	gcont = True

	while gcont:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		gameDisplay.fill(white)
		message_to_screen("Controls", green, -100, size='large')
		message_to_screen("Fire: Spacebar",black, -20, size='small')
		message_to_screen("Move Turret: Up and Down",black, 10, size='small')
		message_to_screen("Move Tank: Left and Right",black, 40, size='small')
		message_to_screen("Press C to continue and Q to quit and P to pause",
			black, 70, size='small')


		button("Play", 150, 500, 100, 50, green, light_green, action="play")
		button("Back", 350, 550, 100, 50, yellow, light_yellow, action='back')
		button("Quit", 550, 500, 100, 50, red, light_red, action="quit")



		pygame.display.update()
		clock.tick(15)

def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()

		gameDisplay.fill(white)
		message_to_screen("Welcome to Tanks", green, -100, size='large')
		message_to_screen("The objective of the game is to shoot and destroy",
			black, -20, size='small')
		message_to_screen("the enemy tank before they destroy you",
			black, 10, size='small')
		message_to_screen("Press C to continue and Q to quit and P to pause",
			black, 40, size='small')


		button("Play", 150, 500, 100, 50, green, light_green, action="play")
		button("Control", 350, 500, 100, 50, yellow, light_yellow, action='control')
		button("Quit", 550, 500, 100, 50, red, light_red, action="quit")



		pygame.display.update()
		clock.tick(15)

def pause():
	paused = True
	message_to_screen("Paused", black, -100, size="large")
	message_to_screen("Press C to continue or Q to quit.", black, 25)
	pygame.display.update()

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
		# gameDisplay.fill(white)
		clock.tick(5)

def gameLoop():
	barrier_width = 50
	mainTankX = display_width * 0.9
	mainTankY = display_height * 0.9
	tankMove = 0

	currentTurPos = 0
	changeTur = 0

	xlocation = display_width/2 + random.randint(-0.2*display_width, 0.2*display_width)
	randomHeight = random.randrange(display_height*0.1, display_height*0.6)

	gameExit = False
	gameOver = False


	while not gameExit:
		gameDisplay.fill(white)
		gun = tank(mainTankX, mainTankY, currentTurPos)
		if gameOver == True:
			# gameDisplay.fill(white)
			direction = 'right'
			message_to_screen("Game over", red, -50, size='large')
			message_to_screen("press C to play again or Q to quit", black, 50, size='medium')
			pygame.display.update()	

		while gameOver == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			# print(event)
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					tankMove = -5
				elif event.key == pygame.K_RIGHT:
					tankMove = 5
				elif event.key == pygame.K_UP:
					changeTur = 1
				elif event.key == pygame.K_DOWN:
					changeTur = -1
				elif event.key == pygame.K_p:
					pause()	
				elif event.key == pygame.K_SPACE:
					fireShell(gun, mainTankX, mainTankY, currentTurPos)

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					tankMove = 0
				elif event.key == pygame.K_RIGHT:
					tankMove = 0
				elif event.key == pygame.K_UP:
					changeTur = 0
				elif event.key == pygame.K_DOWN:
					changeTur = 0


		mainTankX += tankMove
		currentTurPos += changeTur
		if currentTurPos < 0:
			currentTurPos = 0
		elif currentTurPos > 3:
			currentTurPos = 3

		if mainTankX - (tankWidth/2) < xlocation + barrier_width:
			mainTankX += 5
		


		barrier(xlocation, randomHeight, barrier_width)
		pygame.display.update()

		clock.tick(FPS)

	pygame.quit()
	quit()

game_intro()
gameLoop()