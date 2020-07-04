import os.path

def menu(local) ->str:
    x = bool(True)
    
    
    while(x):
       
        if False == (os.path.exists(local)):
            print("ERRO ARQUIVO NÃO EXISTE ")
            local = input("Porfavor digite o local arquivo: ")
        else:
            x = False

    return local