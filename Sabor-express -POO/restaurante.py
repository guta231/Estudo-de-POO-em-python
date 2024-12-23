class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):

        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):

        return f"nome: {self.nome} / categoria: {self.categoria} / ativo: {self.ativo}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)


restaurante1 = Restaurante("Praça", "Italiana")

Restaurante.listar_restaurantes()



