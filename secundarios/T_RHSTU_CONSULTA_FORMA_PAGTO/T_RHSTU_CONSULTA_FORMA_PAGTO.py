import secundarios.T_RHSTU_CONSULTA_FORMA_PAGTO.aleatorioConsultaFormaPagto as aleatorioConsultaFormaPagto
import csv
import datetime as dt
hoje = dt.date.today()
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientesPS = list(reader)
with open('T_total\\T_RHSTU_CONSULTA.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaConsulta = list(reader)
with open('T_total\\T_RHSTU_UNID_HOSPITALAR.csv',"r",encoding='utf-8') as csvfile:#
                reader = csv.reader(csvfile)
                listaUnidHospitalar = list(reader)
ListaConsultaFormasDePagamento=[]
repeticao = 2

def T_RHSTU_CONSULTA_FORMA_PAGTO(id_consulta_forma_pagto,id_unid_hospital,id_consulta,id_paciente_ps,
                                 id_forma_pagto,dt_pagto_consulta,st_pagto_consulta,dt_cadastro,nm_usuario):
    consultaFormaPagto = {}
    consultaFormaPagto['ID_CONSULTA_FORMA_PAGTO'] = id_consulta_forma_pagto #P
    consultaFormaPagto['ID_UNID_HOSPITAL'] = id_unid_hospital #F
    consultaFormaPagto['ID_CONSULTA'] = id_consulta #F
    consultaFormaPagto['ID_PACIENTE_PS'] = id_paciente_ps #F
    consultaFormaPagto['ID_FORMA_PAGTO'] = id_forma_pagto #F
    consultaFormaPagto['DT_PAGTO_CONSULTA'] = dt_pagto_consulta 
    consultaFormaPagto['ST_PAGTO_CONSULTA'] = st_pagto_consulta
    consultaFormaPagto['DT_CADASTRO'] = dt_cadastro
    consultaFormaPagto['NM_USUARIO'] = nm_usuario
    return consultaFormaPagto 
print("iniciando T_RHSTU_CONSULTA_FORMA_PAGTO")
i=1
while i < len(listaConsulta):
            idConsultaFormaPagto= i
            idUnidHospital= listaConsulta[i][0]
            idConsulta = listaConsulta[i][1]
            idPacientePs = listaPacientesPS[i][0]
            idFormaPagto = aleatorioConsultaFormaPagto.aleatorioFormaPagamento()
            stPagtoConsulta = aleatorioConsultaFormaPagto.aleatorioStatusPagamento()
            if stPagtoConsulta == "P":
                    dtPagtoConsulta = aleatorioConsultaFormaPagto.dataPagamento(listaConsulta[i][4][:4])
            elif stPagtoConsulta == "C":
                    dtPagtoConsulta = aleatorioConsultaFormaPagto.dataPagamento(listaConsulta[i][4][:4])
            else:
                   dtPagtoConsulta = "" 
            
            dtCadastro = hoje
            nmUsuario = "Miron"
            i+=1


            ConsultaFormaDePagamento = T_RHSTU_CONSULTA_FORMA_PAGTO(id_consulta_forma_pagto=idConsultaFormaPagto,id_unid_hospital=idUnidHospital,id_consulta=idConsulta,id_paciente_ps=idPacientePs,id_forma_pagto=idFormaPagto,dt_pagto_consulta=dtPagtoConsulta,st_pagto_consulta=stPagtoConsulta,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaConsultaFormasDePagamento.append(ConsultaFormaDePagamento)
            
with open('T_total\\T_RHSTU_CONSULTA_FORMA_PAGTO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaConsultaFormasDePagamento[0].keys())
        csv_writer.writeheader()
        for line in ListaConsultaFormasDePagamento:
            csv_writer.writerow(line)

print("T_RHSTU_CONSULTA_FORMA_PAGTO finalizado")