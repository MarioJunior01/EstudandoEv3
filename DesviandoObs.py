from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait 

ev3 = EV3Brick()
motorA = Motor(Port.A)
motorB = Motor(Port.B)
sensor_Ur = UltrasonicSensor(Port.S3)
sensor_corEs = ColorSensor(Port.S1)
sensor_corDr = ColorSensor(Port.S2)



velocidade = 300


def andar():
     motorA.run(velocidade)
     motorB.run(velocidade)

def parar():
     motorA.stop()
     motorB.stop()
     wait(500)  

def virarDireita():
     motorA.run(velocidade)
     motorB.run(-velocidade)
     
def virarEsquerda():
     motorB.run(velocidade)
     motorA.run(-velocidade)

def desviarObj():
     #curva 1
     virarDireita()
     wait(700)  
     parar()
     
     andar()
     wait(1500)  
     parar()
     
      #curva 2
     virarEsquerda()
     wait(700)  
     parar()
     
     andar()
     wait(3500)  
     parar()
     
     #curva 3
     virarEsquerda()
     wait(700)
     parar()
     
     andar()
     wait(1000) 
     parar()
     #curva 4
     virarDireita()
     wait(700)
     parar()
    
def seguirLinha():
     colorSeguir = Color.BLACK
     while True:
         corSensor = sensor_corDr.color()
        
    
while True:
     distanciaObj = sensor_Ur.distance()
     
     if distanciaObj <= 20:
         parar()
         desviarObj()
     else:
         seguirLinha()
         
     wait(50)
