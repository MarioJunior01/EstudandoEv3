#!/usr/bin/env python3

# Import the necessary libraries
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
motorA = Motor(Port.A)
motorB = Motor(Port.B)
left_motor = motorA
right_motor = motorB
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)
robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
 
sensor_cor = ColorSensor(Port.S1)
sensor_Ir = UltrasonicSensor(Port.S2)

def andar():
     motorA.run(600)
     motorB.run(600)
     return True

def parar():
     motorA.stop()
     motorB.stop()
     return True

def virarDireita(ativo):
      ativo = ativo
      motorA.run(-300)  
      return ativo

def virarEsquerda(ativo):
      ativo = ativo
      motorB.run(-300)
      return ativo


while True:
     andar()
     ativo= True
     distancia = sensor_Ir.distance()
     print(distancia)
    
     
     if distancia < 30:
          wait(100)
          virarDireita(ativo)
         # if virarDireita(ativo)==True:
          #   wait(200)
           #  virarEsquerda(ativo)
  
wait(100)
# Here is where your code starts


