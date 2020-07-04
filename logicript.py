# ======================DESCRIÇÃO===========================
#ESSA FUNÇÃO TEM COMO OBJETIVO SER A FUNÇÃO PRINCIPAL 
#REALIZARA AS CHAMADAS DAS OUTRAS FUNÇÕES E TRIBUÇOES 
#DOS VALORES DAS VARIAVEIS, LISTAS E ARQUIVOS 

# ================IMPORTAÇÃO DE FUNÇÕES=====================
from calculofato import fati
from  cript import cript, escrever, veris
from conteinerdearq import colunarL, contar
from descrip import chavedesc
from Menu import menu

# =========================fIM ==============================

# =================DECLARACAO DE VARIAVEIS===================
#tabe = [ 'SA1','SB1','SB2','SX1'] # lista  tabelas com as tabelas que serão crip
cont = int(0)
cont2 = int(0)
ini = int(2)
fim = int(6)
tabe = list()
indice = int(0)
Llista = list()
palavra = str()
local:str
arquivo_protheus = list()
banco = str('dicdados.txt')
frase = str()
vDeVerica = "C"
bull = False
bVer:bool
# =========================fIM ==============================

Llista = cript(banco) #passando a tabela para a lista
#local = 'arquivotest.txt'
local = input("Porfavor digite o local arquivo: ")
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
    # =========================fIM ==============================    

