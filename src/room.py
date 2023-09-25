import random
import pygame
from Enemy import Enemy
from Items import Items
from Rock import Rock




class Room:
    def __init__(self, screen, room_image, room_num, leaving_door, room_count, boss_count):

        self.screen = screen

        # All the list of things in each room
        self.doors = []
        self.items = []
        self.items_in_play = []
        self.rocks_in_play = []
        self.enemies = []
        self.boss_dead = False


        # Special rooms
        self.boss_placeholder = pygame.image.load("../assets/boss room filler.png").convert_alpha()
        self.room_before_boss = pygame.image.load("../assets/Room before the boss.png").convert_alpha()
        self.boss_room = pygame.image.load("../assets/Boss Pre-kill.png").convert_alpha()
        self.boss_room_dead = pygame.image.load("../assets/Boss Killed.png").convert_alpha()

        # Creates a random number of enemies per room
        self.enemy_number = random.randint(1, 5)

        # remove
        # self.enemy_number = 1

        # Creates all the enemy objects that are supposed to be in the room
        for i in range(self.enemy_number):
            enemy = Enemy(self.screen, random.randint(int(self.screen.get_width()/3), int(self.screen.get_width()*2/3)),
                          random.randint(int(self.screen.get_height()/3), int(self.screen.get_height()*2/3)), room_count // 10 * 50 + 100)
            self.enemies.append(enemy)

        # sets the room to an image
        self.room = room_image

        # The different option of creating a new room based on the door you exit
        if leaving_door == "top":
            if room_num == 0:
                self.doors = ["top", "bottom", "left", "right"]
            elif room_num == 1:
                self.doors = ["top", "bottom"]
            elif room_num == 2:
                self.doors = ["bottom", "left"]
            elif room_num == 3:
                self.doors = ["bottom", "right"]
        if leaving_door == "bottom":
            if room_num == 0:
                self.doors = ["top", "bottom", "left", "right"]
            elif room_num == 1:
                self.doors = ["top", "bottom"]
            elif room_num == 2:
                self.doors = ["top", "left"]
            elif room_num == 3:
                self.doors = ["top", "right"]
        if leaving_door == "left":
            if room_num == 0:
                self.doors = ["top", "bottom", "left", "right"]
            elif room_num == 1:
                self.doors = ["left", "right"]
            elif room_num == 2:
                self.doors = ["top", "right"]
            elif room_num == 3:
                self.doors = ["bottom", "right"]
        if leaving_door == "right":
            if room_num == 0:
                self.doors = ["top", "bottom", "left", "right"]
            elif room_num == 1:
                self.doors = ["left", "right"]
            elif room_num == 2:
                self.doors = ["top", "left"]
            elif room_num == 3:
                self.doors = ["bottom", "left"]

        self.load_items()

        self.rocknum = random.randint(1,4)
        for k in range(self.rocknum):
            self.rock = Rock(self.screen, random.randint(int(self.screen.get_width()/5),
                                                           int(self.screen.get_width() * 4/5)),
                             random.randint(int(self.screen.get_height() * 1/3),
                                              int(self.screen.get_height() * 15/24)))
            self.rocks_in_play.append(self.rock)


        # chooses random item to put in a room
        self.itemnum = random.randint(0, 180) // 20

        # Random chance to spawn an item in a room
        if random.randint(1, 2) == 1:
            self.item = Items(self.screen, self.screen.get_width()/2,
                             self.screen.get_height()/2, self.items[self.itemnum],
                              self.itemnum)
            self.items_in_play.append(self.item)

        if boss_count >= 20 and leaving_door == "top" or boss_count >= 20 and leaving_door == "bottom" or boss_count >= 20 and leaving_door == "left":
            self.room = self.room_before_boss
            self.doors = ["top", "bottom", "left", "right"]

        if room_num == -1:
            self.room = self.boss_placeholder
            self.doors = ["top", "bottom", "left"]
            self.enemies = []
            self.items_in_play = []

        if room_num == -2:
            self.room = self.boss_room
            self.doors = []
            self.rocks_in_play = []
            self.enemies = []
            self.items_in_play = []
            boss = Enemy(self.screen, 200, self.screen.get_height() / 2 - 100,
                         2500 * room_count //20)
            self.enemies.append(boss)

        if room_count == 0:
            self.enemies = []
            self.items_in_play = []
            self.rocks_in_play = []
            room_count += 1


    # Draws the room background
    def draw(self):

        self.scaled_image = self.room
        info = pygame.display.Info()
        self.scale = info.current_w / 1280
        self.scaled_image = pygame.transform.scale(self.room, (self.room.get_width() * self.scale, self.room.get_height() * self.scale))
        self.screen.blit(self.scaled_image, (0, 0))

    # Removes the enemies from the room when they die
    def remove_dead_enemy(self):

        for k in range(len(self.enemies) - 1, -1, -1):
            if self.enemies[k].dead:
                spawn_heart = random.randint(1, 100)
                if spawn_heart <= 10:
                    self.item = Items(self.screen, self.enemies[k].x,
                                      self.enemies[k].y, self.items[9], 9)
                    self.items_in_play.append(self.item)
                del self.enemies[k]

    # Remove items when they are picked up
    def remove_items(self):
        for k in range(len(self.items_in_play) - 1, -1, -1):
            if self.items_in_play[k].item_pickup:
                del self.items_in_play[k]

    def load_items(self):
        # All different images for different items that can be created in a new room
        calculator_item = pygame.image.load("../assets/Calculator.png").convert_alpha()
        computer_item = pygame.image.load("../assets/Computer.png").convert_alpha()
        anime_girl_item = pygame.image.load("../assets/anime_girl.png").convert_alpha()
        gun = pygame.image.load("../assets/gun.png").convert_alpha()
        coffee = pygame.image.load("../assets/coffee.png").convert_alpha()
        beer = pygame.image.load("../assets/beer.png").convert_alpha()
        shoe = pygame.image.load("../assets/shoe.png").convert_alpha()
        eye_laser = pygame.image.load("../assets/eye_laser.png").convert_alpha()
        eye_ball = pygame.image.load("../assets/eye_ball.png").convert_alpha()
        heart = pygame.image.load("../assets/heart left.png").convert_alpha()

        # List of all the items
        self.items = [calculator_item, computer_item, anime_girl_item, gun, coffee, beer, shoe, eye_laser,eye_ball,heart]
