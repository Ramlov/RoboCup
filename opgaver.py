#!/usr/bin/env pybricks-micropython

def opgave1(ev3, maskine, robot):
    ev3.speaker.beep()
    maskine.fullDrive = 100
    maskine.fullTurnRate = 60
    maskine.turnRate = 30
    maskine.autodrive()
    robot.straight(-400)
    maskine.fullDrive = 30
    maskine.fullTurnRate = 60
    maskine.turnRate = 40
    maskine.autodrive()


