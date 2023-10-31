import secundarios.T_RHSTU_CONTATO_PACIENTE.aleatorioContatoPaciente as aleatorioContatoPaciente
import csv
import datetime as dt
hoje = dt.date.today()
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)
ListaContatoPacientes=[]


def T_RHSTU_CONTATO_PACIENTE(id_paciente,id_contato,id_tipo_contato,nm_contato,nr_ddi,nr_ddd,nr_telefone,dt_cadastro,nm_usuario):
    contato_paciente = {}
    
    contato_paciente['ID_PACIENTE'] = id_paciente #PF
    contato_paciente['ID_CONTATO'] = id_contato #P
    contato_paciente['ID_TIPO_CONTATO'] = id_tipo_contato#F
    contato_paciente['NM_CONTATO'] = nm_contato
    contato_paciente['NR_DDI'] = nr_ddi
    contato_paciente['NR_DDD'] = nr_ddd
    contato_paciente['NR_TELEFONE'] = nr_telefone
    contato_paciente['DT_CADASTRO'] = dt_cadastro
    contato_paciente['NM_USUARIO'] = nm_usuario
    return contato_paciente
print("iniciando T_RHSTU_CONTATO_PACIENTE")
i=1
while i < len(listaPacientes):
            idContato = i
            idPaciente = listaPacientes[i][0]
            nome = aleatorioContatoPaciente.nomes()
            sobrenome = aleatorioContatoPaciente.sobrenomes()
            nomeInteiro = nome +" "+sobrenome
            nmContato = nomeInteiro
            IdTipoContato = aleatorioContatoPaciente.verificacaoContatos(nome)
            nrDDI = "55" 
            nrDDD = aleatorioContatoPaciente.Ddd()
            nrTelefone = aleatorioContatoPaciente.Tel()
            dtCadastro = hoje
            nmUsuario = "Miron"
            i+=1
            
            ContatoPaciente = T_RHSTU_CONTATO_PACIENTE(id_paciente=idPaciente,id_contato=idContato,id_tipo_contato=IdTipoContato,nm_contato=nmContato,nr_ddd=nrDDD,nr_ddi=nrDDI,nr_telefone=nrTelefone,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaContatoPacientes.append(ContatoPaciente)

with open('T_total\\T_RHSTU_CONTATO_PACIENTE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaContatoPacientes[0].keys())
        csv_writer.writeheader()
        for line in ListaContatoPacientes:
            csv_writer.writerow(line)
                       
print("T_RHSTU_CONTATO_PACIENTE finalizado")

