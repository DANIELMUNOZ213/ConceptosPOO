class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print("Cordenadas:", self.x, ",", self.y)
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        distancia = ((dx ** 2) + (dy ** 2)) ** 0.5
        return distancia
