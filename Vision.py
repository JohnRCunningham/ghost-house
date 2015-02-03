import pygame, math

class Vision():
    def __init__(self, kind, player):
        self.kind = kind
        self.player = player
        if self.kind == "small":
            self.image = pygame.image.load("40pxRadius.png")
        self.rect = self.image.get_rect(center = self.player.rect.center)   
        
        
    def update(self):
        self.rect.center = self.player.rect.center
        
    
