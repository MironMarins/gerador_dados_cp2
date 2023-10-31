import random


def Tel():
    
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    chance = random.randint(0, (len(numeros)-1))
    if chance < 6:
        while i < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            i = i + 1
        num = "9"+ num 
    else:
        while i < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            i = i + 1
    return num


def tipoTel(numero):
    numero=int(numero)
    
    if numero // 100000000 !=9:
        telefone = "RESIDENCIAL"
    else:
        telefone="CELULAR"
    return telefone





def Ddd():
    numeros = ("11","12","13","14","15","16","17","18","19","21","22","24","27","28","31","32",
               "33","34","35","37","38","41","42","43","44","45","46","47","48","49","51","53","54","55","61","62",
               "63","64","65","66","67","68","69","71","73","74","75","77","79","81","82","83","84","85","86","87","88",
               "89","91","92","93","94","95","96","97","98","99")
    pos = random.randint(0, (len(numeros)-1))
    return numeros[pos]




