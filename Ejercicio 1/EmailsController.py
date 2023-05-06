from Email import *
import csv
class EmailsController:
    __cuentas = [];

    def __init__(self):
        pass
    
    def CrearUnEmail(self):
        email = Email()
        email.crearCuenta(input('ingrese email: '))
        self.__cuentas.append(email)
        
    def CargarCsv(self,nombre):
        with open(f"{nombre}.csv", newline='') as archivo_csv:
            emails = csv.reader(archivo_csv, delimiter=',')
            next(emails)
            for email in emails:
                auxiliar =Email()
                """ print(f'Nombre: {email[0]}') """
                auxiliar.crearCuenta(email[0])
                self.__cuentas.append(auxiliar)
                
    def ContarDominio(self,dominio):
        contador = 0
        for cuenta in self.__cuentas:
             """ print(f"{cuenta.getDominio()}") """
             if cuenta.getDominio() == dominio:
                contador +=1
        print(f"Aviso: Coinciden con las busqueda {contador} resultados")
            
    
            
    