import pygame
import random
import math
from Projectile import Projectile
from laser import Laser


class Enemy:
    def __init__(self, screen, x, y, max_hp):

        # Gets info about the screen and adds in a scaling feature with display size
        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        # needed initial variables for placement and movement
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

        # lists of things the enemies can create
        self.projectiles = []
        self.laser = []
        self.laser_indicator = []

        # Setting accumulators for movement and firing
        self.count = random.randint(0, 100)
        self.count_fire = 0
        self.count_fire_laser = 0

        # Enemy stats
        self.fire_rate = .5
        self.projectile_speed = 3
        self.max_hp = max_hp
        self.direction = 3
        # Different enemy Sprites
        self.hp = max_hp
        self.dead = False
        self.speed = 2

        # Different enemy Sprites and sounds
        self.load_enemy_assets()

        # List of all the enemy types
        self.enemy_variants = [self.apple_enemy,
                               self.delta_enemy,
                               self.sigma_right_enemy,
                               self.theta_enemy,
                               self.cat_right_enemy,
                               self.charmander_right_enemy,
                               self.trigon_boss]

        # Decided if the enemy being spawned is a boss and if not randomizes enemies spawned
        if self.max_hp >= 2500:
            self.enemy_type = len(self.enemy_variants) - 1
        else:
            self.enemy_type = random.randint(0, len(self.enemy_variants) - 2)

        # Enemy movement boundaries
        self.left_bound = 75 * self.scale
        self.top_bound = 72 * self.scale
        self.right_bound = self.screen.get_width() - 75 * self.scale
        self.bottom_bound = (720 - 72) * self.scale

        # Scales the image of the enemy with the screen size and creates hit box for it
        self.scaled_image = pygame.transform.scale(self.enemy_variants[self.enemy_type], (
            self.enemy_variants[self.enemy_type].get_width() * self.scale,
            self.enemy_variants[self.enemy_type].get_height() * self.scale))
        self.hit_box = pygame.Rect(self.x, self.y,
                                   self.scaled_image.get_width(),
                                   self.scaled_image.get_height())

        # sets the sounds for different enemies
        if self.enemy_type == 0:
            self.sound = self.apple_crunch
            self.sound.set_volume(.5)
        elif self.enemy_type == 4:
            self.sound = self.cat_meow
            self.sound.set_volume(.5)
        else:
            self.sound = self.oof
            self.sound.set_volume(.5)

    # draws the enemy
    def draw(self):

        # Gets info about the screen and adds in a scaling feature with display size
        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        # Creates image to scale and blits in on the screen
        self.scaled_image = pygame.transform.scale(self.enemy_variants[self.enemy_type], (
            self.enemy_variants[self.enemy_type].get_width() * self.scale,
            self.enemy_variants[self.enemy_type].get_height() * self.scale))
        self.screen.blit(self.scaled_image, (self.x, self.y))

        # Creates and displays a health bar for the bosses
        if self.enemy_type == len(self.enemy_variants) - 1:
            pygame.draw.rect(self.screen, (20, 20, 20),
                             (self.screen.get_width() / 20, (720 - 36) * self.scale, 500 * self.scale, 20 * self.scale))
            pygame.draw.rect(self.screen, (250, 0, 0),
                             (self.screen.get_width() / 20, (720 - 36) * self.scale,
                              500 * self.scale * self.hp / self.max_hp, 20 * self.scale))

    # moves the enemy
    def move(self):

        # decided which direction the enemy will move and how long it will move in that direction
        if self.count >= 90:
            self.direction = random.randint(0, 3)
            # Enemy moving towards the right
            if self.direction == 0:
                self.enemy_variants[2] = self.sigma_right_enemy
                self.enemy_variants[4] = self.cat_right_enemy
                self.enemy_variants[5] = self.charmander_right_enemy

            # Enemy moving towards the left
            if self.direction == 2:
                self.enemy_variants[2] = self.sigma_left_enemy
                self.enemy_variants[4] = self.cat_left_enemy
                self.enemy_variants[5] = self.charmander_left_enemy

            self.speed_x = math.cos((-self.direction * math.pi) / 2) * self.speed
            self.speed_y = math.sin((-self.direction * math.pi) / 2) * self.speed
            self.count = 0

        # Moves the hit box with the enemy
        self.hit_box = pygame.Rect(self.x, self.y,
                                   self.scaled_image.get_width(),
                                   self.scaled_image.get_height())

        # Adds in a pause period in the movement of the enemy
        if 60 < self.count < 90:
            self.speed_x = 0
            self.speed_y = 0
        self.count += 1

        # # Actually moves the enemy
        self.x += self.speed_x
        self.y += self.speed_y

        # recreates the bounds of the screen for the enemy in the case that the screen size changed
        self.left_bound = 75 * self.scale
        self.top_bound = 72 * self.scale
        self.right_bound = self.screen.get_width() - 75 * self.scale
        self.bottom_bound = (720 - 72) * self.scale

        # Makes the enemy not leave the room
        if self.x < self.left_bound:
            self.x = self.left_bound
        if self.x > self.right_bound - self.scaled_image.get_width():
            self.x = self.right_bound - self.scaled_image.get_width()
        if self.y < self.top_bound:
            self.y = self.top_bound
        if self.y > self.bottom_bound - self.scaled_image.get_height():
            self.y = self.bottom_bound - self.scaled_image.get_height()

    def fire(self):

        # Shoots new projectiles based on the rate given
        if self.count_fire * self.fire_rate >= 60:

            # Makes a small offset in where the circle of the projectiles
            # starts so that it fires a little different each time
            offset = random.randint(1, 10)

            # Creates a circle of projectiles
            for k in range(0, 14, 1):
                self.fire_projectile(offset / 10 + k / 3.5)
            self.count_fire = 0
        self.count_fire += 1

        # fire 4 lasers and precursor indicators for the lasers
        if self.count_fire_laser >= 120:
            for k in range(0, 4, 1):
                self.fire_laser(k)
                self.count_fire_laser = 0
        if self.count_fire_laser >=60:
            for j in range(0,4,1):
                self.fire_indicator(j)
        self.count_fire_laser += 1

    def fire_projectile(self, direction):
        # Makes the projectiles that were fired
        proj = Projectile(self.screen, self.projectile_speed, self.x + self.scaled_image.get_width() / 2,
                          self.y + self.scaled_image.get_height() / 2, direction)
        self.projectiles.append(proj)

    def fire_laser(self, direction):
        # Makes the lasers that were fired
        laser_beam = Laser(self.screen, self.x, self.y, self.scaled_image, direction, 1500)
        self.laser.append(laser_beam)

    def fire_indicator(self, direction):
        # Makes the laser indicators that were fired
        laser_indicator = Laser(self.screen, self.x, self.y, self.scaled_image, direction, 1500)
        self.laser_indicator.append(laser_indicator)

    # gets rid of all the projectiles and lasers
    def remove_projectiles(self):
        # Gets rid of projectiles for all cases
        for k in range(len(self.projectiles) - 1, -1, -1):
            if self.projectiles[k].y < self.top_bound or self.projectiles[k].y > self.bottom_bound - \
                    self.projectiles[k].image.get_height() / 2 or self.projectiles[k].x < self.left_bound + \
                    self.projectiles[k].image.get_width() / 2 or self.projectiles[k].x > self.right_bound - \
                    self.projectiles[k].image.get_width() / 2 or self.projectiles[k].tear_gone:
                del self.projectiles[k]

        # gets rid of lasers
        for k in range(len(self.laser) - 1, -1, -1):
            if self.laser[k].lasergone:
                del self.laser[k]

        # gets rid of laser indicators
        for k in range(len(self.laser_indicator) - 1, - 1, - 1):
            if self.laser_indicator[k].lasergone:
                del self.laser_indicator[k]

    # Loads and sets all pictures and sounds to variables
    def load_enemy_assets(self):

        self.apple_enemy = pygame.image.load("../assets/apple.png").convert_alpha()

        self.delta_enemy = pygame.image.load("../assets/Delta.png").convert_alpha()

        self.theta_enemy = pygame.image.load("../assets/theta.png").convert_alpha()

        self.sigma_right_enemy = pygame.image.load("../assets/Sigma_enemy_right.png").convert_alpha()
        self.sigma_left_enemy = pygame.image.load("../assets/Sigma_enemy_left.png").convert_alpha()

        self.cat_right_enemy = pygame.image.load("../assets/cat_right.png").convert_alpha()
        self.cat_left_enemy = pygame.image.load("../assets/cat_left.png").convert_alpha()

        self.charmander_right_enemy = pygame.image.load("../assets/charmander_right.png").convert_alpha()
        self.charmander_left_enemy = pygame.image.load("../assets/charmander_left.png").convert_alpha()

        self.apple_crunch = pygame.mixer.Sound("../assets/Crunch.mp3")
        self.cat_meow = pygame.mixer.Sound("../assets/Meow.mp3")
        self.oof = pygame.mixer.Sound("../assets/minecraft oof.mp3")

        self.trigon_boss = pygame.image.load("../assets/trigon.png").convert_alpha()
