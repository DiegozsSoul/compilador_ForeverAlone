class tablaVariables(object):
    def __init__(self):
        self.arreglo = {}

    
    def agrega(self, nombre, tipo):
        self.arreglo[nombre] = {
            'nombre' : nombre,
            'tipo' : tipo
        }
	  
    def getNombre(self):
        return self.arreglo

    def busca(self, query ):
        return query in self.arreglo


    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def imprimiArreglo(self):
        print(self.arreglo.items())

                
        