from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, qtdPortas):
        super().__init__(marca, modelo)
        self._qtdPortas = qtdPortas
        self.prox = None

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'Qtd. Portas: {self._qtdPortas}')

    def getQtdPortas(self):
        return self._qtdPortas