from ViajeroController import ViajeroController


def test():
    ui =ViajeroController()
    ui.cargarViajeros(input('Coloque el nombre del archivo sin ".csv": '))
    ui.iniciar()
    
    
    
if __name__ == '__main__':
    test()