from math import *
from operator import mod

class Complex:
    def __init__(self, real, imag):
        self.x = real
        self.y = imag
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x + other.x, self.y + other.y)
        else:
            return Complex(self.x + other, self.y)
    def __sub__(self, other):
        return self + (-1 * other)
    def __str__(self) -> str:
        s = "+" if self.y >= 0 else ""
        return f"{self.x}{s}{self.y}i"
    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
        else:
            other = Complex(other, 0)
            return self * other
    __rmul__ = __mul__
    def inv(self):
        modsq = (self.x **2) + (self.y **2)
        return Complex(self.x/modsq, -self.y/modsq)
    def __truediv__(self, other):
        if isinstance(other, Complex):
            return self * other.inv()
        else:
            other = Complex(other, 0)
            return self/other
    def __rtruediv__(self, other):
        return other * self.inv()


a = Complex(1, -1)
b = Complex(2, -2)
print(a/2)
print(a/b)
print(2/a)
print(b/a)