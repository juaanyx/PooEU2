class Materia:
    def __init__(self,dni,nombreMateria,fecha,nota,aprobacion):
        self.__dni = int(dni)
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = float(nota)
        self.__aprobacion = aprobacion
    @staticmethod
    def nueva(list:list): 
        return Materia(list[0],list[1],list[2],list[3],list[4])
    def getNota(self):
        return self.__nota
    def getDni(self):
        return self.__dni
    def getMateria(self):
        return self.__nombreMateria
    def getFecha(self):
        return self.__fecha
    def getAprobacion(self):
        return self.__aprobacion
    