import graphics as gp
from settings import *
import time

class Transition:
    def __init__(self, game):
        self.game = game
    
    def intro(self):
        circle = gp.Circle(gp.Point(HALF_WIDTH, HALF_HEIGHT), 160)
        color = 0
        circle.draw(self.game.screen)

        self.game.music.play_music("intro")

        for i in range(21):
            self.game.screen.clear(1)
            circle.setFill(gp.color_rgb(color, color, color))
            image = gp.Image(gp.Point(HALF_WIDTH, HALF_HEIGHT), f"images/intro/intro-{i}.png")
            image.draw(self.game.screen)
            gp.update(24)
            color += 12
        time.sleep(2)
        
        for i in range(20, -1, -1):
            self.game.screen.clear(1)
            circle.setFill(gp.color_rgb(color, color, color))
            image = gp.Image(gp.Point(HALF_WIDTH, HALF_HEIGHT), f"images/intro/intro-{i}.png")
            image.draw(self.game.screen)
            gp.update(24)
            color -= 12
        self.game.screen.clear()
        gp.update()
        time.sleep(0.5)