from ViajeroFrecuente import ViajeroFrecuente 
import csv
class ViajeroController:
    __viajeros=[]
    __viajero:ViajeroFrecuente
    def __init__(self):
        pass
    def cargarViajeros(self,nombre):
        """ with open(f"{nombre}.csv", newline='') as archivo_csv:
            viajeros= csv.reader(archivo_csv,delimiter=',')
            next(viajeros)
            for viajero in viajeros:
                auxiliar =ViajeroFrecuente(viajero[0],viajero[1],viajero[2],viajero[3],viajero[4])
                self.__viajeros.append(auxiliar) """
                
        with open(f"{nombre}.csv", 'r') as archivo_csv:
            viajeros = csv.reader(archivo_csv,delimiter=';')
            next(viajeros)
            for viajero in viajeros:
                auxiliar =ViajeroFrecuente(viajero[0],viajero[1],viajero[2],viajero[3],viajero[4])
                self.__viajeros.append(auxiliar) 
                
    def iniciar(self):
         
         resultado= self.buscar(input('ingrese numero de viajero: '))
         self.__viajero= self.__viajeros[resultado]
         if isinstance( self.__viajero,ValueError):
             print(f"Error: El numero no corresponde a un viajero ")
         else:
             
             self.menu()
         
    def buscar(self,numero):
        resultado = self.__viajeros.index(numero)  
        return resultado
        
            
              
            
    def menu(self):
        opcion = ''
    
        while(opcion != 'g'):
            print("Menu:")
            print("a- Consultar Cantidad de Millas.")
            print("b- Acumular Millas.")
            print("c- Canjear Millas.")
            print("g- Terminar programa")
            print('f- Determiar viajero con mas millas')
            print("")
            opcion = input('Selecione una opcion: ')
            if opcion == 'a':
                print(self.__viajero.cantidadTotaldeMillas())
            elif opcion == 'b':
                self.__viajero.acumularMillas(input('Ingrese cantidad de millas a añadir: '))
            elif opcion == 'c':
                self.__viajero.canjearMillas(input('Ingrese cantidad de millas a Canjear: '))
            elif opcion == 'g':
                pass
            elif opcion == 'f':
                print(f"{max(self.__viajeros )}") 
            else: 
                print('Error: valor incorrecto')
            
                