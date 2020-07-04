# ====================DESCRIÇÃO=============================
#ESSA FUNÇÃO TEM COMO OBJETIVO RECEBER COMO PARAMETO UM PALAVRA
#NO FORMATO STR FAZER A TRATATIVA DA PALAVRA E RETORNAR NO FORMATO
# LISTA EX: 'SB1' RETORNA ['S','B','1']

def palaLista (palavra) -> list:
    # ==============DECLARACAO DE VARIAVEIS ================
    nLista = list()
    i = len(palavra)
    cont = int(0)
    # ======================fIM ============================
    
    for palavra in range(0,i):
        nLista.append(palavra[cont:cont+1]) 
        cont +=1

    return nLista

# ====================DESCRIÇÃO=============================
# ESSA FUNÇÃO TEM COMO OBJETIVO UNIR AS LETRAS DA LISTA EM
# UMA UNICA VAIRAVEL STR 

def retfinal (lista,num)->str:
   nPalavra = str() 
   for x in range(0,num):
    nPalavra = nPalavra + lista[x]

   #print("resut final: {}".format(nPalavra))
   return nPalavra
   