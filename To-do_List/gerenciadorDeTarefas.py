


class Tarefa:

    def __init__(self, nome, status):
        self.nome = nome
        self.status = status

    def __str__(self):
        return f"{self.nome} - {self.status}"
    
    def marcar_concluida(self):
        self.status = "Concluida"
    
    def marcar_em_andamento(self):
        self.status = "Em andamento"
    
    def marcar_pendente(self):
        self.status = "Pendente"

class Lista_de_tarefas:

    def __init__ (self):
        
        self.lista = []
    

    def adicionar_tarefa(self, nome, status):
        tarefa = Tarefa(nome, status)
        self.lista.append(tarefa)
        print(f"tarefa {tarefa.nome} - {tarefa.status} adicionada com sucesso")

    def remover_tarefa(self, nome):
        i = 0
        for tarefa in self.lista:
            if tarefa.nome == nome:
                self.lista.pop(i)
            i += 1

    def ver_lista_de_tarefas(self):
        for tarefa in self.lista:
            print(tarefa)
    
    def gerenciar_tarefa(self, nome):
        i = 0
        for tarefa in  self.lista:
            if tarefa.nome == nome:
                print(tarefa)
                user_choice = int(input("O que deseja fazer? \n 1-marcar como concluida \n 2-marcar como em andamento \n 3-marcar como pendente \n 4-Cancelar \n "))
                match user_choice:
                    case 1:
                        tarefa.marcar_concluida()
                        print(f"{tarefa.nome} marcada como {tarefa.status}")
                    case 2:
                        tarefa.marcar_em_andamento()
                        print(f"{tarefa.nome} marcada como {tarefa.status}")
                    case 3:
                        tarefa.marcar_pendente()
                        print(f"{tarefa.nome} marcada como {tarefa.status}")
                    case 4:
                        print("Alteração cancelada")
                    
            i += 1