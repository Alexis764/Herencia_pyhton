class Alumno: 
    
    # declaramos el metodo __init__
    def __init__(self):
        
        self.nombre = input("Ingrese el nombre del alumno: ")
        self.nota_alumno = float(input("Ingrese la nota del alumno: "))

    # dedclaramos el metodo imprimir
    def imprimir(self):

        print("")
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota_alumno)





# declaramos la clase aprobado
# la clase aprobado hereda los atributos y metodos de la clase alumno
class aprobado(Alumno):

    # declaramos el metodo __init__
    def __init__(self):

        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()

    # declaramos el metodo imprimir
    def imprimir(self):

        super().imprimir()

    # declaramos el metodo nota_aprobada
    # comprobamos si el estudiante aprobo o reprobo
    def nota_aprobada(self):

        if (self.nota_alumno >= 3):

            print("APROBADO")

        else:

            print("REPROBADO")
            




#Bloque principal 
alumno1 = aprobado()
alumno1.imprimir()
alumno1.nota_aprobada()
