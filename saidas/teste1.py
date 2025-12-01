from funcoes import *

# Dispositivos declarados:
# Dev: Termometro (sensor: temperatura)
# Dev: Ventilador (sensor: potencia)
temperatura = 0 # Inicialização automática
potencia = 0 # Inicialização automática

temperatura = 40
potencia = 90
if temperatura > 30:
    ligar("Ventilador")