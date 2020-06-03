from tablavar import tablaVariables
import sys
class tablaFunciones(object):

    def __init__(self):
        self.arreglo = {}

    def agregaf(self, nombre, tipo, tipoParam, cantParam, pilaParam, cantVarLoc, iniciaCuadru, contTemp):
        if(nombre not in self.arreglo.values()):
            self.arreglo[nombre] ={
            'nombre' : nombre,
            'tipo' : tipo,
            'tvar' : tablaVariables(),
            'tparam' : tipoParam,
            'tcantparam' : cantParam,
            'pilaParam'  : pilaParam,
            'cantVarLoc' : cantVarLoc,
            'iniciaCuadru' : iniciaCuadru,
            'contTemp'   : contTemp
            }
            #print("added function " + nombre)
        else:
            print("function ",nombre," already declared")
            

    #Agrega variables a la tabla de variables
    def agregav(self, nombref, nombrev, tipov, locmemv, tabArr):
        if (nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            if (tabVar['tvar'].busca(nombrev) == True):
                print("Variable",nombrev , "ya existe en la funcion",nombref )
                sys.exit()
            else:
                tabVar['tvar'].agrega(nombrev, tipov, locmemv,tabArr)
        else:
            print("La funcion",nombref,"no existe")
            sys.exit()

    #Agrega los tipos de parametros a la tabla de funcion
    def agregaTablaTipoParam(self,nombref,tiposDeParam,cantParam):
        if(nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            tabVar['tparam'] = tiposDeParam
            tabVar['tcantparam'] = cantParam

    #Agrega la cantidad de variables locales que declara la funcion
    def agregaCantidadVarLoc(self,nombref,cantVarLoc):
        if(nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            tabVar['cantVarLoc'] = cantVarLoc
        else:
            print("Funcion no", nombref," existe")
            sys.exit()

    #Agrega la cantidad de parametros que recibe la funcion
    def agregaContTemp(self,nombref,contTemp):
        if(nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            tabVar['contTemp'] = contTemp
        else:
            print("Funcion ",nombref,"no existe")
            sys.exit()


    #Agrega los parametros a la tabla de funcion correspondiente
    def agregaPilaParam(self,nombref,pilaParam):
        if(nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            tabVar['pilaParam'] = pilaParam

    #Regresa la pila de Param de la funcion correspondiente (REPETIDA, NO SE UTILIZA)
    def getPilaTemp(self,nombref):
        if(nombref in self.arreglo):
           return self.arreglo[nombref]['pilaParam']

    #Regresa la locacion de memoria correspondiente a la variable que se busque
    def getLocMem(self,nombref, nombrev):
        if (nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            if(tabVar['tvar'].busca(nombrev) == True):
                #variable viene de una funcion
                return tabVar['tvar'].getLocacionMemoria(nombrev)
            else:
                print("variable no existe")
                sys.exit()


    #Agrega el numero de cuadruplo en el que inicia la funcion
    def agregaContCuadruplo(self,nombref, iniciaCuadru):
        if(nombref in self.arreglo):
            tabVar = self.arreglo[nombref]
            tabVar['iniciaCuadru'] = iniciaCuadru
        else: 
            print("Funcion no existe")

    def getInicioCuadruplo(self,nombref):
        if(nombref in self.arreglo):
            return self.arreglo[nombref]['iniciaCuadru']
        else: 
            print("Funcion",nombref," no existe")
            sys.exit()  

    #Agrega el tipo de funcion 
    def getTipoFunc(self,nombref):
        if(nombref in self.arreglo):
            return self.arreglo[nombref]['tipo']
    
    #Regresa el tipo del parametro a la funcion correspondiente
    def getTipoParam(self,nombref):
            return self.arreglo[nombref]['tparam']

    #Regresa la pila de parametros de la funcion correspondiente(REPETIDA)
    def getPilaParam(self,nombref):
        if(nombref in self.arreglo):
            return self.arreglo[nombref]['pilaParam']
        else:
            print("Funcion",nombref," no existe")
            sys.exit()

    def getContPilaParam(self,nombref):
        if(nombref in self.arreglo):
            return self.arreglo[nombref]['tcantparam']
        else:
            print("Funcion no existe")
    #Busca si existe la funcion en la tabla de funciones
    def busca(self, query):
        return query in self.arreglo

    #Regresa verdadero o falso, dependiendo de si la funcion existe en la tabla de funciones
    def funcionExiste(self,nombref):
        if(nombref in self.arreglo):
            return True
        else:
            return False

    #Imprimi la tabla de variables de la funcion que se indique
    def testerVariable(self, nombref):
        if nombref in self.arreglo:
            testerino = self.arreglo[nombref]
            return testerino['tvar'].imprimiArreglo()

    #Se utiliza para mostrar la tabla de funciones
    def getDir(self, query):
        if self.busca(query):
            #print("TESTERINO", self.arreglo[query] )
            return self.arreglo[query]
            
        else:
            print("Error not found")
            return None

    def arref(self):
        print(self.arreglo)


