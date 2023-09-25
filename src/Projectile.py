import pygame
import math


class Projectile:
    def __init__(self, screen, speed, x, y, direction):
        # Everything needed to create a new projectile
        self.screen = screen
        self.speed = speed
        self.x = x
        self.y = y
        self.direction = direction
        self.image = pygame.image.load("../assets/tear.png").convert_alpha()
        self.scaled_image = self.image
        info = pygame.display.Info()
        self.scale = info.current_w / 1280
        self.scaled_image = pygame.transform.scale(self.image, (
        self.image.get_width() * self.scale, self.image.get_height() * self.scale))

        self.tear_gone = False

        self.speed_x = math.cos((-self.direction * math.pi) / 2) * self.speed
        self.speed_y = math.sin((-self.direction * math.pi) / 2) * self.speed

        # The hit box of each projectile
        self.hit_box = pygame.Rect(self.x - self.image.get_width() / 2,
                                   self.y - self.image.get_height() / 2,
                                   self.image.get_width(), self.image.get_height())

    # Draws the projectile
    def draw(self):
        self.scaled_image = self.image
        info = pygame.display.Info()
        self.scale = info.current_w / 1280
        self.scaled_image = pygame.transform.scale(self.image, (
            self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.screen.blit(self.scaled_image, (self.x - self.scaled_image.get_width() / 2, self.y - self.scaled_image.get_height() / 2))

    # Moves the projectile based on the direction character is facing
    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x

        # Moves the hit box with the projectile
        self.hit_box = pygame.Rect(self.x - self.scaled_image.get_width() / 2,
                                   self.y - self.scaled_image.get_height() / 2,
                                   self.scaled_image.get_width(), self.scaled_image.get_height())
