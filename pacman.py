import pyglet
from pyglet.window import key

win = pyglet.window.Window(width=496, height=290)
pyglet.gl.glClearColor(0.3, 0.1, 0.5, 1)

imgPacman = pyglet.image.load_animation("d:\develop\python\pacman\pacman.gif")
imgEnemy = pyglet.image.load('d:\develop\python\pacman\ghost.bmp')
label = pyglet.text.Label('Crash', font_name='Times New Roman', font_size=36, x=win.width//2, y=win.height//2, anchor_x='center', anchor_y='center')

imgPacmanSprite = pyglet.sprite.Sprite(imgPacman)
imgEnemySprite = pyglet.sprite.Sprite(imgEnemy)
imgPacmanSprite.x = (win.width - imgPacmanSprite.width) / 2
imgPacmanSprite.y = (win.height - imgPacmanSprite.width) / 2

# state of pacman direction
pacmanDirection = 'right'
pacmanStep = 4
# state of ghost direction
enemyDirection = 'right'


@win.event
def on_draw():
    win.clear()
    imgPacmanSprite.draw()
    imgEnemySprite.draw()
    # determinate Crash Enemy and Pacman
    if( ((imgEnemySprite.x >= imgPacmanSprite.x) and (imgEnemySprite.x <= imgPacmanSprite.x + 80)) and ((imgEnemySprite.y >= imgPacmanSprite.y) and (imgEnemySprite.y <= imgPacmanSprite.y + 80)) ):
        label.draw()


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

pyglet.clock.schedule_interval(update, 0.01)


@win.event
def on_key_press(symbol, modifiers):
    # ... handle this event ...

    # if symbol == key.LEFT:
    #     imgPacmanSprite.image = imgPacman.get_transform(False, True, 180)
    # if symbol == key.RIGHT:
    #     imgPacmanSprite.image = imgPacman.get_transform(False, False, 360)
    # if symbol == key.UP:
    #     imgPacmanSprite.image = imgPacman.get_transform(True, False, 90)
    # if symbol == key.DOWN:
    #     imgPacmanSprite.image = imgPacman.get_transform(False, False, 90)
    if symbol == key.LEFT:
        imgPacmanSprite.image = imgPacman.get_transform(True, False, 0)
    if symbol == key.RIGHT:
        imgPacmanSprite.image = imgPacman.get_transform(False, False, 180)
    if symbol == key.UP:
        imgPacmanSprite.image = imgPacman.get_transform(True, False, 90)
    if symbol == key.DOWN:
        imgPacmanSprite.image = imgPacman.get_transform(False, False, 90)


@win.event
def on_text_motion(motion):
    from pyglet.window import key
    if motion == key.MOTION_LEFT:
        imgPacmanSprite.x -= pacmanStep
    if motion == key.MOTION_RIGHT:
        imgPacmanSprite.x += pacmanStep
    if motion == key.MOTION_UP:
        imgPacmanSprite.y += pacmanStep
    if motion == key.MOTION_DOWN:
        imgPacmanSprite.y -= pacmanStep

pyglet.app.run()
