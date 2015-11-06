import pyglet, os, sys
from pyglet.window import key

SCRIPT_PATH = sys.path[0]


class Pacman:
    # state of pacman direction
    pacmanDirection = key.RIGHT

    def __init__(self, winW, winH):
        self.winW = winW
        self.winH = winH
        self.anim_pacman = {}
        self.anim_pacman_current = {}
        self.anim_pacman["right"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_right.gif")))
        self.anim_pacman["left"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_left.gif")))
        self.anim_pacman["up"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_up.gif")))
        self.anim_pacman["down"] = pyglet.sprite.Sprite(pyglet.image.load_animation(os.path.join(SCRIPT_PATH, "pacman_down.gif")))
        self.anim_pacman_current = self.anim_pacman["right"]
        self.anim_pacman_current.x = (winW - self.anim_pacman_current.width) / 2
        self.anim_pacman_current.y = 200 #(winH - self.anim_pacman_current.height) / 2
        self.dataArray = []
        self.currentRow = 'eleven'
        # state of pacman step
        self.pacmanStep = 5

    def setDataArray(self, arr):
        self.dataArray = arr

    def draw(self):
        self.anim_pacman_current.draw()

    def getColByX(self, coord):
        return int(round(coord / 20))

    def getRowByY(self, coord):
        return {
            0:   'one',
            20:  'two',
            40:  'three',
            60:  'four',
            80:  'five',
            100: 'six',
            120: 'seven',
            140: 'eight',
            160: 'nine',
            180: 'ten',
            200: 'eleven',
            220: 'twelve',
            240: 'thirteen',
            260: 'fourteen',
            280: 'fifteen',
            300: 'sixteen',
            320: 'seventeen',
            340: 'eighteen',
            360: 'nineteen',
            380: 'twenty',
            400: 'twentyone',
            420: 'twentytwo',
            440: 'twentythree',
            460: 'twentyfour',
            480: 'twentyfive',
            500: 'twentysix',
            520: 'twentyseven',
            540: 'twentyeight'
        }.get(round(coord), 'undefined')

    def clash(self, pacmanX, pacmanY):
        col = self.getColByX(pacmanX)
        row = self.getRowByY(pacmanY)
        if row == 'undefined':
            row = self.currentRow
        else:
            self.currentRow = row

        elem = self.dataArray[row][col]
        if elem == 0:
            return False
        else:
            return True

    def move(self, symbol):
        from pyglet.window import key
        self.pacmanDirection = symbol
        prev_x = self.anim_pacman_current.x
        prev_y = self.anim_pacman_current.y

        if symbol == key.LEFT or symbol == key.MOTION_LEFT:
            self.anim_pacman_current = self.anim_pacman["left"]
            prev_x -= self.pacmanStep
        if symbol == key.RIGHT or symbol == key.MOTION_RIGHT:
            self.anim_pacman_current = self.anim_pacman["right"]
            prev_x += self.pacmanStep
        if symbol == key.UP or symbol == key.MOTION_UP:
            self.anim_pacman_current = self.anim_pacman["up"]
            prev_y += self.pacmanStep
        if symbol == key.DOWN or symbol == key.MOTION_DOWN:
            self.anim_pacman_current = self.anim_pacman["down"]
            prev_y -= self.pacmanStep

        # check clash
        if self.clash(prev_x, prev_y):
            return

        self.anim_pacman_current.x = prev_x
        self.anim_pacman_current.y = prev_y

        if prev_x >= self.winW-self.anim_pacman_current.width:
            self.move(key.LEFT)
        if prev_x <= 0:
            self.move(key.RIGHT)
        if prev_y >= self.winH-self.anim_pacman_current.height:
            self.move(key.DOWN)
        if prev_y <= 0:
            self.move(key.UP)
