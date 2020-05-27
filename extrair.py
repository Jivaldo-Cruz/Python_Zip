from zipfile import ZipFile
import os
import glob


name_file = []
name_compac = []

def listar_desc():
    for arq in glob.iglob("*.zip"):
        name_file.append(arq)

    if(name_file == []):
        print("Não existem nenhum arquivo compactado...")
    else:
        print("Todos arquivos criado...")
        for al in name_file:
            print(al)
            
def listar_criar():
    for arq in glob.iglob("*"):
        name_compac.append(arq)

    if(name_compac == []):
        print("Não existem nenhum arquivo compactado...")
    else:
        print("Todos arquivos criado...")
        for al in name_compac:
            print(al)
    

def criar():
    listar_criar()
    print(f"{'='*17}")
    try:
        nome = str(input("Qual dos arquivo queres compactar[0 -> close]: "))
        if(nome == "0"):
                return False#para fechar programa
        with ZipFile(f"arquivo_comprimido{len(name_compac)}.zip", "w") as extra:
            extra.write(nome)
        extra.close()
        print("Arquivo comprimido com sucesso!")
    except FileNotFoundError:
        print("Desculpa, mas o nome não encaixa!")


def descomapactar():
    listar_desc()
    print(f"{'='*17}")
    while True:
        try:
            nome = str(input("Qual dos arquivo queres descompactar[0 -> close]: "))
            if(nome == "0"):
                return False#para fechar programa
            with ZipFile(nome, "r") as extra:
                extra.printdir()
                extra.extractall()
                extra.close()
                print("Arquivo descompactado com sucesso!")
                break
        except FileNotFoundError:
            print("Desculpa, mas o nome não encaixa!")
            


def main():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("1. Criar compactação | 2. Descompactar Arquivo")
            valor = int(input("Insira valor[0 -> close]: "))
            if(valor == 1):
                criar()
                input("Preciona qualquer tecla para continuar...")
                os.system("cls" if os.name == "nt" else "clear")
                main()
            elif(valor == 2):
                descomapactar()
                input("Preciona qualquer tecla para continuar...")
                os.system("cls" if os.name == "nt" else "clear")
                main()
            elif(valor == 0):
                os.system("cls" if os.name == "nt" else "clear")
                break
        except ValueError:
            print("Só pode usar número!")

main()#executar algoritmo
