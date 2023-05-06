import csv
from PlanAhorro import PlanAhorro

class Cargar:
    @staticmethod
    def archivo(nombre):
        lista=[]
        archivo = open(f'{nombre}.csv')#abre el archivo
        reader = csv.reader(archivo,delimiter=';') #lee el archivo
        for plan in reader:
            lista.append(PlanAhorro.nuevoPlan(plan))
        archivo.close() #cierra el archivo
        for plan in lista:
            print(plan)
        return lista