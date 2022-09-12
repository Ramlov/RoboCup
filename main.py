#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Button, Color
from pybricks.tools import wait, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
import opgaver


#Definitionen af motor samt diverse sensor
ev3 = EV3Brick()

#Motors
lmotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rmotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
klo = Motor(Port.A)

robot = DriveBase(lmotor, rmotor, wheel_diameter=44.5, axle_track=160)

#Sensors
Ultra = UltrasonicSensor(Port.S1)
touch_sensor = TouchSensor(Port.S4)
leftColor = ColorSensor(Port.S2)
rightColor = ColorSensor(Port.S3)




class Maskine():
    #Colorsensor værdier
    threshold = 0
    blackThreshold = 0

    #Drive værdier
    fullDrive = 0
    turnRate = 0
    fullTurnRate = 0
    turnDirection = "none"

    #Følgende værdier fra Mortens vinkeldokument / eksperiment
    driveFactor = 1.10              #robot.straight(200 * driveFactor)
    rotationFactor = 1.53           #robot.turn(180 * rotationFactor)

    #Længden vi forventer flasken at være væk
    flaskeAfstand = 500


    def turn(self, angle):
        """A corrected robot.turn() function."""
        robot.turn(angle * self.rotationFactor)


    def angle(self):
        """A corrected robot.angle() function."""
        return robot.angle() / self.rotationFactor


    def sdv(self):
        """ Set defualt Values for driving"""
        self.fullDrive = 450
        self.turnRate = 20
        self.fullTurnRate = 70
    

    def autodrive(self):
        while True:
            #REFLECTION
            leftReflection = leftColor.reflection()
            rightReflection = rightColor.reflection()

            leftGuess = ""
            rightGuess = ""

            #CHECKING LEFT GUESS
            if leftReflection >= self.threshold:
                leftGuess = "White"
            elif self.threshold > leftReflection > self.blackThreshold:
                leftGuess = "Grey"
            elif leftReflection <= self.blackThreshold:
                leftGuess = "Black"

            #CHECKING RIGHT GUESS
            if rightReflection >= self.threshold:
                rightGuess = "White"
            elif self.threshold > rightReflection > self.blackThreshold:
                rightGuess = "Grey"
            elif rightReflection <= self.blackThreshold:
                rightGuess = "Black"
        
            right=rightGuess
            left=leftGuess

            ev3.screen.clear()
            ev3.screen.draw_text(50, 0, "REFLECTION")
            ev3.screen.draw_text(0, 25, left)
            ev3.screen.draw_text(75, 25, right)
            wait(100)

            if left == "Grey" and right == "Grey":  #Ligeud
                robot.drive((self.fullDrive*1.2), 0)

            elif left == "White" and right == "Grey":  #Drej højre
                robot.drive(self.fullDrive, self.turnRate)
                self.turnDirection = "right"

            elif left == "Grey" and right == "White":  #Drej venstre
                robot.drive(self.fullDrive, -self.turnRate)
                self.turnDirection = "left"

            elif left == "White" and right == "White":    #Drej MEGET
                if self.turnDirection == "right":
                    robot.drive((self.fullDrive/4), self.fullTurnRate)
                elif self.turnDirection == "left":
                    robot.drive((self.fullDrive/4), -self.fullTurnRate)
            elif left == "Black" or right == "Black":
                robot.stop()
                break


    def Kalibrering(self):

        #Kalibrering i starten
        greyLine = (leftColor.reflection() + rightColor.reflection())/2
        robot.turn(55)
        robot.straight(100)
        whiteLine = (leftColor.reflection() + rightColor.reflection())/2
        robot.straight(-100)
        robot.turn(-55)

        self.threshold = (greyLine + whiteLine) / 2      # Gennemsnittet mellem grå og hvid
        self.blackThreshold = greyLine / 3
    

    def openklo(self):
        klo.run_time(700, 1100)
        wait(100)
        klo.run_until_stalled(400, duty_limit=40)
        wait(100)
        klo.run_time(-800, 1800)
        wait(200)
        ev3.speaker.beep()


    def closeklo(self):
        klo.run_until_stalled(-400, duty_limit=70)


    def flaske(self):
        while not touch_sensor.pressed():
            robot.drive(-100, 0)
        robot.drive(0, 0)
        self.closeklo()


    def saff(self):
        """Search and Find Flaske: Find flaske og grib den"""
        maxAngle = 70                   #SKAL ÆNDRES

        flaskeFundet = False
        dist = Ultra.distance()
        if dist < self.flaskeAfstand:       #Hvis den allerede kan se flasken, så skip scanningen
            flaskeFundet = True

        if flaskeFundet == False:
            #Scan til højre
            robot.reset()                   #Resetter vinklen til angle()
            robot.drive(0, 50)              #Ligesom self.turn(10) men asynkront og konstant
            while self.angle() < maxAngle:
                dist = Ultra.distance()

                ev3.screen.clear()
                ev3.screen.draw_text(0, 20, self.angle())

                if dist < self.flaskeAfstand:
                    flaskeFundet = True
                    self.turn(10)
                    break
            
            robot.stop()

        
        if flaskeFundet == False:            #Også søg til venstre nu
            self.turn(-self.angle())    #TIlbage til midterpunktet
            wait(1000)
            robot.reset()
            robot.drive(0, -50)

            while self.angle() > -maxAngle:
                dist = Ultra.distance()

                ev3.screen.clear()
                ev3.screen.draw_text(0, 20, self.angle())
    
                if dist < self.flaskeAfstand:
                    flaskeFundet = True
                    self.turn(-10)
                    break
            
            robot.stop()
        
        if flaskeFundet:
            for i in range(3):
                ev3.light.on(Color.RED)
                wait(250)

        #
        #   Flasken er fundet, vi finder nu dens midten
        #

        robot.reset()
        robot.drive(0, 30)
        while Ultra.distance() > self.flaskeAfstand:
            pass

        
        # while True:
        #     robot.drive(-80, 0)
        #     dist = Ultra.distance()
        #     if dist < 40:
        #         robot.stop()
        #         robot.straight(-40)
        #         maskine.closeklo()

        #         break
        # robot.straight(-80)
        # maskine.openklo()
        # robot.straight(200)

##############################################







maskine = Maskine()

#--------------START--------------
maskine.sdv()
#maskine.openklo()
#maskine.Kalibrering()

#opgaver.opgave1(ev3, maskine, robot)

maskine.saff()
