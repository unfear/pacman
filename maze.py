import json
import pyglet, os, sys, math

SCRIPT_PATH = sys.path[0]

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

class Maze:
    def __init__(self):
        f = open("data.json","r")
        self.dataArray = json.load(f)
        self.tilesArray = []
        self.batch = pyglet.graphics.Batch()
        self.tileImg = pyglet.image.load(os.path.join(SCRIPT_PATH, "wall.png"))
        self.tileBlankImg = pyglet.image.load(os.path.join(SCRIPT_PATH, "blank.png"))

    def getDataArray(self):
        return self.dataArray

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
                    self.tilesArray.append(pyglet.sprite.Sprite(self.tileBlankImg, self.getXByPos(count), self.getYByPos(line), batch=self.batch))
                elif elem == 1:
                    self.tilesArray.append(pyglet.sprite.Sprite(self.tileImg, self.getXByPos(count), self.getYByPos(line), batch=self.batch))
                else:
                    self.tilesArray.append(pyglet.sprite.Sprite(self.tileBlankImg, self.getXByPos(count), self.getYByPos(line), batch=self.batch))
                count += 1

    def re_draw(self):
        self.batch.draw()
