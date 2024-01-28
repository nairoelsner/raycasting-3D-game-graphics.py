import graphics as gp
import math
from settings import *
from random import randint

class RayCasting():
    def __init__(self, game):
        self.game = game
    
    def ray_cast(self):
        ox, oy = self.game.player.position()
        x_map, y_map = self.game.player.map_position()

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #horizontais
            if sin_a > 0:
                y_hor, dy = (y_map + 1, 1)
            else:
                y_hor, dy = (y_map - 1e-6, -1)
            
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = (int(x_hor), int(y_hor))
                if tile_hor in self.game.map.world_map:
                    break

                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            #verticais
            if cos_a > 0:
                x_vert, dx = (x_map + 1, 1)
            else:
                x_vert, dx = (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = (int(x_vert), int(y_vert))
                if tile_vert in self.game.map.world_map:
                    break

                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            #profundidade
            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            #removendo efeito olho de peixe
            depth *= math.cos(self.game.player.angle - ray_angle)
            
            '''
            scale = MAP_SCALE
            line = gp.Line(gp.Point(scale * ox, scale * oy), gp.Point(scale * ox + scale * depth * cos_a, scale * oy + scale * depth * sin_a))
            line.setWidth(2)
            line.setFill("yellow")
            line.draw(self.game.screen)
            '''

            #projeção
            projection_height = SCREEN_DIST / (depth + 0.0001)

            #desenhando as paredes
            x0 = ray * SCALE
            y0 = HALF_HEIGHT - projection_height // 2

            rectangle = gp.Rectangle(gp.Point(x0, y0), gp.Point(x0 + SCALE, y0 + projection_height))
            color = math.ceil(255 / (1 + depth * 0.4))
            rectangle.setFill(gp.color_rgb(color, color, color))
            rectangle.setOutline(gp.color_rgb(color, color, color))
            #rectangle.setFill(gp.color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
            rectangle.draw(self.game.screen)

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()