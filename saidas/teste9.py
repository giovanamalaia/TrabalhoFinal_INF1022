from funcoes import *

# Dispositivos declarados:
# Dev: Lampada
# Dev: ArCondicionado (sensor: temperatura)
# Dev: Janela (sensor: chuva)
# Dev: Sensor (sensor: luminosidade)
umidade = 0 # Inicialização automática
movimento = 0 # Inicialização automática
chuva = 0 # Inicialização automática
temperatura = 0 # Inicialização automática
potencia = 0 # Inicialização automática
luminosidade = 0 # Inicialização automática

temperatura = 28
luminosidade = 10
chuva = True
if temperatura > 25 and chuva == True:
    ligar("ArCondicionado")
if luminosidade > 50:
    desligar("Lampada")
else:
    alerta("Lampada", "Ambiente escuro, nivel:", luminosidade)