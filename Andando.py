#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
motor_Dr = Motor(Port.C)
motor_Es = Motor(Port.B)  
sensor_Ir = InfraredSensor(Port.S3)
sensor_corDr = ColorSensor(Port.S1)
sensor_corEs = ColorSensor(Port.S2)

virarEsquerda = None
desviar = None

def andar():
    motor_Es.run(300)
    motor_Dr.run(300)

def parar():
    motor_Dr.stop()
    motor_Es.stop()

def virarEsquerda():
    motor_Es.run_angle(300, 30, then=Stop.HOLD, wait=True)  

def virarDireita():
    motor_Dr.run_angle(300, 30, then=Stop.HOLD, wait=True)    

while desviar == False:
    andar()
    
    distancia = sensor_Ir.distance()
    if distancia <= 30: 
        virarEsquerda()
        virarEsquerda = True
        if virarEsquerda == True:
            wait(500)
            virarDireita()  
        else:
            virarEsquerda = False
            desviar = True

wait(100)  


while True:
    corDr = sensor_corDr.color()
    corEs = sensor_corEs.color()
    
    if corDr == Color.BLACK:
        andar()
   
    else:
        if corEs == Color.BLACK:
         parar()
         virarEsquerda()
         wait(100)
         andar() 

wait(100)
