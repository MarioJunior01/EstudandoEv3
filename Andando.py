#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
motorA = Motor(Port.C)
motorB = Motor(Port.B)
sensor_Ir = InfraredSensor(Port.S3)
sensor_colorA = ColorSensor(Port.S1)
sensor_colorB = ColorSensor(Port.S2)
COR_PARAR = Color.BLACK 
motorA.run(300)
motorB.run(300)
while True:

    cor = sensor_colorA.color()

    if cor == COR_PARAR :
        ev3.screen.draw_text(0, 40, "Color BLACK ")
        ev3.screen.draw_text(0, 60, "Parando ")
        motorA.stop()  
        motorB.stop()
        ev3.speaker.beep(300,400)
        break
              
           
  
wait(100)