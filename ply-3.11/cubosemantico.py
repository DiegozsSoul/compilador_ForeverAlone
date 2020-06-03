class ConsideracionesSemanticas ():
        def __init__(self):
            self.cuboSemantico = {
                #Int 

                #Int con int
                'int' : { 'int': { 
                    '+' : 'int', '-' : 'int', '*' : 'int', '/' : 'int', '=' : 'int',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','<>' : 'bool',
                },
                #Int con float
                'float' : { 
                    '+' : 'float', '-' : 'float', '*' : 'float', '/' : 'float', '=' : 'int',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','<>' : 'bool',
                },
                #Int con boolean
                'bool' : { 
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #Int con char
                'char' : { 
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #Int con string
                'string' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                }
                 },

                #Float

                #Float con entero
                 'float' : { 'int': {
                    '+' : 'float', '-' : 'float', '*' : 'float', '/' : 'float', '=' : 'float',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','<>' : 'bool',
                },
                #Float con float
                'float' : {
                    '+' : 'float', '-' : 'float', '*' : 'float', '/' : 'float', '=' : 'float',
                    '==' : 'bool', '<' : 'bool', '>' : 'bool', '<=' : 'bool', '>=' : 'bool','<>' : 'bool',
                },
                #Float con boolean
                'bool' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #Float con char
                'char' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #Float con string
                'string' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                }
                 },

                #Boolean

                #boolean con boolean
                 'bool' : { 'int': { 
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #boolean con float
                'float' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #boolean con booelean
                'bool' : { 
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'bool',
                    '==' : 'bool', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #boolean con char
                'char' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #boolean con string
                'string' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                }
                 },

                #Char

                #char con entero
                 'char' : { 'int': {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #char con doble
                'float' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #char con boolean
                'bool' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #char con char
                'char' : {
                    '+' : 'char', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'char',
                    '==' : 'bool', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #char con string
                'string' : {
                    '+' : 'string', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError', #Revisar == y != como bools ?
                }
                 },

                #String

                #string con entero
                 'string' : { 'int': {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #string con float
                'float' : { 
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #string con boolean
                'bool' : {
                    '+' : 'typeError', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'typeError', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                },
                #string con char
                'char' : {
                    '+' : 'string', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'typeError',
                    '==' : 'bool', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',  #Revisar == y != como bools ?
                },
                #string con string
                'string' : {
                    '+' : 'string', '-' : 'typeError', '*' : 'typeError', '/' : 'typeError', '=' : 'string',
                    '==' : 'bool', '<' : 'typeError', '>' : 'typeError', '<=' : 'typeError', '>=' : 'typeError','<>' : 'typeError',
                }
                 }

            }

        def getTipo(self, operando1, operando2, operador):
            return self.cuboSemantico[operando1][operando2][operador]

def main():
    print("reee")
    test = ConsideracionesSemanticas()
    print(test.getTipo('int', 'int', '>'))

if __name__== "__main__":
  main()