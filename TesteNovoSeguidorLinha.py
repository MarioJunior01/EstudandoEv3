#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, InfraredSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait


ev3 = EV3Brick()
motorA = Motor(Port.A)
motorB = Motor(Port.B)
sensor_Ir = InfraredSensor(Port.S3)
sensor_corEs = ColorSensor(Port.S1)
sensor_corDr = ColorSensor(Port.S2)


velocidade = 300
velocidade_curva = 200
distancia_obstaculo = 5
desviando = False

# PID variáveis globais
integral = 0
erro_anterior = 0

# Calibração simples
PRETO = 10
BRANCO = 90
ALVO = (PRETO + BRANCO) / 2


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

def re():
    motorA.run(-velocidade_curva)
    motorB.run(-velocidade_curva)

# Desviar obstáculo
def desviarObj():
    global desviando
    desviando = True
    re()
    wait(500)
    virarEsquerda()
    wait(1300)
    
    corDr = sensor_corDr.color()
    corEs = sensor_corEs.color()
    while corDr != Color.BLACK or corEs != Color.BLACK:
        motorA.run(velocidade)        
        motorB.run(velocidade * 0.6)
        wait(100)
        corDr = sensor_corDr.color()
        corEs = sensor_corEs.color()
        
        if corDr == Color.BLACK or corEs == Color.BLACK:
            parar()
            wait(500)
            ev3.speaker.beep(400)
            andar()
            wait(200)
            virarEsquerda()
            wait(1000)
            desviando = False
            break

# Seguir linha com PID
def seguirLinha():
    global integral, erro_anterior

    # Lê valores de reflexão dos sensores (0 = preto, 100 = branco)
    corDr = sensor_corDr.reflection()
    corEs = sensor_corEs.reflection()
     
    erroEs = corEs-ALVO
    erroDr = corDr - ALVO
    
    # Calcula erro (diferença entre os erros dos sensores em relacao ao alvo)
    erro = erroEs - erroDr
    erro_abs = abs(erro)

    # PID clássico
    proporcional = erro 
    integral += erro
    derivativo = erro - erro_anterior
    erro_anterior = erro

    # --- AJUSTE DINÂMICO ---
    # Reduz velocidade se estiver muito fora da linha
    # Ex: erro alto → velocidade menor
    vel_base = velocidade - erro_abs * 2
    vel_base = max(150, min(vel_base, velocidade))  # limita entre 150 e velocidade normal

    # Ajusta ganhos do PID dinamicamente
    # Quanto maior o erro, mais forte a correção (Kp e Kd aumentam)
    Kp = 1.2 + (erro_abs * 0.05)   # aumenta conforme curva basicamente é a força da curva
    Ki = 0.001                     # pequeno para evitar acumulação ou seja ele tenta estabilizar na linha
    Kd = 0.08 + (erro_abs * 0.02)  # deixa o movimento mais suave 

    # Calcula correção PID
    correcao = Kp * proporcional + Ki * integral + Kd * derivativo

    # Calcula velocidades dos motores
    velA = vel_base + correcao
    velB = vel_base - correcao

    # Limita velocidades para segurança
    velA = max(-400, min(400, velA))
    velB = max(-400, min(400, velB))

    # Executa motores
    motorA.run(velA)
    motorB.run(velB)

# Loop principal
while True:
    if not desviando:
        distanciaObj = sensor_Ir.distance() 
        if distanciaObj <= distancia_obstaculo:
            parar()
            desviarObj()
        else:
            seguirLinha()
    wait(10)
