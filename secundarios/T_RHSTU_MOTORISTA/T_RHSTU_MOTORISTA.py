import secundarios.T_RHSTU_MOTORISTA.aleatorioMotorista as aleatorioMotorista
import csv
import datetime as dt
hoje = dt.date.today()
ListaMotoristas=[]


def T_RHSTU_MOTORISTA(id_func,nr_crm,nm_categoria_cnh,dt_validade_cnh,dt_cadastro,nm_usuario):
    motorista = {}
    motorista['ID_FUNC'] = id_func #PF
    motorista['NR_CRM'] = nr_crm
    motorista['NM_CATEGORIA_CNH'] = nm_categoria_cnh
    motorista['DT_VALIDADE_CNH'] = dt_validade_cnh
    motorista['DT_CADASTRO'] = dt_cadastro
    motorista['NM_USUARIO'] = nm_usuario
    return motorista 

print("iniciando T_RHSTU_MOTORISTA")


for i in range(len(aleatorioMotorista.listaMotoristas)):
            idFunc = aleatorioMotorista.listaMotoristas[i]
            nrCRM =aleatorioMotorista.CRM()
            nmCategoriaCNH =aleatorioMotorista.carteiraMotorista()
            dtValidadeCNH =aleatorioMotorista.dataValidade(aleatorioMotorista.idades())
            dtCadastro = hoje
            nmUsuario = "Miron"




 

            motorista = T_RHSTU_MOTORISTA(id_func=idFunc,nr_crm=nrCRM,nm_categoria_cnh=nmCategoriaCNH,dt_validade_cnh=dtValidadeCNH,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaMotoristas.append(motorista)
with open('T_total\\T_RHSTU_MOTORISTA.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaMotoristas[0].keys())
        csv_writer.writeheader()
        for line in ListaMotoristas:
            csv_writer.writerow(line)                 

print("T_RHSTU_MOTORISTA finalizada")
