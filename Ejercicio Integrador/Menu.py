from ManejadorAlumnos import ManejadorAlumnos as ma
from ManejadorMaterias import ManejadorMaterias as mm

class Menu:
    def __init__(self) -> None:
        self.__alumnos = ma()
        self.__materias = mm()
    def opciones(self,opcion):
        opcion=opcion
        match opcion:
            case 1:
                self.__materias.Sacarpromedio(input('ingrese Dni > '))
            case 2:
                self.__materias.listarMateria(self.__alumnos,input('ingrse materia> '))
            case 3:
                self.__alumnos.imprimirListado()
            case 5:
                print('adios...')
            case other:
                print('error...')
    def mostrarop(self):
        print('menu')
        print('1-Leer por teclado el número de dni de un alumno e informar promedio')
        print('2- Leer por teclado el nombre de una materia e informar aprobados')
        print('3- Obtener un listado de alumnos ordenado')
        print('5- Salir')
    def iniciar(self):
        opcion = 99
        while opcion != 5:
            self.mostrarop()
            opcion=int(input('opcion > '))
            self.opciones(opcion)