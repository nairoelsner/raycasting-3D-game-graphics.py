import graphics as gp
from settings import *
from maps import *

mini_map = map_1

class Map():
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        self.tiles = []

    def get_map(self):
        for i in range(len(self.mini_map)):
            for j in range(len(self.mini_map[i])):
                if self.mini_map[i][j] == 1:
                    self.world_map[(j, i)] = self.mini_map[i][j]
                elif self.mini_map[i][j] == 2:
                    self.level_end = (j, i)

    def draw(self):
        scale = MAP_SCALE
        for pos in self.world_map:
            x0 = pos[0] * scale
            y0 = pos[1] * scale
            rectangle = gp.Rectangle(gp.Point(x0, y0), gp.Point(x0 + scale, y0 + scale))
            rectangle.setWidth(2)
            rectangle.setOutline("white")
            rectangle.setFill("darkgrey")
            rectangle.draw(self.game.screen)
            self.tiles.append(rectangle)