# ====================DESCRIÇÃO=============================
# ESSA FUNÇÃO TEM COMO OBJETIVO FAZER O RETORNO DO ARQUIVO  
# CRIPITOGRAFADO TRAZENDO O ARQUIVO LEGIVEL 
# ESSA FUNÇÃO RETORNA A VARIAVEL BOOL PARA FUNÇÃO PRINCIPAL

# ================IMPORTAÇÃO DE FUNÇÕES=====================
from calculofato import fati
from  cript import cript, escrever, veris
from conteinerdearq import colunarL, contar
# =========================fIM ==============================

def chavedesc (banco ,ini , fim)->bool :

 # =================DECLARACAO DE VARIAVEIS===================   
    Arq_cript = list() # lista do arquivo criptografado
    dic = list() # dicionario de dados 
    Axiliar = list() # lista axiliar
    local  = '테스트.txt' #local do nome do arquivo
    cont:int
    frase = str()
    vDeVerica = "D"
 # =========================fIM ==============================
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