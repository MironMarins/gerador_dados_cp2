import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaEnderecoUnidhosp=[]
repeticao = 2

def T_RHSTU_ENDERECO_UNIDHOSP(id_end_unidhosp,id_unid_hospital,id_logradouro,nr_logradouro,ds_ponto_referencia,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    endereco_unidhosp = {}
    endereco_unidhosp['ID_END_UNIDHOSP'] = id_end_unidhosp #PK
    endereco_unidhosp['ID_UNID_HOSPITAL'] = id_unid_hospital #FK T_RHSTU_UNID_HOSPITALAR
    endereco_unidhosp['ID_LOGRADOURO'] = id_logradouro #FK T_RHSTU_LOGRADOURO
    endereco_unidhosp['NR_LOGRADOURO'] = nr_logradouro
    endereco_unidhosp['DS_PONTO_REFERENCIA'] = ds_ponto_referencia
    endereco_unidhosp['DT_INICIO'] = dt_inicio
    endereco_unidhosp['DT_FIM'] = dt_fim
    endereco_unidhosp['DT_CADASTRO'] = dt_cadastro
    endereco_unidhosp['NM_USUARIO'] = nm_usuario
    return endereco_unidhosp 

for i in range(repeticao):
            idEndUnidhosp = #PK
            idUnidHospital = #FK T_RHSTU_UNID_HOSPITALAR
            idLogradouro = #FK T_RHSTU_LOGRADOURO
            nrLogradouro =
            dsPontoReferencia = 
            dtInicio = 
            dtFim = 
            dataCadastro = aleatorioEstado.hoje
            nmUsuario =

            enderecoUnidhosp = T_RHSTU_ENDERECO_UNIDHOSP(id_end_unidhosp=idEndUnidhosp,id_unid_hospital=idUnidHospital,id_logradouro=idLogradouro,nr_logradouro=nrLogradouro,ds_ponto_referencia=dsPontoReferencia,dt_inicio=dtInicio,dt_fim=dtFim,dt_cadastro=dataCadastro,nm_usuario=nmUsuario)
            ListaEnderecoUnidhosp.append(enderecoUnidhosp)
            


