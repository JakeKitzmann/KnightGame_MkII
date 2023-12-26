import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Zelda')

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('resources/audio/main.ogg')
        main_sound.set_volume(.4)
        main_sound.play(loops = -1)



    def run(self):


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            if self.level.new_game:
                self.level = Level()




if __name__ == '__main__':
    game = Game()
    game.run()
