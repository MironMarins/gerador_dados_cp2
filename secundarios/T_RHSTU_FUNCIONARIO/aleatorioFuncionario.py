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


presidente = 0
diretor= 1
gerente= 28
coordenador= 325
funcionario1= 2998

def Salario(cargo):
    if cargo == "presidente":
        salario = random.uniform(150000.9,200000.9)
        salario = round(salario,2)
    elif cargo == "diretor":
         salario = random.uniform(75000.9,100000.9)
         salario = round(salario,2)
    elif cargo == "gerente":
         salario = random.uniform(40000.9,60000.9)
         salario = round(salario,2)
    elif cargo == "coordenador":
         salario = random.uniform(25000.9,35000.9)
         salario = round(salario,2)
    elif cargo == "funcionario":
         salario = random.uniform(10000.9,20000.9)
         salario = round(salario,2)
    
    return salario

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