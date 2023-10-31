import csv
import random

with open('T_total\\T_RHSTU_PLANO_SAUDE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPlanoSaude = list(reader)

def idsPlanoSaudePacientes(lista):
    idsPlanoSaude=[]
    lista = lista
    c=1
    while c < len(lista):
            idsPlanoSaude.append(lista[c][0])
            c+=1
    pos = random.randint(0, (len(idsPlanoSaude)-1))
    return idsPlanoSaude[pos]





def codPlanoSaude():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 15:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
        
    return num                      
    

        
def idades():
    pos = random.randint(1, 15)
    return pos

def dataInicio(idade):
        anoNascimento = 2023 - idade
        anoNascimento = str(anoNascimento)
        data = anoNascimento + "-"
        mes = random.randint(1,12)
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            mes = str(mes)
            data = data + mes + "-"
            dia = random.randint(1,31)
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            mes = str(mes)
            data = data + mes + "-"
            dia = random.randint(1,30)
        elif mes == 2:
             mes = str(mes)
             data = data + mes + "-"
             dia = random.randint(1,28)
        
        dia = str(dia)
        data = data + dia
        return data




  
