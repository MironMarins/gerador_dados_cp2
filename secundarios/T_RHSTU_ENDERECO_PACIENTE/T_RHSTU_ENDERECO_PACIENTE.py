import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaEnderecoPacientes=[]
repeticao = 2

def T_RHSTU_ENDERECO_PACIENTE(id_endereco,id_paciente,id_logradouro,nr_logradouro,ds_complemento_numero,ds_ponto_referencia,dt_inicio,dt_fim,dt_cadastro,nm_usuario):
    endereco_paciente = {}
    endereco_paciente['ID_ENDERECO'] = id_endereco #P
    endereco_paciente['ID_PACIENTE'] = id_paciente #F
    endereco_paciente['ID_LOGRADOURO'] = id_logradouro #F
    endereco_paciente['NR_LOGRADOURO'] = nr_logradouro
    endereco_paciente['DS_COMPLEMENTO_NUMERO'] = ds_complemento_numero
    endereco_paciente['DS_PONTO_REFERENCIA'] = ds_ponto_referencia
    endereco_paciente['DT_INICIO'] = dt_inicio
    endereco_paciente['DT_FIM'] = dt_fim
    endereco_paciente['DT_CADASTRO'] = dt_cadastro
    endereco_paciente['NM_USUARIO'] = nm_usuario
    return endereco_paciente 

for i in range(repeticao):
            idEdenreco = #P
            idPaciente = #F
            idLogradouro= #F
            nrLogradouro =
            dsComplementoNumero =
            dsPontoReferencia = 
            dtInicio = 
            dtFim = 
            dataCadastro = aleatorioEstado.hoje
            nmUsuario = 


            enderecoPaciente = T_RHSTU_ENDERECO_PACIENTE(id_endereco=idEdenreco,id_paciente=idPaciente,id_logradouro=idLogradouro,nr_logradouro=nrLogradouro,ds_complemento_numero=dsComplementoNumero,ds_ponto_referencia=dsPontoReferencia,dt_inicio=dtInicio,dt_fim=dtFim,dt_cadastro=dataCadastro,nm_usuario=nmUsuario)
            ListaEnderecoPacientes.append(enderecoPaciente)
            


