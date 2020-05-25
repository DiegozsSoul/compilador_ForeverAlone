class tablaVariables(object):
    def __init__(self):
        self.arreglo = {}

    
    def agrega(self, nombre, tipo, locmem,tabArr):
        self.arreglo[nombre] = {
            'nombre' : nombre,
            'tipo' : tipo,
            'locmem' : locmem,
            'tabArr' : tabArr
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
    def agregaTabArr(self,vname,isArray):
        if(self.busca(vname)):
            self.arreglo[vname]['tabArr'] = isArray
    def getTabArr(self,vname):
        if(self.busca(vname)):
            return self.arreglo[vname]['tabArr']
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipoVar(self,vname):
        if(self.busca(vname)):
            return self.arreglo[vname]['tipo']
        else:
            print("variable no delcarada",vname)
    
    def getLocacionMemoria(self,vname):
        if(self.busca(vname)):
            return self.arreglo[vname]['locmem']
        else:
            print("Variable no se encontro",vname)

    def imprimiArreglo(self):
        print(self.arreglo.items())

                
        