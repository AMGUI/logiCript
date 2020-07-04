import os.path
from pathlib import Path

def cript (local) ->list:
    #tabelas_pro = [ 'SA1','SB1','SB2','SF4']
    Llista = list()  #criando lista para receber o dicionario
    arquivo = open(local, 'r') # abrindo aquivo 
    Llista  = arquivo.readlines() # readlines lista recebe as linas do arquivo 
    arquivo.close() # fechando arquivo
    #fati(tabelas_pro[1],Llista)
    return Llista
    
def escrever(frase,vDeVerica):
    if vDeVerica == "C":
     arquivo = open('C:\\CCPy\\테스트.txt', 'w')
    if vDeVerica == "D":
     arquivo = open('C:\\CCPy\\descript.txt', 'w')
    arquivo.write(frase)
    arquivo.close()   

def veris()-> bool :
  file = Path('C:\\CCPy\\테스트.txt') #OBTENDO O LOCADO ARQUIVO
  isFile = file.is_file() #VERIFICANDO SE O ARQUIVO EXISTE E RETORNADO O VALOR V OU F 
  return isFile # RETONO DA VARIAVEL 

def fati(tabela , lista , ini , fim, vDeVerica) ->str:
   #tabela = aquivo crip
   #lista = dicionario


   num = len(tabela) #contando quantos elementos tem na lista
   palavra = str()
   nlista =list()  


   for x in range(0,num): #Lupe para todas as palavras sejam trocadas 
    
    
     i = int(1)
     if vDeVerica == "C":
      vAxiliar = tabela[x]
      sub2 =  str (lista[0][0:1])

     if vDeVerica == "D":
        vAxiliar = tabela[x]
        sub2 =  str (lista[0][ini:fim])
   
     
     if vAxiliar != sub2: #compara rativo do primeiro momento 'S' é fiferente de 'A'
          
          #lupe usado para percor e compara todas as palavras do arquivo             
          while i < len(lista): # i é maior que tamanho total de linhas do arquivo 
           
           if vDeVerica == "C": 
            sub2 = lista[i][0:1] #indo para a proxima palavra da linha i no arquivo 
            if vAxiliar == sub2: # S = B                       
             nlista.append(lista[i][ini:fim]) # adicionado a palavra trocada 'S' POR '108'
             i=len(lista) #Finalizar a busca 

           if vDeVerica == "D":
            sub2 =  lista[i][ini:fim]
            if vAxiliar == sub2: # S = B                       
             nlista.append(lista[i][0:1]) # adicionado a palavra trocada 'S' POR '108'
             i=len(lista) #Finalizar a busca 
                       
           i += 1
               
     elif vAxiliar == sub2:
        #print("sãõ iguais ")
        if vDeVerica == "C":
         nlista.append(lista[i][ini:fim])
        
        if vDeVerica == "D":
         nlista.append(lista[i][0:1])

     else:
        print("ERRO palavra não encontrada")
        break
        
   
   palavra = retfinal(nlista, len(nlista))     
   
   return palavra  

def colunarL(linha,cont,vDeVerica)->list: #CONT = QUAL PALAVRA DEVE SER QUEBRADA
    
    lista_linha = list()
    lista_palavra = list()
    i = int(0)

    
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

def contar (linha) -> int:
   
    # =================DECLARACAO DE VARIAVEIS===================    
    lista_linha = list()
    cont = int(0)
    # ======================fIM =================================
    
    lista_linha.append(linha.split()) #tranfomando os elementos da linha para lista 
    lista_linha = lista_linha[0] #TRATATIVA PARA TIRA O ELEMETO DOS []
    cont = len(lista_linha)
    return cont

def chavedesc (banco ,ini , fim)->bool :

  
    Arq_cript = list() # lista do arquivo criptografado
    dic = list() # dicionario de dados 
    Axiliar = list() # lista axiliar
    local  = '테스트.txt' #local do nome do arquivo
    cont:int
    frase = str()
    vDeVerica = "D"

    Arq_cript = cript(local)
    dic = cript(banco)    
    #cont = len(Arq_cript)
   
    for j in range (0, len(Arq_cript)):
      cont = contar(Arq_cript[j])
      
      for x in range(0, cont):
         Axiliar = colunarL(Arq_cript[j],x,vDeVerica)
         palavra = fati(Axiliar,dic, ini, fim, vDeVerica)
         frase = frase + palavra + " " 
      frase = frase + "\n"
      print(frase)
      escrever(frase,vDeVerica)        

    return True

