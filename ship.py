import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, ai_settings,screen):
        super().__init__()
        """Initialize the ship, and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left  = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        # 根据移动标志调整飞机的位置
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center1 += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center1 -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center2 -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center2 += self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx = self.center1
        self.rect.centery = self.center2
    def center_ship(self):
        #让飞船在屏幕上居中
        self.center1 = self.screen_rect.centerx
        self.center2= self.screen_rect.bottom
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
