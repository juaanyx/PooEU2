from Archivo import Archivo as a
from ManejadorAlumnos import ManejadorAlumnos as ma
class ManejadorMaterias:
    def __init__(self):
        self.__materias= a.cargarMaterias()
    def buscarDni(self,dni):
        dni = int(dni)
        lista= []
        for materia in self.__materias:
            if dni == materia.getDni():
                lista.append(materia)
        return lista
    def buscarMateria(self,materia):
        lista=[]
        for elemento in self.__materias:
            if elemento.getMateria() == materia and elemento.getAprobacion() == 'P' and elemento.getNota() >=7:
                lista.append(elemento)
        return lista
    def Sacarpromedio(self,dni):
        lista= self.buscarDni(dni)
        contadorSinA = 0
        sumadorSinA =0
        contadorConA = 0
        sumadorConA = 0
        for materia in lista:
            contadorConA +=1
            sumadorConA += materia.getNota()
            if materia.getNota() > 3:
                contadorSinA+=1
                sumadorSinA+= materia.getNota()
        print(f"El promedio del Dni:{lista[0].getDni()} es con aplazos: {sumadorConA/contadorConA}y sin aplazos {sumadorSinA/contadorSinA}")
    def listarMateria(self,alumnos:ma,materia):
        listado= self.buscarMateria(materia)
    
        if len(listado)>=1:
            for elemento in listado:
                alumno= alumnos.buscarAlumno(elemento)
                print(f"{alumno.getDni()} {alumno.getNyA()} {elemento.getFecha()} {elemento.getNota()} {alumno.getAño()}")
            