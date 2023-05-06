import csv
from Registro import Registro
class Archivo:
    @staticmethod
    def cargar(nombre):
        lista=[[]]
        archivo = open(f'{nombre}.csv')#abre el archivo
        reader = csv.reader(archivo,delimiter=',') #lee el archivo
        bandera = True
        dia = 0
        for dato in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                if dia != int(dato[0])-1: #si el dia del dato es distinto al dia abre una fila(dia)
                    lista.append([])
                    dia=int(dato[0])-1
                reg=Registro(dato[0],dato[1],dato[2],dato[3],dato[4])
                lista[int(dato[0])-1].append(reg) #guarda el registro en la columna (hora) """
                
        archivo.close() #cierra el archivo
        return lista