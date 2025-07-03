def divide(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Los argumentos deben ser números.")
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b