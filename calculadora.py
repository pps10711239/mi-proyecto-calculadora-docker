class Calculadora:
    def multiplicar(self, a, b):
        return a * b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python3 calculadora.py <num1> <num2>")
        sys.exit(1)
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    calc = Calculadora()
    resultado = calc.multiplicar(num1, num2)
    print("Resultado:", resultado)
# Linea añadida
# Cambio de prueba para Jenkins
# Ojalá que funciones
