class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "Nombre: {self.nombre} Nota: {self.nota}"


    def is_aprobado(self, nota):
        if self.nota >= 6:
            return "Condicion: APROBADO"
        else:
            return "Condicion: DESAPROBADO"


nombre = "victor"
nota = 8

alumno =Alumno(nombre, nota)

print(alumno)
print(alumno.is_aprobado(nota))
