import pyglet, os, sys, math


# Used in sequence: obj.move() -> checkCollistion() -> obj.draw()
class CollisionDetector:
    def __init__(self, winH, winW):
        self.winW = winW
        self.winH = winH
