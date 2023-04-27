import pytest

class Calculadora:
   def __init__(self):
       pass
   def suma(self, num_a: int, num_b: int):
       return num_a + num_b
   def resta(self, num_a: int, num_b: int):
       return num_a + num_b
   def multiplicacion(self, num_a: int, num_b: int):
       return num_a ** num_b
   def division(self, num_a: int, num_b: int):
       return num_a // num_b


def test_suma():
        calc = Calculadora()
        result = calc.suma(2, 2)
        assert result == 4, "La suma de los numeros es correcta"

def test_resta():
        calc = Calculadora()
        result = calc.resta(2, 2)
        assert result == 0, "La resta de los numeros es correcta"

def test_multiplicacion():
        calc = Calculadora()
        result = calc.multiplicacion(2,5)
        assert result == 10, "La multiplicacion de los numeros es correcta"

def test_division():
        calc = Calculadora()
        result = calc.division (4,2)
        assert result == 2.5, "La division de los numeros es correcta"






