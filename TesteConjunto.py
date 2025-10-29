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
    
    ev3.speaker.beep()  
    
    virarDireita()
    wait(600)
    
    
    andar()
    wait(2000)
    
    
    virarEsquerda()
    wait(700)
    
    
    andar()
    wait(2000)
    
    virarEsquerda()
    wait(600)
   
    while corEs!= Color.BLACK and  corDr != Color.BLACK:
       corDr = sensor_corDr.color()
       corEs = sensor_corEs.color()
       andar()
       wait(1000)
      
      
     
       if corDr == Color.BLACK or corEs == Color.BLACK:
         ev3.speaker.beep(1000)  
         main()
         
        
 
    
    
    
    andar()
    wait(2000)
    
    virarDireita()
    wait(1000) 
    
    andar()
    
    
        

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
        
def main ():
 while True:
    if desviando == False:
         distanciaObj = sensor_Ir.distance()
        
         if distanciaObj <= distancia_obstaculo:
             parar()
             desviarObj()
         else:
             seguirLinha()
    
    wait(10)

main()
