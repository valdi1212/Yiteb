import pygame
import configparser
import collections
import os

Config = collections.namedtuple('Config', 'screen_width, screen_height')


def main():
    # TODO: Figure out how the hell PyGame works again because I can't bloody well remember anything
    # TODO: Create a main menu that allows you to start a new game or load a save file
    # TODO: Create a save file system that can load and save
    # TODO: After pressing new game the player should be taken to character creation
    # TODO: Find and implement sounds. I will need music, sound effects, UI selections sounds, etc.
    running = True

    while running:
        # locking framerate to 30FPS
        pygame.time.Clock().tick(30)

        # events
        e = pygame.event.poll()
        key = pygame.key.get_pressed()
        if e.type == pygame.QUIT:
            running = False
        if key[pygame.K_ESCAPE]:
            running = False

        # render
        # TODO: render something

    pygame.quit()


def main_menu():
    pass


def load_settings():
    parser = configparser.ConfigParser()

    if not os.path.isfile('settings.cfg'):
        parser['GRAPHICS'] = {'screen_width': '800',
                              'screen_height': '600'}
        with open('settings.cfg', 'w') as cfgfile:
            parser.write(cfgfile)

    parser.read('settings.cfg')
    c = Config(screen_width=parser.get('GRAPHICS', 'screen_width'),
               screen_height=parser.get('GRAPHICS', 'screen_height'))
    return c


if __name__ == '__main__':
    # setting up pygame
    pygame.init()

    # loading settings from file
    config = load_settings()

    # setting the constants and variables
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = int(config.screen_width), int(config.screen_height)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    pygame.display.set_caption('Yiteb: God of Madness')
    font = pygame.font.SysFont('monospace', 15)
    large_font = pygame.font.SysFont('monospace', 45)

    main()
