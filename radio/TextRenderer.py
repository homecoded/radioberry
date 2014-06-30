import pygame

fonts = []
is_initialized = False

FONT_TINY = 0
FONT_SMALL = 1
FONT_BIG = 2

CENTER_X = 'center_x'

def render(text, x, y, font_id, surface, render_mode=0):
    global is_initialized
    global fonts

    if not is_initialized:
        fonts = [
            pygame.font.Font('gfx/MunroSmall.ttf', 10),
            pygame.font.Font('gfx/MunroSmall.ttf', 20),
            pygame.font.Font('gfx/MunroSmall.ttf', 40)
        ]
        is_initialized = True

    temp_surface = fonts[font_id].render(text, 0, (255, 0, 0))
    if render_mode == CENTER_X:
        text_rect = temp_surface.get_rect()
        text_rect.x = x - tuple(text_rect)[2]/2
        text_rect.y = y
        surface.blit(temp_surface, text_rect)
    else:
        surface.blit(temp_surface, (x, y))