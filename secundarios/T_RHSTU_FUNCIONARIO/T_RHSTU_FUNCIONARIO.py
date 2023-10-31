import secundarios.T_RHSTU_FUNCIONARIO.aleatorioFuncionario as aleatorioFuncionario
import datetime as dt
import csv
hoje = dt.date.today()
ListaFuncionarios=[]


def T_RHSTU_FUNCIONARIO(id_func,id_superior,nm_func,ds_cargo,nr_cpf,nr_rg,dt_nascimento,vl_salario,
                     st_func,dt_cadastro,nm_usuario):
    funcionario = {}
    funcionario['ID_FUNC'] = id_func #PK
    funcionario['ID_SUPERIOR'] = id_superior #FK
    funcionario['NM_FUNC'] = nm_func
    funcionario['DS_CARGO'] =ds_cargo
    funcionario['DT_NASCIMENTO'] = dt_nascimento
    funcionario['VL_SALARIO'] = vl_salario
    funcionario['NR_RG'] = nr_rg
    funcionario['NR_CPF'] = nr_cpf
    funcionario['ST_FUNC'] = st_func
    funcionario['DT_CADASTRO'] = dt_cadastro
    funcionario['NM_USUARIO'] = nm_usuario
    return funcionario 
print("iniciando T_RHSTU_FUNCIONARIO")
func = 0
presidente = 1
diretor= 1
gerente= 28
coordenador= 325
funcionario2= 2998
cont=0


    
cargo = "presidente"
idFunc = 1
nmFunc= aleatorioFuncionario.nomes() + " "+ aleatorioFuncionario.sobrenomes()
idSuperior = ""
idPres = idFunc
cont+=1
dtNascimento = aleatorioFuncionario.dataNascimento(aleatorioFuncionario.idades())
vlSalario = aleatorioFuncionario.Salario(cargo)
nrRG = aleatorioFuncionario.repetidasRG[cont+1800000]
nrCPF = aleatorioFuncionario.repetidasCPF[1600000+cont]
stFunc = "A"
dtCadastro = hoje
nmUsuario = "Miron"
funcionario = T_RHSTU_FUNCIONARIO(id_func=idFunc,id_superior=idSuperior,nm_func=nmFunc,ds_cargo=cargo,dt_nascimento=dtNascimento,vl_salario=vlSalario,nr_rg=nrRG,nr_cpf=nrCPF,st_func=stFunc,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
ListaFuncionarios.append(funcionario)
for d in range(0,27):
    cargo="diretor"
    diretor = diretor + 1
    idFunc = diretor
    nmFunc = aleatorioFuncionario.nomes() + " "+ aleatorioFuncionario.sobrenomes()
    idSuperior = presidente
    idDir = idFunc
    cont+=1
    dtNascimento = aleatorioFuncionario.dataNascimento(aleatorioFuncionario.idades())
    vlSalario = aleatorioFuncionario.Salario(cargo)
    nrRG = aleatorioFuncionario.repetidasRG[cont+1800000]
    nrCPF = aleatorioFuncionario.repetidasCPF[1600000+cont]
    stFunc = "A"
    dtCadastro = hoje
    nmUsuario = "Miron"
    funcionario = T_RHSTU_FUNCIONARIO(id_func=idFunc,id_superior=idSuperior,nm_func=nmFunc,ds_cargo=cargo,dt_nascimento=dtNascimento,vl_salario=vlSalario,nr_rg=nrRG,nr_cpf=nrCPF,st_func=stFunc,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
    ListaFuncionarios.append(funcionario)
    for g in range(0,11):
        cargo="gerente"
        gerente = gerente + 1
        idFunc=gerente
        nmFunc =aleatorioFuncionario.nomes() + " "+ aleatorioFuncionario.sobrenomes()
        idSuperior = idDir
        idGer = idFunc
        cont+=1
        dtNascimento = aleatorioFuncionario.dataNascimento(aleatorioFuncionario.idades())
        vlSalario = aleatorioFuncionario.Salario(cargo)
        nrRG = aleatorioFuncionario.repetidasRG[cont+1800000]
        nrCPF = aleatorioFuncionario.repetidasCPF[1600000+cont]
        stFunc = "A"
        dtCadastro = hoje
        nmUsuario = "Miron"
        funcionario = T_RHSTU_FUNCIONARIO(id_func=idFunc,id_superior=idSuperior,nm_func=nmFunc,ds_cargo=cargo,dt_nascimento=dtNascimento,vl_salario=vlSalario,nr_rg=nrRG,nr_cpf=nrCPF,st_func=stFunc,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
        ListaFuncionarios.append(funcionario)
        for c in range(0,9):
            cargo="coordenador"
            coordenador=coordenador+1
            idFunc=coordenador
            nmFunc =aleatorioFuncionario.nomes() + " "+ aleatorioFuncionario.sobrenomes()
            idSuperior =idGer
            idCoord = idFunc
            cont+=1
            dtNascimento = aleatorioFuncionario.dataNascimento(aleatorioFuncionario.idades())
            vlSalario = aleatorioFuncionario.Salario(cargo)
            nrRG = aleatorioFuncionario.repetidasRG[cont+1800000]
            nrCPF = aleatorioFuncionario.repetidasCPF[1600000+cont]
            stFunc = "A"
            dtCadastro = hoje
            nmUsuario = "Miron"
            funcionario = T_RHSTU_FUNCIONARIO(id_func=idFunc,id_superior=idSuperior,ds_cargo=cargo,nm_func=nmFunc,dt_nascimento=dtNascimento,vl_salario=vlSalario,nr_rg=nrRG,nr_cpf=nrCPF,st_func=stFunc,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaFuncionarios.append(funcionario)
            for f in range(0,20):
                funcionario2=funcionario2+1
                cargo="funcionario"
                idFunc=funcionario2
                nmFunc =aleatorioFuncionario.nomes() + " "+ aleatorioFuncionario.sobrenomes()
                idSuperior = idCoord
                cont+=1
                dtNascimento = aleatorioFuncionario.dataNascimento(aleatorioFuncionario.idades())
                vlSalario = aleatorioFuncionario.Salario(cargo)
                nrRG = aleatorioFuncionario.repetidasRG[cont+1800000]
                nrCPF = aleatorioFuncionario.repetidasCPF[1600000+cont]
                stFunc = "A"
                dtCadastro = hoje
                nmUsuario = "Miron"
                funcionario = T_RHSTU_FUNCIONARIO(id_func=idFunc,id_superior=idSuperior,nm_func=nmFunc,ds_cargo=cargo,dt_nascimento=dtNascimento,vl_salario=vlSalario,nr_rg=nrRG,nr_cpf=nrCPF,st_func=stFunc,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
                ListaFuncionarios.append(funcionario)
                
with open('T_total\\T_RHSTU_FUNCIONARIO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaFuncionarios[0].keys())
        csv_writer.writeheader()
        for line in ListaFuncionarios:
            csv_writer.writerow(line)

print("T_RHSTU_FUNCIONARIO finalizado")