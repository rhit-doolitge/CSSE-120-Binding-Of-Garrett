import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("Testing the Game Over Screen")
    screen = pygame.display.set_mode((640, 650))
    run_game_over_loop(screen)

def run_game_over_loop(screen):
    clock = pygame.time.Clock()
    info = pygame.display.Info()
    scale = info.current_w / 1280
    win = pygame.image.load("../assets/Win_screen.png").convert_alpha()
    play_again = pygame.image.load("../assets/Resume.png").convert_alpha()
    title_screen = pygame.image.load("../assets/Title_screen.png").convert_alpha()
    while True:
        clock.tick(60)
        info = pygame.display.Info()
        scale = info.current_w / 1280

        scaled_win = pygame.transform.scale(win, (
            win.get_width() * scale, win.get_height() * scale))
        scaled_play_again = pygame.transform.scale(play_again, (
            play_again.get_width() * scale, play_again.get_height() * scale))
        scaled_title_screen = pygame.transform.scale(title_screen, (
            title_screen.get_width() * scale, title_screen.get_height() * scale))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                click_pos = event.pos

                if screen.get_width() / 2 - scaled_play_again.get_width() / 2 < click_pos[
                    0] < screen.get_width() / 2 + scaled_play_again.get_width() / 2 and \
                        ((screen.get_height() / 2) - (scaled_play_again.get_height() / 2)) < click_pos[1] < (
                        (screen.get_height() / 2) + (scaled_play_again.get_height() / 2)):
                    print("You clicked the screen.  You will now leave this screen.")
                    return True
                if screen.get_width()/2 - scaled_title_screen.get_width()/2 < click_pos[
                    0] < screen.get_width()/2 + scaled_title_screen.get_width()/2 and \
                        (screen.get_height()/2- scaled_title_screen.get_height()/2+scaled_play_again.get_height()+75) < click_pos[1] < (
                        (screen.get_height()/2+ scaled_title_screen.get_height()/2+scaled_play_again.get_height()+75+scaled_title_screen.get_height())):
                    print("You clicked title screen button.  You will now leave this screen.")
                    return False
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(scaled_win,(0,0))
        screen.blit(scaled_play_again, (screen.get_width()/2 - scaled_play_again.get_width()/2,screen.get_height()/2- scaled_play_again.get_height()/2))
        screen.blit(scaled_play_again, (screen.get_width()/2 - scaled_play_again.get_width()/2,screen.get_height()/2- scaled_play_again.get_height()/2))
        screen.blit(scaled_title_screen, (screen.get_width()/2 - scaled_title_screen.get_width()/2,screen.get_height()/2- scaled_title_screen.get_height()/2+scaled_play_again.get_height()+50))

        pygame.display.update()


if __name__ == "__main__":
    main()