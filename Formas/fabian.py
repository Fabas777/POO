import math
import time
import turtle

class Forma:
    def __init__(self, nome:str, cor:str, x:int, y:int) -> None:
        self.nome=nome
        self.cor=cor
        self.x=x
        self.y=y
    
    def desenhar(self):
        t = turtle.Turtle()
        t.speed(10)
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
    def __init__(self, lado:int, cor:str, x:int, y:int) -> None:
        super().__init__("Triangulo", cor, x, y)
        self.lado=lado
    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(3):
            t.right(240)
            t.forward(self.lado)
        t.end_fill()   # Inicia o preenchimento

class Circulo(Forma):
    def __init__(self, raio:int, cor:str, x:int, y:int) -> None:
        super().__init__('Bola', cor, x, y)
        self.raio=raio
    
    def desenhar_forma(self, t: turtle.Turtle):
        t.left(180)  # Desenha o círculo para baixo
        t.circle(self.raio)
        t.end_fill()  # Encerra o preenchimento

class Trapezio(Forma):
    def __init__(self, B_menor:int, B_maior:int, altura:int, lado:int, cor: str, x: int, y: int) -> None:
        super().__init__("Trapezio", cor, x, y)
        self.B_menor=B_menor
        self.B_maior=B_maior
        self.altura=altura
        self.lado=lado
    
    def desenhar_forma(self, t: turtle.Turtle):
        t.forward(self.B_menor)
        t.right(45)
        t.forward(self.lado)
        t.right(135)
        t.forward(self.B_maior)
        t.right(90)
        t.forward(self.altura)

class TrapezioInvertido(Forma):
    def __init__(self, B_menor:int, B_maior:int, altura:int, lado:int, cor: str, x: int, y: int) -> None:
        super().__init__("Trapezio", cor, x, y)
        self.B_menor=B_menor
        self.B_maior=B_maior
        self.altura=altura
        self.lado=lado
    
    def desenhar_forma(self, t: turtle.Turtle):
        t.right(180)
        t.forward(self.B_menor)
        t.left(45)
        t.forward(self.lado)
        t.left(135)
        t.forward(self.B_maior)
        t.left(90)
        t.forward(self.altura)



tri = Triangulo(100, 'green', 0, 0)
circ = Circulo(50, 'black', 30, 0)

offsets = [-20, 20, 60, 100, 140]
trapezios = [Trapezio(100, 200, 80, 110, 'green', 0, offset) for offset in offsets]


trapezioi1=TrapezioInvertido(100,200,80,110,'green',40,-20)
trapezioi2=TrapezioInvertido(100,200,80,110,'green',40,20)
trapezioi3=TrapezioInvertido(100,200,80,110,'green',40,60)
trapezioi4=TrapezioInvertido(100,200,80,110,'green',40,100)
trapezioi5=TrapezioInvertido(100,200,80,110,'green',40,140)
formas=[(for i in trapezios),trapezioi1,trapezioi2,trapezioi3,trapezioi4,trapezioi5]
for f in formas:
    f.desenhar()
time.sleep(3)