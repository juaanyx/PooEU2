class Ventana:
    
    def __init__(self, titulo, x1=0, y1=0, x2=500, y2=500):
        self.__titulo = titulo
        self.__x1 = max(0, x1) # el menor valor para x1 es 0
        self.__y1 = max(0, y1) # el menor valor para y1 es 0
        self.__x2 = min(500, x2) # el mayor valor para x2 es 500
        self.__y2 = min(500, y2) # el mayor valor para y2 es 500
        
    def alto(self):
        return self.__y2 - self.__y1
    def ancho(self):
        return self.__x2 - self.__x1
    def getTitulo(self):
        return self.__titulo
    def mostrar(self):
        print(f"vértice superior izquierdo ({self.__x1},{self.__y1})")
        print(f"vértice inferior derecho ({self.__x2},{self.__y2})")
    def moverDerecha(self,cantidad=1):
        self.__x1 = max(0, self.__x1+cantidad)# el menor valor para x1 es 0
        self.__x2 = min(500, self.__x2+cantidad) # el mayor valor para x2 es 500
    def moverIzquierda(self,cantidad=1):
        self.__x1 = max(0, self.__x1-cantidad)# el menor valor para x1 es 0
        self.__x2 = min(500, self.__x2-cantidad) # el mayor valor para x2 es 500
    def subir(self,cantidad=1):
        self.__y1 = max(0, self.__y1+cantidad) # el menor valor para y1 es 0
        self.__y2 = min(500, self.__y2+cantidad) # el mayor valor para y2 es 500
    def bajar(self,cantidad=1):
        self.__y1 = max(0, self.__y1-cantidad) # el menor valor para y1 es 0
        self.__y2 = min(500, self.__y2-cantidad) # el mayor valor para y2 es 500
    