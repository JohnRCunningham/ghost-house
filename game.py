import pygame, sys, random
import level
import score
import Pax
#import menu
#import Spawnchance
from PhaseGhost import PhaseGhost
from HUD import Text
from HUD import Score
from Button import Button
from Pax import Pax
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
mapImage = "Maplv1.png"

bgImage = pygame.image.load("startMenu.png").convert()
bgRect = bgImage.get_rect()

ghosts = []

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
    
    player = Pax([width/2, height/2])
    
    ghost = PhaseGhost(PhaseGhost)
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
                
            
        if len(ghosts) < 10:
            if random.randint(0, .25*60) == 0:
                ghosts += [PhaseGhost("images/Ball/ball.png",
                          [random.randint(15,100), random.randint(15,100)],
                          [random.randint(100, width-100), random.randint(100, height-100)])
                          ]
                print ghosts[-1].rect.center
        player.update(width, height)
        
        for ghost in ghosts:
            ghost.update(width, height)
            
        for bully in ghosts:
            for victem in ghosts:
                bully.collideGhost(victem)
                bully.collidePlayer(player)
        
        for ghost in ghosts:
            if not ghost.living:
                    ghosts.remove(ghost)
 
        
        bgColor = r,g,b
        screen.fill(bgColor)
        for ghost in ghosts:
            screen.blit(ghost.image, ghost.rect)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
        clock.tick(60)

