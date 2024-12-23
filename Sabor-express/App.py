import os

lista_de_restaurantes = [{"nome":"Pizzaria suprema", "categoria":"pizzaria", "ativo":False},
                         {"nome":"Praça", "categoria":"italiana", "ativo":True}]



def iniciar_programa():

    print("͓̽🍺🥂🍸 𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼 🍻🍷🍹\n")

    print("Cadastras Restaurante - 1")
    print("Listar Restaurantes - 2")
    print("Ativar restaurante - 3")
    print("Sair - 4")

def escolha():

    try:

        user_choice = int(input("Escolha uma opção: "))
        if user_choice == 1:
            cadastrar_restaurante()
            
        elif user_choice == 2:
            listar_restaurantes()
        elif user_choice == 3:
            ativar_restaurante()
        elif user_choice == 4:
            finalizar_programa()
        else:
            opcao_invalida()

    except:
        opcao_invalida()


def cadastrar_restaurante():
    os.system("cls")
    nome_restaurante = str(input("digite o nome do restaurante: "))
    categoria_restaurante = str(input("Digite o a categoria do restaurante: "))
    dados_restaurante = {
        "nome":nome_restaurante,
        "categoria":categoria_restaurante,
        "ativo":False
    }
    lista_de_restaurantes.append(dados_restaurante)
    input(f"{nome_restaurante} cadastrado com sucesso\nDigite qualquer tecla para voltar ao menu principal")
    main()
def ativar_restaurante():
    os.system("cls")
    nome_restaurante = str(input("Digite o nome do restaurante que deseja ativar: "))
    for restaurante in lista_de_restaurantes:
        if restaurante["nome"] == nome_restaurante:
            if restaurante["ativo"] == False:
                restaurante["ativo"] = True
                input(f"Restaurante: {restaurante["nome"]} ativado com sucesso")
                main()
            elif restaurante["ativo"] == True:
                restaurante["ativo"] = False
                input(f"Restaurante: {restaurante["nome"]} desativado")
                main()
    input("Nenhum restaurante encontrado aperte enter para voltar ao menu principal")
    main()
def listar_restaurantes():
    os.system("cls")
    for restaurante in lista_de_restaurantes:
        print(f" - {restaurante["nome"]} / {restaurante["ativo"]}")
    input("Digite enter para voltar ao menu principal")
    main()
    
def opcao_invalida():

    input("Opção inválida \ndigite uma tecla para voltar ao menu principal")
    main()

def finalizar_programa():
    os.system("cls")
    print("Finalizando programa")

def main():
    os.system("cls")
    iniciar_programa()
    escolha()

if __name__ == "__main__":
    main()