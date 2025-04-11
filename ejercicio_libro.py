class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    
    def mostrar_informacion(self):
        print(f"Título: {self.titulo} {self.edicion} edición")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.lugar[0]} ({self.lugar[1]})")
        print(f"{self.fecha_edicion}")
        print(f"{self.paginas} páginas")


autor = Persona("Y. Daniel", "Liang")

libro = Libro(
    "Introduction to Java Programming",
    autor,
    "0-13-031997-X",
    784,
    "3a.",
    "Prentice-Hall",
    ("New Jersey", "USA"),
    "viernes 16 de noviembre de 2001"
)

libro.mostrar_informacion()