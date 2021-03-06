import pyglet, os, sys, math

SCRIPT_PATH = sys.path[0]


class Ghost:
    def __init__(self, winW, winH, x=20, y=20):
        self.winW = winW
        self.winH = winH
        self.imgGhost = pyglet.image.load(os.path.join(SCRIPT_PATH, "ghost_red.png"))
        self.ghostSprite = pyglet.sprite.Sprite(self.imgGhost)
        self.ghostSprite.y = x  # TODO: set init position from constructor
        self.ghostSprite.x = y
        self.enemyDirection = 'right'  # TODO: set random

    def getX(self):
        return self.ghostSprite.x

    def getY(self):
        return self.ghostSprite.y

    def draw(self):
        self.ghostSprite.draw()

    def update(self, dt):
        if self.ghostSprite.x >= self.winW-self.ghostSprite.width:
            self.enemyDirection = 'left'
        if self.ghostSprite.x <= 0:
            self.enemyDirection = 'right'

        if self.enemyDirection == 'left':
            self.ghostSprite.x -= 2
        if self.enemyDirection == 'right':
            self.ghostSprite.x += 2
