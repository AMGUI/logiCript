
import cript

def abrir(nome_arq):

    narq = open(nome_arq, 'w')
    print('ARQUIVO NÃO EXISTE')
    print('ARQUIVO CRIADO COM SUCESSO ')
    narq.close()

    narq = open(nome_arq,'r+')
    print(narq)
    texto = str(input('Digite um texto a ser criptografado: '))
    cript.alfa(texto)
    narq.close()





