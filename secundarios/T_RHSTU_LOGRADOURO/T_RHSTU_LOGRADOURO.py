import oracledb
import T_RHSTU_PACIENTE.aleatorio as aleatorio
import aleatorioEstado
ListaLogradouros=[]
repeticao = 2

def T_RHSTU_LOGRADOURO(id_logradouro,id_bairro,nm_logradouro,nr_cep,dt_cadastro,nm_usuario):
    logradouro = {}
    logradouro['ID_LOGRADOURO'] = id_logradouro #PK
    logradouro['ID_BAIRRO'] = id_bairro #FK T_RHSTU_BAIRRO
    logradouro['NM_LOGRADOURO'] = nm_logradouro
    logradouro['NR_CEP'] = nr_cep
    logradouro['DT_CADASTRO'] = dt_cadastro
    logradouro['NM_USUARIO'] = nm_usuario
    return logradouro 

for i in range(repeticao):
            idLogradouro = #PK
            idBairro =  #FK T_RHSTU_BAIRRO
            nmLogradouro = 
            nrCEP = 
            dataCadastro = aleatorioEstado.hoje
            nmUsuario =


            logradouro = T_RHSTU_LOGRADOURO(id_logradouro=idLogradouro,id_bairro=idBairro,nm_logradouro=nmLogradouro,nr_cep=nrCEP,dt_cadastro=dataCadastro,nm_usuario=nmUsuario)
            ListaLogradouros.append(logradouro)
            


