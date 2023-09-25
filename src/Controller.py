import pygame
import sys
from Game import Game


# DONE: Put your names here (entire team)
# Garrett Doolittle, Yueyang Chen, Austin Frisk


class Controller:
    def __init__(self, game: Game):
        self.game = game

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        # changes shooting direction based on which arrow key is pressed
        pressedkey = pygame.key.get_pressed()
        if pressedkey[pygame.K_UP]:
            self.game.Garrett.fire(1)
        elif pressedkey[pygame.K_DOWN]:
            self.game.Garrett.fire(3)
        elif pressedkey[pygame.K_LEFT]:
            self.game.Garrett.fire(2)
        elif pressedkey[pygame.K_RIGHT]:
            self.game.Garrett.fire(0)

        # Changes movement direction based off of WASD
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            self.game.Garrett.move(1)
            self.game.Garrett.bounds(self.game.Room)
            self.game.Garrett.hit_box_make()
            for rock in self.game.Room.rocks_in_play:
                rock.collision(self.game.Garrett)
        if pressed_keys[pygame.K_a]:
            self.game.Garrett.move(2)
            self.game.Garrett.bounds(self.game.Room)
            self.game.Garrett.hit_box_make()
            for rock in self.game.Room.rocks_in_play:
                rock.collision(self.game.Garrett)
        if pressed_keys[pygame.K_s]:
            self.game.Garrett.move(3)
            self.game.Garrett.bounds(self.game.Room)
            self.game.Garrett.hit_box_make()
            for rock in self.game.Room.rocks_in_play:
                rock.collision(self.game.Garrett)
        if pressed_keys[pygame.K_d]:
            self.game.Garrett.move(0)
            self.game.Garrett.bounds(self.game.Room)
            self.game.Garrett.hit_box_make()
            for rock in self.game.Room.rocks_in_play:
                rock.collision(self.game.Garrett)

        # Use code like the following, but for YOUR Game object.
        #     if pressed_keys[pygame.K_LEFT]:
        #         self.game.fighter.move_left()
        #     if pressed_keys[pygame.K_RIGHT]:
        #         self.game.fighter.move_right()
        #
        #     if self.key_was_pressed_on_this_cycle(pygame.K_SPACE, events):
        #         self.game.fighter.fire()

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
