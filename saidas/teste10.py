from funcoes import *

# Dispositivos declarados:
# Dev: Termometro (sensor: temperatura)
# Dev: Ventilador (sensor: potencia)
# Dev: Celular
potencia = 0 # Inicialização automática
temperatura = 0 # Inicialização automática

temperatura = 35
potencia = 0
if temperatura > 30 and potencia == 0:
    ligar("Ventilador")
if temperatura < 20:
    desligar("Ventilador")
else:
    alerta("Celular", "Temperatura segue alta:", temperatura)