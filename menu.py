import pygame
from settings import *

class Menu():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.menu_surf = pygame.image.load('resources/images/menu_screen/pixelated_castle.jpg')
        self.menu_rect = self.menu_surf.get_rect(topleft = (0,0))

        self.text_surf = self.font.render('Monster Rush', False, TEXT_COLOR)
        self.text_rect = self.text_surf.get_rect(topleft = (500,630))

        self.direction_surf = self.font.render('Press Space to Begin!', False, TEXT_COLOR)
        self.direction_rect = self.direction_surf.get_rect(topleft = (500,670))

        self.girl_surf = pygame.image.load('resources/images/graphics/player/selection.png')
        self.girl_rect = self.girl_surf.get_rect(topleft = (50, 50))

        self.knight_surf = pygame.image.load('resources/images/graphics/knight/selection.png')
        self.knight_rect = self.knight_surf.get_rect(topleft = (300, 50))

    def display(self):
        self.display_surface.blit(self.menu_surf, self.menu_rect)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.menu_rect)
        self.display_surface.blit(self.menu_surf, self.menu_rect)
        self.display_surface.blit(self.text_surf, self.text_rect)
        self.display_surface.blit(self.direction_surf, self.direction_rect)
        self.display_surface.blit(self.girl_surf, self.girl_rect)
        self.display_surface.blit(self.knight_surf, self.knight_rect)



        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
