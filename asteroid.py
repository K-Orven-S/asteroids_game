from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=(self.position.x, self.position.y), radius=PLAYER_RADIUS, width=LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)