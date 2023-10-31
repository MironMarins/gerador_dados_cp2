import random
import csv
listaMedicos=[]
listaMotoristas=[]
listaFunc=[]
with open('T_total\\T_RHSTU_FUNCIONARIO.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaFuncionarios = list(reader)

i=1
while i< len(listaFuncionarios):
    func=listaFuncionarios[i][0]
    func=int(func)
    if func >=2999:           
        listaFunc.append(func)
    i=i+1 

med=0
mot=0
i=0
while i < len(listaFunc):
    if med <17:
        listaMedicos.append(listaFunc[i])
        med+=1
    elif med>=17 and med <20:
        listaMotoristas.append(listaFunc[i])
        med+=1
    elif med <=20:
        listaMedicos.append(listaFunc[i])
        med=1
    i=i+1
#for i in range(30):
    #print(listaMedicos[i])
#for i in range(7):
     #rint(listaMotoristas[i])


def CRM():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 9:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    return num

def idades():
    pos = random.randint(1, 5)
    return pos

def dataValidade(idade):
        anoNascimento = 2023 + idade
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

def carteiraMotorista():
     tipo=["D","E"]
     pos = random.randint(0, (len(tipo)-1))
     return tipo[pos]