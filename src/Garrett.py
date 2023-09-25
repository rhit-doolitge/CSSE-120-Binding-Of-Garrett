
import pygame
import math
from Projectile import Projectile
from laser import Laser



class Garrett:
    def __init__(self, screen, x, y, character_num):

        # Gets info about the screen and adds in a scaling feature with display size
        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        # Things needed to create character
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = 3
        self.count = 0
        self.alldead = False
        self.roomcount = 1
        self.boss_room_count = 1
        self.proj_type = 0

        # Loads images and stats of the characters
        self.load_images()
        self.load_stats(character_num)

        # Projectiles list
        self.projectiles = []
        self.lasers = []

        # Moving Bounds for the character
        self.left_bound = 75 * self.scale
        self.top_bound = 72 * self.scale
        self.right_bound = self.screen.get_width() - 75 * self.scale
        self.bottom_bound = (720 - 72) * self.scale

        # Different images for the character movement

        self.image = self.character
        self.scaled_image = pygame.transform.scale(self.image,(self.image.get_width()*self.scale,self.image.get_height()*self.scale))

        # self.sound = pygame.mixer.Sound("../assets/Garrett.mp3")
        self.hit_box = pygame.Rect(self.x - self.image.get_width() / 2,
                                   self.y - self.image.get_height() / 2,
                                   self.image.get_width(), self.image.get_height())

    # Draws the character on the window
    def draw(self):

        # Gets info about the screen and adds in a scaling feature with display size
        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        # Creates scaled image and blits image of charcter on screen
        self.scaled_image = pygame.transform.scale(self.image,(self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.screen.blit(self.scaled_image, (self.x - self.scaled_image.get_width() / 2, self.y- self.scaled_image.get_height() / 2))

    # Moves the character
    def move(self, direction):
        self.direction = direction

        # Movement in different directions
        if self.direction == 2:
            self.image = self.character_to_left
        if self.direction == 0:
            self.image = self.character_to_right
        if self.direction == 1:
            self.image = self.character_to_back
        if self.direction == 3:
            self.image = self.character

        # Gets info about the screen and adds in a scaling feature with display size
        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        # Scales speed and creates x and y components
        self.scaled_speed = self.speed * self.scale
        self.speedx = math.cos((-direction * math.pi) / 2) * self.scaled_speed
        self.speedy = math.sin((-direction * math.pi) / 2) * self.scaled_speed

        # Resets bounds just in case the screen size changed
        self.left_bound = 75 * self.scale
        self.top_bound = 72 * self.scale
        self.right_bound = self.screen.get_width() - 75 * self.scale
        self.bottom_bound = (720 - 72) * self.scale

        # Makes character actually move
        self.x += self.speedx
        self.y += self.speedy

    # Shoots a new projectile based on the direction that is given from arrow keys
    def fire(self, direction):

        # Sets the direction gotten from arrow keys
        self.direction = direction

        if self.proj_type == 0:
            # Shoots new projectiles based on the rate given if that is the projectile type
            if self.count * self.fire_rate >= 60:
                proj = Projectile(self.screen, self.projectile_speed, self.x, self.y, self.direction)
                self.projectiles.append(proj)
                self.count = 0

        # Shoots a laser if that is the projectile type
        if self.proj_type == 1:
            laser = Laser(self.screen, self.x - self.scaled_image.get_width() / 2, self.y - self.scaled_image.get_height() / 2,
                          self.scaled_image, self.direction, self.projectile_speed * 25)
            self.lasers.append(laser)

    # Gets rid of projectiles
    def remove_projectiles(self):
        for k in range(len(self.projectiles) - 1, -1, -1):
            if self.projectiles[k].y < self.top_bound or self.projectiles[k].y > self.bottom_bound - \
                    self.projectiles[k].image.get_height() / 2 or self.projectiles[k].x < self.left_bound + \
                    self.projectiles[k].image.get_width() / 2 or self.projectiles[k].x > self.right_bound - \
                    self.projectiles[k].image.get_width() / 2 or self.projectiles[k].tear_gone:
                del self.projectiles[k]
        for k in range(len(self.lasers) - 1, -1, -1):
            if self.lasers[k].count == 1:
                del self.lasers[k]

    # Creates the player hit box
    def hit_box_make(self):
        self.hit_box = pygame.Rect(self.x - self.scaled_image.get_width() / 2,
                                   self.y - self.scaled_image.get_height() / 2,
                                   self.scaled_image.get_width(), self.scaled_image.get_height())

    # All the logic for the movement boundaries and ability to go through doors
    def bounds(self, room):
        top = False
        bot = False
        left = False
        right = False
        # If all the enemies are dead it creates openings in the boundaries for the doors if there is a door there
        if self.alldead:
            for k in range(len(room.doors)):
                if room.doors[k] == "top":
                    top = True
                if room.doors[k] == "bottom":
                    bot = True
                if room.doors[k] == "left":
                    left = True
                if room.doors[k] == "right":
                    right = True

            if self.y < self.top_bound and top == False:
                self.y = self.top_bound
            if self.y > self.bottom_bound - self.scaled_image.get_height() / 2 and bot == False:
                self.y = self.bottom_bound - self.scaled_image.get_height() / 2
            if self.x < self.left_bound + self.scaled_image.get_width() / 2 and left == False:
                self.x = self.left_bound + self.scaled_image.get_width() / 2
            if self.x > self.right_bound - self.scaled_image.get_width() / 2 and right == False:
                self.x = self.right_bound - self.scaled_image.get_width() / 2

            if self.x < self.screen.get_width() / 2 - self.scaled_image.get_width() / 2 or \
                    self.x > self.screen.get_width() / 2 + self.scaled_image.get_width() / 2:
                if self.y < self.top_bound:
                    self.y = self.top_bound
                if self.y > self.bottom_bound - self.scaled_image.get_height() / 2:
                    self.y = self.bottom_bound - self.scaled_image.get_height() / 2
            if self.y < self.screen.get_height() / 2 - self.scaled_image.get_height() / 2 or \
                    self.y > self.screen.get_height() / 2 + self.scaled_image.get_height() / 2:
                if self.x < self.left_bound + self.scaled_image.get_width() / 2:
                    self.x = self.left_bound + self.scaled_image.get_width() / 2
                if self.x > self.right_bound - self.scaled_image.get_width() / 2:
                    self.x = self.right_bound - self.scaled_image.get_width() / 2


        # If there are enemies alive there are no openings for doors
        else:
            # Movement bounds
            if self.x < self.left_bound + self.scaled_image.get_width() / 2:
                self.x = self.left_bound + self.scaled_image.get_width() / 2
            if self.x > self.right_bound - self.scaled_image.get_width() / 2:
                self.x = self.right_bound - self.scaled_image.get_width() / 2
            if self.y < self.top_bound:
                self.y = self.top_bound
            if self.y > self.bottom_bound - self.scaled_image.get_height() / 2:
                self.y = self.bottom_bound - self.scaled_image.get_height() / 2

    def change_stats(self, item):

        self.hp += item.hp_change
        self.max_hp += item.max_hp_change
        self.damage += item.damage_change
        self.fire_rate += item.fire_rate_change
        self.speed += item.speed_change
        self.projectile_speed += item.projectile_speed
        if item.item_num == 7 or item.item_num == 8:
            self.proj_type = item.proj_type

        # Makes sure stats don't go above or below set values to keep the game playable
        if self.speed < 2:
            self.speed = 2
        if self.damage < 10:
            self.damage = 10
        if self.fire_rate < 2:
            self.fire_rate = 2
        if self.projectile_speed < 5:
            self.projectile_speed = 5
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.max_hp < 2:
            self.max_hp = 2

    def draw_stats(self, row, col):
        info = pygame.display.Info()
        self.scale = info.current_w / 1280
        font_size = int(28*self.scale)
        font = pygame.font.Font(None, font_size)
        frame = pygame.image.load("../assets/Frame.png").convert_alpha()
        scaled_frame =  pygame.transform.scale(frame, (
        frame.get_width() * self.scale, frame.get_height() * self.scale))
        empty_heart = pygame.image.load("../assets/heart empty.png").convert_alpha()
        first_half_heart = pygame.image.load("../assets/heart left.png").convert_alpha()
        second_half_heart = pygame.image.load("../assets/heart right.png").convert_alpha()

        display_hp = font.render("HP:" + str(round(self.hp, 1)), True, (0, 0, 0))
        display_dmg = font.render("DMG:" + str(round(self.damage, 1)), True, (0, 0, 0))
        display_speed = font.render("Speed:" + str(round(self.speed, 1)), True, (0, 0, 0))
        display_fire_rate = font.render("Fire Rate:" + str(round(self.fire_rate, 1)), True, (0, 0, 0))
        display_position = font.render(("Pos:" + str(row - 49) + "," + str(col - 49)), True, (0, 0, 0))

        self.screen.blit(scaled_frame, (self.screen.get_width()//1.8, 5*self.scale))
        self.screen.blit(display_hp, (self.screen.get_width()/1.7, 15*self.scale))
        self.screen.blit(display_dmg, (self.screen.get_width()/1.6, 15*self.scale))
        self.screen.blit(display_speed, (self.screen.get_width()/1.45, 15*self.scale))
        self.screen.blit(display_fire_rate, (self.screen.get_width()/1.31, 15*self.scale))
        self.screen.blit(display_position, (self.screen.get_width()/1.17, 15*self.scale))

        current_max_hp = round(self.max_hp / 2 + .1, 0)
        for k in range(int(current_max_hp)):
            self.screen.blit(empty_heart, (100 + (34 * k), 15))

        for k in range(self.hp):
            if k % 2 == 0:
                self.screen.blit(first_half_heart, (100 + (17 * k), 15))
            else:
                self.screen.blit(second_half_heart, (117 + ((k - 1) * 17), 15))

    def load_images(self):
        self.garrett = pygame.image.load("../assets/Garrett.png").convert_alpha()
        self.garrett_to_right = pygame.image.load("../assets/Garrett_to_right.png").convert_alpha()
        self.garrett_to_left = pygame.image.load("../assets/Garrett_to_left.png").convert_alpha()
        self.garrett_to_back = pygame.image.load("../assets/Garrett_to_back.png").convert_alpha()

        self.kevin = pygame.image.load("../assets/Kevin.png").convert_alpha()
        self.kevin_to_right = pygame.image.load("../assets/Kevin right.png").convert_alpha()
        self.kevin_to_left = pygame.image.load("../assets/kevin left.png").convert_alpha()
        self.kevin_to_back = pygame.image.load("../assets/Kevin back.png").convert_alpha()

        self.jared = pygame.image.load("../assets/Jared.png").convert_alpha()
        self.jared_to_right = pygame.image.load("../assets/Jared right.png").convert_alpha()
        self.jared_to_left = pygame.image.load("../assets/Jared left.png").convert_alpha()
        self.jared_to_back = pygame.image.load("../assets/Jared back.png").convert_alpha()

        self.yueyang = pygame.image.load("../assets/Yueyang.png").convert_alpha()
        self.yueyang_to_right = pygame.image.load("../assets/Yueyang right.png").convert_alpha()
        self.yueyang_to_left = pygame.image.load("../assets/Yueyang left.png").convert_alpha()
        self.yueyang_to_back = pygame.image.load("../assets/Yueyang back.png").convert_alpha()

        self.austin = pygame.image.load("../assets/Austin.png").convert_alpha()
        self.austin_to_right = pygame.image.load("../assets/Austin right.png").convert_alpha()
        self.austin_to_left = pygame.image.load("../assets/Austin left.png").convert_alpha()
        self.austin_to_back = pygame.image.load("../assets/Austin back.png").convert_alpha()


    def load_stats(self,character_num):

        if character_num == 0:
            # player stats starting values
            self.speed = 4
            self.fire_rate = 3
            self.projectile_speed = 10
            self.hp = 6
            self.damage = 25
            self.max_hp = 6
            self.character = self.garrett
            self.character_to_right = self.garrett_to_right
            self.character_to_left = self.garrett_to_left
            self.character_to_back = self.garrett_to_back
        if character_num == 1:
            # kevin:
            self.speed = 5
            self.fire_rate = 6
            self.projectile_speed = 14
            self.hp = 4
            self.damage = 15
            self.max_hp = 4
            self.character = self.kevin
            self.character_to_right = self.kevin_to_right
            self.character_to_left = self.kevin_to_left
            self.character_to_back = self.kevin_to_back
        if character_num == 2:
            # Jared's Stats
            self.speed = 5
            self.fire_rate = 3
            self.projectile_speed = 14
            self.max_hp = 4
            self.hp = 4
            self.damage = 23
            self.character = self.jared
            self.character_to_right = self.jared_to_right
            self.character_to_left = self.jared_to_left
            self.character_to_back = self.jared_to_back
        if character_num == 3:
            # Yueyang Stats
            self.speed = 2.5
            self.fire_rate = 2.5
            self.projectile_speed = 15
            self.max_hp = 8
            self.hp = 8
            self.damage = 35
            self.character = self.yueyang
            self.character_to_right = self.yueyang_to_right
            self.character_to_left = self.yueyang_to_left
            self.character_to_back = self.yueyang_to_back
        if character_num == 4:
            # Austin Stats
            self.speed = 4
            self.fire_rate = 3
            self.projectile_speed = 15
            self.max_hp = 7
            self.hp = 7
            self.damage = 25
            self.proj_type = 1
            self.character = self.austin
            self.character_to_right = self.austin_to_right
            self.character_to_left = self.austin_to_left
            self.character_to_back = self.austin_to_back
