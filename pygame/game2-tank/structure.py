import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
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

# Pix = pygame.PixelArray(gameDisplay)
# Pix[10][10] = red
# pygame.draw.line(gameDisplay, red, (200, 300), (500, 500), 5)
# pygame.draw.circle(gameDisplay, red, (200, 200), 100)
# pygame.draw.rect(gameDisplay, green, (150, 150, 200, 100))
# pygame.draw.polygon(gameDisplay, white, ((140, 5),(200,16),(88, 333)))

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
			black, -30, size='small')
		message_to_screen("the enemy tank before they destroy you",
			black, 10, size='small')
		message_to_screen("Press C to continue and Q to quit and P to pause",
			black, 40, size='small')
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

	gameExit = False
	gameOver = False

	while not gameExit:

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
					pass
				elif event.key == pygame.K_RIGHT:
					pass
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					pass
				elif event.key == pygame.K_p:
					pause()	


		gameDisplay.fill(white)
		pygame.display.update()

		clock.tick(FPS)

	pygame.quit()
	quit()

game_intro()
gameLoop()