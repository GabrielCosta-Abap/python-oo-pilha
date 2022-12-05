from Drone import Drone

class PilhaDrones:
    def __init__(self):
        self.top = None

    def printDrones(self):
        print('*'*30)
        if not self.top:
            return print("Pilha vazia.")
        temp = self.top
        while temp:
            temp.imprimir_informacoes()
            temp = temp.prox
        print('*'*30)

    def adicionaDrone(self, marca, modelo, qtdHelices):
        drone = Drone(marca, modelo, qtdHelices)
        if not self.top:
            self.top = drone
        else:
            drone.prox = self.top
            self.top = drone
        print('DRONE ADICIONADO COM SUCESSO! :)))')

    def remove(self):
        if not self.top:
            return print("Pilha vazia.")
        if self.top.prox == None:
            self.top = None
        else:
            self.top = self.top.prox
        print('DRONE REMOVIDO COM SUCESSO! :)))')