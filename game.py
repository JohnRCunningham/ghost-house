import pygame, sys, random
import player
import level
import HUD
import score
import menu
import Spawnchance


pygame.init()

clock= pygame.time.Clock()

width = 1200 
height = 600
size = width, height

bgColor = r,g,b = 225, 10, 10

screen = pygame.display.set_mode(size)

player = PlayerPax([width/2, height/2])
