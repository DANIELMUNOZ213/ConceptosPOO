class Rectangulo:
    def __init__(self):
        self.esquina_x1 = 1
        self.esquina_x2 = 2
        self.esquina_y1 = 1
        self.esquina_y2 = 2

    def calcular_perimetro(self):
        self.altura = self.esquina_y1 - self.esquina_y2
        self.base = self.esquina_x1 - self.esquina_x2
        perimetro = ((self.altura*2) + (self.base*2))
        return perimetro
    
    def calcular_area(self):
        area = self.base * self.altura
        return area
    
    def cuadrado(self):
        if self.altura == self.base:
            return ("El rectangulo es cuadrado")
        
        else:
            return ("No es cuadrado")