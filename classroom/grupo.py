from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for numasig,asignatura  in kwargs.items():
            self._asignaturas.append(Asignatura(asignatura))

    def agregarAlumno(self, alumno, lista=None):
        if lista ==None:
            lista=[]
            lista.append(alumno)
        else:
            lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
         return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

