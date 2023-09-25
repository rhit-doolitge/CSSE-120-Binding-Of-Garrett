import pygame
from Game import Game
from Controller import Controller
from View import View


# DONE: Put your names here (entire team)
# Garrett Doolittle, Yueyang Chen, Austin Frisk


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)  # TODO: Choose your own size
    pygame.display.set_caption("Binding Of Garrett")  # TODO: Choose your own title
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller
    frame_rate = 60  # TODO: Choose your own frame rate

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()


main()
