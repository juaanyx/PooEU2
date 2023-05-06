class Email:
    __password = ""
    __idCuenta = ""
    __dominio = ""
    __tipoDeDominio = ""
    

    def __init__(self):
        """ __self.idCuenta = input("Ingrese idCuenta: " )
        __self.dominio = input("Ingrese dominio: ")
        __self.tipoDeDominio = input("Ingrese tipoDeDominio: ")
        __self.password = input("Ingrese password: ") """

    def retornaEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDeDominio}"

    def getDominio(self):
        return self.__dominio

    def crearCuenta(self, email):
        
        if isinstance(email, str):
            partes = email.split('@')
            if len(partes) == 2:
                self.__idCuenta = partes[0]
                if '.' in partes[1]:
                    self.__dominio, self.__tipoDeDominio = partes[1].split('.')
                    """ self.__password= input("Ingrese la contraseña: ") """
                    print(f"Aviso: Cuenta {self.retornaEmail()} creado")
                else:
                    print(f"Error: la dirección de correo \"{email}\" es incorrecta ")
            else:
                print(f"Error: la dirección de correo \"{email}\" es incorrecta ")
        else:
            print("Error: Tipo de dato incorrecto")