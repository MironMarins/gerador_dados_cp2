import secundarios.T_RHSTU_PRESCRICAO_MEDICA.aleatorioPrescricaoMedica as aleatorioPrescricaoMedica
import csv
import datetime as dt
hoje = dt.date.today()
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)
with open('T_total\\T_RHSTU_CONSULTA.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaConsulta = list(reader)
with open('T_total\\T_RHSTU_MEDICAMENTO.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaMedicamentos = list(reader)
ListaPrescricaoMedicas=[]
repeticao = 2

def T_RHSTU_PRESCRICAO_MEDICA(id_prescricao_medica,id_unid_hospital,id_consulta,id_medicamento,ds_posologia,ds_via,ds_observacao_uso,qt_medicamento,dt_cadastro,nm_usuario):
    prescricao_medica = {}
    prescricao_medica['ID_PRESCRICAO_MEDICA'] = id_prescricao_medica #P
    prescricao_medica['ID_UNID_HOSPITAL'] = id_unid_hospital #F
    prescricao_medica['ID_CONSULTA'] = id_consulta #F
    prescricao_medica['ID_MEDICAMENTO'] = id_medicamento #F
    prescricao_medica['DS_POSOLOGIA'] = ds_posologia
    prescricao_medica['DS_VIA'] = ds_via
    prescricao_medica['DS_OBSERVACAO_USO'] = ds_observacao_uso
    prescricao_medica['QT_MEDICAMENTO'] = qt_medicamento
    prescricao_medica['NM_USUARIO'] = nm_usuario
    prescricao_medica['DT_CADASTRO'] = dt_cadastro
    
    return prescricao_medica 
print("iniciando T_RHSTU_PRESCRICAO_MEDICA")
i=1
while i < len(listaPacientes):
            idPrescricaoMedica = i
            idUnidHospital = listaConsulta[i][0]
            idConsulta = listaConsulta[i][1]
            idMedicamento = aleatorioPrescricaoMedica.aletorioIdPosologia(listaMedicamentos)
            dsPosologia = aleatorioPrescricaoMedica.aleatorioPosologia(idMedicamento)
            dsVia = aleatorioPrescricaoMedica.aleatorioVia(idMedicamento)
            dsObservacaoUso = ""
            qtMedicamento = aleatorioPrescricaoMedica.aletorioDosagem(idMedicamento)
            dtCadastro =hoje
            nmUsuario ="Miron"
            i=i+1



            prescricaoMedica = T_RHSTU_PRESCRICAO_MEDICA(id_prescricao_medica=idPrescricaoMedica,id_unid_hospital=idUnidHospital,id_consulta=idConsulta,id_medicamento=idMedicamento,ds_posologia=dsPosologia,ds_via=dsVia,ds_observacao_uso=dsObservacaoUso,qt_medicamento=qtMedicamento,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaPrescricaoMedicas.append(prescricaoMedica)
            
with open('T_total\\T_RHSTU_PRESCRICAO_MEDICA.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaPrescricaoMedicas[0].keys())
        csv_writer.writeheader()
        for line in ListaPrescricaoMedicas:
            csv_writer.writerow(line)

print("T_RHSTU_PRESCRICAO_MEDICA finalizado")
