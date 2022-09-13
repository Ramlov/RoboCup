#!/usr/bin/env pybricks-micropython

def opgave1(ev3, maskine, robot):
    ev3.speaker.beep()
    maskine.autodrive()
    maskine.turn(45)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    maskine.turn(-45)
    maskine.autodrive()
    maskine.turn(-45)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    maskine.turn(45)
    maskine.autodrive()

def opgave2(ev3, maskine, robot):
    robot.straight(100)
    maskine.turn(90)
    
    
