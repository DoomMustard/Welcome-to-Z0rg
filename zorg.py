
# Importing the modules needed for the program
import sys
import pygame
from settings import Settings
from pygame import mixer
from pygame import font

white = (255, 255, 255)
black = (0,0,0)
X = 1200
Y = 800



# initializing the music for the main screen
mixer.init()
mixer.music.load('/users/doomm/onedrive/desktop/spacetheme.mp3')
mix = mixer.music.play()

# opening and initializing the background image
bg = pygame.image.load('/users/doomm/onedrive/desktop/space2.png')
bg = pygame.transform.scale(bg, (1200, 800))

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 64)
text = font.render('Welcome to Z0rg!', True, white)
textRect = text.get_rect()
textRect.center = (X//2, Y//2)

# Starts and makes the class for the games basics
class Zorg:
    
    def __init__(self):
        # starts the game, creates resources
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Welcome To Z0rg!")
        
        self.settings = Settings()
        
        


        
        
    def run_game(self):
        # Starts mainloop and starts game
        while True:
            # Watch for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            
            self.screen.blit(bg, [0,0]) 
            self.screen.blit(text, [X//2, Y//2])          
            pygame.display.flip()
            
            
if __name__ == '__main__':
    # make instance and runs game
    zo = Zorg()
    zo.run_game()
                