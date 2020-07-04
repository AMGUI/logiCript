# ======================DESCRIÇÃO===========================
# ESSA FUNÇÃO TEM COMO OBJETIVO DE VERIFIVCAR E CRIAR 
# UM DICINARIO DE EXEÇÕES NOS QUAIS NÃO SERÃO CRIPTOGRAFADOS  
# RETORNA UM STR "X" CASO CONDICAO SEJA VERDADEIRA 

from cript import cript

def exececao(palavra,vDeVerica) -> str:
    #dic = ["SELECT","GROUP","BY","AS","ON","FROM","WITH","JOIN","LEFT","INNER","WHERE","THEN","ELSE","IF","CASE","AND","SUM","WHEN","CREATE","VIEW"]
    dic = list()
    arquivo = open("dicionario_de excecao.txt",'r')
    dic = arquivo.readlines()
    arquivo.close()
    Alx = str(dic[0])
    dic = Alx.split(',')
    
    for x in range(0,len(dic)):
        if palavra == dic[x]:
            vDeVerica = "X"
            return vDeVerica

    return vDeVerica
