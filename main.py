#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait, DataLog
from pybricks.robotics import DriveBase


ev3 = EV3Brick()


lmotor = Motor(Port.B, Direction.CLOCKWISE)
rmotor = Motor(Port.C, Direction.CLOCKWISE)
klo = Motor(Port.A)
touch_sensor = TouchSensor(Port.S4)
robot = DriveBase(lmotor, rmotor, wheel_diameter=55.5, axle_track=104)
colorS = ColorSensor(Port.S3)

#robot.straight(100)

#Klo
klo.run_time(700, 1500)
wait(100)
klo.run_until_stalled(400, duty_limit=40)
wait(100)
klo.run_time(-700, 1600)
wait(200)
ev3.speaker.beep()
while not touch_sensor.pressed():
    robot.drive(100, 0)
robot.drive(0, 0)
klo.run_until_stalled(-400, duty_limit=70)



#klo.run_until_stalled(200)      #kloen drejer

robot.straight(-100)

wait(200)

#klo.run_time(700, 7000)


#Log ting
#ev3.screen.print(deviation)
#wait(10000)
#DataLog(name='log', timestamp=True, extension='csv', append=False)


#---Kør efter linje
#proportionalGain = 1.5

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