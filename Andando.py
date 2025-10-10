from pybricks.hubs import EV3Brick
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *
from pybricks.ev3devices import Motor,UltrasonicSensor
from pybricks.tools import wait
from pybricks.parameters import *
from pybricks.robotics import *


ev3 = EV3Brick()
motorA = Motor(OUTPUT_A)
motorB = Motor(OUTPUT_B)
sensor_Ur = UltrasonicSensor(Port.S2)

tempo = 0

while True:
      distancia = sensor_Ur.distance() / 10
      print(distancia)
      
      if distancia < 10:
          wait(100)
          motorA.stop()
          motorB.stop()
          ev3.screen.print("Objeto na frente ")
          ev3.speaker.beep(200, 200)  # tom grave prolongado de 600 ms
          wait(100)
          ev3.speaker.beep(100, 400) 
          break
      else:
         motorA.run(500)
         motorB.run(500)
        
      if tempo == 9000:
         ev3.screen.print("------>")
         motorA.stop()
        
      if tempo == 15000:
         motorB.stop()
         ev3.screen.print("------>")
        
      if tempo == 20000:
         motorA.stop()
         motorB.stop()
         ev3.speaker.beep(500, 200)  
         wait(100)
         ev3.speaker.beep(200, 400)
         ev3.screen.print("---Fim----")
         break
        
      tempo = tempo+1000
      wait(1000)
    
wait(50)

