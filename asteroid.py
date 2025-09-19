from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
  containers = ()

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return True
    else:
      random_angle = random.uniform(20, 50)
      vector1 = self.velocity.rotate(random_angle)
      vector2 = self.velocity.rotate(random_angle * -1)
      new_radius = self.radius - ASTEROID_MIN_RADIUS

      offset1 = vector1.normalize() * 5
      offset2 = vector2.normalize() * 5

      asteroid1 = Asteroid(self.position.x + offset1.x, self.position.y + offset1.y, new_radius)
      asteroid2 = Asteroid(self.position.x + offset2.x, self.position.y + offset2.y, new_radius)
      asteroid1.velocity = vector1 * 1.2
      asteroid2.velocity = vector2 * 1.2
      return False

class Shot(CircleShape):
  containers = ()

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
  
  def update(self, dt):
    self.position += self.velocity * dt