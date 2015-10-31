import pyglet, os, sys
from pacman import Pacman
import json

# TODO: move to Level class load method
# j = json.loads('{"one" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],'
#                ' "two" : [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],'
#                '"three" : [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],'
#                '"four" : [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],'
#                '"five" : [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],'
#                '"six" : [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],'
#                '"seven" : [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],'
#                '"eight" : [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],'
#                '"nine" : [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],'
#                '"ten" : [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],'
#                '"eleven" : [1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],'
#                '"twelve" : [1,1,1,1,1,1,0,1,1,0,1,1,1,2,2,1,1,1,0,1,1,0,1,1,1,1,1,1],'
#                '"thirteen" : [1,1,1,1,1,1,0,0,0,0,1,1,2,2,2,2,1,1,0,0,0,0,1,1,1,1,1,1],'
#                '"fourteen" : [1,1,1,1,1,1,0,1,1,0,1,1,2,2,2,2,1,1,0,1,1,0,1,1,1,1,1,1],'
#                '"fifteen" : [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],'
#                '"sixteen" : [1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1],'
#                '"seventeen" : [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],'
#                '"eighteen" : [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],'
#                '"nineteen" : [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],'
#                '"twenty" : [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],'
#                '"twentyone" : [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],'
#                '"twentytwo" : [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],'
#                '"twentythree" : [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],'
#                '"twentyfour" : [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],'
#                '"twentyfive" : [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],'
#                '"twentysix" : [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],'
#                '"twentyseven" : [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],'
#                '"twentyeight" : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]''}')
#
# f = open("data.json","w")
# f.write(json.dumps(j, ensure_ascii=False))
# f.close()
# print j["two"]

SCRIPT_PATH = sys.path[0]

# Maze consist of 28x28 parts, so 1 part = 20px
winWidth = 560
winHeight = 560
win = pyglet.window.Window(winWidth, winHeight)
pyglet.gl.glClearColor(0.3, 0.1, 0.5, 1)

# TODO: move ghost to ghost.py
imgEnemy = pyglet.image.load(os.path.join(SCRIPT_PATH, "ghost_red.png"))
tileImg = pyglet.image.load(os.path.join(SCRIPT_PATH, "wall-straight-horiz.gif"))
tileBlankImg = pyglet.image.load(os.path.join(SCRIPT_PATH, "blank.gif"))
label = pyglet.text.Label('Crash', font_name='Times New Roman', font_size=36, x=win.width//2, y=win.height//2, anchor_x='center', anchor_y='center')

imgEnemySprite = pyglet.sprite.Sprite(imgEnemy)
imgEnemySprite.y = 20
imgEnemySprite.x = 20
# state of ghost direction
enemyDirection = 'right'

pacman = Pacman(win.width, win.height)


class Maze:
    def __init__(self):
        f = open("data.json","r")
        self.dataArray = json.load(f)
        self.tilesArray = []
        self.batch = pyglet.graphics.Batch()

    def getXByPos(self, col):
        x = 20 * col
        return x

    def getYByPos(self, row):
        return {
            'one': 0,
            'two': 20,
            'three': 40,
            'four': 60,
            'five': 80,
            'six': 100,
            'seven': 120,
            'eight': 140,
            'nine': 160,
            'ten': 180,
            'eleven': 200,
            'twelve': 220,
            'thirteen': 240,
            'fourteen': 260,
            'fifteen': 280,
            'sixteen': 300,
            'seventeen': 320,
            'eighteen': 340,
            'nineteen': 360,
            'twenty': 380,
            'twentyone': 400,
            'twentytwo': 420,
            'twentythree': 440,
            'twentyfour': 460,
            'twentyfive': 480,
            'twentysix': 500,
            'twentyseven': 520,
            'twentyeight': 540
        }.get(row, 0)

    def draw(self):
        for line in self.dataArray:
            arr = self.dataArray[line]
            count = 0
            for elem in arr:
                if elem == 0:
                    self.tilesArray.append(pyglet.sprite.Sprite(tileBlankImg, self.getXByPos(count), self.getYByPos(line), batch=self.batch))
                    count += 1
                elif elem == 1:
                    self.tilesArray.append(pyglet.sprite.Sprite(tileImg, self.getXByPos(count), self.getYByPos(line), batch=self.batch))
                    count += 1
                else:
                    self.tilesArray.append(pyglet.sprite.Sprite(tileBlankImg, self.getXByPos(count), self.getYByPos(line), batch=self.batch))
                    count += 1

    def re_draw(self):
        self.batch.draw()

maze = Maze()
maze.draw()


@win.event
def on_draw():
    win.clear()
    pacman.draw()
    imgEnemySprite.draw()
    maze.re_draw()
    # determinate Crash Enemy and Pacman
    # if( ((imgEnemySprite.x >= anim_pacman_current.x) and (imgEnemySprite.x <= anim_pacman_current.x + 80)) and ((imgEnemySprite.y >= anim_pacman_current.y) and (imgEnemySprite.y <= anim_pacman_current.y + 80)) ):
    #     label.draw()


def update(dt):
    global enemyDirection
    if imgEnemySprite.x >= winWidth-imgEnemySprite.width:
        enemyDirection = 'left'
    if imgEnemySprite.x <= 0:
        enemyDirection = 'right'

    if enemyDirection == 'left':
        imgEnemySprite.x -= 2
    if enemyDirection == 'right':
        imgEnemySprite.x += 2
    pacman.move(pacman.pacmanDirection)

pyglet.clock.schedule_interval(update, 0.01)


@win.event
def on_key_press(symbol, modifiers):
    # ... handle this event ...
    pacman.move(symbol)


@win.event
def on_text_motion(motion):
    pacman.move(motion)


pyglet.app.run()
