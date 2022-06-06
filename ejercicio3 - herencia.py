class calculadora:

    # Declaramos el metodo __init__
    def __init__(self):
        
        self.num1 = int(input("Digite el primer numero: "))
        self.num2 = int(input("Digite el segundo numero: "))

    # Declaramos el metodo suma 
    def suma(self):

        self.suma = self.num1+self.num2

    # Declaramos el metodo resta
    def resta(self):

        self.resta = self.num1-self.num2

    # Declaramos el metodo multiplicacion
    def multiplicacion(self):

        self.multiplicacion = self.num1*self.num2

    # Declaramos el metodo division
    def division(self):

        self.division = self.num1/self.num2
    
    # Declaramos el metodo imprimir
    def imprimir(self):

        print("Suma: ",self.suma)
        print("Resta: ",self.resta)
        print("Multiplicacion: ",self.multiplicacion)
        print("Division: ",self.division)
        print("")


# Creacion de objetos
operacion1 = calculadora()
operacion1.suma()
operacion1.resta()
operacion1.multiplicacion()
operacion1.division()
operacion1.imprimir()

operacion2 = calculadora()
operacion2.suma()
operacion2.resta()
operacion2.multiplicacion()
operacion2.division()
operacion2.imprimir()
