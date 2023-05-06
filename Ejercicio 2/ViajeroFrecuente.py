class ViajeroFrecuente:
    __numViajero:int
    __dni:str
    __nombre:str
    __apellido:str
    __millasAcum:int
    
    
    def __init__(self,numViajero,dni,nombre,apellido,millasAcum=0):
        self.__numViajero = int(numViajero)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = int(millasAcum)
        
    def getNumero(self):
        return self.__numViajero
    
    def cantidadTotaldeMillas(self):
        return self.__millasAcum
    
    def acumularMillas(self,millas):
        millas= int(millas)
        self.__millasAcum += millas
        print(f"Exito: Se Sumaron {millas} millas La cantidad actual es {self.__millasAcum}.")
        
    def canjearMillas(self,millas):
        mensaje:str
        millas =int(millas)
        if self.__millasAcum >= millas:
            self.__millasAcum -= millas
            mensaje= f"Exito: Se canjearon {millas} millas La cantidad actual es {self.__millasAcum}."
        else:
            mensaje = f"Error: Millas insuficientes "
            
        print(mensaje)
        
    def __eq__(self, valor) -> bool:
        resultado:bool
        if isinstance(valor, ViajeroFrecuente) :
            resultado =self.__numViajero == valor.__numViajero
        else:
            
            resultado = self.__numViajero == int(valor)
        return resultado
        
    