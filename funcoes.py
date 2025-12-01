# Funções exigidas no trabalho 

def ligar(id_device):
    print(f"{id_device} ligado!")

def desligar(id_device):
    print(f"{id_device} desligado!")

def alerta(id_device, msg, var=None):
    print(f"{id_device} recebeu o alerta:\n")
    if var is None:
        print(msg)
    else:
        # Concatenação com espaço em branco
        print(f"{msg} {var}") 

def difundir(lista_devices, msg, var=None):
    for dev in lista_devices:
        alerta(dev, msg, var)