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

tempo = 0


while True:
      distancia = sensor_Ir.distance()
      print(distancia)
      
      if distancia < 20:
          wait(100)
          
          motorB.stop()
          
          ev3.screen.print("Objeto na frente ")
          ev3.speaker.beep(570)  
          wait(100)
          ev3.speaker.beep(410)
          motorB.stop()



      
      else:
         motorA.run(200)
         motorB.run(200)
        
      if tempo == 9000:
         ev3.screen.print("------>")
         motorA.stop()
        
      if tempo == 15000:
         motorB.stop()
         ev3.screen.print("<------")
        
       
        
      tempo = tempo+1000
      wait(1000)
    
wait(50)

