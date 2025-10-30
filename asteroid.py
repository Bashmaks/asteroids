import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        one = Asteroid(*self.position, radius)
        two = Asteroid(*self.position, radius)
        one.velocity = 1.2 * self.velocity.rotate(angle)
        two.velocity = 1.2 * self.velocity.rotate(-angle)


