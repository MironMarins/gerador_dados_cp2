import csv
import random
with open('T_total\\T_RHSTU_CONSULTA.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaConsulta = list(reader)
with open('T_total\\T_RHSTU_MEDICAMENTO.csv',"r") as csvfile:
                reader = csv.reader(csvfile)
                listaMedicamento = list(reader)



#0 unid hosp
#1 idconsulta
#
def aletorioIdPosologia(lista):
        
        pos = random.randint(1,len(lista)-1)
        return int(lista[pos][0])
        

        

def aletorioDosagem(idMedicamento):
    dosagems = ("1","","5","10","2","2","","1","15","","3","20","3","1","","10","25","","2","30","4","1","",
               "5","12","4","18","3","1","","2","30","8","2","","8","5","1","","15","20","12","4","2","","25","7",
               "10","")
    idMedicamento = int(idMedicamento)
    
    if idMedicamento > 0 and idMedicamento < 2000:
            dosagem = dosagems[0]
    elif idMedicamento >= (2000*1) and idMedicamento < (2000*2):
            dosagem = dosagems[1]
    elif idMedicamento >= (2000*2) and idMedicamento < (2000*3):
            dosagem = dosagems[2]
    elif idMedicamento >= (2000*3) and idMedicamento < (2000*4):
            dosagem = dosagems[3]
    elif idMedicamento >= (2000*4) and idMedicamento < (2000*5):
            dosagem = dosagems[4]
    elif idMedicamento >= (2000*5) and idMedicamento < (2000*6):
            dosagem = dosagems[5]
    elif idMedicamento >= (2000*6) and idMedicamento < (2000*7):
            dosagem = dosagems[6]
    elif idMedicamento >= (2000*7) and idMedicamento < (2000*8):
            dosagem = dosagems[7]
    elif idMedicamento >= (2000*8) and idMedicamento < (2000*9):
            dosagem = dosagems[8]
    elif idMedicamento >= (2000*9) and idMedicamento < (2000*10):
            dosagem = dosagems[9]
    elif idMedicamento >= (2000*10) and idMedicamento < (2000*11):
            dosagem = dosagems[10]
    elif idMedicamento >= (2000*11) and idMedicamento < (2000*12):
            dosagem = dosagems[11]
    elif idMedicamento >= (2000*12) and idMedicamento < (2000*13):
            dosagem = dosagems[12]
    elif idMedicamento >= (2000*13) and idMedicamento < (2000*14):
            dosagem = dosagems[13]
    elif idMedicamento >= (2000*14) and idMedicamento < (2000*15):
            dosagem = dosagems[14]
    elif idMedicamento >= (2000*15) and idMedicamento < (2000*16):
            dosagem = dosagems[15]
    elif idMedicamento >= (2000*16) and idMedicamento < (2000*17):
            dosagem = dosagems[16]
    elif idMedicamento >= (2000*17) and idMedicamento < (2000*18):
            dosagem = dosagems[17]
    elif idMedicamento >= (2000*18) and idMedicamento < (2000*19):
            dosagem = dosagems[18]
    elif idMedicamento >= (2000*19) and idMedicamento < (2000*20):
            dosagem = dosagems[19]
    elif idMedicamento >= (2000*20) and idMedicamento < (2000*21):
            dosagem = dosagems[20]
    elif idMedicamento >= (2000*21) and idMedicamento < (2000*22):
            dosagem = dosagems[21]
    elif idMedicamento >= (2000*22) and idMedicamento < (2000*23):
            dosagem = dosagems[22]
    elif idMedicamento >= (2000*23) and idMedicamento < (2000*24):
            dosagem = dosagems[23]
    elif idMedicamento >= (2000*24) and idMedicamento < (2000*25):
            dosagem = dosagems[24]
    elif idMedicamento >= (2000*25) and idMedicamento < (2000*26):
            dosagem = dosagems[25]
    elif idMedicamento >= (2000*26) and idMedicamento < (2000*27):
            dosagem = dosagems[26]
    elif idMedicamento >= (2000*27) and idMedicamento < (2000*28):
            dosagem = dosagems[27]
    elif idMedicamento >= (2000*28) and idMedicamento < (2000*29):
            dosagem = dosagems[28]
    elif idMedicamento >= (2000*29) and idMedicamento < (2000*30):
            dosagem = dosagems[29]
    elif idMedicamento >= (2000*30) and idMedicamento < (2000*31):
            dosagem = dosagems[30]
    elif idMedicamento >= (2000*31) and idMedicamento < (2000*32):
            dosagem = dosagems[31]
    elif idMedicamento >= (2000*32) and idMedicamento < (2000*33):
            dosagem = dosagems[32]
    elif idMedicamento >= (2000*33) and idMedicamento < (2000*34):
            dosagem = dosagems[33]
    elif idMedicamento >= (2000*34) and idMedicamento < (2000*35):
            dosagem = dosagems[34]
    elif idMedicamento >= (2000*35) and idMedicamento < (2000*36):
            dosagem = dosagems[35]
    elif idMedicamento >= (2000*36) and idMedicamento < (2000*37):
            dosagem = dosagems[36]
    elif idMedicamento >= (2000*37) and idMedicamento < (2000*38):
            dosagem = dosagems[37]
    elif idMedicamento >= (2000*38) and idMedicamento < (2000*39):
            dosagem = dosagems[38]
    elif idMedicamento >= (2000*39) and idMedicamento < (2000*40):
                dosagem = dosagems[39]
    elif idMedicamento >= (2000*40) and idMedicamento < (2000*41):
                dosagem = dosagems[40]
    elif idMedicamento >= (2000*41) and idMedicamento < (2000*42):
                dosagem = dosagems[41]
    elif idMedicamento >= (2000*42) and idMedicamento < (2000*43):
                dosagem = dosagems[42]
    elif idMedicamento >= (2000*43) and idMedicamento < (2000*44):
                dosagem = dosagems[43]
    elif idMedicamento >= (2000*44) and idMedicamento < (2000*45):
                dosagem = dosagems[44]
    elif idMedicamento >= (2000*45) and idMedicamento < (2000*46):
                dosagem = dosagems[45]
    elif idMedicamento >= (2000*46) and idMedicamento < (2000*47):
                dosagem = dosagems[46]
    elif idMedicamento >= (2000*47) and idMedicamento < 200000:
                dosagem = dosagems[47]
    
    
    return dosagem
def aleatorioVia(idMedicamento):
    vias =("oral","epidermal","oral","subcutanea","nasal","oral","epidermal","oral","oral","epidermal","oral","intramuscular","ocular",
          "oral","epidermal","oral","subcutânea","epidermal","oral","intravenosamente","nasal","oral","epitelial","oral","oral","oral",
          "subcutanea","auricular","oral","epitelial","oral","intramuscular","intravenosamente","oral","epitelial","oral","nasal",
          "oral","epitelial","subcutanea","intramuscular","oral","nasal","oral","epidermal","intravenosamente","oral","subcutanea","epidermal")
    idMedicamento = int(idMedicamento)
    
    if idMedicamento > 0 and idMedicamento < 2000:
            via = vias[0]
    elif idMedicamento >= (2000*1) and idMedicamento < (2000*2):
            via = vias[1]
    elif idMedicamento >= (2000*2) and idMedicamento < (2000*3):
            via = vias[2]
    elif idMedicamento >= (2000*3) and idMedicamento < (2000*4):
            via = vias[3]
    elif idMedicamento >= (2000*4) and idMedicamento < (2000*5):
            via = vias[4]
    elif idMedicamento >= (2000*5) and idMedicamento < (2000*6):
            via = vias[5]
    elif idMedicamento >= (2000*6) and idMedicamento < (2000*7):
            via = vias[6]
    elif idMedicamento >= (2000*7) and idMedicamento < (2000*8):
            via = vias[7]
    elif idMedicamento >= (2000*8) and idMedicamento < (2000*9):
            via = vias[8]
    elif idMedicamento >= (2000*9) and idMedicamento < (2000*10):
            via = vias[9]
    elif idMedicamento >= (2000*10) and idMedicamento < (2000*11):
            via = vias[10]
    elif idMedicamento >= (2000*11) and idMedicamento < (2000*12):
            via = vias[11]
    elif idMedicamento >= (2000*12) and idMedicamento < (2000*13):
            via = vias[12]
    elif idMedicamento >= (2000*13) and idMedicamento < (2000*14):
            via = vias[13]
    elif idMedicamento >= (2000*14) and idMedicamento < (2000*15):
            via = vias[14]
    elif idMedicamento >= (2000*15) and idMedicamento < (2000*16):
            via = vias[15]
    elif idMedicamento >= (2000*16) and idMedicamento < (2000*17):
            via = vias[16]
    elif idMedicamento >= (2000*17) and idMedicamento < (2000*18):
            via = vias[17]
    elif idMedicamento >= (2000*18) and idMedicamento < (2000*19):
            via = vias[18]
    elif idMedicamento >= (2000*19) and idMedicamento < (2000*20):
            via = vias[19]
    elif idMedicamento >= (2000*20) and idMedicamento < (2000*21):
            via = vias[20]
    elif idMedicamento >= (2000*21) and idMedicamento < (2000*22):
            via = vias[21]
    elif idMedicamento >= (2000*22) and idMedicamento < (2000*23):
            via = vias[22]
    elif idMedicamento >= (2000*23) and idMedicamento < (2000*24):
            via = vias[23]
    elif idMedicamento >= (2000*24) and idMedicamento < (2000*25):
            via = vias[24]
    elif idMedicamento >= (2000*25) and idMedicamento < (2000*26):
            via = vias[25]
    elif idMedicamento >= (2000*26) and idMedicamento < (2000*27):
            via = vias[26]
    elif idMedicamento >= (2000*27) and idMedicamento < (2000*28):
            via = vias[27]
    elif idMedicamento >= (2000*28) and idMedicamento < (2000*29):
            via = vias[28]
    elif idMedicamento >= (2000*29) and idMedicamento < (2000*30):
            via = vias[29]
    elif idMedicamento >= (2000*30) and idMedicamento < (2000*31):
            via = vias[30]
    elif idMedicamento >= (2000*31) and idMedicamento < (2000*32):
            via = vias[31]
    elif idMedicamento >= (2000*32) and idMedicamento < (2000*33):
            via = vias[32]
    elif idMedicamento >= (2000*33) and idMedicamento < (2000*34):
            via = vias[33]
    elif idMedicamento >= (2000*34) and idMedicamento < (2000*35):
            via = vias[34]
    elif idMedicamento >= (2000*35) and idMedicamento < (2000*36):
            via = vias[35]
    elif idMedicamento >= (2000*36) and idMedicamento < (2000*37):
            via = vias[36]
    elif idMedicamento >= (2000*37) and idMedicamento < (2000*38):
            via = vias[37]
    elif idMedicamento >= (2000*38) and idMedicamento < (2000*39):
            via = vias[38]
    elif idMedicamento >= (2000*39) and idMedicamento < (2000*40):
                via = vias[39]
    elif idMedicamento >= (2000*40) and idMedicamento < (2000*41):
                via = vias[40]
    elif idMedicamento >= (2000*41) and idMedicamento < (2000*42):
                via = vias[41]
    elif idMedicamento >= (2000*42) and idMedicamento < (2000*43):
                via = vias[42]
    elif idMedicamento >= (2000*43) and idMedicamento < (2000*44):
                via = vias[43]
    elif idMedicamento >= (2000*44) and idMedicamento < (2000*45):
                via = vias[44]
    elif idMedicamento >= (2000*45) and idMedicamento < (2000*46):
                via = vias[45]
    elif idMedicamento >= (2000*46) and idMedicamento < (2000*47):
                via = vias[46]
    elif idMedicamento >= (2000*47) and idMedicamento < 200000:
                via = vias[47]
    
    return via
def aleatorioPosologia(idMedicamento):
    posologias = ("Tome comprimido a cada 8 horas.", 
    "Aplique uma fina camada na área afetada, duas vezes ao dia.", 
    "Administre  em ml do medicamento a cada 4 horas, conforme necessário.", 
    "Injete em unidades subcutaneamente todas as manhãs.", 
    "Use pulverizações nas narinas, a cada 6 horas.", 
    "Tome cápsulas antes das refeições, três vezes ao dia.", 
    "Aplique o creme topicamente na pele, a cada 12 horas.", 
    "Engula colher de sopa do xarope a cada 4 horas.", 
    "Administre gotas, a cada 6 horas.", 
    "Aplique uma camada generosa na área afetada, de manhã e à noite.", 
    "Tome comprimidos de uma vez, a cada 12 horas.", 
    "Injete em mg intramuscularmente, conforme necessário.", 
    "Use pulverizações em cada olho, duas vezes ao dia.",
    "Tome comprimido a cada 6 horas durante a febre.",
    "Aplique o gel topicamente, de acordo com a necessidade.", 
    "Engula em ml do líquido, duas vezes ao dia.", 
    "Administre unidades por via subcutânea, uma vez ao dia.", 
    "Aplique uma fina camada na pele afetada, de manhã e à noite.", 
    "Tome colheres de chá a cada 8 horas.", 
    "Injete em mg intravenosamente, conforme indicado.", 
    "Use pulverizações nas narinas, a cada 4 horas.", 
    "Tome cápsula antes de dormir, diariamente.", 
    "Aplique o creme na área afetada, de acordo com a prescrição.", 
    "Engula em ml do xarope, a cada 6 horas.", 
    "Administre em gotas por via oral, a cada 8 horas.", 
    "Tome comprimidos a cada 12 horas durante o tratamento.", 
    "Injete em unidades subcutaneamente, conforme necessário.", 
    "Use pulverizações em cada ouvido, duas vezes ao dia.", 
    "Tome comprimido a cada 4 horas, se a dor persistir.", 
    "Aplique uma camada espessa na pele afetada, de manhã e à noite.", 
    "Engula colheres de sopa do líquido, três vezes ao dia.", 
    "Administre em mg por via intramuscular, uma vez ao dia.", 
    "Injete unidades intravenosamente, conforme indicado.", 
    "Tome cápsulas antes das refeições, duas vezes ao dia.", 
    "Aplique o gel na área afetada, conforme a necessidade.", 
    "Engula em ml do xarope, a cada 6 horas.", 
    "Use pulverizações nas narinas, a cada 4 horas.", 
    "Tome comprimido a cada 6 horas, conforme a dor.", 
    "Aplique uma camada generosa na pele, duas vezes ao dia.", 
    "Injete unidades subcutaneamente, conforme necessário.", 
    "Administre em mg intramuscularmente, uma vez ao dia.", 
    "Engula em gotas por via oral, a cada 8 horas.", 
    "Use pulverizações nas narinas, de acordo com a necessidade.", 
    "Tome colheres de chá a cada 4 horas.", 
    "Aplique o creme na área afetada, duas vezes ao dia.", 
    "Injete em mg intravenosamente, conforme indicado.", 
    "Engula em ml do líquido, a cada 6 horas.", 
    "Administre unidades por via subcutânea, a cada 12 horas.", 
    "Aplique uma camada fina na pele, a cada 6 horas.")
    
    
    idMedicamento = int(idMedicamento)
    
    if idMedicamento > 0 and idMedicamento < 2000:
            posologia = posologias[0]
    elif idMedicamento >= (2000*1) and idMedicamento < (2000*2):
            posologia = posologias[1]
    elif idMedicamento >= (2000*2) and idMedicamento < (2000*3):
            posologia = posologias[2]
    elif idMedicamento >= (2000*3) and idMedicamento < (2000*4):
            posologia = posologias[3]
    elif idMedicamento >= (2000*4) and idMedicamento < (2000*5):
            posologia = posologias[4]
    elif idMedicamento >= (2000*5) and idMedicamento < (2000*6):
            posologia = posologias[5]
    elif idMedicamento >= (2000*6) and idMedicamento < (2000*7):
            posologia = posologias[6]
    elif idMedicamento >= (2000*7) and idMedicamento < (2000*8):
            posologia = posologias[7]
    elif idMedicamento >= (2000*8) and idMedicamento < (2000*9):
            posologia = posologias[8]
    elif idMedicamento >= (2000*9) and idMedicamento < (2000*10):
            posologia = posologias[9]
    elif idMedicamento >= (2000*10) and idMedicamento < (2000*11):
            posologia = posologias[10]
    elif idMedicamento >= (2000*11) and idMedicamento < (2000*12):
            posologia = posologias[11]
    elif idMedicamento >= (2000*12) and idMedicamento < (2000*13):
            posologia = posologias[12]
    elif idMedicamento >= (2000*13) and idMedicamento < (2000*14):
            posologia = posologias[13]
    elif idMedicamento >= (2000*14) and idMedicamento < (2000*15):
            posologia = posologias[14]
    elif idMedicamento >= (2000*15) and idMedicamento < (2000*16):
            posologia = posologias[15]
    elif idMedicamento >= (2000*16) and idMedicamento < (2000*17):
            posologia = posologias[16]
    elif idMedicamento >= (2000*17) and idMedicamento < (2000*18):
            posologia = posologias[17]
    elif idMedicamento >= (2000*18) and idMedicamento < (2000*19):
            posologia = posologias[18]
    elif idMedicamento >= (2000*19) and idMedicamento < (2000*20):
            posologia = posologias[19]
    elif idMedicamento >= (2000*20) and idMedicamento < (2000*21):
            posologia = posologias[20]
    elif idMedicamento >= (2000*21) and idMedicamento < (2000*22):
            posologia = posologias[21]
    elif idMedicamento >= (2000*22) and idMedicamento < (2000*23):
            posologia = posologias[22]
    elif idMedicamento >= (2000*23) and idMedicamento < (2000*24):
            posologia = posologias[23]
    elif idMedicamento >= (2000*24) and idMedicamento < (2000*25):
            posologia = posologias[24]
    elif idMedicamento >= (2000*25) and idMedicamento < (2000*26):
            posologia = posologias[25]
    elif idMedicamento >= (2000*26) and idMedicamento < (2000*27):
            posologia = posologias[26]
    elif idMedicamento >= (2000*27) and idMedicamento < (2000*28):
            posologia = posologias[27]
    elif idMedicamento >= (2000*28) and idMedicamento < (2000*29):
            posologia = posologias[28]
    elif idMedicamento >= (2000*29) and idMedicamento < (2000*30):
            posologia = posologias[29]
    elif idMedicamento >= (2000*30) and idMedicamento < (2000*31):
            posologia = posologias[30]
    elif idMedicamento >= (2000*31) and idMedicamento < (2000*32):
            posologia = posologias[31]
    elif idMedicamento >= (2000*32) and idMedicamento < (2000*33):
            posologia = posologias[32]
    elif idMedicamento >= (2000*33) and idMedicamento < (2000*34):
            posologia = posologias[33]
    elif idMedicamento >= (2000*34) and idMedicamento < (2000*35):
            posologia = posologias[34]
    elif idMedicamento >= (2000*35) and idMedicamento < (2000*36):
            posologia = posologias[35]
    elif idMedicamento >= (2000*36) and idMedicamento < (2000*37):
            posologia = posologias[36]
    elif idMedicamento >= (2000*37) and idMedicamento < (2000*38):
            posologia = posologias[37]
    elif idMedicamento >= (2000*38) and idMedicamento < (2000*39):
            posologia = posologias[38]
    elif idMedicamento >= (2000*39) and idMedicamento < (2000*40):
                posologia = posologias[39]
    elif idMedicamento >= (2000*40) and idMedicamento < (2000*41):
                posologia = posologias[40]
    elif idMedicamento >= (2000*41) and idMedicamento < (2000*42):
                posologia = posologias[41]
    elif idMedicamento >= (2000*42) and idMedicamento < (2000*43):
                posologia = posologias[42]
    elif idMedicamento >= (2000*43) and idMedicamento < (2000*44):
                posologia = posologias[43]
    elif idMedicamento >= (2000*44) and idMedicamento < (2000*45):
                posologia = posologias[44]
    elif idMedicamento >= (2000*45) and idMedicamento < (2000*46):
                posologia = posologias[45]
    elif idMedicamento >= (2000*46) and idMedicamento < (2000*47):
                posologia = posologias[46]
    elif idMedicamento >= (2000*47) and idMedicamento < 200000:
                posologia = posologias[47]
        
    return posologia
    






