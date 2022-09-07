#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait, DataLog
from pybricks.robotics import DriveBase


#Defination af motor samt diverse sensor
ev3 = EV3Brick()

lmotor = Motor(Port.B, Direction.CLOCKWISE)
rmotor = Motor(Port.C, Direction.CLOCKWISE)
klo = Motor(Port.A)
touch_sensor = TouchSensor(Port.S4)
ultra_sensor = UltrasonicSensor(Port.S2)
robot = DriveBase(lmotor, rmotor, wheel_diameter=55.5, axle_track=104)
colorS = ColorSensor(Port.S3)



#Definere åben og luk af klo
def openklo():
    klo.run_time(700, 1500)
    wait(100)
    klo.run_until_stalled(400, duty_limit=40)
    wait(100)
    klo.run_time(-700, 1800)
    wait(200)
    ev3.speaker.beep()

def closeklo():
    klo.run_until_stalled(-400, duty_limit=70)

def drive(x):                                               # Drive funktion
    deviation = colorS.reflection() - threshold             
    turnRate = proportionalGain * deviation
    robot.drive(x, turnRate)

    wait(10)




#---Linjeværdier
proportionalGain = 1.5

greyLine = colorS.reflection() + 2                          #grå
white = colorS.reflection()                                 #hvid
threshold = (greyLine + white) / 2                          # threshold mellem grå og hvid
blackLines = greyLine / 3                                   #sort
robot.turn(720)

#Defination af variabler brugt til opgaver
opgavenr = 0

def main():                                              # Opgaver
    global opgavenr

    while True():
        if colorS.reflection() <= blackLines:       #HVIS DEN RAMMER SORT. SKAL LAVES OM
            opgavenr += 1

        if opgavenr == 1:
            opgave1()





def opgave1():
    while colorS.reflection() > blackLines:
        drive(100)
        robot.drive(100, 0)
        wait(300)
        robot.stop()
        robot.turn(45)

        while colorS.reflection() > greyLine:
            robot.drive(100, 0)

        robot.straight(50)
        robot.stop()
        robot.turn(-45)

        while colorS.reflection() > blackLines:
            drive(100)
        
        robot.turn(-45)

        while colorS.reflection() > greyLine:
            robot.drive(100, 0)
        wait(750)
        robot.stop()
        robot.turn(45)







# Funktion for at touchsensor
    #while not touch_sensor.pressed():
     #   robot.drive(100, 0)
    #robot.drive(0, 0)



#greyLine = colorS.reflection() + 2   
#robot.turn(-45)                         
#white = colorS.reflection()                      
#robot.turn(45)                           
#threshold = (greyLine + white) / 2 
#blackLines = greyLine / 3    
    
#def drive(x):                                
#    deviation = colorS.reflection() - threshold             

 #   turnRate = proportionalGain * deviation

#    robot.drive(x, turnRate)

#    wait(10)    


#while colorS.reflection() > blackLines:
#    robot.drive(100, 0)




main()