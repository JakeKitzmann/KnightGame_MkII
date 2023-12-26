import pygame
from settings import *

class MainMenu():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.menu_surf = pygame.image.load('resources/images/menu_screen/pixelated_castle.jpg')
        self.menu_rect = self.menu_surf.get_rect(topleft = (0,0))

        self.text_surf = self.font.render('The Legend of Zelda', False, TEXT_COLOR)
        self.text_rect = self.text_surf.get_rect(topleft = (500,630))

        self.direction_surf = self.font.render('Press Space to Begin!', False, TEXT_COLOR)
        self.direction_rect = self.direction_surf.get_rect(topleft = (500,670))

    def display(self):
        self.display_surface.blit(self.menu_surf, self.menu_rect)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.menu_rect)
        self.display_surface.blit(self.menu_surf, self.menu_rect)
        self.display_surface.blit(self.text_surf, self.text_rect)
        self.display_surface.blit(self.direction_surf, self.direction_rect)



        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return 1
