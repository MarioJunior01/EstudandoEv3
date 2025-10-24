#!/usr/bin/env python3

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait 


ev3 = EV3Brick()
motor_Es = Motor(Port.A)
motor_Dr = Motor(Port.B)
sensor_corEs = ColorSensor(Port.S1)
sensor_corDr = ColorSensor(Port.S2)
sensor_Ir = UltrasonicSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S4)


def andar():
    motor_Es.run(300)
    motor_Dr.run(300)

def parar():
    motor_Es.stop()
    motor_Dr.stop()

def virarEsquerda():
    motor_Es.run_angle(-300, 90, then=Stop.HOLD, wait=100)
    motor_Dr.run_angle(300, 90, then=Stop.HOLD, wait=100)

def virarDireita():
    motor_Es.run_angle(300, 90, then=Stop.HOLD, wait=100)
    motor_Dr.run_angle(-300, 90, then=Stop.HOLD, wait=100)


def seguir_linha():
    while True:
        corEs = sensor_corEs.color()
        corDr = sensor_corDr.color()

        
        if corEs == Color.BLACK and corDr == Color.BLACK:
            andar()

       
        elif corEs == Color.WHITE and corDr == Color.BLACK:
            parar()
            virarDireita()
            wait(100)
            andar()

     
        elif corEs == Color.BLACK and corDr == Color.WHITE:
            parar()
            virarEsquerda()
            wait(100)
            andar()

       
        else:
            parar()
           
            motor_Es.run(150)
            motor_Dr.run(-150)
            wait(100)

        wait(10)  

ev3.speaker.beep()
seguir_linha()
