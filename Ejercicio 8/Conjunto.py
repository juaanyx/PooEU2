import numpy as np
class Conjunto:
    def __init__(self,list:list) -> None:
        self.__arreglo = np.array(list,dtype=int) #recibe una slita y crea un array
    def getConjunto(self):
        return self.__arreglo
    def __str__(self) -> str:
        return f"{self.__arreglo.tolist()}" #trasforma a lista para que se imprima separado por comas
    def __add__(self,other):
        return np.union1d(self.getConjunto(), other.getConjunto()) #union de dos arreglos
    def __sub__(self,other):
        return  np.setdiff1d(self.getConjunto(), other.getConjunto()) #diferencia
    def __eq__(self, other: object) -> bool:
        array1 =  self.getConjunto()
        array2= other.getConjunto() 
        tamaño= array1.size == array2.size
        aux=np.setdiff1d(self.getConjunto(), other.getConjunto()) #comprueba que los elementos de a (self) esten en b(other)
        elementos= aux.size == 0 #devuelve verdadero si al sacar la diferencia da un arreglo vacio
        return tamaño and elementos #si ambas se cumplen  retorna verdadero ya que tienen el mismo tamaño y elementos
            