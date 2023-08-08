class Rectangulo:
    def __init__(self, punto1, punto2):
        self.esquina1 = punto1
        self.esquina2 = punto2

    def calcular_perímetro(self):
        base = abs(self.esquina2.x - self.esquina1.x)
        altura = abs(self.esquina2.y - self.esquina1.y)
        return 2 * (base + altura)

    def calcular_área(self):
        base = abs(self.esquina2.x - self.esquina1.x)
        altura = abs(self.esquina2.y - self.esquina1.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina2.x - self.esquina1.x)
        altura = abs(self.esquina2.y - self.esquina1.y)
        return base == altura