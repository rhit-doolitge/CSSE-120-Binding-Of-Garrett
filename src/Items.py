
import pygame



class Items:
    def __init__(self, screen, x, y, item, item_number):

        # Code isn't needed
        # self.calculator_item = pygame.image.load("../assets/Calculator.png")
        # self.computer_item = pygame.image.load("../assets/Computer.png")
        # self.anime_girl_item = pygame.image.load("../assets/anime_girl.png")
        # self.gun = pygame.image.load("../assets/gun.png")
        # self.beer = pygame.image.load("../assets/beer.png")
        # self.coffee = pygame.image.load("../assets/coffee.png")
        # self.shoe = pygame.image.load("../assets/shoe.png")

        # initial item variables
        self.item_pickup = False
        self.x = x
        self.y = y
        self.count = 1
        self.screen = screen
        self.image = item
        self.item_num = item_number

        # Initial stat changes before deciding which item it is
        self.hp_change = 0
        self.damage_change = 0
        self.speed_change = 0
        self.fire_rate_change = 0
        self.projectile_speed = 0
        self.max_hp_change = 0
        self.proj_type = 0

        # different stat changes for different items
        if item_number == 0:  # calculator
            self.damage_change = 5
            self.fire_rate_change = .2

        if item_number == 1:  # computer
            self.fire_rate_change = 1
            self.speed_change = -.3

        if item_number == 2:  # anime girl
            self.speed_change = .6
            self.max_hp_change = 1
            self.damage_change = -3
            self.projectile_speed = -1


        if item_number == 3:  # gun
            self.projectile_speed = 2
            self.speed_change = -.3
            self.fire_rate_change = .4
            self.damage_change = 3

        if item_number == 4:  # coffee
            self.speed_change = .6
            self.fire_rate_change = .5
            self.hp_change = -1



        if item_number == 5:  # beer
            self.damage_change = 10
            self.speed_change = -.6
            self.fire_rate_change = -.4
            self.max_hp_change = -1

        if item_number == 6:  # shoe
            self.speed_change = 1
            self.projectile_speed = .7

        if item_number == 7:  # eye_laser
            self.proj_type = 1
            self.projectile_speed = .5

        if item_number == 8: # eye_ball
            self.proj_type = 0
            self.projectile_speed = -.5

        if item_number == 9:  # heart
            self.hp_change = 1

        # sound for picking up item
        self.sound = pygame.mixer.Sound("../assets/powerup_sound.mp3")
        self.sound.set_volume(.3)

        # creates a hit box for each item
        self.hit_box = pygame.Rect(self.x,
                                   self.y,
                                   self.image.get_width(),
                                   self.image.get_height())

    # Draws the items
    def draw(self):

        info = pygame.display.Info()
        self.scale = info.current_w / 1280
        self.scaled_image = pygame.transform.scale(self.image, (
            self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.screen.blit(self.scaled_image, (self.x, self.y))
        self.hit_box = pygame.Rect(self.x,
                                   self.y,
                                   self.scaled_image.get_width(),
                                   self.scaled_image.get_height())
