class Alumno:
    def __init__(self,dni,apellido,nombre,carrera,año):
        self.__dni = int(dni)
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = int(año)
    @staticmethod
    def nuevo(list:list): 
        return Alumno(list[0],list[1],list[2],list[3],list[4])
    def getDni(self):
        return self.__dni
    def getNyA(self):
        return f"{self.__apellido},{self.__nombre}"
    def getCarrera(self):
        return self.__carrera
    def getAño(self):
        return self.__año
    def __lt__(self,other):
        resultado= self.getAño() < other.getAño() #compara si el año es menor que
        if self.getAño() == other.getAño(): #en caso de ser el mismo año
            resultado =self.getNyA() < other.getNyA() #compra si el orden alfabetico del apellido y nombre
        return resultado #devuelve el resultado
    def __str__(self) -> str:
        return f"{self.getDni()} {self.getNyA()} {self.getAño()} {self.getCarrera()}"
    def __eq__(self, other) -> bool:
       return self.getDni() == other.getDni()