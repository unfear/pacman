import pyglet, os, sys

from maze import Maze
from collisiondetector import CollisionDetector
from pacman import Pacman
from ghost import Ghost


# Maze consist of 28x28 parts, so 1 part = 20px
winWidth = 560
winHeight = 560
win = pyglet.window.Window(winWidth, winHeight)
pyglet.gl.glClearColor(0, 0, 0, 1)

pacman = Pacman(win.width, win.height)
ghost_1 = Ghost(win.width, win.height)
ghost_2 = Ghost(win.width, win.height, 100, 20)
gameover = False
maze = Maze()
maze.draw()
gameOverLabel = pyglet.text.Label('GAME OVER', font_name='Times New Roman', font_size=36, x=winWidth/2, y=winHeight/2, anchor_x='center', anchor_y='center')

collision = CollisionDetector(win.width, win.height)
collision.setGameObject(pacman)
collision.setGameObject(ghost_1)
collision.setGameObject(ghost_2)

#WTF? Why do I need to pass the array to pacman? Why pacman should know about array?
pacman.setDataArray(maze.getDataArray())

@win.event
def on_draw():
    win.clear()
    maze.re_draw()
    pacman.draw()
    ghost_1.draw()
    ghost_2.draw()
    if gameover:
        gameOverLabel.draw()

@win.event
def on_key_press(symbol, modifiers):
    # ... handle this event ...
    pacman.move(symbol)


@win.event
def on_text_motion(motion):
    pacman.move(motion)

#GameLoop
def update(dt):
    ghost_1.update(dt)
    ghost_2.update(dt)
    if collision.checkCollision():
        pacman.catched()
        global gameover
        gameover = True

pyglet.clock.schedule_interval(update, 0.01)

pyglet.app.run()


