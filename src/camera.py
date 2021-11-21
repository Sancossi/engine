from math import floor


def get_direction(next_x, lock_distance):
    if next_x > lock_distance:
        return 1
    elif next_x < -lock_distance:
        return -1
    return 0


class Camera:
    def __init__(self, game):
        self.game = game
        self.target_pos = [0, 0]
        self.true_pos = [0, 0]

        self.rate = 0.3
        self.restiction_point = None
        self.lock_distance = 200

        self.track_entity = None

    def focus(self):
        self.update()
        self.true_pos = self.target_pos.copy()

    def update(self):
        if self.track_entity:
            x, y = self.track_entity.pos
            x -= self.game.window.display.get_width() // 2,
            y -= self.game.window.display.get_heigth() // 2,
            self.set_target((x, y))

        speed = self.rate / self.game.window.dt
        self.true_pos[0] += (self.target_pos[0] - self.true_pos[0]) / speed
        self.true_pos[1] += (self.target_pos[1] - self.true_pos[1]) / speed

        if self.restiction_point:
            x_center = self.game.window.display.get_width() // 2
            next_x = self.true_pos[0] + x_center - self.restiction_point[0]

            direction = get_direction(next_x, self.lock_distance)
            if direction:
                self.true_pos[0] = self.restiction_point[0] - \
                     x_center + direction * self.lock_distance

            y_center = self.game.window.display.get_heigth()
            next_y = self.true_pos[1] + y_center - self.restiction_point[1]

            direction = get_direction(next_y, self.lock_distance)
            if direction:
                self.true_pos[1] = self.restiction_point[1] - \
                    y_center + direction * self.lock_distance

    def set_tracked_entity(self, entity):
        self.track_entity = entity

    def set_target(self, pos):
        self.target_pos = list(pos)

    def set_restriction(self, pos):
        self.restriction_point = list(pos)

    @property
    def render_offset(self):
        return [
            self.true_pos[0] - self.game.window.offset[0],
            self.true_pos[1] - self.game.window.offset[1]
        ]

    @property
    def pos(self):
        return [
            int(floor(self.true_pos[0])),
            int(floor(self.true_pos[1])),
        ]
