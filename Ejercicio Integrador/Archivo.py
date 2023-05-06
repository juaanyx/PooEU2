from Alumnos import Alumno
import csv
import numpy as np
from Materias import Materia

class Archivo:
    @staticmethod 
    def cargarMaterias():
        lista=[]
        archivo = open('materiasAprobadas.csv')#abre el archivo
        reader = csv.reader(archivo,delimiter=';') #lee el archivo
        bandera = True #archivo con cabecera
        
        for materia in reader:
            if bandera:
                bandera= not bandera
            else:
                lista.append(Materia.nueva(materia))
        archivo.close() #cierra el archivo
        return lista
    
    @staticmethod
    def cargarAlumnos():
        dimension=10
        arreglo= np.empty(dimension,dtype=Alumno) #crea un array de 10 elementos
        archivo = open('alumnos.csv')#abre el archivo
        reader = csv.reader(archivo,delimiter=';') #lee el archivo
        bandera = True #archivo con cabecera
        incremento= 5
        cantidad=0
        for alumno in reader:
            if bandera: #salta la cabecera
                bandera= not bandera
            else:
                if cantidad == dimension: #si estan todos los lugares ocupados
                    dimension += incremento #si estan incrementa la dimension
                    arreglo.resize(dimension)#expande el arreglo
                arreglo[cantidad]=Alumno.nuevo(alumno) #añade un elemento al arreglo
                cantidad +=1 #suma uno a la cantidad
                
        if cantidad != dimension: #Ajustamos la dimension del arreglo para que coincida con la cantidad
            dimension = cantidad 
            arreglo.resize(dimension)
        archivo.close() #cierra el archivo
        return arreglo
    
    @staticmethod
    def cargarAlumnos2():
        archivo = open('alumnos.csv')#abre el archivo
        reader = csv.reader(archivo,delimiter=';') #lee el archivo
        bandera = True #archivo con cabecera 
        tamaño = len(list(reader))-1 #tarasforma a lsitas y luego devuevle sus filas
        arreglo= np.empty(tamaño, dtype=Alumno) #Crea el arreglo
        cantidad=0
        for alumno in reader:
            if bandera: #salta la cabecera
                bandera= not bandera
            else:
                arreglo[cantidad](Alumno.nuevo(alumno))
                cantidad+=1
        archivo.close() #cierra el archivo
        return arreglo