import pyglet, os, sys
from pacman import Pacman
from ghost import Ghost
from maze import Maze

# Maze consist of 28x28 parts, so 1 part = 20px
winWidth = 560
winHeight = 560
win = pyglet.window.Window(winWidth, winHeight)
pyglet.gl.glClearColor(0, 0, 0, 1)

label = pyglet.text.Label('Crash', font_name='Times New Roman', font_size=36, x=win.width//2, y=win.height//2, anchor_x='center', anchor_y='center')

pacman = Pacman(win.width, win.height)
ghost_1 = Ghost(win.width, win.height)

maze = Maze()
maze.draw()

pacman.setDataArray(maze.getDataArray())


@win.event
def on_draw():
    win.clear()
    pacman.draw()
    ghost_1.draw()
    maze.re_draw()


@win.event
def on_key_press(symbol, modifiers):
    # ... handle this event ...
    pacman.move(symbol)


@win.event
def on_text_motion(motion):
    pacman.move(motion)


pyglet.app.run()
