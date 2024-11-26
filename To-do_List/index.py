
from gerenciadorDeTarefas import Lista_de_tarefas

lista = Lista_de_tarefas()


while True:
    user_choice = int(input("Seja bem vindo ao Gerenciados de tarefas \n o que deseja fazer? \n 1-Ver lista de tarefas \n 2-Gerenciar uma tarefa \n 3-Adicionar tarefa \n 4-Remover tarefa \n 5-Sair \n "))

    match user_choice:
        case 1:
            lista.ver_lista_de_tarefas()
        case 2:
            user_manipulation = str(input("Qual tarefa deseja mudar? "))
            lista.gerenciar_tarefa(user_manipulation)
            for tarefa in lista.lista:
                print(tarefa)
        case 3:
            tarefa_name = str(input("Digite o nome da tarefa que deseja adicionar: "))
            tarefa_status = int(input("Qual o status da tarefa? \n 1-Pendente \n 2-Em andamento \n 3-Concluida \n "))
            if tarefa_status == 1:
                lista.adicionar_tarefa(tarefa_name, "Pendente")
            elif tarefa_status == 2:
                lista.adicionar_tarefa(tarefa_name, "Em andamento")
            elif tarefa_status == 3:
                lista.adicionar_tarefa(tarefa_name, "Concluida")
            else:
                print("valor inválido")
        case 4:
            tarefa_name = str(input("Digite o nome da tarefa que deseja remover: "))
            lista.remover_tarefa(tarefa_name) 
        case 5:
            break


