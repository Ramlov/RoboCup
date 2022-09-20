#!/usr/bin/env pybricks-micropython

from pybricks.tools import StopWatch, wait

def opgave1(ev3, maskine, robot, music):
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


def opgave2(ev3, maskine, robot, music):
    """Flaske"""
    maskine.sdv()

    robot.straight(200)
    maskine.turn(-90)
    
    maskine.BottleFinder()

    robot.straight(-250)

    maskine.BottleFinder()
    maskine.flaske()

    maskine.straight_until_color("Black", -1)

    #Stopper ved blå, skal laves færdig!?
    #Kræver at BottleFinder() bliver opdateret
    return
    maskine.openklo()

    maskine.turn(30)
    maskine.straight_until_color("Grey")
    robot.straight(30)
    maskine.turn(60)
    maskine.autodrive()



def opgave3(ev3, maskine, robot, music):
    """Vippen"""
    watch = StopWatch()
    maskine.autodrive()
    robot.straight(150)
    maskine.turn(-90)
    maskine.fullDrive = 100
    maskine.autodrive()
    while watch.time() < 25000:
        straight_until_color("Grey")
        robot.drive(100, 0)
    maskine.turn(-90)
    robot.straight(50)
    maskine.autodrive()


def opgave4(ev3, maskine, robot, music, rightColor):   #Må gerne opdateres så wait() ikke skal bruges! plsss
    """De 4 brudte steger"""
    glCount=0
    if glCount == 0:
        robot.straight(300)
        robot.turn(-30)
        robot.drive(100, 0)
        glCount += 1
    while glCount < 3:
        if rightColor.reflection() > maskine.threshold:
            glCount += 1
            wait(2500)
    robot.straight(20)
    robot.turn(30)  
    maskine.autodrive()                   


def opgave5(ev3, maskine, robot, music):   #Brug BottleFinder()
    """Flaske i målskiven"""
    


def opgave6(ev3, maskine, robot, music):   #Brug BottleFinder() til at sætte indgangsvinkel bedre
    """Uden om flaske"""
    ev3.speaker.beep()


