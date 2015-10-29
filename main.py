import pyglet, os, sys
from pacman import Pacman

SCRIPT_PATH = sys.path[0]

win = pyglet.window.Window(width=496, height=290)
pyglet.gl.glClearColor(0.3, 0.1, 0.5, 1)

# TODO: move ghost to ghost.py
imgEnemy = pyglet.image.load(os.path.join(SCRIPT_PATH, "ghost.bmp"))
label = pyglet.text.Label('Crash', font_name='Times New Roman', font_size=36, x=win.width//2, y=win.height//2, anchor_x='center', anchor_y='center')

imgEnemySprite = pyglet.sprite.Sprite(imgEnemy)

# state of ghost direction
enemyDirection = 'right'

pacman = Pacman(win.width, win.height)


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
    if imgEnemySprite.x >= 496-imgEnemySprite.width:
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
