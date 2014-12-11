import pygame, sys, random
#import player
import level
import HUD
import score
#import menu
#import Spawnchance


pygame.init()

clock= pygame.time.Clock()

width = 1200 
height = 600
size = width, height

bgColor = r,g,b = 225, 10, 10

screen = pygame.display.set_mode(size)

run = False
options = False
playerType = "pax"

while True:
	while not run and not options:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					run = True
		bgColor = 20,20,20
		screen.fill(bgColor)
		pygame.display.flip()
		clock.tick(60)
	
	player = Player(playerType, [0,0])
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
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("stop left")
			
		if len(balls) < 10:
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
