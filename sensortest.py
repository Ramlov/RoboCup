#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait, DataLog
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

#Farvetest. SHeeeesh
colorS = ColorSensor(Port.S3)

amb = colorS.ambient()

color = colorS.color()

reflection = colorS.reflection()

while True:
    rgbTuple = colorS.rgb()

    ev3.screen.clear()
    ev3.screen.draw_text(40, 50, rgbTuple)

    rgbTuple[0]

    wait(1000)
