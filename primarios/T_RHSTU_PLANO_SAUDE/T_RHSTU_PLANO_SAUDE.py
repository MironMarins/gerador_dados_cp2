import primarios.T_RHSTU_PLANO_SAUDE.aleatorioPlanoSaude as aleatorioPlanoSaude
import csv
import datetime as dt
hoje = dt.date.today()
ListaPlanosDeSaude=[]


def T_RHSTU_PLANO_SAUDE(id_plano_saude,ds_razao_social,nm_fantasia_plano_saude,ds_plano_saude,
                        nr_cnpj,nm_contato,ds_telefone,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    planoSaude = {}
    planoSaude['ID_PLANO_SAUDE'] = id_plano_saude #P
    planoSaude['DS_RAZAO_SOCIAL'] = ds_razao_social
    planoSaude['NM_FANTASIA_PLANO_SAUDE'] = nm_fantasia_plano_saude #F
    planoSaude['DS_PLANO_SAUDE'] = ds_plano_saude
    planoSaude['NR_CNPJ'] = nr_cnpj
    planoSaude['NM_CONTATO'] = nm_contato
    planoSaude['DS_TELEFONE'] = ds_telefone
    planoSaude['DT_INICIO'] = dt_inicio
    planoSaude['DT_FIM'] = dt_fim
    planoSaude['DT_CADASTRO'] = dt_cadastro
    planoSaude['NM_USUARIO'] = nm_usuario
    return planoSaude 
print("iniciando T_RHSTU_PLANO_SAUDE")
i=0
while i < len(aleatorioPlanoSaude.planos_de_saude_reais):
       
            dsRazaoSocial = aleatorioPlanoSaude.planos_de_saude_reais[i]
            nmFantasiaPlanoSaude = aleatorioPlanoSaude.planos_de_saude_reais[i]
            dsPlanoSaude = aleatorioPlanoSaude.descricaoPS()
            nrCNPJ = aleatorioPlanoSaude.cnpjReais[i]
            primeiroNome = aleatorioPlanoSaude.nomes()
            sobreNome = aleatorioPlanoSaude.sobrenomes()
            nmContato = primeiroNome + " " + sobreNome
            dsTelefone = aleatorioPlanoSaude.randTelefones()
            dtInicio = aleatorioPlanoSaude.dataFundacao(aleatorioPlanoSaude.idades())
            dtFim = ""
            dtCadastro = hoje
            nmUsuario = "Miron"
            i=i+1
            idPlanoSaude = i

            PlanoDeSaude = T_RHSTU_PLANO_SAUDE(id_plano_saude=idPlanoSaude,ds_razao_social=dsRazaoSocial,nm_fantasia_plano_saude=nmFantasiaPlanoSaude,ds_plano_saude=dsPlanoSaude,nr_cnpj=nrCNPJ,nm_contato=nmContato,ds_telefone=dsTelefone,dt_inicio=dtInicio,dt_fim=dtFim,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaPlanosDeSaude.append(PlanoDeSaude)
            
with open('T_total\\T_RHSTU_PLANO_SAUDE.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaPlanosDeSaude[0].keys())
        csv_writer.writeheader()
        for line in ListaPlanosDeSaude:
            csv_writer.writerow(line)

print("T_RHSTU_PLANO_SAUDE finalizado")

            
            
