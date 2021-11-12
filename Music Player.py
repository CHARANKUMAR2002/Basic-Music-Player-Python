from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()

def stop():
    mixer.music.stop()


class MusicPlayer:
    root.config(bg='black')
    root.geometry("280x75")

    def __init__(self, window):

        def des():
            root.destroy()
        window.title("Music Player v1.0")
        window.resizable(0, 0)
        Load = Button(window, text='Load', width=10, command=self.load, bg='black', fg="green", font=("times", 10))
        Play = Button(window, text='Play', width=10, command=self.play, bg='green', fg="#fcfcec", font=("times", 10))
        Pause = Button(window, text='Pause', width=10,
                       command=self.pause, bg='orange', fg="#fcfcec", font=("times", 10))
        Stop = Button(window, text='Stop', width=10, command=stop, bg='red', fg="#fcfcec", font=("times", 10))
        Close = Button(window, text='Close', width=10, command=des, bg='black', fg="red", font=("times", 10))
        Load.place(x=75, y=45)
        Play.place(x=30, y=20)
        Pause.place(x=100, y=20)
        Stop.place(x=175, y=20)
        Close.place(x=150, y=45)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False


app = MusicPlayer(root)
root.mainloop()
