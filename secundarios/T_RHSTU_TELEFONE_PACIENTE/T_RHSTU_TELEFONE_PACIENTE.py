import secundarios.T_RHSTU_TELEFONE_PACIENTE.aleatorioTelefonePaciente as aleatorioTelefonePaciente
import csv
import datetime as dt
hoje = dt.date.today()
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)

ListaTelefonesPaciente=[]
repeticao = 2

def T_RHSTU_PACIENTE_TELEFONE_PACIENTE(id_paciente,id_telefone,nr_ddi,nr_ddd,nr_telefone,tp_telepone,st_telefone,dt_cadastro,nm_usuario):
    telefonePaciente = {}
    telefonePaciente['ID_PACIENTE'] = id_paciente #PF
    telefonePaciente['ID_TELEFONE'] = id_telefone #P
    telefonePaciente['NR_DDI'] = nr_ddi 
    telefonePaciente['NR_DDD'] = nr_ddd
    telefonePaciente['NR_TELEFONE'] = nr_telefone
    telefonePaciente['TP_TELEFONE'] = tp_telepone
    telefonePaciente['ST_TELEFONE'] = st_telefone
    telefonePaciente['DT_CADASTRO'] = dt_cadastro
    telefonePaciente['NM_USUARIO'] = nm_usuario
    return telefonePaciente 
print("iniciando T_RHSTU_PACIENTE_TELEFONE_PACIENTE")
i=1
while i < len(listaPacientes):
            idTelefone = i
            idPaciente = listaPacientes[i][0]
            nrDDI = "55"
            nrDDD =aleatorioTelefonePaciente.Ddd()
            nrTelefone = aleatorioTelefonePaciente.Tel()
            tpTelepone = aleatorioTelefonePaciente.tipoTel(nrTelefone)
            stTelefone = "A"
            dtCadastro =hoje
            nmUsuario ="Miron"
            i=i+1
            



            TelefonePaciente = T_RHSTU_PACIENTE_TELEFONE_PACIENTE(id_paciente=idPaciente,id_telefone=idTelefone,nr_ddi=nrDDI,nr_ddd=nrDDD,nr_telefone=nrTelefone,tp_telepone=tpTelepone,st_telefone=stTelefone,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaTelefonesPaciente.append(TelefonePaciente)
with open('T_total\\T_RHSTU_TELEFONE_PACIENTE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaTelefonesPaciente[0].keys())
        csv_writer.writeheader()
        for line in ListaTelefonesPaciente:
            csv_writer.writerow(line)
            
print("T_RHSTU_PACIENTE_TELEFONE_PACIENTE finalizado")

