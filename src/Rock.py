import sys
import pygame

class Rock:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("../assets/rock.png")
        self.hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.count = 0

    def draw(self):
        info = pygame.display.Info()
        self.scale = info.current_w / 1280
        self.scaled_image = pygame.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.screen.blit(self.scaled_image, (self.x, self.y))
        self.hit_box = pygame.Rect(self.x, self.y, self.scaled_image.get_width(), self.scaled_image.get_height())
        self.count +=1

    def collision(self,mover):
            if mover.direction == 2 and mover.hit_box.colliderect(self.hit_box):
                    mover.x = self.x + self.scaled_image.get_width() + mover.scaled_image.get_width() / 2 + mover.scaled_speed /2

            elif mover.direction == 0 and mover.hit_box.colliderect(self.hit_box):
                    mover.x = self.x - mover.scaled_image.get_width() / 2 - mover.scaled_speed /2

            elif mover.direction == 1 and mover.hit_box.colliderect(self.hit_box):
                    mover.y = self.y + self.scaled_image.get_height() + mover.scaled_image.get_height() / 2 + mover.scaled_speed /2

            elif mover.direction == 3 and mover.hit_box.colliderect(self.hit_box):
                    mover.y = self.hit_box.y - mover.scaled_image.get_height() / 2 - mover.scaled_speed / 2
