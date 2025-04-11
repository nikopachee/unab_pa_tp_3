class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f'({self.x}, {self.y})'


class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mueve_derecha(self, distancia):
        self.punto_a.x += distancia
        self.punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        self.punto_a.x -= distancia
        self.punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self.punto_a.y += distancia
        self.punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self.punto_a.y -= distancia
        self.punto_b.y -= distancia