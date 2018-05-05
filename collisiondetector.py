import pyglet, os, sys, math


# Used in sequence: obj.move() -> checkCollistion() -> obj.draw()
class CollisionDetector:
    def __init__(self, winH, winW):
        self.winW = winW
        self.winH = winH
        self.objectsArray = []
        self.count = 0

    def setGameObject(self, obj):
        self.objectsArray.append(obj)
        self.count = len(self.objectsArray)

    def checkCollision(self):
        if self.count <= 1:
            print "CheckCollision() count <= 1. Nothing to check!"
            return
        # obj1 is a pacman
        obj1 = self.objectsArray[0]
        for line in range(1, self.count):
            obj2 = self.objectsArray[line]
            if (obj1.getX() >= obj2.getX()) and (obj1.getX() <= obj2.getX() + 20) \
                    and (obj1.getY() >= obj2.getY()) and (obj1.getY() <= obj2.getY() + 20):
                return True
        return False
