import pygame, sys, random
import level
import score
import Pax
#import menu
#import Spawnchance
from HUD import Text
from HUD import Score
from Button import Button
from Pax import Pax
pygame.init()

clock= pygame.time.Clock()

width = 800 
height = 800
size = width, height

bgColor = r,g,b = 225, 10, 10

screen = pygame.display.set_mode(size)

timer = Score([80, height - 25], "Time: ", 36)
timerWait = 0
timerWaitMax = 6

run = False
options = False
playerType = "Pax"

bgImage = pygame.image.load("startMenu.png").convert()
bgRect = bgImage.get_rect()

startButton = Button([width/2, height-550], 
				     "startButton.png", 
				     "startButtonClicked.png")
				    

while True:
	while not run and not options:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					run = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				startButton.click(event.pos)
			if event.type == pygame.MOUSEBUTTONUP:
				if startButton.release(event.pos):
					run = True
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(startButton.image, startButton.rect)
		pygame.display.flip()
		clock.tick(60)
	
	player = Pax(playerType
	)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("left")
				if event.key == pygame.K_space:
					player.go("skill")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("stop left")
				if event.key == pygame.K_space:
					player.go("stop skill")
			
		if len(ghost) < 10:
			if random.randit(0, .25*60) == 0:
				balls += [Ball("images/Ball/ball.png",
						  [random.randint(0,10), random.randint(0,10)],
						  [random.randint(100, width-100), random.randint(100, height-100)])
						  ]
		player.update(width, height)
		for ball in balls:
			ball.update(width, height)
			
		for bully in balls:
			for victem in balls:
				bully.collideBall(victem)
				bully.collidePlayer(player)
		
		for ball in balls:
			if not ball.living:
				balls.remove(ball)
		
		bgColor = r,g,b
		screen.fill(bgColor)
		for ball in balls:
			screen.blit(ball.image, ball.rect)
		screen.blit(player.image, player.rect)
		pygame.display.flip()
		clock.tick(60)
