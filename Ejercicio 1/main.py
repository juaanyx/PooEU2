from EmailsController import *


def test():
    """ email = Email()
    email.crearCuenta(input('ingrese email: '))
    email.retornaEmail()
    cuentas = []
    
    
    contador = 0
    for cuenta in cuentas: """
    """ print(f"{cuenta.getDominio()}") """
    """ if cuenta.getDominio() == dominio:
            contador +=1
    print(f"Aviso: Coinciden con las busqueda {contador} resultados")
             """
    cuentas = EmailsController()
    cuentas.CrearUnEmail()
    cuentas.CargarCsv(input('ingrese nombre de archivo sin .csv: '))
    cuentas.ContarDominio(input('ingrese un dominio a buscar: '))
    
    
    
if __name__ == '__main__':
    test()
