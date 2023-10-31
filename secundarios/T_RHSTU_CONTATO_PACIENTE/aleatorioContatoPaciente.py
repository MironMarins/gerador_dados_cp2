import csv
import random
with open('T_total\\T_RHSTU_PACIENTE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPacientes = list(reader)
with open('T_total\\T_RHSTU_PLANO_SAUDE.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaPlanoSaude = list(reader)

def idsContatosPacientes(lista):
    idsPlanoSaude=[]
    lista = lista
    c=1
    while c < len(lista):
            idsPlanoSaude.append(lista[c][0])
            c+=1
    pos = random.randint(0, (len(idsPlanoSaude)-1))
    return idsPlanoSaude[pos]

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



def verificacaoContatos(nome):
    idcontatoF =("2","3","5","6")
    idcontatoM =("1","4","6")
    
    nomesFemininos =("Maria","Ana","Laura","Sofia","Isabella","Helena","Valentina","Luísa",
                     "Giovanna","Alice","Clara","Camila","Beatriz","Julia","Manuela","Mariana",
                     "Gabriela","Rafaela","Carolina","Joana","Amanda","Letícia","Vitória","Emanuela",
                     "Bruna","Renata","Isadora","Lívia","Eloísa","Thais","Roberta","Júlia","Marta","Andrea",
                     "Vanessa","Bárbara","Flávia","Natália","Bianca","Fernanda","Raquel","Daniela","Patrícia",
                     "Juliana","Débora","Larissa","Verônica","Renata","Adriana","Cláudia")
    if nome in nomesFemininos:
       pos = random.randint(0, (len(idcontatoF)-1))
       contato = idcontatoF[pos]
    else:
        pos = random.randint(0,(len(idcontatoM)-1))     
        contato = idcontatoM[pos]
    return contato

def Ddd():
    numeros = ("11","12","13","14","15","16","17","18","19","21","22","24","27","28","31","32",
               "33","34","35","37","38","41","42","43","44","45","46","47","48","49","51","53","54","55","61","62",
               "63","64","65","66","67","68","69","71","73","74","75","77","79","81","82","83","84","85","86","87","88",
               "89","91","92","93","94","95","96","97","98","99")
    pos = random.randint(0, (len(numeros)-1))
    return numeros[pos]

def Tel():
    
    
    numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    i = 0
    num = ""
    chance = random.randint(0, (len(numeros)-1))
    if chance < 6:
        while i < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            i = i + 1
        num = "9"+ num 
    else:
        while i < 8:
            pos = random.randint(0, (len(numeros)-1))
            num = num + str(pos)
            i = i + 1
    return num
#1,Pai,2016-5-4,None,2023-10-16,Miron
#2,Mãe,2020-9-26,None,2023-10-16,Miron
#3,Esposa,2019-8-26,None,2023-10-16,Miron
#4,Primo,2013-1-11,None,2023-10-16,Miron
#5,Prima,2019-12-20,None,2023-10-16,Miron
#6,Outros contatos,2022-9-17,None,2023-10-16,Miron