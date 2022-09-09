#!/usr/bin/env pybricks-micropython

class Musik(ev3):
    ev3.speaker.set_volume(100)
    Lydeffekt = 0
    def musik_play():
        ev3.speaker.play_file("Pornhub-30.rsf")
    wait(1000)

    