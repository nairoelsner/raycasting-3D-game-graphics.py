from settings import *
import graphics as gp
import math
from keyboard import *
from collisions import *


class Player():
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POSITION
        self.angle = PLAYER_ANGLE

    def movement(self):
        speed = PLAYER_SPEED
        rotation_speed = PLAYER_ROTATION_SPEED
        
        dx = 0
        dy = 0
        
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        if is_pressed("w"):
            dx += speed_cos
            dy += speed_sin
        if is_pressed("s"):
            dx -= speed_cos
            dy -= speed_sin
        
        if is_pressed("a"):
            self.angle -= rotation_speed
        if is_pressed("d"):
            self.angle += rotation_speed


        self.angle %= math.tau #tau = 2 * pi        
        self.check_wall_collision(dx, dy)
    
    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
            
    def check_wall(self, x, y):
        if (x, y) not in self.game.map.world_map:
            return True
        return False
        
    def draw(self):
        scale = MAP_SCALE

        x0, y0 = self.x * scale, self.y * scale

        vision = gp.Line(gp.Point(x0, y0), gp.Point(x0 + WIDTH * math.cos(self.angle), y0 + WIDTH * math.sin(self.angle)))
        vision.setWidth(2)
        vision.setFill("green")
        vision.draw(self.game.screen)
        
        
        player = gp.Circle(gp.Point(self.x * scale, self.y * scale), 15)
        player.setWidth(2)
        player.setFill("blue")
        player.draw(self.game.screen)
        
    def update(self):
        self.movement()

    #propriedades
    def position(self):
        return (self.x, self.y)
    
    def map_position(self):
        return (int(self.x), int(self.y))