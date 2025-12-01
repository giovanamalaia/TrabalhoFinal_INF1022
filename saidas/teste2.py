from funcoes import *

# Dispositivos declarados:
# Dev: Monitor
# Dev: Celular
# Dev: Termometro (sensor: temperatura)
potencia = 0 # Inicialização automática
temperatura = 0 # Inicialização automática

if temperatura > 30:
    difundir(['Monitor', 'Celular'], "Temperatura em ", temperatura)