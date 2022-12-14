#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Button, Color, Stop
from pybricks.tools import wait, DataLog, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
from pybricks.tools import StopWatch
import opgaver      #Opgaver.py
from threading import Thread        #Erstatter _thread. Til musicplayeren
import math


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
#touch_sensor = TouchSensor(Port.S4)
leftColor = ColorSensor(Port.S2)
rightColor = ColorSensor(Port.S3)

#StopWatch
stopwatch = StopWatch()

class Maskine():
    #Colorsensor værdier
    threshold = 0
    blackThreshold = 0

    #Drive værdier ( bliver sat af maskine.sdv(), ikke rør! )
    fullDrive = 0
    turnRate = 0
    fullTurnRate = 0

    #retop konstanten
    retOpKonstant = 1.82
    retHenKonstant = 1.8

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
        self.fullDrive = 175
        self.turnRate = 32
        self.fullTurnRate = 65

       ## SDV med procentvise værdier til turnrates
      #  self.turnRate = (150/32) * self.fullDrive
        
      #  self.fullTurnRate = (150/65) * self.fullDrive

    def autodrive(self, stopTime=False):
        """
        AutoDrive-funktion
        stopTime er et countdown, hvor autoDrive stopper når tiden løber ud.
        stopTime er slået fra som default.
        """
        autoDriveWatch = StopWatch()

        while autoDriveWatch.time() < (stopTime * 1000) or stopTime == False:    
        #while True:
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
        robot.stop()


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

            if right != color and left != color:
                robot.drive((dir * self.fullDrive), 0)
            else:
                robot.stop()
                break


    def Kalibrering(self):
        #Kalibrering i starten
        greyLine = (leftColor.reflection() + rightColor.reflection())/2
        robot.straight(70)
        whiteLine = (leftColor.reflection() + rightColor.reflection())/2
        maskine.turn(-90)

        self.threshold = (greyLine + whiteLine) / 2.2      # Gennemsnittet mellem grå og hvid
        self.blackThreshold = (greyLine / 3) + 10
        
    
    def retOp(self):
        wait(300)
        maskine.straight_until_color("Grey")
        ev3.speaker.beep()

        retOpWatch = StopWatch()
        
        hasLeftHit = False
        hasRightHit = False
        leftTime = 0
        rightTime = 0

        #Kør frem indtil BEGGE sensorer har set sort!
        while hasLeftHit == False or hasRightHit == False:
            robot.drive(-10, 0)
            if leftColor.reflection() < self.blackThreshold and hasLeftHit == False:
                hasLeftHit = True
                print("LEFT HAS HIT at", retOpWatch.time())
                leftTime = retOpWatch.time()
                ev3.speaker.beep()

            if rightColor.reflection() < self.blackThreshold and hasRightHit == False:
                hasRightHit = True
                print("RIGHT HAS HIT at", retOpWatch.time())
                rightTime = retOpWatch.time()
                ev3.speaker.beep()
        
        robot.stop()
        ev3.light.on(Color.RED)
        ev3.speaker.beep()

        timeDifference = leftTime - rightTime
        print("Right Time: ", rightTime)
        print("Left Time: ", leftTime)
        print("The time difference is: ", timeDifference," ms")

        angle = timeDifference/100 * -1 * self.retOpKonstant
        distance = timeDifference/100 * self.retHenKonstant
        print("Angle = ", angle, ". Distance =", distance)
        robot.straight(abs(distance))
        maskine.turn(angle)
        wait(50)

    def openklo(self):
        klo.run_until_stalled(200, duty_limit=40)
        wait(100)
        klo.run_time(-100, 50)
        wait(200)
        ev3.speaker.beep()

    def closeklo(self):
        #klo.run_until_stalled(-200, duty_limit=80)
        #klo.dc(-30)
        klo.run_until_stalled(-300, then=Stop.HOLD, duty_limit=85)

    def flaske(self):
        while Ultra.distance() > 100:
            robot.drive(-120, 0)
            print(Ultra.distance())
        robot.stop()
        robot.straight(-70)
        maskine.closeklo()

    def BottleFinder(self):
        """Search and Find Flaske"""
        maxAngle = 50                   #SKAL ÆNDRES ved testning
        
        flaskeFundet = False

        if Ultra.distance() < self.flaskeAfstand:
            flaskeFundet = True

        if flaskeFundet == False:           #Scan til højre
            robot.reset()                   #Resetter vinklen til angle()
            robot.drive(0, 50)              #Ligesom self.turn(10) men asynkront og konstant
            while self.angle() < maxAngle:
                ev3.screen.clear()
                ev3.screen.draw_text(0, 20, self.angle())

                if Ultra.distance() < self.flaskeAfstand:
                    maskine.turn(15)
                    flaskeFundet = True
                    break
        robot.stop()
        
        if flaskeFundet == False:           #Søg til venstre hvis ikke fundet til højre
            self.turn(-self.angle())        #TIlbage til midterpunktet
            wait(500)
            robot.reset()
            robot.drive(0, -50)

            while self.angle() > -maxAngle:
                ev3.screen.clear()
                ev3.screen.draw_text(0, 20, self.angle())
    
                if Ultra.distance() < self.flaskeAfstand:
                    maskine.turn(-15)
                    flaskeFundet = True
                    break
        
        robot.stop()

        ev3.light.on(Color.RED)
        ev3.speaker.beep()
        wait(1000)
        ev3.light.on(Color.GREEN)


        robot.reset()
        while Ultra.distance() < self.flaskeAfstand:
            print(Ultra.distance())
            robot.drive(0,10)
        robot.stop()
        ra = self.angle()
        maskine.turn(-ra)
        ev3.speaker.beep()

        wait(500)
        robot.reset()
        while Ultra.distance() < self.flaskeAfstand:
            robot.drive(0,-10)
        robot.stop()
        la = self.angle()

        maskine.turn(-(la - (ra+la)/2))
        maskine.turn(4)

        
#7.95 Volt - mathias 1


################## MUSIK ####################
class Music():
    def threadMusic(self, fileName):
        ev3.speaker.set_volume(100)
        ev3.speaker.play_file("music/" + fileName + ".rsf")
    
    def PlayAsyncMusic(self, musicTitle):
        t = Thread(target=self.threadMusic, args=(musicTitle,))
        t.start()
        wait(1)             #Wait, else the motors speeds up

##############################################



#----------------------------START----------------------------
maskine = Maskine()
music = Music()
maskine.sdv()
robot.settings(maskine.fullDrive)       #Set robot.straight() 's speed

maskine.closeklo()
maskine.Kalibrering()


opgaver.opgave1(ev3, maskine, robot, music)

opgaver.opgave2(ev3, maskine, robot, music)
opgaver.opgave3(ev3, maskine, robot, music)
opgaver.opgave4(ev3, maskine, robot, music, rightColor)
opgaver.opgave5(ev3, maskine, robot, music, Ultra)        #MÅLSKIVE SKIPPET
opgaver.opgave6(ev3, maskine, robot, music)

opgaver.opgave7(ev3, maskine, robot, music, Ultra)
opgaver.opgave8(ev3, maskine, robot, music)

opgaver.opgave9(ev3, maskine, robot, music)
