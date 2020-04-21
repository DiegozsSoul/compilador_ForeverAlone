from tablavar import tablaVariables

class tablaFunciones(object):

    def __init__(self):
        self.arreglo = {}

    def agregaf(self, nombre, tipo):
        self.arreglo[nombre] ={
        'nombre' : nombre,
        'tipo' : tipo,
        'tvar' : tablaVariables()
        }

    def agregav(self, nombref, nombrev, tipov):
        if nombref in self.arreglo:
            tabVar = self.arreglo[nombref]
            print(access['tvar'].busca(nombrev))
            if tabVar['tvar'].busca(nombrev) == True:
                print("Variable ya existe")
            else:
                tabVar['tvar'].agrega(nombrev, tipov)
        else:
            print("La funcion no existe")

    def busca(self, query):
        return query in self.arreglo


    def testerVariable(self, nombref):
        if nombref in self.arreglo:
            testerino = self.arreglo[nombref]
            return testerino['tvar'].printTable()

    def getDir(self, query):
        if self.busca(query) == 'True':
            return self.arreglo[query]
        else:
            print("Error not found")
            return None

    def arref(self):
        print(self.arreglo)
