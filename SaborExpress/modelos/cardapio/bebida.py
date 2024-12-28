from .item_cardapio import ItemCardapio


class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
    

    def __str__(self):
        return f"Nome: {self._nome} / Preço: {self._preco} / Tamanho: {self._tamanho}"
    
    def aplicar_desconto(self):

        self._preco -= (self._preco * 0.08)