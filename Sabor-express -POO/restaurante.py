class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):

        return f"nome: {self._nome} / categoria: {self._categoria} / ativo: {self.ativo}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    @property

    def ativo(self):
        return 'Ativado' if self._ativo == True else 'Desativado'

restaurante1 = Restaurante("Praça", "Italiana")

Restaurante.listar_restaurantes()



