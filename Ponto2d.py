import math
import random

class Ponto2d:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self): # Representation - equivalente ao operador << em C++. Serve para print
        return f"({self.x:.2f}, {self.y:.2f})\n"

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x 

    def get_y(self):
        return self.y
     
    def __add__(self, other):
        if isinstance(other, Ponto2d):
            return Ponto2d(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Ponto2d):
            return Ponto2d(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int,float)):
            return Ponto2d(self.x * scalar, self.y * scalar)
        return NotImplemented

    def distance_to(self, other): # Calculo de distancia Euclidiana
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)
