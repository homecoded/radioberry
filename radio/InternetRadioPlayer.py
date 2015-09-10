import os


class InternetRadioPlayer:
    def __init__(self):
        self.streams = ['http://streams.rsa-sachsen.de/rsa-live/mp3-128/mediaplayerrsa']
        self.names = ['Radio RSA Sachsen']

    def play(self):
        print('play ' + self.streams[0])
        os.system('mpc volume 100')
        os.system('mpc add ' + self.streams[0])
        os.system('mpc play')

    def stop(self):
        print("InternetRadioPlayer: off")
        os.system("mpc stop")
        os.system("mpc clear")

