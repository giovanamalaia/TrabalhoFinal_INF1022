from funcoes import *

# Dispositivos declarados:
# Dev: Monitor
# Dev: Celular (sensor: movimento)
# Dev: Higrometro (sensor: umidade)
# Dev: Lampada (sensor: potencia)
potencia = 0 # Inicialização automática
umidade = 0 # Inicialização automática
temperatura = 0 # Inicialização automática
movimento = 0 # Inicialização automática

potencia = 100
if umidade < 30:
    alerta("Monitor", "Ar seco detectado")
if movimento == True:
    ligar("Lampada")
else:
    desligar("Lampada")