import sys
import pygame

from typing import Tuple
from src.core import swap_color, clip


def load_font_img(path: str, font_color: Tuple[int, int, int]):
    fg_color = (255, 0, 0)
    bg_color = (0, 0, 0)
    font_img = pygame.image.load(path).convert()
    font_img = swap_color(font_img, fg_color, font_color)

    last_x = 0
    letters = []

    letter_spacing = []

    for x in range(font_img.get_width()):
        if font_img.get_at((x, 0))[0] == 127:
            letters.append(clip(font_img, last_x, 0, x
                           - last_x, font_img.get_height()))
            letter_spacing.append(x - last_x)
            last_x = x + 1
    for letter in letters:
        letter.set_colorkey(bg_color)
    return letters, letter_spacing, font_img.get_height()


class Font():
    def __init__(self, path, color):
        self.letters, self.letter_spacing, self.line_height = load_font_img(
            path, color)
        self.font_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '-', ',', ':', '+', '\'', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"', '<', '>', ';', '%',
                           'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

        self.space_width = self.letter_spacing[0]
        self.base_spacing = 1
        self.line_spacing = 2

    def render(self, text, surface, location, line_widht=0):
        x_offset = 0
        y_offset = 0

        if line_widht != 0:
            spaces = []
            x = 0
            for i, char in enumerate(text):
                if char == '\n':
                    continue
                elif char == ' ':
                    spaces.append((x, i))
                    x += self.space_width + self.base_spacing
                else:
                    x += self.letter_spacing(self.font_order.index(char)
                                             ) + self.base_spacing

            line_offset = 0
            for i, space in enumerate(spaces):
                if (space[0] - line_offset) > line_widht:
                    line_offset += spaces[i - 1][0] - line_offset
                    if i != 0:
                        text = text[:spaces[i - 1][1]
                                    + '\n' + text[spaces[i - 1][1] + 1:]]

            for char in text:
                if char not in ['\n', ' ']:
                    x = location[0] + x_offset
                    y = location[1] + y_offset
                    surface.blit(
                        self.letters[self.font_order.index(char)], (x, y))
                elif char == ' ':
                    x_offset += self.space_width + self.base_spacing
                else:
                    y_offset += self.line_spacing + self.line_height
                    x_offset = 0

    def width(self, text):
        text_width = 0
        for char in text:
            if char == ' ':
                text_width += self.space_width + self.base_spacing
            else:
                text_width += self.letter_spacing[self.font_order.index(
                    char)] + self.base_spacing
        return text_width