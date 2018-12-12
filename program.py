import pygame
import configparser
import collections
import os

Config = collections.namedtuple('Config', 'screen_width, screen_height')


def main():
    # TODO: After pressing new game the player should be taken to character creation
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

    menu = True

    # play menu music
    pygame.mixer.music.load("src/sounds/music/BRPG_Assault_FULL_Loop.wav")
    pygame.mixer.music.play(-1)

    while menu:
        # locks FPS to 30
        pygame.time.Clock().tick(30)

        # events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        # key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            menu = False

        # rendering
        screen.fill(WHITE)
        text_surf, text_rect = text_objects("YITEB", large_font)
        text_rect.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/4))
        screen.blit(text_surf, text_rect)
        pygame.display.update()


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


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


if __name__ == '__main__':
    # setting up pygame
    pygame.init()

    # setting up sound mixer
    pygame.mixer.init(48000, 16, 2)

    # loading sounds

    # loading settings from file
    config = load_settings()

    # setting the constants and variables
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = int(config.screen_width), int(config.screen_height)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    pygame.display.set_caption('Yiteb: God of Madness')
    font = pygame.font.SysFont('monospace', 15)
    large_font = pygame.font.SysFont('monospace', 45)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    main_menu()
    main()
