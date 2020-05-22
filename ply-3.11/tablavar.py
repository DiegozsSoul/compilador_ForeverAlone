class tablaVariables(object):
    def __init__(self):
        self.arreglo = {}

    
    def agrega(self, nombre, tipo, locmem):
        self.arreglo[nombre] = {
            'nombre' : nombre,
            'tipo' : tipo,
            'locmem' : locmem
        }
	  
    def getNombre(self):
        return self.arreglo

    def busca(self, query ):
        return query in self.arreglo

    def getvar(self,vname):
        if (self.busca(vname)): 
            return self.arreglo[vname] 
        else:
            return None

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipoVar(self,vname):
        if(self.busca(vname)):
            return self.arreglo[vname]['tipo']
        else:
            print("variable no delcarada")
    
    def getLocacionMemoria(self,vname):
        return self.arreglo[vname]['locmem']

    def imprimiArreglo(self):
        print(self.arreglo.items())

                
        