import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

img = pygame.image.load('snake.png')
img_apple = pygame.image.load('apple.png')

clock = pygame.time.Clock()
block_size = 20
AppleThickness = 30
FPS = 15
direction = 'right'

font = pygame.font.SysFont(None, 25)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def randAppleGen():
	randAppleX = round(random.randrange(0, display_width - AppleThickness))#/block_size)*block_size
	randAppleY = round(random.randrange(0, display_height - AppleThickness))#/block_size)*block_size
	return randAppleX, randAppleY

def text_objects(text, color, size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	if size == "medium":
		textSurface = medfont.render(text, True, color)
	if size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displayce = 0, size = "small"):
	# screen_text = font.render(msg, True, color)
	# gameDisplay.blit(screen_text, [display_width/2, display_height/2])
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
		message_to_screen("Welcome to Slither", green, -100, size='large')
		message_to_screen("The objective of the game is to eat red apples",
			black, -30, size='small')
		message_to_screen("The more apples you eat, the longer you will be",
			black, 10, size='small')
		message_to_screen("Press C to continue and Q to quit and P to pause",
			black, 40, size='small')
		pygame.display.update()
		clock.tick(15)

def score(score):
	text = smallfont.render("Score: "+str(score), True, black)
	gameDisplay.blit(text, [0, 0])

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

def snake(block_size, snakelist):

	if direction == 'right':
		head = pygame.transform.rotate(img, 270)
	if direction == 'left':
		head = pygame.transform.rotate(img, 90)
	if direction == 'up':
		head = img
	if direction == 'down':
		head = pygame.transform.rotate(img, 180)

	gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
	for XnY in snakelist[:-1]:
		pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def gameLoop():

	global direction

	gameExit = False
	gameOver = False

	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = block_size
	lead_y_change = 0
	snakeList = []
	snakeLength = 1

	randAppleX, randAppleY = randAppleGen()

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
					# lead_x_change -= 10
					direction = 'left'
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					# lead_x_change += 10
					direction = 'right'
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					# lead_y_change -= 10
					direction = 'up'
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					# lead_y_change += 10	
					direction = 'down'		
					lead_y_change = block_size
					lead_x_change = 0
				elif event.key == pygame.K_p:
					pause()	
			# print(event)

			'''
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					lead_y_change = 0
			'''
		if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
			gameOver = True


		lead_x += lead_x_change
		lead_y += lead_y_change

		gameDisplay.fill(white)


		# pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
		gameDisplay.blit(img_apple, (randAppleX, randAppleY))
		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				gameOver = True

		snake(block_size, snakeList)

		score(snakeLength-1)

		pygame.display.update()

		
		if lead_x > randAppleX - block_size and lead_x < randAppleX + AppleThickness:
			if lead_y > randAppleY - block_size and lead_y < randAppleY + AppleThickness:
				snakeLength +=  1
				randAppleX, randAppleY = randAppleGen()


		clock.tick(FPS)

		
	# message_to_screen("You Lose, byebye~", red)
	# pygame.display.update()
	# time.sleep(2)


	pygame.quit()
	quit()


if __name__ == '__main__':
	game_intro()
	gameDisplay.fill(white)
	message_to_screen("Please Choose the speed(1~3)", red)
	pygame.display.update()	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					FPS = 5
					gameLoop()
				elif event.key == pygame.K_2:
					FPS = 15
					gameLoop()
				elif event.key == pygame.K_3:
					FPS = 30
					gameLoop()

	