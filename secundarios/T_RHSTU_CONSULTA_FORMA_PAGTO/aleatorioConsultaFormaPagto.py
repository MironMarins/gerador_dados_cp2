import csv
import random
#with open('primarios\\T_RHSTU_PACIENTE\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                #reader = csv.reader(csvfile)
                #listaPacientes = list(reader)
with open('T_total\\T_RHSTU_UNID_HOSPITALAR.csv',"r",encoding='utf-8') as csvfile:#
                reader = csv.reader(csvfile)
                listaUnidHospitalar = list(reader)
with open('T_total\\T_RHSTU_CONSULTA.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaConsulta = list(reader)
with open('T_total\\T_RHSTU_PACIENTE_PLANO_SAUDE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientesPS = list(reader)
with open('T_total\\T_RHSTU_FORMA_PAGAMENTO.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaFormaPagamento = list(reader)
#idConsultaFormaPagto= i
#idUnidHospital= #F
#idConsulta = #F
#idPacientePs = #F
#idFormaPagto = #F

def aleatorioFormaPagamento():
        pos = random.randint(1,len(listaFormaPagamento)-1)
        return int(listaFormaPagamento[pos][0])

def aleatorioStatusPagamento():
        status=["A","C","P"]
        pos = random.randint(0,len(status)-1)
        return status[pos]





#def aleatorioPacientePlanoSaude(numero):
        #if numero == 2:
        #posição lista, data consulta, 

print(listaConsulta[2][4])
cont=0
texto=""
data=""
for i in range(len(listaConsulta[1][4])):
    if listaConsulta[2][4][i] == "a":
           break
    texto=texto+listaConsulta[2][4][i]

texto = texto[5::]

for i in range(len(texto)):
    if texto[i] == "-":
        dia = texto[i+1:]
        mes = texto[:i]

ano = listaConsulta[i][4][:4]
ano = int(ano)






velhodia = int(dia)
velhomes = int(mes)


def dataPagamento(idade):
        anoNascimento = int(idade) + 1
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







#print(listaConsulta[1][4][:5])


#def planoSaudePaciente(pos):
    #numero = listaPacientesPS[pos][2]
    #return numero

