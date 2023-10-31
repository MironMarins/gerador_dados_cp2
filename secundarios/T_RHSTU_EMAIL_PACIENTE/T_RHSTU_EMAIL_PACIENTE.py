import secundarios.T_RHSTU_EMAIL_PACIENTE.aleatorioEmailPaciente as aleatorioEmailPaciente
import csv
import datetime as dt
hoje = dt.date.today()
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)

ListaEmailsPaciente=[]
repeticao = 2

def T_RHSTU_PACIENTE_EMAIL_PACIENTE(id_paciente,id_email,ds_email,tp_email,st_email,dt_cadastro,nm_usuario):
    emailPaciente = {}
    emailPaciente['ID_PACIENTE'] = id_paciente #F
    emailPaciente['ID_TELEFONE'] = id_email #P
    emailPaciente['DS_EMAIL'] = ds_email
    emailPaciente['TP_EMAIL'] = tp_email
    emailPaciente['ST_EMAIL'] = st_email
    emailPaciente['DT_CADASTRO'] = dt_cadastro
    emailPaciente['NM_USUARIO'] = nm_usuario
    return emailPaciente 
print("iniciando T_RHSTU_PACIENTE_EMAIL_PACIENTE")
i=1
while i < len(listaPacientes):
            idPaciente = listaPacientes[i][0]
            idEmail = i
            dsEmail = listaPacientes[i][1][0]+aleatorioEmailPaciente.segundaletra(listaPacientes[i][1])+listaPacientes[i][4][2:4] + "@" + aleatorioEmailPaciente.servidoresEmail()
            tpEmail = aleatorioEmailPaciente.tipoEmail()
            stEmail = "A"
            dtCadastro = hoje
            nmUsuario = "Miron"
            i=i+1



            EmailPaciente = T_RHSTU_PACIENTE_EMAIL_PACIENTE(id_paciente=idPaciente,id_email=idEmail,ds_email=dsEmail,tp_email=tpEmail,st_email=stEmail,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaEmailsPaciente.append(EmailPaciente)
            
with open('T_total\\T_RHSTU_EMAIL_PACIENTE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaEmailsPaciente[0].keys())
        csv_writer.writeheader()
        for line in ListaEmailsPaciente:
            csv_writer.writerow(line)
            
print("T_RHSTU_PACIENTE_EMAIL_PACIENTE finalizado")
