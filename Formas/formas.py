import math
import time
import turtle

class Forma:
    def __init__(self, nome, cor, x, y) -> None:
        self.nome=nome
        self.cor=cor
        self.x=x
        self.x=y
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.begin_fill()   # Inicia o preenchimento
        self.desenhar_forma(t)
        t.end_fill()

    def desenhar_forma(self, t:turtle.Turtle):
        raise Exception("Metodo base")

class Triangulo(Forma):
    def __init__(self, altura, largura, nome, cor, x, y) -> None:
        super().__init__(nome, cor, x, y)
        self.altura=altura
        self.largura=largura
    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(3):
            t.right(120)
            t.forward(self.lado)
        t.end_fill()   # Inicia o preenchimento