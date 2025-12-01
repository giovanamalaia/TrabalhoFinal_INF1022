from funcoes import *

# Dispositivos declarados:
# Dev: Monitor
# Dev: Higrometro (sensor: umidade)
umidade = 0 # Inicialização automática
movimento = 0 # Inicialização automática
potencia = 0 # Inicialização automática
temperatura = 0 # Inicialização automática

if umidade < 40:
    alerta("Monitor", "Ar seco detectado")