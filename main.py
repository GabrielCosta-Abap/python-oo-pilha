from PilhaDrones import PilhaDrones
from PilhaCarros import PilhaCarros


pilhaCarros = PilhaCarros()
pilhaDrones = PilhaDrones()

while True:
    option = input('''O que você deseja fazer???
1 - Adicionar carro;
2 - Remover carro;
3 - Adicionar Drone;
4 - Remover Drone;
5 - Imprimir pilha de carros;
6 - Imprimir pilha de drones;
7 - Encerrar operação.
''')

    if option == '1':
        marca = input('Digite a Marca do carro: ')
        modelo = input('Digite o Modelo do carro: ')
        portas = input('Digite a quantidade de portas: ')
        pilhaCarros.adicionaCarro(marca,modelo,portas)
    
    elif option == '2':
        pilhaCarros.remove()
    
    elif option == '3':
        marca = input('Digite a Marca do Drone: ')
        modelo = input('Digite o Modelo do Drone: ')
        helices = input('Digite a quantidade de Hélices: ')
        pilhaDrones.adicionaDrone(marca,modelo,helices)
    
    elif option == '4':
        pilhaDrones.remove()

    elif option == '5':
        pilhaCarros.printCarros()

    elif option == '6':
        pilhaDrones.printDrones()
    
    elif option == '7':
        print('Operação encerrada!')
        break
    print('-'*10)