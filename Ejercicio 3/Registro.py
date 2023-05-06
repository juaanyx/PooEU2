class Registro:
   def __init__(self,dia,hora,temperatura,humedad,presion):
      self.__dia = int(dia)
      self.__hora = int(hora)
      self.__temperatura= int(temperatura)
      self.__humedad= int(humedad)
      self.__presion = int(presion)
   def __str__(self) -> str:
      return f" {self.__hora} {self.__temperatura}  {self.__humedad}  {self.__presion}" #devuelve ese sting cuando se imprime la variable
   def getTemperatura(self):
      return self.__temperatura  
   def getHumedad(self):
      return self.__humedad
   def getPresion(self):
      return self.__presion
   def getHora(self):
      return self.__hora
   def getDia(self):
      return self.__dia