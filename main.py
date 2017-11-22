import pyglet, os, sys
from pacman import Pacman
from ghost import Ghost
from maze import Maze

# Maze consist of 28x28 parts, so 1 part = 20px
winWidth = 560
winHeight = 560
win = pyglet.window.Window(winWidth, winHeight)
pyglet.gl.glClearColor(0, 0, 0, 1)

pacman = Pacman(win.width, win.height)
ghost_1 = Ghost(win.width, win.height, pacman)

maze = Maze()
maze.draw()

pacman.setDataArray(maze.getDataArray())


@win.event
def on_draw():
    win.clear()
    maze.re_draw()
    pacman.draw()
    ghost_1.draw()


@win.event
def on_key_press(symbol, modifiers):
    # ... handle this event ...
    pacman.move(symbol, ghost_1)


@win.event
def on_text_motion(motion):
    pacman.move(motion, ghost_1)


pyglet.app.run()
