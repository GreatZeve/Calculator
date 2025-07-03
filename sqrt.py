def square_root(number):
    try: 
        number = float(number)
    except ValueError:
        raise ValueError("El valor ingresado no es un número válido.")
    if number < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return number ** 0.5