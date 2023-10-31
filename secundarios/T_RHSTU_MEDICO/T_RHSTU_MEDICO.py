import secundarios.T_RHSTU_MEDICO.aleatorioMedico as aleatorioMedico
import csv
import datetime as dt
hoje = dt.date.today()
ListaMedicos=[]


def T_RHSTU_MEDICO(id_func,nr_crm,ds_especialidade,dt_cadastro,nm_usuario):
    medico = {}
    medico['ID_FUNC'] = id_func #PF
    medico['NR_CRM'] = nr_crm
    medico['DS_ESPECIALIDAE'] = ds_especialidade
    medico['DT_CADASTRO'] = dt_cadastro
    medico['NM_USUARIO'] = nm_usuario
    return medico 

print("iniciando T_RHSTU_MEDICO")



for i in range(len(aleatorioMedico.listaMedicos)):
            idFunc = aleatorioMedico.listaMedicos[i]
            nrCRM = aleatorioMedico.CRM()
            dsEspecialidade = aleatorioMedico.especialidadesMedicas()
            dtCadastro = hoje
            nmUsuario = "Miron"
            




 

            medico = T_RHSTU_MEDICO(id_func=idFunc,nr_crm=nrCRM,ds_especialidade=dsEspecialidade,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaMedicos.append(medico)
with open('T_total\\T_RHSTU_MEDICO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaMedicos[0].keys())
        csv_writer.writeheader()
        for line in ListaMedicos:
            csv_writer.writerow(line)            


print("T_RHSTU_MEDICO finalizada")