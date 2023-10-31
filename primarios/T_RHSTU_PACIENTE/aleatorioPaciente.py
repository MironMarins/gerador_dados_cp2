import random
from datetime import datetime, timedelta

repetidas = []
repetidasTel = []
repetidasCPF = []
repetidasRG = []
def nomesMasculinos():
    nomesMasculinos = ("João","Pedro","Antônio","Luís","Gabriel","Rafael","Felipe","Daniel","André","Carlos","Marcos","Eduardo","Lucas","Marcelo","Rodrigo","Mateus","Alexandre","Roberto","Thiago","Gustavo","Leonardo","Bruno","João Pedro","Raul","Miguel","Fernando","Paulo","Francisco","Matheus","Vinícius","Guilherme","Diego","Rafael","Fabio","Otávio","William","Renato","Emanuel","Davi","Flávio","José","César","Márcio","Leandro","Alan","Vitor","Augusto","Juan","Ângelo","Hugo")
    pos = random.randint(0, (len(nomesMasculinos)-1))
    return nomesMasculinos[pos]

def nomesFemininos():
    nomesFemininos =("Maria","Ana","Laura","Sofia","Isabella","Helena","Valentina","Luísa","Giovanna","Alice","Clara","Camila","Beatriz","Julia","Manuela","Mariana","Gabriela","Rafaela","Carolina","Joana","Amanda","Letícia","Vitória","Emanuela","Bruna","Renata","Isadora","Lívia","Eloísa","Thais","Roberta","Júlia","Marta","Andrea","Vanessa","Bárbara","Flávia","Natália","Bianca","Fernanda","Raquel","Daniela","Patrícia","Juliana","Débora","Larissa","Verônica","Renata","Adriana","Cláudia")
    pos = random.randint(0, (len(nomesFemininos)-1))
    return nomesFemininos[pos]
def sobrenomes(): 
    sobrenomes = ("da Silva", "Oliveira", "Machado", "dos Santos", "Fraga", "Moura", "Menezes","Pereira","Oliveira","Souza","Costa","Rodrigues","Martins","Ferreira","Alves","Lima","Araújo","Barbosa","Gomes","Vieira","Barbosa","Ribeiro","Fernandes","Carvalho","Mendes","Dantas","Cardoso","Dias","Cunha","Rocha",
                  "Castro","Nunes","Moreira","Torres","Lopes","Pinto","Monteiro","Fonseca","Amaral","Xavier","Guedes","Magalhães","Andrade","Abreu","Tavares","Santos","Reis","Coelho","Guimarães","Mota","Machado","Azevedo","Correia","Teixeira","Medeiros","Mello","Nascimento","Aguiar","Sá","Freitas","Rios","Marques",
                  "Caldeira","Cardoso","Viana","Vasconcelos","Bessa","Simões","Moraes","Peixoto","Sampaio","Pinheiro","Brito","Soares","Barros","Pires","Guerra","Veloso","Azevedo","Rangel","Cordeiro","Abreu","Peçanha","Britto","Santana","Nogueira","Dantas","Galvão","Guimarães","Paiva","Lima","Siqueira","Vasconcelos","Goulart",
                  "Franco","Couto","Lobato","Duarte","Pacheco","Brites","Bastos","Pinho","Lacerda","Rios","Brandão")
    pos = random.randint(0, (len(sobrenomes)-1))
    return sobrenomes[pos]
masc = nomesMasculinos()
fem = nomesFemininos()

def nomes():
    nome1 = nomesMasculinos()
    nome2 = nomesFemininos()
    pos = random.randint(1,2)
    #print(pos)
    if pos == 2:
        nome = nome1
    elif pos == 1:
        nome = nome2
    return nome
    

def estadoCivil(nome):
    estadoCivil = ("solteiro","namorando","casado","solteiro","separado","viuvo","solteira","namorando","casada","solteira","separada","viuva",)
        
    nomesFemininos =("Maria","Ana","Laura","Sofia","Isabella","Helena","Valentina","Luísa","Giovanna","Alice","Clara","Camila","Beatriz","Julia","Manuela","Mariana","Gabriela","Rafaela","Carolina","Joana","Amanda","Letícia","Vitória","Emanuela","Bruna","Renata","Isadora","Lívia","Eloísa","Thais","Roberta","Júlia","Marta","Andrea","Vanessa","Bárbara","Flávia","Natália","Bianca","Fernanda","Raquel","Daniela","Patrícia","Juliana","Débora","Larissa","Verônica","Renata","Adriana","Cláudia")
       
    if nome in nomesFemininos:
        pos = random.randint(6,len(estadoCivil)-1)
    else:
        pos = random.randint(0,5)
        
    return estadoCivil[pos]
    


def sexoBiologico(nome):
    nomesFemininos =("Maria","Ana","Laura","Sofia","Isabella","Helena","Valentina","Luísa","Giovanna","Alice","Clara","Camila","Beatriz","Julia","Manuela","Mariana","Gabriela","Rafaela","Carolina","Joana","Amanda","Letícia","Vitória","Emanuela","Bruna","Renata","Isadora","Lívia","Eloísa","Thais","Roberta","Júlia","Marta","Andrea","Vanessa","Bárbara","Flávia","Natália","Bianca","Fernanda","Raquel","Daniela","Patrícia","Juliana","Débora","Larissa","Verônica","Renata","Adriana","Cláudia")
    chanceT = random.randint(1,100)
    chanceHerma = random.randint(1,1000)
    
    if nome in nomesFemininos:
        sexo = "F"
    else:
        sexo="M"
    if chanceT==1:
        if sexo =="F":
            sexo ="M"
        else:
            sexo = "M"
    if chanceHerma==1:
        sexo = "I"
    return sexo


