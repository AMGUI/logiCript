from diexececao import exececao

# ====================DESCRIÇÃO=============================
# ESSA FUNÇÃO TEM COMO OBJETIVO RECEBER A LINHA, QUEBRAS A LINHA EM PALAVRAS
# E DEPOIS EM LETRAS RETORNA AS LETRAS DAS PALAVRAS QUEBRADAS 
def colunarL(linha,cont,vDeVerica)->list: #CONT = QUAL PALAVRA DEVE SER QUEBRADA
# =================DECLARACAO DE VARIAVEIS===================    
    lista_linha = list()
    lista_palavra = list()
    i = int(0)
# ======================fIM =================================
    
    lista_linha.append(linha.split()) #tranfomando os elementos da linha para lista 
    lista_linha = lista_linha[0] #!!Trata tiva para tirar a linha do elemento [[pala]] = [pala] !!
    i = len(lista_linha[cont])
    #===funçõa de exceção para n ser criptografado ============
    vDeVerica = exececao(lista_linha[cont],vDeVerica)

    #================FIm================
    if vDeVerica == "C":
        for x in range(0,i):
            lista_palavra.append(lista_linha[cont][x:x+1])

    if vDeVerica == "D":
        for x in range(0,i,4):
            lista_palavra.append(lista_linha[cont][x:x+4])

    if vDeVerica == "X":
        lista_palavra.append(lista_linha[cont])       
   
    return lista_palavra


# ======================DESCRIÇÃO===========================
# ESSA FUNÇÃO TEM COMO OBJETIVO CONTAR QUANTO PALAVRAS EXISTE 
# NA LINHA E RETORNA UM INTEIRO DE QUANTAS PALAVRAS 
def contar (linha) -> int:
   
    # =================DECLARACAO DE VARIAVEIS===================    
    lista_linha = list()
    cont = int(0)
    # ======================fIM =================================
    
    lista_linha.append(linha.split()) #tranfomando os elementos da linha para lista 
    lista_linha = lista_linha[0] #TRATATIVA PARA TIRA O ELEMETO DOS []
    cont = len(lista_linha)
    return cont