import add
import subtract
import multiply
import divide
import power
import sqrt

def main():
    print("Calculadora de operaciones básicas")
    while True:
        option = input("¿Qué operación desea realizar?\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Potencia\n6. Raíz cuadrada\n7. Salir\n")
        while option != '7':
            if option == '1':
                tipo = input("¿Qué tipo de suma desea realizar?\n1. Suma simple\n2. Suma múltiple\n")
                if tipo == '1':
                    print("Suma simple.")
                    a, b = input("Ingrese dos números separados por espacio: ").split()
                    result = add.add(a, b)
                    print(f"Resultado de {a}+{b} es: {result}")
                    break
                elif tipo == '2':
                    print("Suma múltiple.")
                    args = input("Ingrese los números separados por espacio: ").split()
                    result = add.add_multiple(*args)
                    print(f"Resultado de sumar {args} es: {result}")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

            elif option == '2':
                print("Resta.")
                a, b = input("Ingrese los números a restar, separados por un espacio").split()
                result = subtract.subtract(a, b)
                print(f"Resultado de {a}-{b}: {result}")
                break
            elif option == '3':
                print("Multiplicación.")
                a, b = input("Ingrese dos números a multiplicar: ").split()
                result = multiply.multiply(a, b)
                print(f"Resultado de {a}*{b} es: {result}")
                break
            elif option == '4':
                print("División.")
                a, b = input("Ingrese dividendo y divisor, separador por un espacio:").split()
                result = divide.divide(a, b)
                print(f"Resultado: de {a}/{b} es: {result}")
                break
            elif option == '5':
                print("Potencia.")
                a, b = input("Ingrese la base y el exponente separados por espacio: ").split()
                result = power.power(a, b)
                print(f"Resultado de {a}^{b} es: {result}")
                break
            elif option == '6':
                print("Raíz cuadrada.")
                a = input("Ingrese un número para calcular su raíz cuadrada: ")
                result = sqrt.square_root(a)
                print(f"Resultado: {result}")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                break
        else:
            print("Saliendo de la calculadora.")
            break

if __name__ == "__main__":
    main()