def tipoSanguineo():
    tipoSanguineo = ("A+","A-","O+","O-","AB+","AB-","B+","B-")
    pos = random.randint(0, (len(tipoSanguineo)-1))
    return tipoSanguineo[pos]

def ids():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 8:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    while repetidas.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidas.append(num)
    
    return num


def Tel():
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    while i < 8:
        pos = random.randint(0, (len(numeros)-1))
        num = num + str(pos)
        i = i + 1
    # permite checar se o codigo dado já não esta presente na lista "repetidas" 
    while repetidasTel.count(num) >= 1:
        num = ""
        o = 0
        # enquanto ouver outro codigo igual na lista "repetidas" a função
        # criará outro
        while o < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            o = o + 1
    repetidasTel.append(num)

def Ddd():
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    ddd = ""
    while i < 2:
        pos = random.randint(0, (len(numeros)-1))
        ddd = ddd + str(pos)
        i = i + 1
        return ddd

#------------------------------------------------------------------------------------------------------------------
# escolher aleatoriamente idades
#def idadeInfanto():
    #idade = random.randint(1,17)
    #return idade

#def idadeAdulto():
    idade = random.randint(18,59)
    return idade

#def idadeIdoso():
    idade = random.randint(60,107)
    return idade

#idadeInfanto = idadeInfanto()
#idadeAdulto = idadeAdulto()
#idadeIdoso = idadeIdoso()

#geracao = [idadeInfanto,idadeAdulto,idadeIdoso]



# pega uma idade para definir o ano de nascimento 


def idades():
    pos = random.randint(18, 104)
    return pos

def dataNascimento(idade):
        anoNascimento = 2023 - idade
        anoNascimento = str(anoNascimento)
        data = anoNascimento + "-"
        mes = random.randint(1,12)
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            mes = str(mes)
            data = data + mes + "-"
            dia = random.randint(1,31)
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            mes = str(mes)
            data = data + mes + "-"
            dia = random.randint(1,30)
        elif mes == 2:
             mes = str(mes)
             data = data + mes + "-"
             dia = random.randint(1,28)
        
        dia = str(dia)
        data = data + dia
        return data






def dataInscricao(idade):
    
    dataNascimento = 2023 - idade
    anoInscricao = random.randint(1900, 2023)
    while anoInscricao < dataNascimento:
        idade = random.randint(1,30)
        anoInscricao = 2023 - idade
    anoInscricao = str(anoInscricao)
    data = anoInscricao + "-"
    mes = random.randint(1,12)
    mes = str(mes)
    data = data + mes + "-"
    dia = random.randint(1,30)
    dia = str(dia)
    data = data + dia 
      
    return data



def Altura(novaidade):
    #if novaidade <= 3:
        #altura =  random.uniform(0.2,0.8)
        #altura = round(altura,2)
    #elif novaidade > 3 and novaidade <= 8:
       # altura = random.uniform(0.5, 1.20)
        #altura = round(altura,2)
    #elif novaidade > 8 and novaidade <=14:
        #altura = random.uniform(0.8, 1.7)
        #altura = round(altura,2)
    #elif novaidade > 14:
    altura = random.uniform(1.2,2.3)
    altura = round(altura,2)
    return altura

def Peso():
    #if novaidade <= 3:
        #peso =  random.uniform(0, 5)
        #peso = round(peso,1)
    #elif novaidade > 3 and novaidade <= 8:
        #peso = random.uniform(10, 30)
        #peso = round(peso,1)
    #elif novaidade > 8 and novaidade <=14:
        #peso = random.uniform(30, 80)
        #peso = round(peso,1)
    #elif novaidade > 14:
    peso = random.uniform(30, 120)
    peso = round(peso,1)
    return peso



#-------------------------------------------------------------------------------------------------------------------------------------

def escolaridadePaciente():
    escolaridade = ("nulo","Analfabeto","5º Ano Incompleto","5º Ano Completo","6º ao 9º Ano do Fundamental","Fundamental Completo","Médio Incompleto","Médio Completo","Superior Incompleto","Superior Completo","Mestrado","Doutorado")
    #if idade <= 7:
        #pos = 0
    #elif idade > 7 and idade <= 17:      
        #pos = random.randint(1, 7)
    #elif idade > 17 and idade <=25:
       # pos = random.randint(1,10)
    #else:
    pos = random.randint(1,(len(escolaridade)-1))
    
    return escolaridade[pos]

def Cpf(numero):
    dicCpf = {}
    dicCpf['cpf'] = numero

    return dicCpf
def Rg(numero):
    dicRg ={}
    dicRg['rg'] = numero
    
    return dicRg
b=0
a =0
i = 527932156955
while i< 871130656955:
    repetidasCPF.append(i)
    i=i+114359
    a=a+1

l = 294987593
while l< 984987593:
    repetidasRG.append(l)
    l=l+171
    b=b+1


