from tablavar import tablaVariables

class tablaFunciones(object):

    def __init__(self):
        self.arreglo = {}

    def agregaf(self, nombre, tipo, tipoParam, cantParam, cantVarLoc):
        if(nombre not in self.arreglo.keys()):
            self.arreglo[nombre] ={
            'nombre' : nombre,
            'tipo' : tipo,
            'tvar' : tablaVariables(),
            'tparam' : tipoParam,
            'tcantparam' : cantParam,
            'cantVarLoc' : cantVarLoc
            }
            #print("added function " + nombre)
        else:
            print("function " + nombre + "already declared")

    def agregav(self, nombref, nombrev, tipov, locmemv):
        if (nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            if (tabVar['tvar'].busca(nombrev) == True):
                print("Variable ya existe" )
            else:
                tabVar['tvar'].agrega(nombrev, tipov, locmemv)
        else:
            print("La funcion no existe")

    def agregaTablaTipoParam(self,nombref,tiposDeParam,cantParam):
        if(nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            tabVar['tparam'] = tiposDeParam
            tabVar['tcantparam'] = cantParam

    def agregaCantidadVarLoc(self,nombref,cantVarLoc):
        if(nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            tabVar['cantVarLoc'] = cantVarLoc

    def getLocMem(self,nombref, nombrev):
        if (nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            if(tabVar['tvar'].busca(nombrev) == True):
                #variable viene de una funcion
                return tabVar['tvar'].getLocMem(nombrev)
            else:
                print("variable no existe")

    def getTipoFunc(self,nombref):
        if(nombref in self.arreglo):
            return self.arreglo[nombref]['tipo']

    def busca(self, query):
        return query in self.arreglo


    def testerVariable(self, nombref):
        if nombref in self.arreglo:
            testerino = self.arreglo[nombref]
            return testerino['tvar'].imprimiArreglo()

    def getDir(self, query):
        if self.busca(query):
            #print("TESTERINO", self.arreglo[query] )
            return self.arreglo[query]
            
        else:
            print("Error not found")
            return None

    def arref(self):
        print(self.arreglo)


