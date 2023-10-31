import secundarios.T_RHSTU_PACIENTE_PLANO_SAUDE.aleatorioPacientePlanoSaude as aleatorioPacientePlanoSaude
import csv
import datetime as dt
hoje = dt.date.today()
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)
with open('T_total\\T_RHSTU_PLANO_SAUDE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPlanoSaude = list(reader)
ListaPacientePlanosDeSaude=[]
repeticao = 2

def T_RHSTU_PACIENTE_PLANO_SAUDE(id_paciente_ps,id_paciente,id_plano_saude,nr_carteira_ps,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    pacientePlanoSaude = {}
    pacientePlanoSaude['ID_PACIENTE_PS'] = id_paciente_ps #P
    pacientePlanoSaude['ID_PACIENTE'] = id_paciente #F
    pacientePlanoSaude['ID_PLANO_SAUDE'] = id_plano_saude #F
    pacientePlanoSaude['NR_CARTEIRA_PS'] = nr_carteira_ps
    pacientePlanoSaude['DT_INICIO'] = dt_inicio
    pacientePlanoSaude['DT_FIM'] = dt_fim
    pacientePlanoSaude['DT_CADASTRO'] = dt_cadastro
    pacientePlanoSaude['NM_USUARIO'] = nm_usuario
    return pacientePlanoSaude 
print("iniciando T_RHSTU_PACIENTE_PLANO_SAUDE")
i=1
while i < len(listaPacientes):
            idPacientePs = i
            idPaciente = listaPacientes[i][0]
            idPlanoSaude = aleatorioPacientePlanoSaude.idsPlanoSaudePacientes(listaPlanoSaude)
            nrCarteiraPs = aleatorioPacientePlanoSaude.codPlanoSaude()
            dtInicio = aleatorioPacientePlanoSaude.dataInicio(aleatorioPacientePlanoSaude.idades())
            dtFim = ""
            dtCadastro = hoje
            nmUsuario = "Miron"
            i=i+1


            PacientePlanoDeSaude = T_RHSTU_PACIENTE_PLANO_SAUDE(id_paciente_ps=idPacientePs,id_paciente=idPaciente,id_plano_saude=idPlanoSaude,nr_carteira_ps=nrCarteiraPs,dt_inicio=dtInicio,dt_fim=dtFim,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaPacientePlanosDeSaude.append(PacientePlanoDeSaude)
            
with open('T_total\\T_RHSTU_PACIENTE_PLANO_SAUDE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaPacientePlanosDeSaude[0].keys())
        csv_writer.writeheader()
        for line in ListaPacientePlanosDeSaude:
            csv_writer.writerow(line)

print("T_RHSTU_PACIENTE_PLANO_SAUDE finalizado")
