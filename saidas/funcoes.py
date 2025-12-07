# Giovana Malaia Pinheiro - 2312080
# Gabriele Sequeira - 2310202


def ligar(id_device):
    print(f"{id_device} ligado!")

def desligar(id_device):
    print(f"{id_device} desligado!")

def alerta(id_device, msg, var=None):
    print(f"{id_device} recebeu o alerta:\n")
    if var is None:
        print(msg)
    else:
        print(f"{msg} {var}")  #concatenação com espaço em branco

def difundir(lista_devices, msg, var=None):
    for dev in lista_devices:
        alerta(dev, msg, var)