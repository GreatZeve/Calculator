def subtract(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Los argumentos deben ser números.")
    return a - b
