import pyglet, os, sys
from pyglet.window import key

SCRIPT_PATH = sys.path[0]

# state of pacman step
pacmanStep = 4


class Pacman:
    # state of pacman direction
    pacmanDirection = key.RIGHT

    def __init__(self, winW, winH):
        self.anim_pacman = {}
        self.anim_pacman_current = {}
        self.anim_pacman["right"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_right.gif")))
        self.anim_pacman["left"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_left.gif")))
        self.anim_pacman["up"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_up.gif")))
        self.anim_pacman["down"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_down.gif")))
        self.anim_pacman_current = self.anim_pacman["right"]
        self.anim_pacman_current.x = (winW - self.anim_pacman_current.width) / 2
        self.anim_pacman_current.y = (winH - self.anim_pacman_current.height) / 2

    def draw(self):
        self.anim_pacman_current.draw()

    def move(self, symbol):
        from pyglet.window import key
        self.pacmanDirection = symbol
        prev_x = self.anim_pacman_current.x
        prev_y = self.anim_pacman_current.y

        if symbol == key.LEFT or symbol == key.MOTION_LEFT:
            self.anim_pacman_current = self.anim_pacman["left"]
            prev_x -= pacmanStep
        if symbol == key.RIGHT or symbol == key.MOTION_RIGHT:
            self.anim_pacman_current = self.anim_pacman["right"]
            prev_x += pacmanStep
        if symbol == key.UP or symbol == key.MOTION_UP:
            self.anim_pacman_current = self.anim_pacman["up"]
            prev_y += pacmanStep
        if symbol == key.DOWN or symbol == key.MOTION_DOWN:
            self.anim_pacman_current = self.anim_pacman["down"]
            prev_y -= pacmanStep

        self.anim_pacman_current.x = prev_x
        self.anim_pacman_current.y = prev_y

        if prev_x >= 496-self.anim_pacman_current.width:
            self.move(key.LEFT)
        if prev_x <= 0:
            self.move(key.RIGHT)
        if prev_y >= 290-self.anim_pacman_current.height:
            self.move(key.DOWN)
        if prev_y <= 0:
            self.move(key.UP)
