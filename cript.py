# ====================DESCRIÇÃO=============================
# ESSA FUNÇÃO TEM COMO OBJETIVO ABRIR UM ARQUIVO TXT E CRIAR UMA LISTA
# NO FORMATO STR FAZER A TRATATIVA DA PALAVRA E RETORNAR NO FORMATO
# LISTA EX: 'SB1' RETORNA ['S','B','1']


# ================IMPORTAÇÃO DE FUNÇÕES=====================
from calculofato import fati
from pathlib import Path
# =========================fIM ==============================

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
     arquivo = open('테스트.txt', 'w')
    if vDeVerica == "D":
     arquivo = open('teste.txt', 'w')    
    arquivo.write(frase)
    arquivo.close()   

# ====================DESCRIÇÃO=============================
# ESSA FUNÇÃO TEM COMO OBJETIVO VERIFICAR SE O ARQUIVO COM NOME '테스트.txt' EXISTE
# CASO EXISTA O RETORNO DA FUNÇÃO É VERDADEIRO CASO NÃO EXITA RETORNARA FALSO 
def veris()-> bool :
  file = Path('테스트.txt') #OBTENDO O LOCADO ARQUIVO
  isFile = file.is_file() #VERIFICANDO SE O ARQUIVO EXISTE E RETORNADO O VALOR V OU F 
  return isFile # RETONO DA VARIAVEL 
    
    