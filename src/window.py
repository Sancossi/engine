import time

import pygame


from src.config import config


class Window:
    def __init__(self, game):
        self.game = game
        pygame.init()

        self.base_resolution = config['window']['base_resolution']
        self.scaled_resolution = config['window']['scaled_resolution']
        self.title = config['window']['title']
        self.backgound_color = config['window']['backgound_color']

        self.offset = config['window']['offset']
        self.scale_ratio = (
            self.scaled_resolution[0] // self.base_resolution[0],
            self.scaled_resolution[1] // self.base_resolution[1],
            )
        self.window = pygame.display.set_mode(self.scaled_resolution)

        self.scaled = False

        pygame.display.set_caption(self.title)
        pygame.mouse.set_visible(False)
        surface_width = self.base_resolution[0] - self.offset[0] * 2

        surface_height = self.base_resolution[1] - self.offset[1] * 2
        self.display = pygame.Surface((surface_width, surface_height))

        self.dt = 0.1
        self.frame_history = [0.01]
        self.frame_start = time.time()

        self.cursor_id = 'cursor'

        self.show_fps = True

        self.freeze_frame = {}

    def blit_cursor(self):
        image = self.game.assets.mics[self.cursor_id]
        image_center = (image.get_height() // 2, image.get_width() // 2)
        x = self.game.input.mouse_pos[0] - self.offset[0] - image_center[0]
        y = self.game.input.mouse_pos[1] - self.offset[1] - image_center[1]

        self.display.blit(image, (x, y))

    def blit_window(self):
        real_width = int(self.display.get_width() * self.scale_ratio[0])
        real_height = int(self.display.get_height() * self.scale_ratio[1])
        scale = pygame.transform.scale(self.display, (real_width, real_height))

        x = self.offset[0] * self.scale_ratio[0]
        y = self.offset[1] * self.scale_ratio[1]

        self.window.blit(scale, (x, y))

    def render_frame(self):
        self.blit_cursor()
        self.blit_window()
        pygame.display.update()

        self.display.fill(self.backgound_color)

        self.dt = time.time() - self.frame_start
        self.ui_dt = self.dt

        delete_list = []
        orig_dt = self.dt

        if self.freeze_frame != {}:
            slowest_freeze = min(list(self.freeze_frame))
            if self.frame_frame[slowest_freeze] > self.dt:
                self.dt *= slowest_freeze
            else:
                self.dt -= self.freeze_frame[slowest_freeze] * \
                    (1 - slowest_freeze)

        for freeze_amount in self.freeze_frame:
            if self.freeze_frame[freeze_amount] > orig_dt:
                self.freeze_frame[freeze_amount] -= orig_dt
            else:
                self.freeze_frame[freeze_amount] = 0
                delete_list.append(freeze_amount)

        for freeze in delete_list:
            del self.freeze_frame[freeze]

        self.dt = min(max(0.00001, self.dt), 0.1)
        self.frame_start = time.time()
        self.frame_history.append(self.ui_dt)
        self.frame_history = self.frame_history[-200:]

    def fps(self):
        avg_dt = sum(self.frame_history) / len(self.frame_history)
        fps = 1 / avg_dt
        return fps
