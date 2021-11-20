import pygame


def load_img(path, colorkey=None):
    img = pygame.image.load(path).convert_alpha()
    if colorkey:
        img.set_colorkey(colorkey)
    return img
