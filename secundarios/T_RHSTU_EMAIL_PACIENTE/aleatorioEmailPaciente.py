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

def segundaletra(nome):
    for i in range(len(nome)):
        if  nome[i] == " ":
            segundaletra = nome[i+1]
            return segundaletra
    return nome

def servidoresEmail():
    servidores =("gmail.com","gmail.com.br","hotmail.com","ig.com.br","yahoo.com")
    pos = random.randint(0, (len(servidores)-1))
    return servidores[pos]

def tipoEmail():
    tipoEmail =("pessoal","profissional")
    pos = random.randint(0, (len(tipoEmail)-1))
    return tipoEmail[pos]



