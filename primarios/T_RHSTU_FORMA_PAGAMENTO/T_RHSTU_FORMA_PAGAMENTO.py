import csv
import primarios.T_RHSTU_FORMA_PAGAMENTO.aleatorioFormaPagamento as aleatorioFormaPagamento
import datetime as dt
hoje = dt.date.today()
ListaFormasDePagamento=[]
repeticao = 2

def T_RHSTU_FORMA_PAGAMENTO(id_forma_pagto,nm_forma_pagto,ds_forma_pagto,st_forma_pagto,dt_cadastro,nm_usuario):
    formaPagamento = {}
    formaPagamento['ID_FORMA_PAGTO'] = id_forma_pagto #P
    formaPagamento['NM_FORMA_PAGTO'] = nm_forma_pagto 
    formaPagamento['DS_FORMA_PAGTO'] = ds_forma_pagto
    formaPagamento['ST_FORMA_PAGTO'] = st_forma_pagto
    formaPagamento['DT_CADASTRO'] = dt_cadastro
    formaPagamento['NM_USUARIO'] = nm_usuario
    return formaPagamento 
print("iniciando T_RHSTU_FORMA_PAGAMENTO")
i=0
while i < len(aleatorioFormaPagamento.formaDePagamento):
            
            nmFormaPagto = aleatorioFormaPagamento.formaDePagamento[i]
            dsFormaPagto = aleatorioFormaPagamento.descricao[i]
            stFormaPagto = "A" #tivo #ou "I"nativo 
            dtCadastro = hoje
            nmUsuario = "Miron"
            i=i+1
            idFormaPagto = i


            FormaDePagamento = T_RHSTU_FORMA_PAGAMENTO(id_forma_pagto=idFormaPagto,nm_forma_pagto=nmFormaPagto,ds_forma_pagto=dsFormaPagto,st_forma_pagto=stFormaPagto,dt_cadastro=dtCadastro,nm_usuario=nmUsuario)
            ListaFormasDePagamento.append(FormaDePagamento)
            
with open('T_total\\T_RHSTU_FORMA_PAGAMENTO.csv', 'w', newline='', encoding='utf-8') as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames=ListaFormasDePagamento[0].keys())
        csv_writer.writeheader()
        for line in ListaFormasDePagamento:
            csv_writer.writerow(line)

print("T_RHSTU_FORMA_PAGAMENTO completa")