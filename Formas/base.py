import math
import time
import turtle


class Forma:
    def __init__(self, nome, cor, x, y):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
    
    def desenhar(self):
        raise Exception('Método abstrato.')  # Veremos isso mais tarde
    
    def area(self):
        raise Exception('Método abstrato.')  # Veremos isso mais tarde


class Retangulo(Forma):
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Retângulo', cor, x, y)
        self.largura = largura
        self.altura = altura

    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)
        t.end_fill()  # Encerra o preenchimento

    def area(self):
        return self.largura * self.altura


class Triangulo(Forma):
    def __init__(self, lado, cor, x, y):
        super().__init__('Triângulo', cor, x, y)
        self.lado = lado
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
        t.left(60)
        for _ in range(3):
            t.right(120)
            t.forward(self.lado)
        t.end_fill()   # Inicia o preenchimento

    def area(self):
        return ((self.lado**2) * (3**(1/2))) / 4


class Circulo(Forma):
    def __init__(self, raio, cor, x, y):
        super().__init__('Círculo', cor, x, y)
        self.raio = raio
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
        t.left(180)  # Desenha o círculo para baixo
        t.circle(self.raio)
        t.end_fill()  # Encerra o preenchimento

    def area(self):
        return 2 * math.pi * self.raio


class Estrela(Forma):
    def __init__(self, tamanho, cor, x, y):
        super().__init__('Estrela', cor, x, y)
        self.lado = tamanho
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
        t.left(72)
        for _ in range(5):
            t.right(144)
            t.forward(self.lado)
        t.end_fill()   # Inicia o preenchimento
    
    def area(self):
        return 'Seu professor não sabe calcular 🥲'


ret = Retangulo(75, 100, 'red', -175, 0)
tri = Triangulo(100, 'green', 0, 0)
circ = Circulo(50, 'blue', 150, 0)
est = Estrela(100, 'yellow', 0, 150)

formas = [ret, tri, circ, tri]
for f in formas:
    f.desenhar()
    print(f'Área do {f.nome}: {f.area()}')

time.sleep(3)