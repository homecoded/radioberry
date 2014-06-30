import TextRenderer
import datetime
import pygame
import os

#init gfx
image_background = False
image_off = False


def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def get_date():
    return datetime.datetime.now().strftime("%d.%m.%Y")


class StateIdle:
    def __init__(self):
        print('State Idle')

    def update(self, surface):
        global image_off
        surface.blit(image_off, (0, 0))
        TextRenderer.render(get_date(), 160, 140, TextRenderer.FONT_SMALL, surface, TextRenderer.CENTER_X)
        TextRenderer.render(get_time(), 160, 160, TextRenderer.FONT_BIG, surface, TextRenderer.CENTER_X)


class StateRunning:
    def __init__(self):
        print('State Idle')

    def update(self, surface):
        global image_background
        surface.blit(image_background, (0, 0))
        TextRenderer.render(get_time() + ' ' + get_date(), 160, 220, TextRenderer.FONT_SMALL, surface, TextRenderer.CENTER_X)
        TextRenderer.render('Radio RSA Sachsen', 160, 20, TextRenderer.FONT_SMALL, surface, TextRenderer.CENTER_X)


def init():
    global image_background
    global image_off
    image_background = pygame.image.load(os.path.join("gfx", "display.png")).convert()
    image_off = pygame.image.load(os.path.join("gfx", "display_off.png")).convert()

# instantiate the state objects
Idle = StateIdle()
Running = StateRunning()