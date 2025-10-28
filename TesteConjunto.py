from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()
motorA = Motor(Port.A)
motorB = Motor(Port.B)
sensor_Ir = UltrasonicSensor(Port.S3)
sensor_corEs = ColorSensor(Port.S1)
sensor_corDr = ColorSensor(Port.S2)

# Configurações ajustáveis
velocidade = 300
velocidade_curva = 200
distancia_obstaculo = 20
tempo_verificacao = 10  # ms

# Controle de estado
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
    motorA.run(-vel)

def curvaSuaveDireita():
    # Curva mais suave - motor direito mais lento
    motorA.run(velocidade)
    motorB.run(velocidade * 0.3)

def curvaSuaveEsquerda():
    # Curva mais suave - motor esquerdo mais lento
    motorA.run(velocidade * 0.3)
    motorB.run(velocidade)

def desviarObj():
    global desviando
    desviando = True
    
    ev3.speaker.beep()  # Aviso sonoro
    
    # Curva 1 - direita
    virarDireita()
    wait(600)
    
    # Andar reto contornando obstáculo
    andar()
    wait(1500)
    
    # Curva 2 - esquerda
    virarEsquerda()
    wait(600)
    
    # Andar reto
    andar()
    wait(1900)
    # Curva 3 - esquerda
    virarEsquerda()
    wait(600)
    
    # Andar reto
    andar()
    wait(1200)
    
    # Curva 4 - direita para realinhar
    virarDireita()
    wait(600)
    
    parar()
    desviando = False

def seguirLinha():
    global ultima_correcao
    
    corDr = sensor_corDr.color()
    corEs = sensor_corEs.color()
    
    # Debug no display
    ev3.screen.clear()
    ev3.screen.draw_text(10, 10, f"Esq: {corEs}")
    ev3.screen.draw_text(10, 30, f"Dir: {corDr}")
    
    # Lógica melhorada de seguimento
    if corEs == Color.BLACK and corDr == Color.BLACK:
        # Ambos na linha - seguir reto
        andar()
        ultima_correcao = "centro"
        
    elif corEs == Color.WHITE and corDr == Color.BLACK:
        # Esquerda saiu da linha - curva suave à direita
        curvaSuaveDireita()
        ultima_correcao = "direita"
        
    elif corEs == Color.BLACK and corDr == Color.WHITE:
        # Direita saiu da linha - curva suave à esquerda
        curvaSuaveEsquerda()
        ultima_correcao = "esquerda"
        
    elif corEs == Color.WHITE and corDr == Color.WHITE:
        # Ambos fora da linha - estratégia de recuperação
        if ultima_correcao == "direita":
            virarEsquerda()
            wait(150)
        elif ultima_correcao == "esquerda":
            virarDireita()
            wait(150)
        else:
            # Busca padrão - girar até encontrar linha
            virarDireita()
            wait(300)
        parar()
        
    else:
        # Para cores não mapeadas, seguir reto
        andar()

while True:
    if not desviando:
        distanciaObj = sensor_Ir.distance()
        
        if distanciaObj <= distancia_obstaculo:
            parar()
            desviarObj()
        else:
            seguirLinha()
    
    wait(tempo_verificacao)
