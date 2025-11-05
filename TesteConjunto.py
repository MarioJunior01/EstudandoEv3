#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor,InfraredSensor,ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()
motorA = Motor(Port.C)
motorB = Motor(Port.B)
sensor_Ir = InfraredSensor(Port.S3)
sensor_corEs = ColorSensor(Port.S4)
sensor_corDr = ColorSensor(Port.S2)


velocidade = 300
velocidade_curva = 200
distancia_obstaculo = 15



desviando = False
ultima_correcao = "centro"

def andar(vel=velocidade):
    motorA.run(vel)
    motorB.run(vel)

def parar():
    motorA.stop()
    motorB.stop()
    wait(200)

def virarDireita(vel=velocidade_curva):
    motorA.run(vel)
    motorB.run(-vel)

def virarEsquerda(vel=velocidade_curva):
    motorB.run(vel)
    motorA.run(-vel* 0.3)

def curvaSuaveDireita():
  
    motorA.run(velocidade)
    motorB.run(velocidade * 0.3)

def curvaSuaveEsquerda():
    
    motorA.run(velocidade * 0.3)
    motorB.run(velocidade)
    
    
def re():
    motorA.run(-velocidade_curva)
    motorB.run(-velocidade_curva)

def desviarObj():
     global desviando
     desviando = True
     re()
     wait(500) 
    
    
     virarEsquerda()
     wait(2000)
    
     corDr = sensor_corDr.color()
     corEs = sensor_corEs.color()
     while corDr != Color.BLACK or corEs != Color.BLACK:
         motorA.run(velocidade)        # Roda esquerda mais rápida
         motorB.run(velocidade * 0.6)  # Roda direita mais lenta
         wait(100) 
        

         corDr = sensor_corDr.color()
         corEs = sensor_corEs.color()
        

         if corDr == Color.BLACK or corEs == Color.BLACK:
             parar()
             desviando = False
             break
     parar()

def seguirLinha():
     global ultima_correcao 
     sensorDireitoCor= "Direito"
     sensor_corEr= "Esquerdo"
     corDr = sensor_corDr.color()
     corEs = sensor_corEs.color()
     if corEs == Color.BLACK and corDr == Color.BLACK:
        
        andar()
        ultima_correcao = "centro"
        ev3.screen.draw_text(20,20, ultima_correcao)
        ev3.screen.clear()
        ev3.screen.draw_text(20, 20, "Es{}" .format(corEs))
        ev3.screen.draw_text(40, 30, "Dr{}" .format(corDr))


     elif corEs == Color.WHITE and corDr == Color.BLACK:
       
        curvaSuaveDireita()
        ultima_correcao = "direita"
        ev3.screen.draw_text(20,20, ultima_correcao)
        ev3.screen.clear()
        ev3.screen.draw_text(20, 20, "Es{}" .format(corEs))
        ev3.screen.draw_text(40, 30, "Dr{}" .format(corDr))
        
     elif corEs == Color.BLACK and corDr == Color.WHITE:
       
        curvaSuaveEsquerda()
        ultima_correcao = "esquerda"
        ev3.screen.draw_text(20,20, ultima_correcao)
        ev3.screen.clear()
        ev3.screen.draw_text(20, 20, "Es{}" .format(corEs))
        ev3.screen.draw_text(40, 30, "Dr{}" .format(corDr))
        
     elif corEs == Color.WHITE and corDr == Color.WHITE:
       
        if ultima_correcao == "direita":
            virarEsquerda()
            wait(150)
        elif ultima_correcao == "esquerda":
            virarDireita()
            wait(150)
    
while True:
    if not desviando:
        distanciaObj = sensor_Ir.distance()
        
        if distanciaObj <= distancia_obstaculo:
            parar()
            desviarObj()
        else:
            seguirLinha()
    
    wait(10)
