#!/usr/bin/env pybricks-micropython
import music

def opgave1(ev3, maskine, robot):
    ev3.speaker.beep()
    maskine.fullDrive = 100
    maskine.fullTurnRate = 60
    maskine.turnRate = 30
    maskine.autodrive()


def musik_opgave1(ev3):
    ev3.speaker.set_volume(100)
    ev3.speaker.play_file("music/Tank.rsf")
    

