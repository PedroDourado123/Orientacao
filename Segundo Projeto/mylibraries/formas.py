class Forma:
    def __init__(self):
        # Construtor padrão da classe Forma
        self.tipo = "forma"  # Tipo genérico de forma

class Circulo(Forma):
    def __init__(self, raio):
        # Construtor da classe Circulo, herda de Forma
        super().__init__()
        self.tipo = "circulo"
        self.raio = raio

class Quadrado(Forma):
    def __init__(self, lado):
        # Construtor da classe Quadrado, herda de Forma
        super().__init__()
        self.tipo = "quadrado"
        self.lado = lado

class Triangulo(Forma):
    def __init__(self, lado):
        # Construtor da classe Triangulo, herda de Forma
        super().__init__()
        self.tipo = "triangulo"
        self.lado = lado

# Você pode adicionar funções ou métodos adicionais aqui, se necessário.
