import pygame
from constants import *
from player import Player
from asteroid import Asteroid, Shot
from asteroidfield import AsteroidField
import sys

pygame.init()


x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    try:
        with open("scores.txt", "r") as f:
            high_score = int(f.read())
    except FileNotFoundError:
        high_score = 0
    
    font = pygame.font.Font(None, 36)
    score = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x, y)

    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill((0, 0, 0))
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                if score > high_score:
                    high_score = score
                with open("scores.txt", "w") as f:
                    f.write(str(high_score))
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.detect_collision(asteroid):
                    destroyed = asteroid.split()
                    if destroyed:
                        score += 1

    
        for each_drawable in drawable:
            each_drawable.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        high_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        
        screen.blit(score_text, (10, 10))
        screen.blit(high_text, (10, 40))

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
