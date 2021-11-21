import os

from src.image import load_img
from src.text import Font

FONTS = {
    'normal_white': ('normal_font', (255, 255, 255)),
    'normal_black': ('normal_font', (0, 0, 0)),
}


def load_fonts(path):
    return {
        name: Font(os.path.join(path, f'{data[0]}.png'), data[1]) for name, data in FONTS.items()
    }


class Assets:
    def __init__(self):
        self.images_dir = os.path.join('data', 'images')

        self.mics = self.load_dir(os.path.join(self.images_dir, 'mics'))

        self.fonts = load_fonts(os.path.join(self.images_dir, 'fonts'))

    def load_dir(self, path):
        images_dir = {}
        for file in os.listdir(path):
            images_dir[file.split('.')[0]] = load_img(
                os.path.join(path, file), (0, 0, 0))
        return images_dir
