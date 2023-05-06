class PlanAhorro:
    def __init__(self,codigo,modelo,version,valor,cantCuotas,minimoLicitar) -> None:
        self.__codigo= int(codigo)
        self.__modelo= modelo
        self.__version= version
        self.__valor=  float(valor)
        self.__cantCuotas= int(cantCuotas)
        self.__minimoLicitar= minimoLicitar
        self.__valorCuota= (self.__valor/self.__cantCuotas)+ (self.__valor*0.10)
    def actualizarValorCuota(self):
        self.__valorCuota= (self.__valor/self.__cantCuotas)+ (self.__valor*0.10)
    def __str__(self) -> str:
        return f'Codigo: {self.__codigo},Modelo: {self.__modelo},Version:{self.__version} ,Valor:{self.__valor}'
    def actualizarValor(self,nuevo):
        self.__valor= int(nuevo)
        self.actualizarValorCuota()
    def getValorCuota(self):
        return self.__valorCuota
    def minimoLicitar(self):
        return self.__valorCuota * self.__minimoLicitar
    def __eq__(self, codigo) -> bool:
        return self.__codigo == int(codigo)
    def setMinLicitar(self,nuevo):
        self.__minimoLicitar = int(nuevo)
    def getvalorTotallicitar(self):
        print(f"{self.__minimoLicitar * self.getValorCuota()}")
    @staticmethod
    def nuevoPlan(lista:list):
        return PlanAhorro(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
        