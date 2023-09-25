import pygame
import math

class Laser:
    def __init__(self, screen, x, y, shooter, direction, length):
        self.screen = screen
        self.x = x
        self.y = y
        self.shooter = shooter
        self.lasergone = False
        self.length = length

        self.count = 0
        self.x_change = round(math.cos((-direction * math.pi) / 2),1)
        self.y_change = round(math.sin((-direction * math.pi) / 2),1)


        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        if direction == 0 or direction == 2:
            self.hit_box = pygame.Rect(self.x + self.shooter.get_width() / 2, self.y + self.shooter.get_height() / 2 - 10,
                                       self.length * self.x_change, 20*self.scale)
        else:
            self.hit_box = pygame.Rect(self.x + self.shooter.get_width() / 2 - 10, self.y + self.shooter.get_height() / 2,
                                       20 *self.scale, self.length * self.y_change)

    def draw(self):
        laser_width =int((20 * self.scale) // 1)
        pygame.draw.line(self.screen,(150,0,0),(self.x + self.shooter.get_width() / 2, self.y + self.shooter.get_height() / 2)
                         ,(self.x + self.shooter.get_width() / 2 + self.length * self.x_change, self.y + self.shooter.get_height() / 2 + self.length *
                           self.y_change),laser_width)
        pygame.draw.circle(self.screen,(150,0,0),(self.x + 1+ self.shooter.get_width() / 2 + self.length * self.x_change, self.y + 1 + self.shooter.get_height() / 2 + self.length *
                           self.y_change),10 *self.scale)
        pygame.draw.circle(self.screen, (150, 0, 0), (self.x + 1+self.shooter.get_width() / 2, self.y +1+ self.shooter.get_height() / 2), 10 *self.scale)
        self.count +=1


    def draw_indicator(self):
        pygame.draw.line(self.screen,(150,0,0),(self.x + self.shooter.get_width() / 2, self.y + self.shooter.get_height() / 2)
                         ,(self.x + self.shooter.get_width() / 2 + self.length * self.x_change, self.y + self.shooter.get_height() / 2 + self.length *
                           self.y_change),1)
