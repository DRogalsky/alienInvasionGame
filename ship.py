import pygame

class Ship:
    """a class for the players ship"""

    def __init__(self, ai_game):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the sip image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ships position based on movement flags"""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)