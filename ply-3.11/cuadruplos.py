class cuadruplos(object):
    def __init__(self, operador, operando1, operando2, resultado):
        self.operador = operador
        self.operando1 = operando1
        self.operando2 = operando2
        self.resultado = resultado
    
    def setOperador(self, operador):
        self.operador = operador
    def getOperador(self):
        return self.operador

    def setOperando1(self, operando1):
        self.operando1 = operando1
    def getOperando1(self):
        return self.operando1

    def setOperando2(self, operando2):
        self.operando2 = operando2
    def getOperando2(self):
        return self.operando2

    def setResultado(self, resultado):
        self.resultado = resultado
    def getResultado(self):
        return self.resultado