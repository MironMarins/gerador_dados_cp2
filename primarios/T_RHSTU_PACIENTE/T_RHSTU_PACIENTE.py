#import oracledb
import primarios.T_RHSTU_PACIENTE.aleatorioPaciente as aleatorio
#import aleatorioPaciente as aleatorio
import csv
import datetime as dt
hoje = dt.date.today()
listaPacientes=[]

def return_paciente():
        return listaPacientes


def T_RHSTU_PACIENTE(id_paciente,nm_paciente,nr_cpf,nm_rg,dt_nascimento,fl_sexo_biologico,
                     ds_escolaridade,ds_estado_civil,nm_grupo_sanguineo,nr_altura,nr_peso,
                     dt_cadastro,nm_usuario):
    paciente = {}
    paciente['ID_PACIENTE'] = id_paciente 
    paciente['NM_PACIENTE'] = nm_paciente
    paciente['NR_CPF'] = nr_cpf
    paciente['NM_RG'] = nm_rg
    paciente['DT_NASCIMENTO'] = dt_nascimento
    paciente['FL_SEXO_BIOLOGICO'] = fl_sexo_biologico
    paciente['DS_ESCOLARIDADE'] = ds_escolaridade
    paciente['DS_ESTADO_CIVIL'] = ds_estado_civil
    paciente['NM_GRUPO_SANGUINEO'] = nm_grupo_sanguineo
    paciente['NR_ALTURA'] = nr_altura
    paciente['NR_PESO'] = nr_peso
    paciente['DT_CADASTRO'] = dt_cadastro
    paciente['NM_USUARIO'] = nm_usuario
    return paciente 



print("iniciando T_RHSTU_PACIENTE")
for i in range(1,1500002):
            idPaciente = i
            nome = aleatorio.nomes()

            sobrenome = aleatorio.sobrenomes()
            nomeInteiro = nome +" "+sobrenome
            cpf = aleatorio.repetidasCPF[i]
            rg = aleatorio.repetidasRG[i]
            idade = aleatorio.idades()
            dataNascimento = aleatorio.dataNascimento(idade=idade)
            sexoBiologico =  aleatorio.sexoBiologico(nome)
            escolaridade = aleatorio.escolaridadePaciente()
            estadoCivil = aleatorio.estadoCivil(nome)
            grupoSanguineo = aleatorio.tipoSanguineo()
            altura = aleatorio.Altura(novaidade=idade)
            peso = aleatorio.Peso()
            dataCadastro = hoje
            usuarioNomeCompleto = "Miron"
            if i == 1:
                    print("1")
            elif i == 100: 
                    print("100")
            elif i == 1000: 
                    print("1000")
            elif i == 10000: 
                    print("10000")
            elif i == 100000: 
                    print("100000")
            elif i == 1000000: 
                    print("1000000")
            elif i == 2500000: 
                    print("1250000")
            
            paciente = T_RHSTU_PACIENTE(id_paciente=idPaciente,nm_paciente=nomeInteiro,nr_cpf=cpf,nm_rg=rg,dt_nascimento=dataNascimento,
                                    fl_sexo_biologico=sexoBiologico,ds_escolaridade=escolaridade,ds_estado_civil=estadoCivil,
                                    nm_grupo_sanguineo=grupoSanguineo,nr_altura=altura,nr_peso=peso,dt_cadastro=dataCadastro,
                                                            nm_usuario=usuarioNomeCompleto)
            listaPacientes.append(paciente)
            
            
with open('T_total\\T_RHSTU_PACIENTE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=listaPacientes[0].keys())
        csv_writer.writeheader()
        for line in listaPacientes:
            csv_writer.writerow(line)    

print("T_RHSTU_PACIENTE completa")        
            
            


