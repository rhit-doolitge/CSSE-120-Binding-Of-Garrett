import random
import pygame
from room import Room


class Rooms:

    def __init__(self, screen,garrett):

        self.door_enter = False
        self.screen = screen
        self.room_num = 0
        self.roomcount = 0
        self.boss_tally = 1
        self.boss = False
        self.garrett = garrett
        self.roommap = []
        for k in range(99):
            self.roomrow = []
            for j in range(99):
                self.roomrow.append(".")
            self.roommap.append(self.roomrow)

        self.row = len(self.roommap) // 2
        self.col = len(self.roommap[0]) // 2

        self.load_room_vars()
        # info = pygame.display.Info()
        startroom = pygame.image.load("../assets/starting room.png").convert_alpha()
        # startroom = pygame.transform.scale(startroom,(info.current_w,info.current_h))
        self.room = Room(self.screen, startroom, 0, "top", self.roomcount, self.garrett.boss_room_count)
        self.roommap[self.row][self.col] = self.room

    # Chooses a new room based on the direction the player left the room they were in
    def choose_room(self, direction_leaving):

        if direction_leaving == "top":
            self.room_variants = self.roomvars_bottomdoor
        if direction_leaving == "bottom":
            self.room_variants = self.roomvars_topdoor
        if direction_leaving == "left":
            self.room_variants = self.roomvars_rightdoor
        if direction_leaving == "right":
            self.room_variants = self.roomvars_leftdoor
        self.room_num = random.randint(0, len(self.room_variants) - 1)

        self.room = Room(self.screen, self.room_variants[self.room_num], self.room_num, direction_leaving, self.garrett.roomcount,self.garrett.boss_room_count)

    # Checks to see if the room the player is entering already exist. Returns true if it does
    def open(self, door_direction):
        if door_direction == "top":
            if self.roommap[self.row - 1][self.col] == ".":
                return True
        if door_direction == "bottom":
            if self.roommap[self.row + 1][self.col] == ".":
                return True
        if door_direction == "left":
            if self.roommap[self.row][self.col - 1] == ".":
                return True
        if door_direction == "right":
            if self.roommap[self.row][self.col + 1] == ".":
                return True
        return False

    # When the payer walks through a door it either creates a new room or re-enters an existing room
    def change_room(self, garrett):

        # Checks for player walking through a door and sets which door they walked through
        for k in range(len(self.room.doors)):
            if self.room.doors[k] == "top" and garrett.y < garrett.top_bound - 20:
                self.door_enter = True
                self.door_direction = "top"

            if self.room.doors[k] == "bottom" and garrett.y > garrett.bottom_bound + 20:
                self.door_enter = True
                self.door_direction = "bottom"

            if self.room.doors[k] == "left" and garrett.x < garrett.left_bound - 20:
                self.door_enter = True
                self.door_direction = "left"
                self.boss = True

            if self.room.doors[k] == "right" and garrett.x > garrett.right_bound + 20:
                self.door_enter = True
                self.door_direction = "right"

            # if self.top:
            #     if Garrett.y < Garrett.top_bound - 20:
            #         self.door_direction = "top"

        # Checks for entrance of a door
        if self.door_enter:

            # If the player goes through the boss door it creates the boss room
            if self.boss and self.room.room == self.room.room_before_boss:
                self.roommap[self.row][self.col - 1] = Room(self.screen, self.room_variants[self.room_num], -2,
                                                        "left", self.garrett.roomcount,self.garrett.boss_room_count)
                self.room = self.roommap[self.row][self.col - 1]


                garrett.x = garrett.right_bound
                self.col -= 1

            # If the room player is entering does not exist creates a new room object with new enemies and items
            elif self.open(self.door_direction):
                self.choose_room(self.door_direction)

                if self.door_direction == "top":
                    self.roommap[self.row - 1][self.col] = self.room
                    garrett.y = garrett.bottom_bound - garrett.scaled_image.get_height()/2
                    self.row -= 1
                elif self.door_direction == "bottom":
                    self.roommap[self.row + 1][self.col] = self.room
                    garrett.y = garrett.top_bound  + garrett.scaled_image.get_height()/2
                    self.row += 1
                elif self.door_direction == "left":
                    self.roommap[self.row][self.col - 1] = self.room
                    garrett.x = garrett.right_bound - garrett.scaled_image.get_width()/2
                    self.col -= 1
                elif self.door_direction == "right":
                    self.roommap[self.row][self.col + 1] = self.room
                    garrett.x = garrett.left_bound + garrett.scaled_image.get_width()/2
                    self.col += 1
                self.garrett.roomcount += 1
                self.garrett.boss_room_count += 1
                print(self.garrett.roomcount)
                print(self.garrett.boss_room_count)

            # If the room the player is entering does exist already go back to that room
            else:
                if self.door_direction == "top":
                    self.room = self.roommap[self.row - 1][self.col]
                    garrett.y = garrett.bottom_bound
                    self.row -= 1
                elif self.door_direction == "bottom":
                    self.room = self.roommap[self.row + 1][self.col]
                    garrett.y = garrett.top_bound
                    self.row += 1
                elif self.door_direction == "left":
                    self.room = self.roommap[self.row][self.col - 1]
                    garrett.x = garrett.right_bound
                    self.col -= 1
                elif self.door_direction == "right":
                    self.room = self.roommap[self.row][self.col + 1]
                    garrett.x = garrett.left_bound
                    self.col += 1

            # Resets all the room and door logic after entering new room
            self.top = False
            self.bot = False
            self.left = False
            self.right = False
            self.boss = False
            garrett.projectiles = []
            self.hit_count = -120
            self.door_enter = False

            # Creates a room object in place of the boss room so that the player can't take a
            # secret tunnel into the boss room unexpectedly
            if self.room.room == self.room.room_before_boss:
                self.garrett.boss_room_count = 0
                self.roommap[self.row][self.col - 1] = Room(self.screen, self.room_variants[self.room_num], -1,
                                                            "right", self.garrett.roomcount, self.garrett.boss_room_count)

            # Returns the room object
            return self.room

    def load_room_vars(self):
        # All the different room variations
        door4 = pygame.image.load("../assets/4 door Room.png").convert_alpha()
        door2topbot = pygame.image.load("../assets/2 Door Room(TopBot).png").convert_alpha()
        door2leftright = pygame.image.load("../assets/2 Door Room(RightLeft).png").convert_alpha()
        door2lefttop = pygame.image.load("../assets/2 Door Room(TopLeft).png").convert_alpha()
        door2leftbot = pygame.image.load("../assets/2 Door Room(BotLeft).png").convert_alpha()
        door2righttop = pygame.image.load("../assets/2 Door Room(Top, Right).png").convert_alpha()
        door2rightbot = pygame.image.load("../assets/2 Door Room(Bot,Right).png").convert_alpha()

        self.room_variants = [door4]
        self.roomvars_bottomdoor = [door4, door2topbot, door2leftbot, door2rightbot]
        self.roomvars_topdoor = [door4, door2topbot, door2lefttop, door2righttop]
        self.roomvars_leftdoor = [door4, door2leftright, door2lefttop, door2leftbot]
        self.roomvars_rightdoor = [door4, door2leftright, door2righttop, door2rightbot]
