import pygame, sys, random
import level
import score
import Pax
import Speedypax
#import menu
#import Spawnchance
from PhaseGhost import PhaseGhost
from HUD import Text
from HUD import Score
from Button import Button
from Pax import Pax
from Vision import Vision
from Wall import Wall
pygame.init()

clock= pygame.time.Clock()

width = 800 
height = 800
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

timer = Score([80, height - 25], "Time: ", 36)
timerWait = 0
timerWaitMax = 6

run = False
options = False
playerType = "Pax"

mapImage = pygame.image.load("Resources/Maps/Maplv1.png").convert()
mapRect = mapImage.get_rect()

bgImage = pygame.image.load("Resources/Objects/download.png").convert()
bgRect = bgImage.get_rect()

ghosts = []

walls = [Wall([0,0],[100,800]),
		[Wall([0,100],[800,0]),
		[Wall([800,800],[0,700]),
		[Wall([700,100],[800,800])]

startButton = Button([width/2, height-550], 
					 "Resources/Objects/startButton.png", 
					 "Resources/Objects/startButtonClicked.png")


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
	
	players = [Pax([width/2, height/2])]
	visions = []
	for player in players:
		visions += [Vision("small", player)]
	
	ghosts = []
	while run and len(players)> 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					players[0].go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					players[0].go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					players[0].go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					players[0].go("left")
				#if event.key == pygame.K_SPACE:
				   # screen.blit(vision.image, vision.rect)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					players[0].go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					players[0].go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					players[0].go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					players[0].go("stop left")
				#if event.key == pygame.K_SPACE:
					#not screen.blit(vision.image, vision.rect)
				
				
			
		if len(ghosts) < 10:
			if random.randint(0, .25*60) == 0:
				ghosts += [PhaseGhost("images/Ball/ball.png",
						  [random.randint(-3,3), random.randint(-3,3)],
						  [random.randint(100, width-100), random.randint(100, height-100)])
						  ]
				print ghosts[-1].rect.center
		player.update(width, height)
		for vision in visions:
			vision.update()
		
		for ghost in ghosts:
			ghost.update(width, height)
			
		for player in players:
			for ghost in ghosts:
				player.collideGhost(ghost)
				ghost.collidePlayer(player)
		
		for player in players:
			if not player.living:
					players.remove(player)
		
		for wall in walls:
			player.collideWall(wall)
		
		for wall in walls:
			screen.blit(wall.image, wall.rect)
				
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(mapImage, mapRect)
		for ghost in ghosts:
			screen.blit(ghost.image, ghost.rect)
		for player in players:
			screen.blit(player.image, player.rect)
		screen.blit(vision.image, vision.rect)
		pygame.display.flip()
		clock.tick(60)
	run = False
