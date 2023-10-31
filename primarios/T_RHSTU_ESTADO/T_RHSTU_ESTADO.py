import primarios.T_RHSTU_ESTADO.aleatorioEstado as aleatorioEstado
import datetime as dt
import csv
hoje = dt.date.today()
listaEstados=[]
def return_estado():
        return listaEstados
def T_RHSTU_ESTADO(id_estado,sg_estado,nm_estado,dt_cadastro,nm_usuario):
    paciente = {}
    paciente['ID_ESTADO'] = id_estado #PK
    paciente['SG_ESTADO'] = sg_estado
    paciente['NM_ESTADO'] = nm_estado
    paciente['DT_CADASTRO'] = dt_cadastro
    paciente['NM_USUARIO'] = nm_usuario
    return paciente 
print("iniciando T_RHSTU_ESTADO")
i = 0
while i < len(aleatorioEstado.estados):
                        
            nmEstado = aleatorioEstado.estados[i]
            sgEstado = aleatorioEstado.siglas(nmEstado)
            dataCadastro = hoje
            usuarioNomeCompleto = "Miron"
            i = i + 1
            idEstado = i #PK
                    

            estado = T_RHSTU_ESTADO(id_estado=idEstado,sg_estado=sgEstado,nm_estado=nmEstado,dt_cadastro=dataCadastro,nm_usuario=usuarioNomeCompleto)
            listaEstados.append(estado)
           
print("T_RHSTU_ESTADO completa")
with open('T_total\\T_RHSTU_ESTADO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=listaEstados[0].keys())
        csv_writer.writeheader()
        for line in listaEstados:
            csv_writer.writerow(line)

