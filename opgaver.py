#!/usr/bin/env pybricks-micropython

from pybricks.tools import StopWatch, wait


#%% Opgave 1

def opgave1(ev3, maskine, robot, music):
    """Brudt linje"""
    music.PlayAsyncMusic("Tokyo_Drift1")
    maskine.autodrive()
    maskine.turn(35)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    robot.straight(125)
    maskine.turn(-35)
    maskine.autodrive()
    maskine.turn(-35)
    robot.straight(100)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(38)
    maskine.autodrive()

#%% opgave 2

def opgave2(ev3, maskine, robot, music):
    """Flaske"""
    maskine.retOp()
    robot.straight(160)
    maskine.turn(-88)
    maskine.openklo()
    robot.straight(-380)
    maskine.closeklo()
    maskine.straight_until_color("Black", -1)
    maskine.openklo()
    music.PlayAsyncMusic("Bomb_Plant")
    robot.straight(150)
    maskine.turn(34)
    robot.straight(150)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(55)
    maskine.closeklo()  #Maybe removed?
    maskine.autodrive()


def opgave3(ev3, maskine, robot, music):
    """Vippen"""
    music.PlayAsyncMusic("Tokyo_Drift2")
    watch = StopWatch()
    robot.straight(135)
    maskine.turn(-88)
    maskine.autodrive()
    robot.straight(30)
    maskine.fullDrive = 100
    maskine.blackThreshold -= 10
    maskine.autodrive(7.2)
    wait(550)
    maskine.autodrive(7.6)
    maskine.blackThreshold += 10
    maskine.sdv()
    robot.straight(48)
    maskine.straight_until_color("White")
    maskine.turn(-90)
    robot.straight(50)
    maskine.autodrive()


def opgave4(ev3, maskine, robot, music, rightColor):   #Må gerne opdateres så wait() ikke skal bruges! plsss
    """De 4 brudte steger"""
    music.PlayAsyncMusic("Tokyo_Drift3")
    robot.straight(105)
    maskine.fullDrive = 120
    maskine.autodrive(8.6)
    maskine.turn(-40)
    robot.straight(140)
    maskine.straight_until_color("Grey")
    robot.straight(90)
    maskine.turn(40)
    maskine.fullDrive = 150
    maskine.autodrive()

def opgave5(ev3, maskine, robot, music, Ultra):   #Brug BottleFinder() Bottle in target disc
    """Flaske i målskiven"""
    ev3.speaker.beep()

    robot.straight(135)
    maskine.turn(-90)
    
    maskine.autodrive()

    maskine.openklo()
    maskine.retOp()

    robot.straight(590)

    robot.reset() #Angle to 0
    maskine.turn(180-37)
    
    while Ultra.distance() > 670:
        print(Ultra.distance())
        robot.drive(0, 10)
    robot.stop()
    ev3.speaker.beep()
    
    robot.reset()
    maskine.BottleFinder()
    #maskine.flaske()   #lorte funktion virker aldrig begrund af sensoren
    robot.straight(-410)
    maskine.closeklo()
    
    maskine.turn(2)
    
    #maskine.turn(-maskine.angle())

    robot.straight(630)
    maskine.openklo()
    robot.straight(300)
    maskine.turn(25)
    robot.straight(150)
    maskine.straight_until_color("Grey")
    robot.straight(90)
    maskine.turn(-75)
    maskine.autodrive()


def opgave6(ev3, maskine, robot, music):    #Skal fintunes
    """Uden om flaske"""
    music.PlayAsyncMusic("Tokyo_Drift4")
    maskine.turn(50)
    robot.straight(300)
    maskine.turn(-20)
    maskine.straight_until_color("Grey")

    robot.straight(100)
    maskine.turn(85)
    maskine.autodrive()


def opgave7(ev3, maskine, robot, music, Ultra):
    #maskine.retOp()
    maskine.turn(-120)

    while Ultra.distance() > 600:       #Find muren fra venstre
        robot.drive(0, -20)
    robot.stop()
    ev3.speaker.beep()
    wait(100)

    maskine.turn(-20)


    while Ultra.distance() > 200:       #Kør hen til muren
        robot.drive(-200, 0)
    robot.stop()
    ev3.speaker.beep()
    wait(500)
    
    while Ultra.distance() < 400:       #Drej indtil nu mur
        robot.drive(0, -30)
    robot.stop()
    maskine.turn(-12)
    ev3.speaker.beep()
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
    maskine.turn(20)
    robot.straight(-550)
    maskine.turn(45)
    while Ultra.distance() > 500:
        robot.drive(0, 30)
    robot.stop()
    ev3.speaker.beep()
    maskine.turn(10)
    maskine.straight_until_color("Grey")
    robot.straight(60)
    maskine.turn(30)
    maskine.autodrive()


def opgave8(ev3, maskine, robot, music):  #Uden om flaske 
    maskine.retOp()
    maskine.closeklo()
    robot.straight(30)
    maskine.turn(-50)
    robot.straight(300)
    maskine.turn(50)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(-60)
    maskine.autodrive()



def opgave9(ev3, maskine, robot, music):
    robot.straight(200)
    maskine.turn(-55)
    maskine.straight_until_color("Grey")
    robot.straight(100)
    maskine.turn(55)
    maskine.autodrive(7.9)
    