def exececao(palavra,vDeVerica) -> str:
    #dic = ["SELECT","GROUP","BY","AS","ON","FROM","WITH","JOIN","LEFT","INNER","WHERE","THEN","ELSE","IF","CASE","AND","SUM","WHEN","CREATE","VIEW"]

    dic = list()
    global lDicionarioex
    x = bool(True)    
    
    while(x):
       
        if False == (os.path.exists( lDicionarioex)):
            print("ERRO ARQUIVO NÃO EXISTE ")
            lDicionarioex = input("Porfavor digite o local do dicionario de excecao: ")
        else:
            x = False

    arquivo = open(lDicionarioex,'r')
    dic = arquivo.readlines()
    arquivo.close()
    Alx = str(dic[0])
    dic = Alx.split(',')

    for x in range(0,len(dic)):
        if palavra == dic[x]:
            vDeVerica = "X"
            return vDeVerica
      

    return vDeVerica        

def menu(local) ->str:
    x = bool(True)
    
    
    while(x):
       
        if False == (os.path.exists(local)):
            print("ERRO ARQUIVO NÃO EXISTE ")
            local = input("Porfavor digite o local arquivo: ")
        else:
            x = False

    return local

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

def retfinal (lista,num)->str:
   nPalavra = str() 
   for x in range(0,num):
    nPalavra = nPalavra + lista[x]

   #print("resut final: {}".format(nPalavra))
   return nPalavra
   

cont = int(0)
cont2 = int(0)
ini = int(2)
fim = int(4)
tabe = list()
indice = int(0)
Llista = list()
palavra = str()
local:str
lDicionarioex:str
arquivo_protheus = list()
banco = str('C:\\CCPy\\dicdados.txt')
frase = str()
saida = str('')
vDeVerica = "C"
bull = False
bVer:bool
# =========================fIM ==============================
while(saida != "SAIR"):
    Llista = cript(banco) #passando a tabela para a lista
    #local = 'arquivotest.txt'
    local = input("Porfavor digite o local arquivo: ")
    lDicionarioex = input("Porfavor digite o local do dicionario de excecao: ")
    local = menu(local)

    arquivo_protheus = cript(local) # obtendo as informções do arquivo chamado
    cont2 = len(arquivo_protheus) # recebendo o tamanho em linhas do arquivo 
    bVer = veris() #RETORNA NA VERDADIRO SE O ARQUIVO CRIPTOGRAFADO EXISTIR 

    if bVer: #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        bVer = chavedesc(banco, ini ,fim)
            
    if bVer == False:
        # =======================lupe para criptografar linhas ==============================

        for j in range(0,cont2): # LUPE PERCORRE TODAS AS LINAHS DO AQUIVO 
            if bull != True: 
                cont = contar(arquivo_protheus[j]) #PASANDO ALINHA j PARA CONTAR QUANTAS PALAVRAS NELA
                bull = True # TRATATIVA PARA N SER CONTADO  ATE QUE TODA A LINHA J SEJA TRATADA

            # para teste
            print(arquivo_protheus[j])

            # =======================lupe para criptografar as palavras ==============================
            for x in range(0, cont):
                tabe = colunarL(arquivo_protheus[j],x,vDeVerica) #!!Da para otimizar!!
                if  len(tabe)>1:
                    palavra = fati(tabe,Llista,ini,fim,vDeVerica)
                    frase = frase + palavra + " "
                else:
                    palavra =  tabe[0]  
                    frase = frase + palavra + " " 
            # =========================fIM ===========================================================

            frase = frase + "\n"

            print("Resultado do retorno no algoritimo logicpt: {}".format(frase))
            escrever(frase,vDeVerica)
            bull = False
    saida = input("digite 'SAIR' para finalizar ou qualquer tecla para continuar: \n")