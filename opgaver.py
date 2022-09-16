#!/usr/bin/env pybricks-micropython

from pybricks.tools import StopWatch

def opgave1(ev3, maskine, robot):
    """Brudt linje"""
    ev3.speaker.beep()
    maskine.autodrive()
    maskine.turn(45)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    robot.straight(50)
    maskine.turn(-45)
    maskine.autodrive()
    maskine.turn(-35)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    robot.straight(40)
    maskine.turn(45)
    maskine.autodrive()


def opgave2(ev3, maskine, robot):
    """Flaske"""
    maskine.sdv()
    robot.straight(200)
    maskine.turn(-90)
    robot.straight(-200)
    maskine.flaske()
    maskine.straight_until_color("Black", -1)
    maskine.straight_until_color("Grey")
    maskine.autodrive()

def opgave3(ev3, maskine, robot):
    """Vippen"""
    watch = StopWatch()

    maskine.autodrive()
    robot.straight(150)
    maskine.turn(-90)
    maskine.autodrive()
    maskine.fullDrive= 100
    while watch.time() < 10000:
        maskine.autodrive()
    maskine.autodrive(True, "White")
    print("har set hvid")
    maskine.turn(-90)
    maskine.autodrive()

def opgave4(ev3, maskine, robot, rightColor):
    """De 4 brudte steger"""
    glCount = 0
    maskine.turn(45)
    while glCount < 3:
        robot.drive(100, 0)
        if rightColor() > maskine.threshold:
            wait(200)
            glcount += 1
    


def opgave5(ev3, maskine, robot):
    """Flaske i målskiven"""

def opgave6(ev3, maskine, robot):
    """Uden om flaske"""