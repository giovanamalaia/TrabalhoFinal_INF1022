from funcoes import *

# Dispositivos declarados:
# Dev: Termometro (sensor: temperatura)
# Dev: Ventilador
# Dev: Celular
potencia = 0 # Inicialização automática
temperatura = 0 # Inicialização automática

limite = 35
temperatura = 40
if temperatura > limite:
    alerta("Celular", "Limite variavel excedido!", temperatura)
alvo = 40
if temperatura == alvo:
    ligar("Ventilador")