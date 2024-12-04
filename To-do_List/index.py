

import tkinter as tk







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
        print(f"tarefa {tarefa} adicionada com sucesso")

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


root = tk.Tk()
root.title("To-do list")
lista = Lista_de_tarefas()

def add_tarefa():

    nome_mandar = nome.get()
    status_mandar = status.get()
    lista.adicionar_tarefa(nome_mandar, status_mandar)
    
label_lista = " "
def ver_tarefas():
    

    if label_lista != " ":
        label_lista.destroy()
        label_lista = tk.Label(root, text=" / ".join([str(i)for i in lista.lista]))
        label_lista.pack()
    
    label_lista = tk.Label(root, text=" / ".join([str(i)for i in lista.lista]))
    label_lista.pack()



label_nome = tk.Label(root, text="Digite o nome da tarefa")    
label_nome.pack()
nome = tk.Entry(root)
nome.pack()
label_status = tk.Label(root, text="Digite o status atual da tarefa")
label_status.pack()
status = tk.Entry(root)
status.pack()
button_adicionar_tarefa = tk.Button(root, text="Adicionar tarefa", command=add_tarefa)
button_adicionar_tarefa.pack()
button_ver_tarefas = tk.Button(root, text="Ver tarefas", command=ver_tarefas, bg="blue", fg="white")
button_ver_tarefas.pack()






root.mainloop()




