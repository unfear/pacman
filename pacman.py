import pyglet
from pyglet.window import key

win = pyglet.window.Window(width=496, height=290)
pyglet.gl.glClearColor(0.3, 0.1, 0.5, 1)

imgEnemy = pyglet.image.load('d:\develop\python\pacman\ghost.bmp')
label = pyglet.text.Label('Crash', font_name='Times New Roman', font_size=36, x=win.width//2, y=win.height//2, anchor_x='center', anchor_y='center')

imgEnemySprite = pyglet.sprite.Sprite(imgEnemy)

# state of pacman direction
pacmanDirection = key.RIGHT
pacmanStep = 4
# state of ghost direction
enemyDirection = 'right'


class Pacman:

    def __init__(self):
        self.anim_pacman = {}
        self.anim_pacman_current = {}
        self.anim_pacman["right"] = pyglet.sprite.Sprite(pyglet.image.load_animation("d:\develop\python\pacman\pacman_right.gif"))
        self.anim_pacman["left"] = pyglet.sprite.Sprite(pyglet.image.load_animation("d:\develop\python\pacman\pacman_left.gif"))
        self.anim_pacman["up"] = pyglet.sprite.Sprite(pyglet.image.load_animation("d:\develop\python\pacman\pacman_up.gif"))
        self.anim_pacman["down"] = pyglet.sprite.Sprite(pyglet.image.load_animation("d:\develop\python\pacman\pacman_down.gif"))
        self.anim_pacman_current = self.anim_pacman["right"]
        self.anim_pacman_current.x = (win.width - self.anim_pacman_current.width) / 2
        self.anim_pacman_current.y = (win.height - self.anim_pacman_current.height) / 2

    def draw(self):
        self.anim_pacman_current.draw()

    def move(self, symbol):
        from pyglet.window import key
        pacmanDirection = symbol
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

        if prev_x >= 496:
            self.move(key.LEFT)
        if prev_x <= 0:
            self.move(key.RIGHT)
        if prev_y >= 290:
            self.move(key.DOWN)
        if prev_y <= 0:
            self.move(key.UP)

        self.anim_pacman_current.x = prev_x
        self.anim_pacman_current.y = prev_y

pacman = Pacman()


@win.event
def on_draw():
    win.clear()
    pacman.draw()
    imgEnemySprite.draw()
    # determinate Crash Enemy and Pacman
    # if( ((imgEnemySprite.x >= anim_pacman_current.x) and (imgEnemySprite.x <= anim_pacman_current.x + 80)) and ((imgEnemySprite.y >= anim_pacman_current.y) and (imgEnemySprite.y <= anim_pacman_current.y + 80)) ):
    #     label.draw()


def update(dt):
    global enemyDirection
    if imgEnemySprite.x >= 496:
        enemyDirection = 'left'
    if imgEnemySprite.x <= 0:
        enemyDirection = 'right'

    if enemyDirection == 'left':
        imgEnemySprite.x -= 2
    if enemyDirection == 'right':
        imgEnemySprite.x += 2
    pacman.move(pacmanDirection)

pyglet.clock.schedule_interval(update, 0.01)


@win.event
def on_key_press(symbol, modifiers):
    # ... handle this event ...
    pacman.move(symbol)


@win.event
def on_text_motion(motion):
    pacman.move(motion)


pyglet.app.run()
