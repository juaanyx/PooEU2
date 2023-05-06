from Cargar import Cargar
from PlanAhorro import PlanAhorro

class PlanesController:
    def __init__(self):
        self.__planes = Cargar.archivo(input('Ingrese el nombre del archivo(sin .csv)>  '))
    def actulizarPlanes(self):
        for plan in self.__planes:
            print(plan)
            plan.actualizarValor(input('Ingrese nuevo valor total > '))
            print(plan)
    def cuotasMenores(self,valor):
        valor=float(valor)
        for plan in self.__planes:
            if (plan.getValorCuota() <valor):
                print(plan)
    def modificarCuota(self,valor):
        valor= int(valor)
        indice= self.__planes.index(valor) #busca el valor
       
        self.__planes[indice].setMinLicitar(input('Coloque nueva cantidad minima para licitar > ')) #actualiza valor
       
    def mostrarminlicitar(self,valor):
        valor= int(valor)
        indice= self.__planes.index(valor) #busca el valor
        print(self.__planes[indice].getvalorTotallicitar()) #muestra el valor minimo pagado apra licitar