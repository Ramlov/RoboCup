#!/usr/bin/env pybricks-micropython

from pybricks.tools import StopWatch, wait

def opgave1(ev3, maskine, robot, music):
    """Brudt linje"""
    maskine.autodrive()
    maskine.turn(35)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(-35)
    maskine.autodrive()
    maskine.turn(-35)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(25)
    maskine.autodrive()


def opgave2(ev3, maskine, robot, music):
    """Flaske"""
    robot.straight(150)
    maskine.turn(-90)
    maskine.openklo()
    robot.straight(-200)
    maskine.BottleFinder()
    maskine.flaske()
    maskine.straight_until_color("Black", - 1)
    robot.straight(-100)
    maskine.openklo()
    robot.straight(150)
    maskine.turn(34)
    robot.straight(150)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(55)
    maskine.autodrive()






    """
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
"""


def opgave3(ev3, maskine, robot, music):
    """Vippen"""
    watch = StopWatch()
    robot.straight(150)
    maskine.turn(-90)
    maskine.autodrive()
    robot.straight(30)
    maskine.fullDrive = 100
    maskine.autodrive(7.5)
    wait(550)
    maskine.autodrive(8.5)    
    maskine.turn(-90)
    robot.straight(50)
    maskine.autodrive()


def opgave4(ev3, maskine, robot, music, rightColor):   #Må gerne opdateres så wait() ikke skal bruges! plsss
    """De 4 brudte steger"""
    robot.straight(100)
    maskine.fullDrive = 120
    maskine.autodrive(8.8)
    maskine.turn(-40)
    robot.straight(140)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(20)
    maskine.autodrive()

    """
    robot.straight(50)
    maskine.autodrive(2)
    maskine.turn(-55)


    lastColor = 0
    glCount=0

    while glCount < 2:
        robot.drive(100, 0)

        if maskine.threshold > rightColor.reflection():   #If rightColor is grey
            if lastColor >= maskine.threshold:
                ev3.speaker.beep()
                glCount += 1
        
        print(maskine.threshold , rightColor.reflection())

        lastColor = rightColor.reflection()
    
    ev3.speaker.beep()

    robot.straight(50)
    maskine.turn(55)

    maskine.autodrive()


    glCount=0
    if glCount == 0:
        robot.straight(300)
        robot.turn(-80)
        robot.drive(100, 0)
        glCount += 1
    while glCount < 3:
        if rightColor.reflection() > maskine.threshold:
            glCount += 1
            wait(1500)
    
    robot.straight(100)
    robot.turn(80)  
    maskine.autodrive()                   
"""

def opgave5(ev3, maskine, robot, music):   #Brug BottleFinder()
    """Flaske i målskiven"""
    


def opgave6(ev3, maskine, robot, music):   #Brug BottleFinder() til at sætte indgangsvinkel bedre
    """Uden om flaske"""
    ev3.speaker.beep()

def opgave9(ev3, maskine, robot, music):
    active = 0
    countlol = 0
    while active == 0:
        countlol+1 
    maskine.straight_until_color("Black")
    active = 1
    countlol = countlol/2
    while countlol > 0:
        countlol
    robot.drive(maskine.fullDrive)
