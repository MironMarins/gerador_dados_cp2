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



def CRM():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 9:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    return num
def especialidadesMedicas():
    especialidade=("Cardiologista","Ortopedia","Dermatologia","Oftalmologia","Neurologia",
    "Psiquiatria","Cirurgia Geral","Medicina Interna","Otorrinolaringologia","Endocrinologia")
    pos = random.randint(0, (len(especialidade)-1))
    return especialidade[pos]

