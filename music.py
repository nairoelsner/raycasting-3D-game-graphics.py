from pygame import mixer

class Music():
    def __init__(self, game):
        self.game = game

    def play_music(self, audio):
        mixer.init()
        mixer.music.load("audios/" + audio + ".mp3")
        mixer.music.play()
    
    def stop_music(self):
        mixer.music.stop()

    def play_ambience_song(self):
        self.play_music("ambience")