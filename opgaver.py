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
    robot.straight(150)
    maskine.turn(-90)
    maskine.autodrive()
    maskine.fullDrive = 100
    maskine.autodrive(7.5)
    wait(750)
    maskine.autodrive(8)    
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
    robot.straight(10)
    robot.turn(30)  
    maskine.autodrive()                   


def opgave5(ev3, maskine, robot, music):   #Brug BottleFinder()
    """Flaske i målskiven"""
    


def opgave6(ev3, maskine, robot, music):    #Skal fintunes
    """Uden om flaske"""

    maskine.turn(50)
    robot.straight(300)
    maskine.turn(-20)
    maskine.straight_until_color("Grey")

    robot.straight(100)
    maskine.turn(80)
    maskine.autodrive()


def opgave7(ev3, maskine, robot, music, Ultra):
    #while True:
    #    print(Ultra.distance())

    maskine.turn(-120)

    while Ultra.distance() > 1000:       #Find muren fra venstre
        robot.drive(0, -20)
    robot.stop()
    ev3.speaker.beep()
    wait(1000)

    maskine.turn(-20)


    while Ultra.distance() > 200:       #Kør hen til muren
        robot.drive(-200, 0)
    robot.stop()
    ev3.speaker.beep()
    wait(1000)
    
    while Ultra.distance() < 400:       #Drej indtil nu mur
        robot.drive(0, -30)
    robot.stop()
    maskine.turn(-7)
    ev3.speaker.beep()
    wait(1000)

    robot.straight(-200)

    while Ultra.distance() > 120:           #Kør indtil 2 mur
        robot.drive(-100, 0)
    robot.stop()
    ev3.speaker.beep()


    maskine.turn(70)
    while Ultra.distance() < 1000:           #Drej til frihed
        robot.drive(0, 30)
    robot.stop()
    ev3.speaker.beep()
    maskine.turn(10)
    robot.straight(-500)


    while True:
        print(Ultra.distance())

    
