from src.window import Window
from src.input import Input
from src.assets import Assets
from src.renderer import Renderer


class Game:
    def __init__(self):
        self.window = Window(self)
        self.input = Input(self)
        self.assets = Assets()
        self.renderer = Renderer(self)

        self.world = None
        # full_init()

    def update(self):
        self.input.update()
        # self.world.update()
        self.renderer.render()
        self.window.render_frame()

    def run(self):
        while True:
            self.update()


if __name__ == '__main__':
    Game().run()
