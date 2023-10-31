import secundarios.T_RHSTU_CONSULTA.aleatorioConsulta as aleatorioConsulta
import csv
import datetime as dt
hoje = dt.date.today()
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)
ListaConsultas=[]

def T_RHSTU_CONSULTA(id_unid_hospital,id_consulta,id_paciente,id_func,dt_hr_consulta,nr_consultorio,dt_cadastro,nm_usuario):
    consulta = {}
    consulta['ID_UNID_HOSPITAL'] = id_unid_hospital #PF
    consulta['ID_CONSULTA'] = id_consulta #P
    consulta['ID_PACIENTE'] = id_paciente #F
    consulta['ID_FUNC'] = id_func #F
    consulta['DT_HR_CONSULTA'] = dt_hr_consulta
    consulta['NR_CONSULTORIO'] = nr_consultorio
    consulta['DT_CADASTRO'] = dt_cadastro
    consulta['NM_USUARIO'] = nm_usuario
    return consulta 
print("iniciando T_RHSTU_CONSULTA")
i=1
while i < len(listaPacientes):
            idConsulta = i
            idPaciente = listaPacientes[i][0]
            idFunc = aleatorioConsulta.aleatorioMedico()
            idUnidHospital = aleatorioConsulta.medicoPorUnidade(idFunc)
            dtHrConsulta = aleatorioConsulta.dataAtendimento(aleatorioConsulta.anos()) + " " + str(aleatorioConsulta.horas()) + ":" + str(aleatorioConsulta.minutos())+  ":" + str(aleatorioConsulta.segundos())
            nrConsultorio = aleatorioConsulta.consultorio()
            dtCadastro = hoje
            nmUsuario = "Miron"
            i+=1
            


            consulta = T_RHSTU_CONSULTA(id_unid_hospital=idUnidHospital,id_consulta=idConsulta,id_paciente=idPaciente,id_func=idFunc,dt_hr_consulta=dtHrConsulta,nr_consultorio=nrConsultorio,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaConsultas.append(consulta)
            
with open('T_total\\T_RHSTU_CONSULTA.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaConsultas[0].keys())
        csv_writer.writeheader()
        for line in ListaConsultas:
            csv_writer.writerow(line)

print("T_RHSTU_CONSULTA finalizados")