
from PlanesController import PlanesController
class Menu:
    def __init__(self):
        self.__controller = PlanesController()
        """ self.__menu ={'1' : lambda: self.__controller.actulizarPlanes,
                      '2': lambda: self.__controller.cuotasMenores(input('ingrese Valor limite > ')),
                      '3': lambda: self.__controller.mostrarminlicitar(input('ingrese codigo > ')),
                      '4': lambda: self.__controller.modificarCuota(input('ingrese codigo > ')),
                      '5': lambda:print('saliendo...')} """
        
    def mostrarOpciones(self):
        print('Menu')
        print('1- Actualizar el valor del vehículo de cada plan.')
        print('2- Mostrar por Codigo')
        print('3- Mostrar minimo a licitar ')
        print('4- Modificar la cantidad cuotas que debe tener pagas para licitar')
        print('5-salir')
        print(' ')
    def seleccionar(self,opcion):
        match opcion:
            case '1':
                self.__controller.actulizarPlanes()
            case '2':
                self.__controller.cuotasMenores(input('ingrese Valor limite > '))
            case '3':
                self.__controller.mostrarminlicitar(input('ingrese codigo > '))
            case '4':
                self.__controller.modificarCuota(input('ingrese codigo > '))
            case '5':
                print('saliendo...')
            case other:
                print(f'Error, El valor {opcion} no corresponde a las opciones dadas')
    def Abrir(self):
        llave = '99'
        while llave != '5':
            self.mostrarOpciones()
            self.seleccionar(input('seleccione Opcion > '))
           
                
            