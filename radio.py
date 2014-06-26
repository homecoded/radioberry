#!/usr/bin/python

import sys
sys.path.append('radio')
sys.path.append('gfx')

import pygame
import os
import sys
import TouchControl

# Set the frame buffer device to be the TFT
os.environ["SDL_FBDEV"] = "/dev/fb1"

width = 320
height = 240
radius = 10
stroke = 1

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(0)
running = True
isActive = False


def on_click():
    global isActive
    if isActive:
        isActive = False
        print("off")
        os.system("mpc stop")
        os.system("mpc clear")
        if isActive:
            screen.blit(image_background, (0, 0))
        else:
            screen.blit(image_off, (0, 0))
    else:
        isActive = True
        print("play")
        os.system("mpc volume 100")
        os.system("mpc add http://streams.rsa-sachsen.de/rsa-live/mp3-128/mediaplayerrsa")
        os.system("mpc play")
        if isActive:
            screen.blit(image_background, (0, 0))
        else:
            screen.blit(image_off, (0, 0))
    pygame.display.update()

#init touch
touch_control = TouchControl.TouchControl()
touch_control.on(TouchControl.TOUCH_CLICK, on_click)

#init gfx
image_background = pygame.image.load(os.path.join("gfx", "display.png")).convert()
image_off = pygame.image.load(os.path.join("gfx", "display_off.png")).convert()

#main loop
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    touch_control.update(events)

os.system("mpc stop")
os.system("mpc clear")
pygame.quit()
sys.exit(0)
