import TextRenderer
import datetime
import time
import pygame
import os
import UserInterface
import InetConnection

#init gfx
image_background = False
image_off = False


def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def get_date():
    return datetime.datetime.now().strftime("%d.%m.%Y")


class StateIdle:

    CONNECTION_CHECK_INTERVAL = 5

    def __init__(self):
        print('State Idle')
        #self.settings_button = UserInterface.Button()
        self.time_lastcheck = time.time()
        self.inet_connection = InetConnection.InetConnection()

    def check_internet_connection(self):
        time_elapsed = time.time() - self.time_lastcheck
        if time_elapsed > self.CONNECTION_CHECK_INTERVAL:
            print('Test for connection')
            self.time_lastcheck = time.time()
            self.inet_connection.check()

    def update(self, surface):
        global image_off
        surface.blit(image_off, (0, 0))
        TextRenderer.render(get_date(), 160, 140, TextRenderer.FONT_SMALL, surface, TextRenderer.CENTER_X)
        TextRenderer.render(get_time(), 160, 160, TextRenderer.FONT_BIG, surface, TextRenderer.CENTER_X)
        self.check_internet_connection()
        #self.settings_button.render(surface)


class StateRunning:
    def __init__(self):
        print('State Running')

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