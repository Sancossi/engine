import sys

import pygame

from src.config import config
from pygame.constants import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONUP, MOUSEBUTTONDOWN


def is_keyboard(binding):
    return config['input'][binding]['binding'][0] == 'keyboard'


def filter_input_mode(binding, mode):
    return set(config['input'][binding]['mode']).intersection({'all', mode})


def is_binging_trigger_type(binding, type_list):
    return config['input'][binding]['trigger'] in type_list


class Input:
    def __init__(self, game):
        self.game = game
        self.states = {}
        self.mouse_pos = (0, 0)
        self.input_mode = 'core'
        self.full_reset()

    def full_reset(self):
        for binding in config['input']:
            self.states[binding] = False

        self.mouse_state = {
            'left': False,
            'right': False,
            'left_hold': False,
            'right_hold': False,
            'left_release': False,
            'right_release': False,
            'scroll_up': False,
            'scroll_down': False,
        }

    def soft_reset(self):
        for binding in config['input']:
            if config['input'][binding]['trigger'] == 'press':
                self.states[binding] = False
                self.mouse_state['left'] = False
        self.mouse_state['right'] = False
        self.mouse_state['left_release'] = False
        self.mouse_state['right_release'] = False
        self.mouse_state['scroll_up'] = False
        self.mouse_state['scroll_down'] = False

    def process_keyboard_event(self, event, event_type, state):
        if event.type == event_type:
            for binding in config['input']:
                if filter_input_mode(binding, self.input_mode):
                    if is_keyboard(binding):
                        if is_binging_trigger_type(binding, ['press', 'hold']):
                            key_codes = config['input'][binding]['binding'][1]
                            if event.key in key_codes:
                                self.states[binding] = state
                                print(f'key:{event.key} state: {state}')

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.mouse_pos = (
            int(x / self.game.window.scaled_resolution[0]
                * self.game.window.base_resolution[0]),

            int(y / self.game.window.scaled_resolution[1]
                * self.game.window.base_resolution[1])
        )
        self.soft_reset()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            self.process_keyboard_event(event, KEYDOWN, True)
            self.process_keyboard_event(event, KEYUP, False)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_state['left'] = True
                    self.mouse_state['left_hold'] = True
                if event.button == 3:
                    self.mouse_state['right'] = True
                    self.mouse_state['right_hold'] = True
                if event.button == 4:
                    self.mouse_state['scroll_up'] = True
                if event.button == 5:
                    self.mouse_state['scroll_down'] = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_state['left_release'] = True
                    self.mouse_state['left_hold'] = False
                if event.button == 3:
                    self.mouse_state['right_release'] = True
                    self.mouse_state['right_hold'] = False

        if self.states['exit']:
            pygame.quit()
            sys.exit()