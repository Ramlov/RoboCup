#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Button, Color
from pybricks.tools import wait, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
import opgaver      #Opgaver.py
import _thread      #Til musicplayer og muligvis kloen?


#Definitionen af motor samt diverse sensor
ev3 = EV3Brick()

#Motors
lmotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rmotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
klo = Motor(Port.A)
robot = DriveBase(lmotor, rmotor, wheel_diameter=44.5, axle_track=160)
ev3.speaker.set_volume(100)

#Sensors
Ultra = UltrasonicSensor(Port.S1)
touch_sensor = TouchSensor(Port.S4)
leftColor = ColorSensor(Port.S2)
rightColor = ColorSensor(Port.S3)





class Maskine():
    #Colorsensor værdier
    threshold = 0
    blackThreshold = 0

    #Drive værdier ( bliver sat af maskine.sdv(), ikke rør! )
    fullDrive = 0
    turnRate = 0
    fullTurnRate = 0

    #Autodrive, hvilken retning er robotten igang med at dreje
    turnDirection = "none"

    #Følgende værdier fra Mortens vinkeldokument / eksperiment
    driveFactor = 1.10              #robot.straight(200 * driveFactor)
    rotationFactor = 1.53           #robot.turn(180 * rotationFactor)

    #Længden vi forventer flasken at være væk
    flaskeAfstand = 500     #Skal ændres!? Kig på banen


    def turn(self, angle):
        """A corrected robot.turn() function."""
        robot.turn(angle * self.rotationFactor)

    def angle(self):
        """A corrected robot.angle() function."""
        return robot.angle() / self.rotationFactor

    def sdv(self):
        """ Set defualt Values for driving"""
        self.fullDrive = 150
        self.turnRate = 35
        self.fullTurnRate = 70


    def autodrive(self, stopForFarve=None, stopFarve=None):
        """
        AutoDrive-funktion
        Hvis robotten skal stoppe for en farve på begge sensorer skal stopForFarve = True og
        farven sættes med fx stopFarve = hvid
        """
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
            elif stopForFarve == True and left == stopFarve and right == stopFarve:
                robot.stop()
                break


    def straight_until_color(self, color, dir=1):
        while True:
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

            if right == "White" or left == "White":     #Skal muligvis ændres at at sige (if right != color)
                    robot.drive((dir * self.fullDrive), 0)
            elif left == color or right == color:
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
    

    def retOp(self):        #Måske ændres?
        robot.straight(-200)
        maskine.fullDrive = 50
        maskine.turnRate = 40
        maskine.autodrive()


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
        while Ultra.distance() > 80:
            robot.drive(-100, 0)
            print(Ultra.distance())
        robot.stop()
        wait(3000)
        robot.straight(-70)
        maskine.closeklo()


    def saff(self):
        """Search and Find Flaske"""
        maxAngle = 50                   #SKAL ÆNDRES ved testning
        angleFromEdgeToCenter = 10

        flaskeFundet = False
        
        if Ultra.distance() < self.flaskeAfstand:       #Hvis den allerede kan se flasken, så hurtig ret ind
            while Ultra.distance() > self.flaskeAfstand:
                robot.drive(0, -50)
            
            maskine.turn(angleFromEdgeToCenter)
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
                    self.turn(angleFromEdgeToCenter)
                    break
            
            robot.stop()

        
        if flaskeFundet == False:           #Søg til venstre hvis ikke fundet til højre
            self.turn(-self.angle())        #TIlbage til midterpunktet
            wait(1000)
            robot.reset()
            robot.drive(0, -50)

            while self.angle() > -maxAngle:
                dist = Ultra.distance()

                ev3.screen.clear()
                ev3.screen.draw_text(0, 20, self.angle())
    
                if dist < self.flaskeAfstand:
                    flaskeFundet = True
                    self.turn(-angleFromEdgeToCenter)
                    break
            
            robot.stop()
        
        ev3.light.on(Color.RED)
        wait(250)
        ev3.speaker.beep()
        ev3.light.on(Color.GREEN)

        
        #

##############################################
class Music():
    def musik_intro():
        ev3.speaker.set_volume(100)
        ev3.speaker.play_file("music/Pornhub-intro.rsf")

    def musik_opgave1(song):
        ev3.speaker.set_volume(100)
        ev3.speaker.play_file("music/Tokyo_Drift1.rsf")
    
    def musik_opgave2():
        ev3.speaker.play_file("Tank.rsf")
    

maskine = Maskine()
#--------------START--------------
maskine.sdv()


#maskine.saff()

