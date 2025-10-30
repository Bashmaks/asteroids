import sys
import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Object groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Assign containers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    # Main loop
    dt = 0
    running = True
    while running:
        # poll event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            killed = False
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    killed = True
                    break
            if not killed and asteroid.collision(player):
                print("Game over!")
                sys.exit(0)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()



if __name__ == "__main__":
    main()
