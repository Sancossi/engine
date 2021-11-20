import os

from src.image import load_img


class Assets:
    def __init__(self):
        self.images_dir = os.path.join('data', 'images')
        self.mics = self.load_dir(os.path.join(self.images_dir, 'mics'))

    def load_dir(self, path):
        images_dir = {}
        for file in os.listdir(path):
            images_dir[file.split('.')[0]] = load_img(
                os.path.join(path, file), (0, 0, 0))
        return images_dir
