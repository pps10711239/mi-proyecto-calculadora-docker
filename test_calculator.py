import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(calculadora.sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(calculadora.restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicar(2, 4), 8)

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            calculadora.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
