import pyglet, os, sys, math

SCRIPT_PATH = sys.path[0]


class Ghost:
    def __init__(self, winW, winH, pacman):
        self.winW = winW
        self.winH = winH
        self.pacman = pacman
        self.imgGhost = pyglet.image.load(os.path.join(SCRIPT_PATH, "ghost_red.png"))
        self.ghostSprite = pyglet.sprite.Sprite(self.imgGhost)
        self.ghostSprite.y = 20  # TODO: set init position from constructor
        self.ghostSprite.x = 20
        self.enemyDirection = 'right'  # TODO: set random
        pyglet.clock.schedule_interval(self.update, 0.01)

    def getX(self):
        return self.ghostSprite.x

    def getY(self):
        return self.ghostSprite.y

    def draw(self):
        self.ghostSprite.draw()

    def clashPacman(self):
        if( (self.pacman.getX() >= self.getX()) and (self.pacman.getX() <= self.getX() + 20) and ((self.pacman.getY() >= self.getY()) and (self.pacman.getY() <= self.getY() + 20))):
            self.pacman.catched()


    def update(self, dt):
        if self.ghostSprite.x >= self.winW-self.ghostSprite.width:
            self.enemyDirection = 'left'
        if self.ghostSprite.x <= 0:
            self.enemyDirection = 'right'

        if self.enemyDirection == 'left':
            self.ghostSprite.x -= 2
        if self.enemyDirection == 'right':
            self.ghostSprite.x += 2

        self.clashPacman()
