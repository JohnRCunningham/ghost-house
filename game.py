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
timerWaitMax = 6000

run = False
options = False
playerType = "Pax"



mapImage = pygame.image.load("Resources/Maps/Maplv1.png").convert()
mapRect = mapImage.get_rect()

bgImage = pygame.image.load("Resources/Objects/download.png").convert()
bgRect = bgImage.get_rect()

ghosts = []

walls = [Wall([0,0],[90,800]),
         Wall([710,100],[800,800]),
         Wall([0,0], [800,90]),
         Wall([0,710],[800,800]),
         Wall([127,126],[373,146]),
         Wall([127,126],[146,373]),
         Wall([127,427],[145,674]),
         Wall([127,653],[373,674]),
         Wall([427,654],[674,674]),
         Wall([654,427],[674,674]),
         Wall([654,126],[674,373]),
         Wall([427,126],[674,143]),
         Wall([177,176],[373,196]),
         Wall([177,176],[197,373]),
         Wall([177,427],[197,624]),
         Wall([177,604],[373,624]),
         Wall([427,604],[626,624]),
         Wall([603,427],[626,624]),
         Wall([427,175],[626,196]),
         Wall([603,175],[626,373]),
         Wall([227,227],[373,246]),
         Wall([227,227],[247,373]),
         Wall([227,427],[247,574]),
         Wall([227,554],[373,574]),
         Wall([427,554],[574,574]),
         Wall([554,427],[574,574]),
         Wall([554,227],[574,373]),
         Wall([427,227],[574,246]),
         Wall([427,502],[525,524]),
         Wall([502,427],[525,524]),
         Wall([427,275],[525,298]),
         Wall([276,275],[372,298]),
         Wall([276,275],[298,373]),
         Wall{[277,427],[298,524])]

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
                
                
            
        if len(ghosts) < 20:
            if random.randint(0, .25*100) == 0:
                ghosts += [PhaseGhost("images/Ball/ball.png",
                          [random.randint(-2,2), random.randint(-2,2)],
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
