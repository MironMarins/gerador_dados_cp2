import csv
import random
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)
with open('T_total\\T_RHSTU_MEDICO.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaMedicos = list(reader)



def aleatorioMedico():
    pos =  random.randint(1, (len(listaMedicos)-1))
    return listaMedicos[pos][0]


def medicoPorUnidade(numero):
        numero = int(numero)
        if numero >= 2999 and numero <2999+1980:
                id = str(1)
        elif numero >= 2999+1980 and numero <2999+(1980*2):
                id = str(2)
        elif numero >= 2999+(1980*2) and numero <2999+(1980*3):
                id = str(3)
        elif numero >= 2999+(1980*3) and numero <2999+(1980*4):
                id = str(4)
        elif numero >= 2999+(1980*4) and numero <2999+(1980*5):
                id = str(5)
        elif numero >= 2999+(1980*5) and numero <2999+(1980*6):
                id = str(6)
        elif numero >= 2999+(1980*6) and numero <2999+(1980*7):
                id = str(7)
        elif numero >= 2999+(1980*7) and numero <2999+(1980*8):
                id = str(8)
        elif numero >= 2999+(1980*8) and numero <2999+(1980*9):
                id = str(9)
        elif numero >= 2999+(1980*9) and numero <2999+(1980*10):
                id = str(10)
        elif numero >= 2999+(1980*10) and numero <2999+(1980*11):
                id = str(11)
        elif numero >= 2999+(1980*11) and numero <2999+(1980*12):
                id = str(12)
        elif numero >= 2999+(1980*12) and numero <2999+(1980*13):
                id = str(13)
        elif numero >= 2999+(1980*13) and numero <2999+(1980*14):
                id = str(14)
        elif numero >= 2999+(1980*14) and numero <2999+(1980*15):
                id = str(15)
        elif numero >= 2999+(1980*15) and numero <2999+(1980*16):
                id = str(16)
        elif numero >= 2999+(1980*16) and numero <2999+(1980*17):
                id = str(17)
        elif numero >= 2999+(1980*17) and numero <2999+(1980*18):
                id = str(18)
        elif numero >= 2999+(1980*18) and numero <2999+(1980*19):
                id = str(19)
        elif numero >= 2999+(1980*19) and numero <2999+(1980*20):
                id = str(20)
        elif numero >= 2999+(1980*20) and numero <2999+(1980*21):
                id = str(21)
        elif numero >= 2999+(1980*21) and numero <2999+(1980*22):
                id = str(22)
        elif numero >= 2999+(1980*22) and numero <2999+(1980*23):
                id = str(23)
        elif numero >= 2999+(1980*23) and numero <2999+(1980*24):
                id = str(24)
        elif numero >= 2999+(1980*24) and numero <2999+(1980*25):
                id = str(25)
        elif numero >= 2999+(1980*25) and numero <2999+(1980*26):
                id = str(26)
        elif numero >= 2999+(1980*26):
                id = str(27)
        return id
            
def minutos():
        pos =random.randint(0, 59)
        return pos
def segundos():
        pos =random.randint(0, 59)
        return pos
def horas():
        pos = random.randint(0, 23)
        return pos
def consultorio():
    pos = random.randint(1, 150)
    return pos

def anos():
    pos = random.randint(0, 4)
    return pos

def dataAtendimento(idade):
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
        