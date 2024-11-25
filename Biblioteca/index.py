
livros_open_list = []
livros_close_list = []

class Livro:
    def __init__ (self, titulo, autor, status):

        self.titulo = titulo
        self.autor = autor
        self.status = status

    def __str__ (self):
        return f"Titulo: {self.titulo} autor: {self.autor} - {self.status}"
    
    def alugar (self):
        print(f"livro {self.titulo} de {self.autor} alugado com sucesso")
        self.status = "indisponivel"

    def ver_status (self):
        print(self.status)

    def devolver(self):
        self.status = "disponivel"
        

 
        
livro1 = Livro("a procura da felicidade", "Fernando", "disponivel")

livros_open_list.append(Livro("Patinho feio", "Carol", "disponivel"))

livros_open_list.append(livro1)


while True:

    user_choice = int(input("O que deseja fazer? \n 1-Alugar um livro \n 2-Doar um livro \n 3-Ver lista de livros disponiveis \n 4-Devolver um livro \n 5-Sair \n"))
    match user_choice:
        case 1:
            for livro in livros_open_list:
                print(livro)
            livro_choice = int(input(f"Escolha qual livro deseja alugar pelo seu index começando ao 0: "))
            Livro.alugar(livros_open_list[livro_choice])
            livros_close_list.append(livros_open_list[livro_choice])
            livros_open_list.pop(livro_choice)
            
        case 2:
            nome = str(input("Nome do livro a ser doado: "))
            autor = str(input("Nome do autor do livro: "))
            livro_doado = Livro(nome, autor, "disponivel")
            livros_open_list.append(livro_doado)
            print("Livro doado com sucesso")
        case 3:
            if len(livros_open_list) > 0:
                for livro in livros_open_list:
                    print(livro)
        case 4:
            if len(livros_close_list) > 0:
                for livro in livros_close_list:
                    print(livro)
                devolution_choice = int(input(f"digite o numero do seu livro de acordo com seu index na lista começando no 0: "))
                Livro.devolver(livros_close_list[devolution_choice])
                livros_open_list.append(livros_close_list[devolution_choice])
                livros_close_list.pop(devolution_choice)
        case 5:
            break
                
            
            




