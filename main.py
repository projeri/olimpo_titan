
import time
import random

# Pesos simulados
pesos = {
    "volume": 2.5,
    "rompimento_tecnico": 3.0,
    "sentimento": 1.5,
    "baleias": 2.5,
    "risco_adaptativo": 1.5,
    "multi_sinal": 1.0,
    "manipulacao": -5.0,
    "macro_ciclo": 1.0,
    "cluster_institucional": 2.0,
    "divergencia_rsi": 2.0,
    "bos": 2.5,
    "fibonacci": 1.5,
    "squeeze": 2.0
}

def detectar_sinais():
    # Simula entre 2 a 5 sinais aleatórios por ciclo
    return random.sample(list(pesos.keys()), random.randint(2, 5))

def calcular_nota(sinais, pesos):
    return round(sum(pesos.get(s, 0) for s in sinais), 2)

print("Sistema OLIMPO iniciado com sucesso...")
while True:
    sinais = detectar_sinais()
    nota = calcular_nota(sinais, pesos)
    print(f"[OLIMPO] Sinais detectados: {sinais}")
    print(f"[OLIMPO] Nota calculada: {nota}")
    if nota >= 8.0:
        print(">>> ALERTA: Entrada recomendada!")
    elif nota >= 7.5:
        print(">>> Alerta moderado: Acompanhar.")
    else:
        print("Sem entrada válida.")
    print("-" * 50)
    time.sleep(60)
