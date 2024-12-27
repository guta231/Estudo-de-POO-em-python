from avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._lista_de_avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):

        return f"nome: {self._nome} / categoria: {self._categoria} / ativo: {self.ativo} / avaliação: {self.media_avaliacoes()}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    @property

    def ativo(self):
        return 'Ativado' if self._ativo == True else 'Desativado'
    
    def receber_avaliacao(self, cliente, nota):
        if nota > 5 or nota < 0:
            return

        new_avaliacao = Avaliacao(cliente, nota)
        self._lista_de_avaliacao.append(new_avaliacao)


    
    def media_avaliacoes(self):
        if not self._lista_de_avaliacao:
            return "-" 
        
        soma_das_notas = 0
        for nota in self._lista_de_avaliacao:
            soma_das_notas = soma_das_notas + nota._nota
        
        total_de_avaliacoes = len(self._lista_de_avaliacao)

        media = round(soma_das_notas/total_de_avaliacoes, 1)

        return media



