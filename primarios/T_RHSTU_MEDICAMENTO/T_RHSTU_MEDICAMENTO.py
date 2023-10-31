import csv
import primarios.T_RHSTU_MEDICAMENTO.aleatorioMedicamento as aleatorioMedicamento 
#import aleatorioMedicamento
import datetime as dt
hoje = dt.date.today()
ListaMedicamentos=[]

with open('primarios\\T_RHSTU_MEDICAMENTO\\remedios.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaNomeRemedios = list(reader)


def T_RHSTU_MEDICAMENTO(id_medicamento,nm_medicamento,ds_detalhada_medicamento,nr_codigo_barras,dt_cadastro,nm_usuario):
    medicamento = {}
    medicamento['ID_MEDICAMENTO'] = id_medicamento #P
    medicamento['NM_MEDICAMENTO'] = nm_medicamento 
    medicamento['DS_DETALHADA_MEDICAMENTO'] = ds_detalhada_medicamento 
    medicamento['NR_CODIGO_BARRAS'] = nr_codigo_barras 
    medicamento['DT_CADASTRO'] = dt_cadastro
    medicamento['NM_USUARIO'] = nm_usuario
    return medicamento 
print("iniciando T_RHSTU_MEDICAMENTO")
i=1
while i < len(listaNomeRemedios):
            
            idMedicamento = i 
            nmMedicamento = listaNomeRemedios[i][0][:49]
            dsDetalhadaMedicamento = aleatorioMedicamento.descricao()
            nrCodigoBarras = aleatorioMedicamento.CodBarras()
            dtCadastro = hoje
            nmUsuario = "Miron"
            i+=1
            

            medicamento = T_RHSTU_MEDICAMENTO(id_medicamento=idMedicamento,nm_medicamento=nmMedicamento,ds_detalhada_medicamento=dsDetalhadaMedicamento,nr_codigo_barras=nrCodigoBarras,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaMedicamentos.append(medicamento)

            
aleatorioMedicamento.geradorDeCSV('T_total\\T_RHSTU_MEDICAMENTO.csv',ListaMedicamentos)              
print("T_RHSTU_MEDICAMENTO completa")
