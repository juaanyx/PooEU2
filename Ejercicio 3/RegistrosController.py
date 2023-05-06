from Archivos import Archivo
from Registro import Registro

class RegistrosController:
    def __init__(self) -> None:
        self.__registros= Archivo.cargar(input('Ingrese mes a cargar: ')) 
        #carga el archivo al iniciar el controlador
        self.__tempMin =[ 999,0,0]
        self.__tempMax = [-999,0,0]
        self.__humMin =[999,0,0]
        self.__humMax = [-999,0,0]
        self.__presMin =[ 999,0,0]
        self.__presMax = [-999,0,0]
        self.__promedioHora= [0.0]*24
    def imprimirDia(self,dia):
        print('Hora  Teperatura  Humedad  Presion')
        for  i in range(24): #imprime las 24hs
            print(f"{i} {self.__registros[int(dia)][i]}")
    def mayortemp(self,objet:Registro):#asigna si el objeto actual es mayor la temperatura
        if self.__tempMax[0] < objet.getTemperatura():
            self.__tempMax[0] =objet.getTemperatura()
            self.__tempMax[1] =objet.getDia()
            self.__tempMax[2] =objet.getHora()
    def mayorhum(self,objet:Registro):#asigna si el objeto actual es mayor la humedad
        if self.__humMax[0] < objet.getHumedad():
            self.__humMax[0] =objet.getHumedad()
            self.__humMax[1] =objet.getDia()
            self.__humMax[2] =objet.getHora()
    def mayorpres(self,objet:Registro):#asigna si el objeto actual es mayor la presion
        if self.__presMax[0] < objet.getHumedad():
            self.__presMax[0] =objet.getHumedad()
            self.__presMax[1] =objet.getDia()
            self.__presMax[2] =objet.getHora()
    def menortemp(self,objet:Registro):#asigna si el objeto actual es menor la temperatura
        if self.__tempMin[0] > objet.getTemperatura():
            self.__tempMin[0] =objet.getTemperatura()
            self.__tempMin[1] =objet.getDia()
            self.__tempMin[2] =objet.getHora()
    def menorhum(self,objet:Registro):#asigna si el objeto actual es menor la humedad
        if self.__humMin[0] > objet.getHumedad():
            self.__humMin[0] =objet.getHumedad()
            self.__humMin[1] =objet.getDia()
            self.__humMin[2] =objet.getHora()
    def menorpres(self,objet:Registro):#asigna si el objeto actual es menor la presion
        if self.__presMin[0] > objet.getHumedad():
            self.__presMin[0] =objet.getHumedad()
            self.__presMin[1] =objet.getDia()
            self.__presMin[2] =objet.getHora()
    def buscarMaxyMin(self):
        for dia in self.__registros:
            for hora in dia:
                self.mayortemp(hora)
                self.mayorpres(hora)
                self.mayorhum(hora)
                self.menortemp(hora)
                self.menorpres(hora)
                self.menorhum(hora)
    def imprimirMaxyMin(self):
        print(f"Aviso: La temperatura maxima {self.__tempMax[0]}°, se registro el dia{self.__tempMax[1]} a las {self.__tempMax[2]}hs")
        print(f"Aviso: La temperatura minima {self.__tempMin[0]}°, se registro el dia{self.__tempMin[1]} a las {self.__tempMin[2]}hs")
        print(f"Aviso: La humedad maxima {self.__humMax[0]}°, se registro el dia{self.__humMax[1]} a las {self.__humMax[2]}hs")
        print(f"Aviso: La humedad minima {self.__humMin[0]}°, se registro el dia{self.__humMin[1]} a las {self.__humMin[2]}hs")
        print(f"Aviso: La presion Atomesferica maxima {self.__presMax[0]}°, se registro el dia{self.__presMax[1]} a las {self.__presMax[2]}hs")
        print(f"Aviso: La presion Atomesferica minima {self.__presMin[0]}°, se registro el dia{self.__presMin[1]} a las {self.__presMin[2]}hs")       
    def mayorMenor(self):
        self.buscarMaxyMin()
        self.imprimirMaxyMin()       
    def acumularHora(self):
        for dia in self.__registros:
            for i in range(len(dia)):
                self.__promedioHora[i] += dia[i].getTemperatura() #recorre y suba en las mismas la temperatura
    def sacarPromedio(self):
        for i in range(len(self.__promedioHora)):
            self.__promedioHora[i] /= 6 #divide lo acumulado en la cantidad de dias cargados
    def MostrarPromedios(self):
        print(f"{len(self.__registros)}")
        for i in range(len(self.__promedioHora)):
            print(f"Aviso: Para la hora {i} el promedio Mensual es {self.__promedioHora[i]}")
    def cereo(self):
        for i in range(len(self.__promedioHora)):
            self.__promedioHora[i]= 0
    def promedio(self):
        self.cereo()
        self.acumularHora()
        self.sacarPromedio()
        self.MostrarPromedios()
