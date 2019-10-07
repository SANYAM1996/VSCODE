# creating the ship class
class Ship():
    def __init__(self,screen):
        '''initialize the ship and set its starting'''
        self.screen = screen
        # load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # start each new ship at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image,self.rect)