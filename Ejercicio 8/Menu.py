from Conjunto import Conjunto
class Menu:
    @staticmethod
    def union(A:Conjunto,B:Conjunto):
        print(f"la union es: {A+B}")
    @staticmethod
    def diferencia(A:Conjunto,B:Conjunto):
        print(f"diferencia de {A} - {B} = {A-B}")
    @staticmethod
    def igualdad(A:Conjunto,B:Conjunto):
        print(f"A y B iguales: {A==B}")
    @staticmethod
    def opciones():
        print("a-Union de A + B")
        print("b-Diferencia de A - B")
        print("c-Igualdad de A y B")
        print("d-salir")
        print("")
    @staticmethod
    def seleccionar(opcion,A:Conjunto,B:Conjunto):
        
        match opcion:
            case 'a':
                Menu.union(A,B)
            case 'b':
                Menu.diferencia(A,B)
            case 'c':
                Menu.igualdad(A,B)
            case 'd':
                print('Saliendooo')
            case other:
                print('Error')
    @staticmethod
    def Iniciar(A:Conjunto,B:Conjunto):
        opcion = 'p'
        while opcion != 'd':
            Menu.opciones()
            opcion= input("selecciona opcion >> ")
            Menu.seleccionar(opcion,A,B)