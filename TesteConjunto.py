#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, InfraredSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()
motorA = Motor(Port.C)
motorB = Motor(Port.B)
sensor_Ir = InfraredSensor(Port.S3)
sensor_corEs = ColorSensor(Port.S1)
sensor_corDr = ColorSensor(Port.S2)


velocidade = 300
velocidade_curva = 200
distancia_obstaculo = 15
ultima_correcao="centro"


desviando = False


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
    motorA.run(-vel)

def curvaSuaveDireita():
    
    motorA.run(velocidade)
    motorB.run(velocidade * 0.3)

def curvaSuaveEsquerda():
    
    motorA.run(velocidade * 0.3)
    motorB.run(velocidade)

def desviarObj():
    global desviando
    desviando = True
    ev3.screen.draw_text(20, 20, "Entrando no While", text_color=Color.BLACK, background_color=None)
    ev3.screen.clear()
    ev3.speaker.beep()  
    while desviando == True:
     corDr = sensor_corDr.color()
     corEs = sensor_corEs.color()
     virarDireita()
     wait(600)
    
     ev3.screen.draw_text(20, 20, "Cor Branca", text_color=Color.BLACK, background_color=None)
     andar()
     wait(2000)
     
    
     virarEsquerda()
     wait(700)
    
    
     andar()
     wait(2000)
     
     
     virarEsquerda()
     wait(800)
     while corDr != Color.BLACK or corEs != Color.BLACK:
        andar()
        corDr = sensor_corDr.color()
        corEs = sensor_corEs.color()
        parar()
        wait(3000)         
     if corDr == Color.BLACK or corEs == Color.BLACK:
         ev3.screen.clear()
         ev3.screen.draw_text(20, 20, "Cor Preta", text_color=Color.BLACK, background_color=None)
         ev3.speaker.beep(900) 
         parar()
         desviando = False
        break
    
     andar()
     wait(1000)
    
     virarDireita()
     wait(1000) 

     andar()
     
     wait(1000)
     desviando = False

def seguirLinha():
     global ultima_correcao 
     
     corDr = sensor_corDr.color()
     corEs = sensor_corEs.color()
    
    

     if corEs == Color.BLACK and corDr == Color.BLACK:
       
        andar()
        ultima_correcao = "centro"
        
     elif corEs == Color.WHITE and corDr == Color.BLACK:
       
        curvaSuaveDireita()
        ultima_correcao = "direita"
        
     elif corEs == Color.BLACK and corDr == Color.WHITE:
       
        curvaSuaveEsquerda()
        ultima_correcao = "esquerda"
        
     elif corEs == Color.WHITE and corDr == Color.WHITE:
       
        if ultima_correcao == "direita":
            virarEsquerda()
            wait(150)
        elif ultima_correcao == "esquerda":
            virarDireita()
            wait(150)
    
        parar()
        

while True:
    if desviando == False:
         distanciaObj = sensor_Ir.distance()
        
         if distanciaObj <= distancia_obstaculo:
             parar()
             desviarObj()
         else:
             seguirLinha()
    
    wait(10)
