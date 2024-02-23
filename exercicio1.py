import math
import random

# Gerando pontos iniciais e finais da reta com valores aleatórios
x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
contador = 0

def resultado(x1, y1, x2,y2):
    global contador
# Cálculo do ângulo de inclinação usando a fórmula tan(θ) = (y2 - y1) / (x2 - x1)
    try:
        angulo_inclinacao = math.atan((y2 - y1) / (x2 - x1))
        angulo_graus = math.degrees(angulo_inclinacao)  # Convertendo o ângulo para graus
        print("{} - O ângulo de inclinação da reta que passa pelos pontos ({},{}) e ({},{}) é {:.2f} graus".format(contador,x1,y1,x2,y2,angulo_graus))
        x2 = random.randint(-10, 10)  # Gerando um novo valor aleatório para x2
        contador += 1
        return resultado(x1, y1, x2,y2)

    except ZeroDivisionError:
        print("Erro: O numero é inválido")
        
while True:
    resultado(x1,y1,x2,y2)
        