
ui_font = 'normal_white'


class Renderer:
    def __init__(self, game):
        self.game = game

    def render(self):
        surface = self.game.window.display

        if self.game.window.show_fps:
            self.game.assets.fonts[ui_font].render(
                text=str(int(self.game.window.fps())) + 'fps',
                surface=surface,
                location=(self.game.window.display.get_width() - 114, 22)
            )
