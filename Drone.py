from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtdHelices):
        super().__init__(marca, modelo)
        self.__qtdHelices = qtdHelices
        self.prox = None

    def imprimir_informacoes(self) -> None:
        super().imprimir_informacoes()
        print(f'Qtd. Hélices: {self.getHelices()}')

    def getHelices(self):
        return self.__qtdHelices