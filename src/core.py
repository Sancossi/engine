import pygame


def swap_color(surface, old_color, new_color):
    surface.set_colorkey(old_color)
    new_surf = surface.copy()

    new_surf.fill(new_color)
    new_surf.blit(surface, (0, 0))
    new_surf.set_colorkey((0, 0, 0))

    return new_surf


def clip(surface, x, y, x_size, y_size, copy_surface=True):
    if copy_surface:
        handle_surface = surface.copy()
    else:
        handle_surface = surface
    clip_r = pygame.Rect(int(x), int(y), x_size, y_size)
    handle_surface.set_clip(clip_r)
    return surface.subsurface(handle_surface.get_clip()).copy()
