
import time
import requests
from bs4 import BeautifulSoup

# Pesos dos sinais
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

# Simulação de sinais detectados
def detectar_sinais():
    return ["volume", "rompimento_tecnico", "baleias"]

# Cálculo da nota OLIMPO
def calcular_nota(sinais, pesos):
    return round(sum(pesos.get(s, 0) for s in sinais), 2)

# Loop principal
while True:
    print("Iniciando varredura...")
    sinais = detectar_sinais()
    nota = calcular_nota(sinais, pesos)
    print(f"Sinais detectados: {sinais}")
    print(f"Nota OLIMPO: {nota}")
    if nota >= 8.0:
        print(">>> ALERTA: Entrada recomendada.")
    elif nota >= 7.5:
        print(">>> Alerta moderado: Acompanhar.")
    else:
        print("Sem entrada válida.")
    print("-" * 40)
    time.sleep(60)  # Aguarda 1 minuto antes da próxima varredura
