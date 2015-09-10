import pygame
import os


class Button:
    def __init__(self):
        self.is_initialized = False

    def _init(self):
        self.image_normal = pygame.image.load(os.path.join("gfx", "edit.png")).convert()
        self.image_active = pygame.image.load(os.path.join("gfx", "edit_active.png")).convert()
        self.position = (280, 0)
        self.size = (40, 40)

    def render(self, surface):
        if not self.is_initialized:
            self._init()
            self.is_initialized = True
        surface.blit(self.image_normal, self.position)