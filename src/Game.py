import pygame
from Garrett import Garrett
from Roomselect import Rooms
import Game_Over
import Start_Up
import Win_screen
import random


# Put each class in its own module, using the same name for both.
# Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
#     from Missiles import Missiles
#     from Enemies import Enemies

# DONE: Put your names here (entire team)
# Garrett Doolittle, Yueyang Chen, Austin Frisk


class Game:
    def __init__(self, screen: pygame.Surface):

        # holds screen and creates the scale for the screen
        self.screen = screen
        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        # Initializing all the game parts
        self.Garrett = Garrett(self.screen, 850, 500, 1)
        self.Room_select = Rooms(self.screen, self.Garrett)
        self.Room = self.Room_select.room

        # Initializing the variables used in game class
        self.start_up = True
        self.floor_count = 1
        self.hitcount = 0

        # Makes music play
        # pygame.mixer.music.load("../assets/background sound.mp3")
        # pygame.mixer.music.play(-1)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """

        # Draws the room
        self.Room.draw()

        # Draws stats
        self.Garrett.draw_stats(self.Room_select.row, self.Room_select.col)

        # Draws the character and the projectiles in order depending on direction character is looking
        if self.Garrett.direction == 3:
            self.Garrett.draw()
            for proj in self.Garrett.projectiles:
                proj.draw()
            for laser in self.Garrett.lasers:
                laser.draw()
        else:
            for proj in self.Garrett.projectiles:
                proj.draw()
            for laser in self.Garrett.lasers:
                laser.draw()
            self.Garrett.draw()

        # Draws the enemies in a room and there projectiles
        for enemy in self.Room.enemies:
            enemy.draw()
            for laser in enemy.laser:
                laser.draw()
            for laser_indicator in enemy.laser_indicator:
                laser_indicator.draw_indicator()
            for proj in enemy.projectiles:
                proj.draw()

        # Draws the items in a room
        for item in self.Room.items_in_play:
            item.draw()

        for rock in self.Room.rocks_in_play:
            rock.draw()

        # if self.Room.room == self.Room.boss_room:
        #     for laser in self.Room.boss.laser:
        #         laser.draw()
        #         laser.draw_indicator()
        #     self.Room.boss.draw_boss()
        #     for proj in self.Room.boss.projectiles:
        #         proj.draw()
        # --------------------------------------------------------------------------------------------------------------
        # All the visual testing stuff
        # --------------------------------------------------------------------------------------------------------------

        # # Used to display boundaries of the room to make sure they were in the proper spots
        # pygame.draw.line(self.screen, (150, 0, 0), (self.Garrett.left_bound, 0), (self.Garrett.left_bound, 1500))
        # pygame.draw.line(self.screen, (150, 0, 0), (0, self.Garrett.top_bound), (1500, self.Garrett.top_bound))
        # pygame.draw.line(self.screen, (150, 0, 0), (self.Garrett.right_bound, 0), (self.Garrett.right_bound, 1500))
        # pygame.draw.line(self.screen, (150, 0, 0), (0, self.Garrett.bottom_bound), (1500, self.Garrett.bottom_bound))
        #
        # # Draws player hit box
        # pygame.draw.rect(self.screen,(255,0,0),self.Garrett.hit_box,2)
        #
        # # Draws rock hit boxes
        # for rock in self.Room.rocks_in_play:
        #     pygame.draw.rect(self.screen, (255, 0, 0), rock.hitbox, 2)
        #
        # # Draws projectile hit boxes
        # for proj in self.Garrett.projectiles:
        #     pygame.draw.rect(self.screen, (255, 0, 0), proj.hit_box, 2)
        #
        # # Draws laser hit boxes
        # for laser in self.Garrett.lasers:
        #     pygame.draw.rect(self.screen, (255, 255, 255), laser.hit_box, 2)
        #
        # # Draws enemy hit boxes, their projectile and laser hit boxes
        # for enemy in self.Room.enemies:
        #     pygame.draw.rect(self.screen, (255, 0, 0), enemy.hit_box, 2)
        #     for proj in enemy.projectiles:
        #         pygame.draw.rect(self.screen, (255, 0, 0), proj.hit_box, 2)
        #     for laser in enemy.laser:
        #         pygame.draw.rect(self.screen, (255, 255, 255), laser.hit_box, 2)
        #
        # # Draws item hit boxes
        # for item in self.Room.items_in_play:
        #     pygame.draw.rect(self.screen, (255, 0, 0), item.hit_box, 2)


    def run_one_cycle(self):

        godmode = False

        # uncomment the line below to make it, so you can't die if you want something like that
        godmode = True
        if godmode:
            self.Garrett.damage = 1500
            self.Garrett.speed = 10
            self.Garrett.fire_rate = 15
            self.Garrett.projectile_speed = 20
            self.Garrett.hp = 24
            self.Garrett.max_hp = 24

        # Gets info about the screen and adds in a scaling feature with display size
        info = pygame.display.Info()
        self.scale = info.current_w / 1280

        # Starts game at start screen and allows the game to go back if certain buttons are pressed
        if self.start_up:
            self.character = Start_Up.run_game_started_loop(self.screen)
            self.Garrett = Garrett(self.screen, self.screen.get_width() / 2,
                                   self.screen.get_height() / 2, self.character)
            self.Room_select = Rooms(self.screen, self.Garrett)
            self.Room = self.Room_select.room
            self.floor_count = 1
            self.start_up = False

            # Used to test if the character being passed through was the right one
            print(self.character)

        # When escape key is pressed it end the run and goes back to the start screen
        pressed_key = pygame.key.get_pressed()
        print(self.floor_count)
        if pressed_key[pygame.K_ESCAPE]:
            self.start_up = True
        # ends the game after the specified amount of floors minus one and says you won
        if self.floor_count == 4:
            win = Win_screen.run_game_over_loop(self.screen)
            if win:
                self.floor_count+=1
            else:
                print("restart")
                self.start_up = True

        # --------------------------------------------------------------------------------------------------------------
        # All of Garrett's stuff
        # --------------------------------------------------------------------------------------------------------------

        # Creates the characters hit box
        self.Garrett.hit_box_make()

        # increase the fire count
        self.Garrett.count += 1

        # Makes I Frames if you hit an enemy, so you don't die instantly on touching an enemy
        if self.hitcount <= 30:
            self.hitcount += 1

        # moves all the character's projectiles
        for proj in self.Garrett.projectiles:
            proj.move()
            for rock in self.Room.rocks_in_play:
                if proj.hit_box.colliderect(rock.hit_box):
                    proj.tear_gone = True



        # removes tears based on any of the removal conditions
        self.Garrett.remove_projectiles()

        # if the players health goes to zero they die
        if self.Garrett.hp <= 0:
            pygame.mixer.music.stop()
            Game_Over.run_game_over_loop(self.screen)
            self.start_up = True

        # --------------------------------------------------------------------------------------------------------------
        # All of Enemy's stuff
        # --------------------------------------------------------------------------------------------------------------

        # calls the lists of enemies in the given room
        for enemy in self.Room.enemies:

            # Makes enemies dead when they lose all their health
            if enemy.hp <= 0:
                enemy.dead = True

            # moves the enemies
            enemy.move()

            # removes enemies projectiles based on given conditions
            for rock in self.Room.rocks_in_play:
                if enemy.direction == 2:
                    if enemy.hit_box.colliderect(rock.hit_box):
                        enemy.x = rock.x + rock.scaled_image.get_width()
                if enemy.direction == 0:
                    if enemy.hit_box.colliderect(rock.hit_box):
                        enemy.x = rock.x - enemy.scaled_image.get_width()
                if enemy.direction == 1:
                    if enemy.hit_box.colliderect(rock.hit_box):
                        enemy.y = rock.y + rock.scaled_image.get_height()
                if enemy.direction == 3:
                    if enemy.hit_box.colliderect(rock.hit_box):
                        enemy.y = rock.y - enemy.scaled_image.get_height()
            enemy.remove_projectiles()

            # makes specifically the boss shoot projectiles and lasers
            if enemy.enemy_type == 6:
                enemy.fire()

            # Shoots and ends lasers and indicators
            for laser in enemy.laser:
                if laser.count >= 5:
                    laser.lasergone = True
                if laser.hit_box.colliderect(self.Garrett.hit_box):
                    if self.hitcount >= 30:
                        self.Garrett.hp -= 1
                        self.hitcount = 0
            for laser_indicator in enemy.laser_indicator:
                if laser_indicator.count == 0:
                    laser_indicator.lasergone = True

            # Shoots and ends projectiles
            for proj in enemy.projectiles:
                proj.move()
                if proj.hit_box.colliderect(self.Garrett.hit_box):
                    proj.tear_gone = True
                    if self.hitcount >= 30:
                        self.Garrett.hp -= 1
                        self.hitcount = 0

            # if the characters projectiles hit an enemy it loses health and plays hurt sound
            for proj in self.Garrett.projectiles:
                if enemy.hit_box.colliderect(proj.hit_box):
                    proj.tear_gone = True
                    enemy.hp -= self.Garrett.damage
                    enemy.sound.play()

            # if the characters lasers hit an enemy it loses health
            for laser in self.Garrett.lasers:
                if enemy.hit_box.colliderect(laser.hit_box):
                    enemy.hp -= self.Garrett.damage / 12

            # if the character touches an enemy, the character takes damage
            if self.Garrett.hit_box.colliderect(enemy.hit_box) and self.hitcount >= 30:
                self.Garrett.hp -= 1
                self.hitcount = 0

        # --------------------------------------------------------------------------------------------------------------
        # All of Room's stuff
        # --------------------------------------------------------------------------------------------------------------

        # Removes all dead enemies and grabbed items
        self.Room.remove_dead_enemy()
        self.Room.remove_items()

        # Allows the doors to open when the enemies are all dead
        if len(self.Room.enemies) == 0:
            self.Garrett.alldead = True
            if self.Room.room == self.Room.boss_room:
                self.Room.room = self.Room.boss_room_dead

        else:
            self.Garrett.alldead = False

        # Picks a new room or brings you back to an old one if you go through a door
        if self.Garrett.y < self.Garrett.top_bound - 20 or self.Garrett.y > self.Garrett.bottom_bound + 20 or \
                self.Garrett.x < self.Garrett.left_bound - 20 or self.Garrett.x > self.Garrett.right_bound + 20:
            self.Room = self.Room_select.change_room(self.Garrett)

        # If the boss is defeated, and you go to the hatch you go to next floor
        if self.Room.room == self.Room.boss_room_dead and \
                self.Garrett.hit_box.collidepoint(self.screen.get_width() / 2,
                                                  self.screen.get_height() / 2):
            self.Room_select = Rooms(self.screen, self.Garrett)
            self.Room = self.Room_select.room
            self.Garrett.boss_room_count = 0
            self.floor_count += 1

        # --------------------------------------------------------------------------------------------------------------
        # All of Item's stuff
        # --------------------------------------------------------------------------------------------------------------

        # When a player grabs an item it disappears and give player those stats
        for item in self.Room.items_in_play:
            if self.Garrett.hit_box.colliderect(item.hit_box):
                item.item_pickup = True
                item.sound.play()
                self.Garrett.change_stats(item)

        # --------------------------------------------------------------------------------------------------------------
        # All of rock stuff
        # --------------------------------------------------------------------------------------------------------------
        for k in range(len(self.Room.rocks_in_play)):
            for j in range(len(self.Room.rocks_in_play)):
                if self.Room.rocks_in_play[j].hit_box.colliderect(self.Room.rocks_in_play[k].hit_box) and j != k:
                    self.Room.rocks_in_play[j].x = random.randint(int(self.screen.get_width() / 5),
                                   int(self.screen.get_width() * 4 / 5))
                    self.Room.rocks_in_play[j].y = random.randint(int(self.screen.get_height() * 1 / 3),
                                   int(self.screen.get_height() * 15 / 24))



        # --------------------------------------------------------------------------------------------------------------
        # All the testing things stuff
        # --------------------------------------------------------------------------------------------------------------

        # Used to check if the scale was properly working on resizing the screen
        # print(self.scale)

