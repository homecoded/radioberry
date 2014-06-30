#!/usr/bin/python

import sys
sys.path.append('radio')
sys.path.append('gfx')

import pygame
import os
import sys
import TouchControl
import InternetRadioPlayer
import States

# Set the frame buffer device to be the TFT
os.environ["SDL_FBDEV"] = "/dev/fb1"

width = 320
height = 240

running = True
isActive = False

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(0)

# init radio player
internet_radio_player = InternetRadioPlayer.InternetRadioPlayer()

def on_click():
    global isActive
    if isActive:
        isActive = False
        internet_radio_player.stop()
    else:
        isActive = True
        internet_radio_player.play()

#init touch
touch_control = TouchControl.TouchControl()
touch_control.on(TouchControl.TOUCH_CLICK, on_click)

clock = pygame.time.Clock()
States.init()

#main loop
while running:
    clock.tick(10)
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    touch_control.update(events)
    if isActive:
        States.Running.update(screen)
    else:
        States.Idle.update(screen)
    pygame.display.flip()

os.system("mpc stop")
os.system("mpc clear")
pygame.quit()
sys.exit(0)
