import graphics as gp
from settings import *
from map import *
from player import *
from raycasting import *
from music import *
from transition import *

class Game():
    def __init__(self):
        self.screen = gp.GraphWin("labirinto kkkkkk", WIDTH, HEIGHT, autoflush = False)
        self.screen.setBackground("black")

        self.music = Music(self)
        self.transition = Transition(self)
        
        self.transition.intro()
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        
        self.map.draw()
        #self.music.play_ambience_song()

        self.raycasting = RayCasting(self)
    
    def check_events(self):
        if self.player.map_position() == self.map.level_end:
            print("localização marcada")
       
    def update(self):
        self.player.update()
        self.raycasting.update()
        gp.update(24)

    def draw(self):
        #self.screen.clear(len(self.map.world_map))
        #self.player.draw()
        self.screen.clear()

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()
            
if __name__ == '__main__':
    game = Game()
    game.run()