from Archivo import Archivo as a
import numpy as np
class ManejadorAlumnos:
    def __init__(self) :
        self.__alumnos= a.cargarAlumnos()
    def imprimirListado(self):
        arreglo= np.sort(self.__alumnos)
        for alumno in arreglo:
            print(alumno)
    def buscarAlumno(self,elemento):
        al= np.where(self.__alumnos == elemento )[0] #se coloca para obtener un arreglo unidimensional 
        print(al)
        if al.size == 1:
            
            print(al)
            al= al[0]
            print(al)
            
            resultado = self.__alumnos[al]
            
        else:
            resultado = "No Encontrado"
            
        """ elementos= self.__alumnos.tolist()#version con listas
        indice=elementos.index(elemento)
        resultado= elementos[indice] """ 
        return resultado