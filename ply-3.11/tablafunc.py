from tablavar import tablaVariables

class tablaFunciones(object):

    def __init__(self):
        self.arreglo = {}

    def agregaf(self, nombre, tipo):
        if(nombre not in self.arreglo.keys()):
            self.arreglo[nombre] ={
            'nombre' : nombre,
            'tipo' : tipo,
            'tvar' : tablaVariables()
            }
            #print("added function " + nombre)
        else:
            print("function " + nombre + "already declared")

    def agregav(self, nombref, nombrev, tipov):
        if (nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            if (tabVar['tvar'].busca(nombrev) == True):
                print("Variable ya existe" )
            else:
                tabVar['tvar'].agrega(nombrev, tipov)
        else:
            print("La funcion no existe")

    def busca(self, query):
        return query in self.arreglo


    def testerVariable(self, nombref):
        if nombref in self.arreglo:
            testerino = self.arreglo[nombref]
            return testerino['tvar'].imprimiArreglo()

    def getDir(self, query):
        if self.busca(query):
            return self.arreglo[query]
        else:
            print("Error not found")
            return None

    def arref(self):
        print(self.arreglo)
