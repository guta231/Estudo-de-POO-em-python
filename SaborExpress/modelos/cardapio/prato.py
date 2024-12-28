from .item_cardapio import ItemCardapio

class Prato(ItemCardapio):

    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f"Nome: {self._nome} / Preço: {self._preco} / Descrição: {self._descricao}"
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)