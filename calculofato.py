# ====================DESCRIÇÃO=============================
# ESSA FUNÇÃO TEM COMO OBJETIVO FAZER A TROCA DAS PALVRAS PASSADAS 
# PARA AS NOVAS PALAVRAS QUE ESTÃO CONTIDAS NA VARIAVEL lista
# A VARIAVEL LISTA RECEBE OS DADOS DO ARQUIVO TXT DICDADOS

# ================IMPORTAÇÃO DE FUNÇÕES=====================
from listar_pala import palaLista #!!!!!!!!!!!verifivacar se essa função esta em uso !!!!!!
from listar_pala import retfinal
# =========================fIM ==============================
#int ini = 2 int fim = 6
def fati(tabela , lista , ini , fim, vDeVerica) ->str:
   #tabela = aquivo crip
   #lista = dicionario

# ==============DECLARACAO DE VARIAVEIS ================
   num = len(tabela) #contando quantos elementos tem na lista
   palavra = str()
   nlista =list()
# ======================fIM ============================

   for x in range(0,num): #Lupe para todas as palavras sejam trocadas 
    
    # ==============DECLARANDO VARIAVEIS ================
     i = int(1)
     if vDeVerica == "C":
      vAxiliar = tabela[x]
      sub2 =  str (lista[0][0:1])

     if vDeVerica == "D":
        vAxiliar = tabela[x]
        sub2 =  str (lista[0][ini:fim])
    # ======================fIM ============================
     
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
        
   if len(nlista) == 0 :
      return vAxiliar

   palavra = retfinal(nlista, len(nlista))     
   
   return palavra

