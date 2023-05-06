
from RegistrosController import RegistrosController
from Registro import Registro

class Menu:
    def __init__(self):
        self.__registros= RegistrosController()
        self.__opcion=99
    def impirimirMenu(self): #muestra las opciones del menu
        print('Menu:')
        print('1- Mostrar para cada variable el día y hora de menor y mayor valor')
        print('2-Indicar la temperatura promedio mensual por cada hora.')
        print('3-Dado un número de día listar los valores')
        print('0-Bye')
        
    def seleccionarMenu(self): #selecciona una opcion
        self.__opcion=int(input('Seleccione: '))
        match self.__opcion: #añadido desde 3.10 igual a switch
            case 1:
                self.__registros.mayorMenor()
            case 2:
                self.__registros.promedio()
            case 3:
                self.__registros.imprimirDia(input('Seleccione dia: '))
            case other:
                print(f'Error: La opcion {self.__opcion} No es a un valor acceptable')
    def menu(self):
        while self.__opcion != 0:
            self.impirimirMenu()
            self.seleccionarMenu()
            
   
        