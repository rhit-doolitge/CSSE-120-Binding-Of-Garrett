import pygame
import sys
import math


def main():
    pygame.init()
    pygame.display.set_caption("testing the start up screen")
    screen = pygame.display.set_mode((640, 650))
    run_game_started_loop(screen)


def run_game_started_loop(screen):
    clock = pygame.time.Clock()

    info = pygame.display.Info()
    scale = info.current_w / 1280
    #loading images
    characterselect_background = pygame.image.load("../assets/Character Select.png").convert_alpha()
    start_background = pygame.image.load("../assets/Start screen.png").convert_alpha()

    play_game = pygame.image.load("../assets/start button.PNG").convert_alpha()

    speed_garrett = pygame.image.load("../assets/speed garrett.png").convert_alpha()
    speed_yueyang = pygame.image.load("../assets/speed garrett.png").convert_alpha()
    speed_austin = pygame.image.load("../assets/speed garrett.png").convert_alpha()
    speed_jared = pygame.image.load("../assets/speed garrett.png").convert_alpha()
    speed_kevin = pygame.image.load("../assets/speed kevin.png").convert_alpha()

    damage_garrett = pygame.image.load("../assets/dmg garrett.png").convert_alpha()
    damage_yueyang = pygame.image.load("../assets/dmg Yueyang.png").convert_alpha()
    damage_austin = pygame.image.load("../assets/dmg austin.png").convert_alpha()
    damage_jared = pygame.image.load("../assets/dmg jared.png").convert_alpha()
    damage_kevin = pygame.image.load("../assets/dmg kevin.png").convert_alpha()

    hp_garrett = pygame.image.load("../assets/hp garrett.png").convert_alpha()
    hp_yueyang = pygame.image.load("../assets/hp Yueyang.png").convert_alpha()
    hp_austin = pygame.image.load("../assets/hp austin.png").convert_alpha()
    hp_jared = pygame.image.load("../assets/Hp Jared.png").convert_alpha()
    hp_kevin = pygame.image.load("../assets/hp kevin.png").convert_alpha()

    controls_button = pygame.image.load("../assets/controls button.png").convert_alpha()

    controls_background = pygame.image.load("../assets/controls.png").convert_alpha()

    garrett = pygame.image.load("../assets/Garrett.png").convert_alpha()
    scaled_garrett = pygame.transform.scale(garrett, (garrett.get_width() * 2 *scale, garrett.get_height() * 2*scale))
    kevin = pygame.image.load("../assets/Kevin.png").convert_alpha()
    scaled_kevin = pygame.transform.scale(kevin, (kevin.get_width() * 2*scale, kevin.get_height()*2*scale))
    jared = pygame.image.load("../assets/Jared.png").convert_alpha()
    scaled_jared = pygame.transform.scale(jared, (jared.get_width() * 2*scale, jared.get_height() * 2*scale))
    yueyang = pygame.image.load("../assets/Yueyang.png").convert_alpha()
    scaled_yueyang = pygame.transform.scale(yueyang, (yueyang.get_width() * 2*scale, yueyang.get_height() * 2*scale))
    austin = pygame.image.load("../assets/Austin.png").convert_alpha()
    scaled_austin = pygame.transform.scale(austin, (austin.get_width() * 2*scale, austin.get_height() * 2*scale))

    scaled_hp_garrett = pygame.transform.scale(hp_garrett,
                                               (hp_garrett.get_width() * scale, hp_garrett.get_height() * scale))
    scaled_dmg_garrett = pygame.transform.scale(damage_garrett,
                                                (damage_garrett.get_width() * scale,
                                                 damage_garrett.get_height() * scale))
    scaled_speed_garrett = pygame.transform.scale(speed_garrett,
                                                  (speed_garrett.get_width() * scale,
                                                   speed_garrett.get_height() * scale))

    character_select = False
    selected = False
    character = scaled_garrett
    hp = scaled_hp_garrett
    damage = scaled_dmg_garrett
    speed = scaled_speed_garrett

    controls = False
    while True:
        clock.tick(30)

        info = pygame.display.Info()
        scale = info.current_w / 1280
        # scaling the screen
        scaled_characterselect_background = pygame.transform.scale(characterselect_background, (
        characterselect_background.get_width() * scale, characterselect_background.get_height() * scale))
        scaled_start_background = pygame.transform.scale(start_background, (
        start_background.get_width() * scale, start_background.get_height() * scale))
        scaled_play_game = pygame.transform.scale(play_game,
                                           (play_game.get_width() * scale, play_game.get_height() * scale))

        scaled_hp_garrett = pygame.transform.scale(hp_garrett,
                                                   (hp_garrett.get_width() * scale, hp_garrett.get_height() * scale))
        scaled_hp_yueyang = pygame.transform.scale(hp_yueyang,
                                                   (hp_yueyang.get_width() * scale, hp_yueyang.get_height() * scale))
        scaled_hp_jared = pygame.transform.scale(hp_jared,
                                                 (hp_jared.get_width() * scale, hp_jared.get_height() * scale))
        scaled_hp_austin = pygame.transform.scale(hp_austin,
                                                  (hp_austin.get_width() * scale, hp_austin.get_height() * scale))
        scaled_hp_kevin = pygame.transform.scale(hp_kevin,
                                                 (hp_kevin.get_width() * scale, hp_austin.get_height() * scale))

        scaled_dmg_garrett = pygame.transform.scale(damage_garrett,
                                                    (damage_garrett.get_width() * scale,
                                                     damage_garrett.get_height() * scale))
        scaled_dmg_yueyang = pygame.transform.scale(damage_yueyang,
                                                    (damage_yueyang.get_width() * scale,
                                                     damage_yueyang.get_height() * scale))
        scaled_dmg_jared = pygame.transform.scale(damage_jared,
                                                  (damage_jared.get_width() * scale, damage_jared.get_height() * scale))
        scaled_dmg_austin = pygame.transform.scale(damage_austin,
                                                   (damage_austin.get_width() * scale,
                                                    damage_austin.get_height() * scale))
        scaled_dmg_kevin = pygame.transform.scale(damage_kevin,
                                                  (damage_kevin.get_width() * scale, damage_kevin.get_height() * scale))

        scaled_speed_garrett = pygame.transform.scale(speed_garrett,
                                                      (speed_garrett.get_width() * scale,
                                                       speed_garrett.get_height() * scale))
        scaled_speed_yueyang = pygame.transform.scale(speed_yueyang,
                                                      (speed_yueyang.get_width() * scale,
                                                       speed_yueyang.get_height() * scale))
        scaled_speed_jared = pygame.transform.scale(speed_jared,
                                                    (speed_jared.get_width() * scale, speed_jared.get_height() * scale))
        scaled_speed_kevin = pygame.transform.scale(speed_kevin,
                                                    (speed_kevin.get_width() * scale, speed_kevin.get_height() * scale))
        scaled_speed_austin = pygame.transform.scale(speed_austin,
                                                     (speed_austin.get_width() * scale,
                                                      speed_austin.get_height() * scale))

        scaled_controls_button = pygame.transform.scale(controls_button,
                                                 (controls_button.get_width() * scale, controls_button.get_height() * scale))
        scaled_controls_background = pygame.transform.scale(controls_background, (
        controls_background.get_width() * scale, controls_background.get_height() * scale))
        scaled_garrett = pygame.transform.scale(garrett,
                                                (garrett.get_width() * 2 * scale, garrett.get_height() * 2 * scale))
        scaled_kevin = pygame.transform.scale(kevin, (kevin.get_width() * 2 * scale, kevin.get_height() * 2 * scale))
        scaled_jared = pygame.transform.scale(jared, (jared.get_width() * 2 * scale, jared.get_height() * 2 * scale))
        scaled_yueyang = pygame.transform.scale(yueyang,
                                                (yueyang.get_width() * 2 * scale, yueyang.get_height() * 2 * scale))
        scaled_austin = pygame.transform.scale(austin,
                                               (austin.get_width() * 2 * scale, austin.get_height() * 2 * scale))
        #starting screen and controls
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                click_pos = event.pos
                #start button
                if screen.get_width() / 2 - play_game.get_width() / 2 < click_pos[0] \
                        < screen.get_width() / 2 + play_game.get_width() / 2 and \
                        (screen.get_height() - play_game.get_height() - 100) < click_pos[1] < \
                        (screen.get_height() + play_game.get_height() - 185):
                    print("You clicked the screen.  You will now leave this screen.")
                    character_select = True


                #controls button
                if screen.get_width()/10-controls_button.get_width()/2< click_pos[0] \
                        < screen.get_width()/10+play_game.get_width()/2 and \
                        (screen.get_height() - controls_button.get_height()) < click_pos[1] < \
                        (screen.get_height() + controls_button.get_height()):
                        print("You clicked the screen.  You will now leave this screen.")
                        controls = True
            if event.type == pygame.QUIT:
                sys.exit()

        rect1 = pygame.Rect(screen.get_width()/3.3, screen.get_height()/1.78, 100*scale, 100*scale)
        pygame.draw.rect(screen,(0,0,0),rect1)
        rect2 = pygame.Rect(screen.get_width()/1.6, screen.get_height()/1.78, 100*scale, 100*scale)
        pygame.draw.rect(screen, (0, 0, 0), rect2)
        # lists
        character_list = [scaled_garrett, scaled_kevin,scaled_jared,scaled_yueyang,scaled_austin]
        hp_list = [scaled_hp_garrett,scaled_hp_kevin,scaled_hp_jared,scaled_hp_yueyang,scaled_hp_austin]
        damage_list = [scaled_dmg_garrett,scaled_dmg_kevin,scaled_dmg_jared,scaled_dmg_yueyang,scaled_dmg_austin]
        speed_list = [scaled_speed_garrett,scaled_speed_kevin,scaled_speed_jared,scaled_speed_yueyang,scaled_speed_austin]

        character_number = 0
        #character selection screen
        while character_select:
            clock.tick(30)
            info = pygame.display.Info()
            scale = info.current_w / 1280
            scaled_garrett = pygame.transform.scale(garrett,
                                                    (garrett.get_width() * 2 * scale, garrett.get_height() * 2 * scale))
            scaled_characterselect_background = pygame.transform.scale(characterselect_background, (
                characterselect_background.get_width() * scale, characterselect_background.get_height() * scale))
            rect1 = pygame.Rect(screen.get_width() / 3.3, screen.get_height() / 1.78, 100 * scale, 100 * scale)
            pygame.draw.rect(screen, (0, 0, 0), rect1)
            rect2 = pygame.Rect(screen.get_width() / 1.6, screen.get_height() / 1.78, 100 * scale, 100 * scale)
            pygame.draw.rect(screen, (0, 0, 0), rect2)

            #character select buttons
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    click_pos = event.pos
                    if math.sqrt((rect1.centerx - click_pos[0]) ** 2 + (rect1.centery - click_pos[1]) ** 2) < 50:
                        character_number -=1
                        if character_number < 0:
                            character_number = len(character_list) - 1
                        character = character_list[character_number]
                        hp = hp_list[character_number]
                        damage = damage_list[character_number]
                        speed = speed_list[character_number]
                    if math.sqrt((rect2.centerx - click_pos[0]) ** 2 + (rect2.centery - click_pos[1]) ** 2) < 50:
                        character_number += 1
                        if character_number + 1 > len(character_list):
                            character_number = 0
                        character = character_list[character_number]
                        hp = hp_list[character_number]
                        damage = damage_list[character_number]
                        speed = speed_list[character_number]
                    if screen.get_width() / 2 - scaled_play_game.get_width() / 2 < click_pos[0] \
                            < screen.get_width() / 2 + scaled_play_game.get_width() / 2 and \
                            (screen.get_height() - scaled_play_game.get_height() - 100) < click_pos[1] < \
                            (screen.get_height() + scaled_play_game.get_height() - 185):
                        print("You clicked the character screen.  You will now leave this screen.")
                        selected = True
                        return character_number

                if event.type == pygame.QUIT:
                    sys.exit()
            #drawing characters and stats
            screen.blit(scaled_characterselect_background, (-25, 0))
            screen.blit(scaled_play_game, (screen.get_width() / 2 - play_game.get_width() / 2,
                                    screen.get_height() - play_game.get_height() - 100))

            screen.blit(character, (screen.get_width() / 2 - scaled_garrett.get_width() / 2,
                                  screen.get_height() / 2 - scaled_garrett.get_height() / 2))

            screen.blit(hp, (screen.get_width() / 2 - scaled_hp_garrett.get_width() / 2-350,
                                            screen.get_height() / 2 - scaled_hp_garrett.get_height() / 2-200))

            screen.blit(speed, (screen.get_width() / 2 - scaled_hp_garrett.get_width() / 2-375,
                                            screen.get_height() / 2 - scaled_hp_garrett.get_height() / 2))
            screen.blit(damage, (screen.get_width() / 2 - scaled_hp_garrett.get_width() / 2-375,
                                            screen.get_height() / 2 - scaled_hp_garrett.get_height() / 2-125))




            # pygame.draw.rect(screen, (0, 0, 0), rect1)
            # pygame.draw.rect(screen, (0, 0, 0), rect2)
            pygame.display.update()
        #Starts the game when you press the button
        while controls:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    click_pos = event.pos
                    if 0< click_pos[0] \
                        < screen.get_width() and \
                            (0) < click_pos[1] < \
                            (screen.get_height()):
                        print("You clicked the character screen.  You will now leave this screen.")
                        controls = False
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.blit(scaled_controls_background,(-40,20*scale))

            pygame.display.update()
        screen.fill((255, 255, 255))

        screen.blit(scaled_start_background, (0 + 50, 0))
        screen.blit(scaled_play_game, (screen.get_width() / 2 - scaled_play_game.get_width() / 2,
                                screen.get_height() - scaled_play_game.get_height() - 100))
        screen.blit(scaled_controls_button,(screen.get_width()/9-scaled_controls_button.get_width()/2,
                                     screen.get_height()-scaled_controls_button.get_height()))
        pygame.display.update()

if __name__ == '__main__':
    main()
